placedd = document.querySelector('.place_dropdown');
placebt = document.querySelector('#placebutton'); 
refresh = document.getElementById('station_realtime_refresh');

placebt.addEventListener('click', function(){  
    let rect = placebt.getBoundingClientRect();  
    placedd.style.left = (rect.x-650) + "px";
    placedd.style.top = (rect.y-15) + "px";  
    placedd.style.display = 'block'; 
}) 

document.addEventListener('mouseup', function(e) { 
    if (!placedd.contains(e.target)) {
        placedd.style.display = 'none';
    }
});

refresh.addEventListener('click', function(){
    location.reload();
})
