 

var analysisTitle = document.getElementById("analysisStatus");
var analysisBody = document.getElementById("analysisBody");
var extensionOn;
var serverAnalysisResponse;
var errorMessage = "something went wrong!";

//set result state of the analysis
function setAnalysisState(int numberOfWarnings){
  analysisStatus.innerHtml = "We found "+ numberOfWarnings+" warnings that can be fake news!";
}

//set reasons for derived conclusion 
function setAnalysisBody(var analysisResponse){
  int responsesCounter = 0;
  for(int i=0; i<analysisResponse.length;i++){
    var paragraph = document.createElement("P");
    paragraph.innerHtml = responsesCounter+". "+analysisResponse[i].response;
    analysisBody.appendChild(paragraph);
  }
}

//function that turn on/off the extention action
document.getElementById("extentionStatus").addEventListener('click',function(){
  if(this.checked)
    extensionStatus = true;
  else
    extensionStatus = false;
});

//add event listener that detects when user change surfing page
window.addEventListener("hashchange", mainAction);

//function that extracts sensitive informations from webpage, process and prepare for sending to server 
function extractDataFromWebPage(){
  var sensitiveExtractedData;
  var pageUrl = window.location.href;
  var hostName = window.location.hostname;
  var pathName = window.location.pathname;
  var securityProtocol = window.location.protocol;  //http / https
  var pageBody = document.getElementByTagName("BODY");
  sensitiveExtractedData["pageUrl"] = pageUrl;
  sensitiveExtractedData["hostName"] = hostName;
  sensitiveExtractedData["pathName"] = pathName;
  sensitiveExtractedData["securityProtocol"] = securityProtocol;
  sensitiveExtractedData["pageBody"] = securityProtocol;
  return sensitiveExtractedData;
}

async function sendDataToServer(var data){
  var url = 'https://server/input_data';
  await $.post(url, data, function(data, status){
    if(status == 200){
      serverAnalysisResponse = data;
    }
    else{
      alert(errorMessage);
    }
  });
}


function decorateResponse(){
  setAnalysisState(serverAnalysisResponse.length);
  setAnalysisBody(serverAnalysisResponse);
}

async function mainAction(){
  //extract sensitive data
  var sensitiveData = extractDataFromWebPage();
  //send extracted data to server
  await sendDataToServer(sensitiveData);
  //post process server response and decorate to readble infos
  decorateResponse();
}



/*
function Subject(){
 this.observers = [];
}

Subject.prototype = {  
   subscribe: function(fn)  
   {    
     this.observers.push(fn)  
   },  
   unsubscribe: function(fnToRemove)  
   {    
      this.observers = this.observers.filter( fn => {      
         if (fn != fnToRemove)        
               return fn    
      })  
   },  
   fire: function()  
   {    
      this.observers.forEach( fn => {
         fn.call()    
    })  
}}



function getHtml(){
  var rawHtml = document.getElementByTagName("body").innerHtml;
	return rawHtml
}

function prepareHtml(rawHtml){
  var preparedText = rawHtml
  //Perform operations
	//parse text by tags/key words 
  return preparedText;
}

function parseHtml(){
	var body = getHtml()
	body = prepareHtml(body)
	return body 
}

function getResultFromServer(){
  //implementation for receive the result from server side
}

function sendHtmlToServer(){
  //implementation for sending data from web page to the server
}

function notifyUser(result){
  //notify the user about the current web page if is fake news or not
	alert(result)
}

function pageChanged() {
	//return if page was changed to notify the server about a new page
}




const subject = new Subject();
subject.subscribe(pageChanged)
subject.subscribe(parseHtml)
subject.subscribe(notifyUser)
subject.subscribe(sendHtmlToServer)
subject.fire()

//plugin listener 
chrome.runtime.onInstalled.addListener('DOMContentLoaded', function() {
  //plugin implementation strategy

  //check if page was loaded
   window.addEventListener('load', function () {
        //page loaded
   });
  //extract html code (body)
  //preprocess html code
  //send extracted data to the server side component
  //wait for the server response (fake news state of the analyzed page)

});




var mediator = {};
var orgChart = {
  addNewAction: function(){
 
    // getActionDetail provides a view that plugin interact with
    var actionDetail = this.getEmployeeDetail();
 
    // when the action detail is complete, the mediator (the 'orgchart' object)
    // decides what should happen next
    actionDetail.on("complete", function(action){
 
      // set up additional objects that have additional events, which are used
      // by the mediator to do additional things
      var managerSelector = this.selectManager(action);
      managerSelector.on("save", function(employee){
        employee.save();
      });
 
    });
  },
}
*/