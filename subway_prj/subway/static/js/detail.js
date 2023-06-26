placedd = document.querySelector('.place_dropdown');
placebt = document.querySelector('#placebutton'); 
refresh = document.getElementById('station_realtime_refresh');
timetablebts = document.querySelectorAll('.days');
timetables = document.querySelectorAll('.station_timetable');
//table1 = document.getElementById('timetable_1');
//table2 = document.getElementById('timetable_2');
//table3 = document.getElementById('timetable_3');

placebt.addEventListener('click', function(){  
    let rect = placebt.getBoundingClientRect();  
    placedd.style.left = (rect.x-1425) + "px";
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

timetablebts.forEach( (bt) => {
  bt.addEventListener('click', btclick )
});

function btclick(e){

    flag = this.id.substr(-1)

    timetablebts.forEach( (bt) => {
         bt.classList.remove('clicked')
    })
    timetables.forEach( (table) => {
         table.style.display = 'none'
    })

    table = document.getElementById('timetable_'+flag);
    table.style.display = 'flex'
    this.classList.add('clicked')

}