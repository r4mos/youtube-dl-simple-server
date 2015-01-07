function initialize() {
  if (typeof(localStorage['ydlssServer']) != "undefined") {
    document.getElementById('server').value = localStorage['ydlssServer'];
  } else {
    document.getElementById('server').value = 'localhost'
  }
  if (typeof(localStorage['ydlssPort']) != "undefined") {
    document.getElementById('port').value = localStorage['ydlssPort'];
  } else {
    document.getElementById('port').value = '49149';
  }

}
function save() {
  localStorage['ydlssServer'] = document.getElementById('server').value;
  localStorage['ydlssPort'] = document.getElementById('port').value;
  return false;
}

document.addEventListener('DOMContentLoaded', function () {
  document.getElementById("button").addEventListener('click',save);
  initialize();
});
