// feather.replace()

var body = document.body;
setTimeout(function(){
  body.classList.add('active');
}, 200);
  
document.getElementsByClassName('reload')[0].onclick = function() {
  body.classList.remove('active');
  setTimeout(function() {
    body.classList.add('active');
  }, 1500);
}



function autorefresh() {
    setInterval('humidity()', 1000);
    setInterval('temp()', 1000);
    setInterval('cputemp()', 1000);
    setInterval('pressure()', 1000);
    
}

autorefresh()