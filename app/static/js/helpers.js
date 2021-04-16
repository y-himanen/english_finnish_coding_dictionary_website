let i = 0;
const speed = 100;
const engTxt = ' for Software Developers';
const finTxt = ' Ohjelmistokehittäjille';
let txt;

window.onload = function load() {
    txt = checkLanguage();
    typeWriter();
}


function typeWriter() {
    if (i < txt.length) {
        document.getElementById("heading").innerHTML += txt.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
  }
}


function checkLanguage() {
    if (window.location.pathname == '/fin' | window.location.pathname == '/fin/translate') {
        return finTxt;
    } else {
        return engTxt;
    }
}