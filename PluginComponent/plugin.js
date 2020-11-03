
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
	return rawHtml
}

function prepareHtml(rawHtml){
	return preparedHtml()
}

function parseHtml(){
	var body = getHtml()
	body = prepareHtml(body)
	return body 
}

function getResultFromServer(){}

function notifyUser(result){
	alert(result)
}

function pageChanged() {
	return pageChanged;
}

function sendHtmlToServer(){}


const subject = new Subject();
subject.subscribe(pageChanged)
subject.subscribe(parseHtml)
subject.subscribe(notifyUser)
subject.subscribe(sendHtmlToServer)
subject.fire()


chrome.runtime.onInstalled.addListener('DOMContentLoaded', function() {
    chrome.storage.sync.set({color: '#3aa757'}, function() {
      console.log('Page is loaded');
    });
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
 
  // ...
}