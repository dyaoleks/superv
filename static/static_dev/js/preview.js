var ADDON="_60x60";
var MEDIA_URL="http://www.SERVER.com/";

var userAgent = navigator.userAgent.toLowerCase();
var isReady = false;
var readyBound = false;
browser = {
safari: /webkit/.test( userAgent ),
opera: /opera/.test( userAgent ),
msie: /msie/.test( userAgent ) && !/opera/.test( userAgent ),
mozilla: /mozilla/.test( userAgent ) && !/(compatible|webkit)/.test( userAgent )
};

function ready(){
if ( !isReady ) {
		isReady = true;
		insertImage();
	}
}

function bindReady(){
	if ( readyBound ) return;
	readyBound = true;

	if (!browser.opera)
		document.addEventListener( "DOMContentLoaded", ready, false );

	if ( browser.msie && window == top ) (function(){
		if (isReady) return;
		try {
			document.documentElement.doScroll("left");
		} catch( error ) {
			setTimeout( arguments.callee, 0 );
			return;
		}
		ready();
	}) ();

	document.addEventListener("load", ready, false );
}

function insertImage(){
	var e = document.getElementsByTagName("A");
	for(var i=0;i<e.length;i++) {
		if(e[i].getAttribute("href").indexOf(MEDIA_URL) != -1)
			e[i].innerHTML = e[i].innerHTML + "<br>" + "<img src='" + MEDIA_URL + e[i].innerHTML.replace(/ /g,"") + "'>";}
}

bindReady();