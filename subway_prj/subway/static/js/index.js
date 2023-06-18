const subwayct = document.querySelector("#subway_map_container");
const subwaymap = document.querySelector("#subway_map");

let zoom = 1;
let min_zoom = 1;
let max_zoom = 3;
const ZOOM_SPEED = 0.3; 

document.addEventListener("wheel", function (e) {
    if (e.deltaY < 0) {
        if(zoom < max_zoom) subwaymap.style.transform = `scale(${zoom += ZOOM_SPEED})`;
    } else {
        if(zoom > min_zoom) subwaymap.style.transform = `scale(${zoom -= ZOOM_SPEED})`;
    }
});

let Pressed = false;
let positionX = 0; 
let positionY = 0;     
 
subwaymap.onmousedown = dragstart;
subwaymap.onmouseup = dragend; 
subwayct.onmousemove = move;

// mousedown
function dragstart(e) {
    positionX = e.clientX;
    positionY = e.clientY; 
    Pressed = true;
}

// mouseup
function dragend() {
    Pressed = false;
}

// mousemove
function move(e) {

    if (!Pressed) {
      return;
    }
    
    // 이전 좌표와 현재 좌표 차이값
    const posX = positionX - e.clientX; 
    const posY = positionY - e.clientY; 
    
    // 현재 좌표가 이전 좌표로 바뀜
    positionX = e.clientX; 
    positionY = e.clientY; 
    
    // left, top으로 이동  
    subwaymap.style.left = (subwaymap.offsetLeft - posX) + "px"; 
    subwaymap.style.top = (subwaymap.offsetTop - posY) + "px"; 
    
} 