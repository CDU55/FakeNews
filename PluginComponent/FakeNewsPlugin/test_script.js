var activeStatus = true;
var message ;
var url;
var userOnTwitterFlag = false;
var userOnTwitterAndOnPostFlag = false;
var logsShown = false;
//function that enable/disable manually the chrome extension
/*
...TO BE CONTINUED
document.getElementById("extensionStatus").addEventListener('click', function() {
  if(!activeStatus)
  	activeStatus = true;
  else
  	activeStatus = false;
});
*/
document.getElementById("logsBtn").addEventListener('click',turnLogs);
function turnLogs(){
	if(!logsShown){
		logsShown = true;
		document.getElementById("plugin").style.display="none";
		document.getElementById("logs").style.display="block";
	}
	else{
		logsShown = false;
		document.getElementById("plugin").style.display="block";
		document.getElementById("logs").style.display="none";
	}
}
//event listner that extract the page url
chrome.tabs.getSelected(null, function(tab) {
	if(activeStatus){
    	extractURL(tab.url);
		url = tab.url;
		checkIfUserSurfingOnTwitter(tab.url);		
	}   	
});


function checkIfUserSurfingOnTwitter(url){
	var messageBox = document.getElementById("analysisStatus");
	var t = url;
	
	//check if user is surfing on twitter
	var userOnTwitterExpression = /https?:\/\/(www\.)?(twitter\.com)/;
	var userOnTwitterRegex = new RegExp(userOnTwitterExpression);

	if (t.match(userOnTwitterRegex)) {
		userOnTwitterFlag = true;
  		messageBox.innerText = "User is on Twitter!";
	} else {
		userOnTwitterFlag = false;
  		messageBox.innerText = "User is not on Twitter!";
	}

	//check if user is watching a certain post on twitter
	var userOnTwitterPostExpression = /https?:\/\/(www\.)?(twitter\.com)\/([-a-zA-Z0-9()@:%_\+.~#?&//=]*)\/(status)\/[0-9]*/;
	var userOnTwitterPostRegex = new RegExp(userOnTwitterPostExpression);
	

	if (t.match(userOnTwitterPostRegex)) {
		userOnTwitterAndOnPostFlag = true;
  		messageBox.innerText += " User is on Twitter post!";
	} else {
  		messageBox.innerText += " User is not on Twitter post";
  		userOnTwitterAndOnPostFlag = false;
	}
}

//show in UI the link of the current page
function extractURL(tablink) {
  document.getElementById("currentUrl").innerText = tablink;
}


document.addEventListener('DOMContentLoaded', function () {
  var divs = document.querySelectorAll('body');
  document.getElementById("currentUrl").innerText =divs[0].innerText;
});


//event listener that listen for background messages, catch when background script got html source 
chrome.runtime.onMessage.addListener(function(request, sender) {
  if (request.action == "getSource") {
  	//check if user is on Twitter and is watching a post
  		if(userOnTwitterAndOnPostFlag){
  			//send html body to server
			doPost(request.source);	
  		}
  		{
  			userBehaviourNotOk();
  		}
  }
});

function userBehaviourNotOk(){
	if(!userOnTwitterFlag){
		document.getElementById("htmlTag").innerText = "You have to be on Twitter, otherwise the detection will not run!";
		return;
	}
	if(!userOnTwitterAndOnPostFlag){
		document.getElementById("htmlTag").innerText = "You have to be on a Twitter post, otherwise the detection will not run!";
		return;
	}
}


//function call that do post to server an get server response
async function doPost(htmlSourceCode){
	//test post works with an online api
	/*await $.post("https://www.w3schools.com/jquery/demo_ajax_gethint.asp", {suggest: "d"}, function(result){
      	$("htmlTag").html(result);
      	document.getElementById("htmlTag").innerText =result;
    	});
    	*/	
	var postAddress = "http://127.0.0.1:5000/"
	
	await $.post(postAddress,
      { html: htmlSourceCode, url: url})
    .done(serverResponse => {
        if(!serverResponse) return;
        parseResponse(serverResponse)       
    })
    .catch(error=>{
      document.getElementById("htmlTag").innerText = error;
    })
}

//function that parse server response and shows on UI server's response
function parseResponse(serverResponse){
	document.getElementById("htmlTag").innerText = serverResponse.response;
	//future implementation that parse response and fit it into UI
}


//function called when page is loaded and then extract the html elements with background_for_get_html.js script
function onWindowLoad() {
  message = document.getElementById("htmlTag");
  chrome.tabs.executeScript(null, {
    file: "background_for_get_html.js"
  }, function() {
    if (chrome.runtime.lastError) {
       
      //message.innerHTML = 'There was an error injecting script : \n' + chrome.runtime.lastError.message;
    }
  });
}

//attach onWindowLoad function to execute when page is loaded
window.onload = onWindowLoad;