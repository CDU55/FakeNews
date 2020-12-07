var activeStatus = true;
var message ;
var url;
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

//event listner that extract the page url
chrome.tabs.getSelected(null, function(tab) {
	if(activeStatus){
    	extractURL(tab.url);
	url = tab.url;		
	}   	
});


//show in UI the link of the current page
function extractURL(tablink) {
  // do stuff here
  document.getElementById("currentUrl").innerText = tablink;
   
}


document.addEventListener('DOMContentLoaded', function () {
  console.log("dom loadedddd")
  var divs = document.querySelectorAll('body');
  document.getElementById("currentUrl").innerText =divs[0].innerText;
});



//event listener that listen for background messages, catch when background script got html source 
chrome.runtime.onMessage.addListener(function(request, sender) {
  if (request.action == "getSource") {
		doPost(request.source);	
  }
});


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

//function that parse server response
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
       
      message.innerHTML = 'There was an error injecting script : \n' + chrome.runtime.lastError.message;
    }
  });
}

//attach onWindowLoad function to execute when page is loaded
window.onload = onWindowLoad;

