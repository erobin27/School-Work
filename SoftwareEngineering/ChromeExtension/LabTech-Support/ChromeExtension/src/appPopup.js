document.addEventListener('DOMContentLoaded', function() {
  var checkPageButton = document.getElementById('checkPage');
  checkPageButton.addEventListener('click', function() {

    window.open("https://webpages.uncc.edu/jcao6/Exercise/WebsiteProject/SEproject/SEproject.html");

  }, false);
}, false);



document.addEventListener('DOMContentLoaded', function() {
  var checkPageButton = document.getElementById('contact');
  checkPageButton.addEventListener('click', function() {

      window.open("https://webpages.uncc.edu/jcao6/Exercise/WebsiteProject/SEproject/contact_us.html");

  }, false);
}, false);


document.addEventListener('DOMContentLoaded', function() {
	document.getElementById("quickRep1").style.display="none";

  var qucikReportButton = document.getElementById('quickRep');
  qucikReportButton.addEventListener('click', function() {

      if(document.getElementById("quickRep1").style.display.valueOf()=="block") {
				 document.getElementById("quickRep1").style.display="none";
       }
       else {
         document.getElementById("quickRep1").style.display="block";
       }


  }, false);
}, false);
