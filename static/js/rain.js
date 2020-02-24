document.getElementById('rain-audio').volume = 0.2;

const nbDrop = 250;
const rainGravity = 0.9;
const baseDropWidth = 0.2;
const baseDropHeigth = 3;
const baseDeep = 9; // entre 1 et 10

var drops = [];

function initDrop() {
  return {
      x: Math.floor(Math.random()*101), // entre 0 et 100
      y: Math.floor(Math.random()*101) - 100, // entre -100 et 0
      z: Math.random()*baseDeep + (11-baseDeep),
    };
}

function initDrops() {
  for( i=0 ; i<nbDrop ; i++ ) {
    drops[drops.length] = initDrop();

    var rainBox = document.getElementById('rain-box');
    const old = rainBox.innerHTML;
    rainBox.innerHTML = old + '<div id="rain-drop-' + i + '" class="rain-drop"></div>';

    showDrop(i);
  }
}

function showDrop(i) {
  var rainDrop = document.getElementById('rain-drop-' + i);

  rainDrop.style.left = drops[i].x + '%';
  rainDrop.style.top = drops[i].y + '%';
  rainDrop.style.height = drops[i].z*baseDropHeigth + 'px';
  rainDrop.style.width = drops[i].z*baseDropWidth/baseDropHeigth + 'px';
}

function refreshFrame() {
  for( i=0 ; i<drops.length ; i++) {
    drops[i].y = drops[i].y + rainGravity*drops[i].z

    if(drops[i].y > 100) {
      drops[i] = initDrop();
    }
    showDrop(i);
  }
  setTimeout(refreshFrame, 30);
}

function rainLoop() {
  refreshFrame();
}

initDrops();
rainLoop();
