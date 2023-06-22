var stationName = '';
// function callStation(inputID){
//         location.href = `./station.html?${inputID.split("X")[0]}`;
//     }


function departure(inputID){
    var stationElement = document.getElementById(inputID);
    stationName = stationElement.nextElementSibling.textContent;
    console.log(stationName)
    document.querySelector('#departure_station').value = stationName;
}

function arrival(inputID){
    var stationElement = document.getElementById(inputID);
    stationName = stationElement.nextElementSibling.textContent;
    console.log(stationName)
    document.querySelector('#arrival_station').value = stationName;
}

// function callStation(inputID) {
//     var menuWindow = document.getElementById('menuWindow');
//     // text값 받기
//     var dp = document.querySelector('#departure_station').value;
//     var ar = document.querySelector('#arrival_station').value;


//     // 메뉴 창이 이미 열려있으면 닫고, 닫혀있으면 열기
//     if (menuWindow) {
//         document.body.removeChild(menuWindow);
//     } else {
//         menuWindow = document.createElement('div');
//         menuWindow.id = 'menuWindow';

//         // 메뉴 창 내용 추가
//         menuWindow.innerHTML = `
//         <div id="menuList">
//             <button><a href="#" onclick="departure('${inputID}')">출발</a></button>
//             <button><a href="#" onclick="arrival('${inputID}')">도착</a></button>
//             <button><a href="#">혼잡 예측</a></button>
//             <button><a href="./station.html?${inputID.split("X")[0]}">역 상세 정보</a></button>
//         `;

//         document.body.appendChild(menuWindow);
//     }
// }

function callStation(inputID, event) {
    var infowindow = document.getElementById('subway_infowindow');
    let modal = document.querySelector('.congestion_modal');

    // text값 받기
    var dp = document.querySelector('#departure_station').value;
    var ar = document.querySelector('#arrival_station').value;


    // var x = event.clientX;
    // var y = event.clientY;
    // console.log("마우스 위치 x : " + x);
    // console.log("마우스 위치 y : " + y);

    // 메뉴 창이 이미 열려있으면 닫고, 닫혀있으면 열기
    if (infowindow.style.display == 'block') {
       // document.body.removeChild(infowindow);
       infowindow.style.display = 'none'
    } else {
        //placedd = document.querySelector(`#${inputID}`);
        // 메뉴 창 내용 추가
        infowindow.innerHTML = `
            <div id="infowindow_btbar">
                <div class="infowindow_bt">
                    <a onclick="departure('${inputID}')">
                        <i class="fa-solid fa-location-dot green"></i><br>
                        <span>출발</span>
                    </a>
                </div>
                <div class="infowindow_sepline"></div>
                <div class="infowindow_bt">
                    <a onclick="arrival('${inputID}')">
                        <i class="fa-solid fa-location-dot red"></i><br>
                        <span>도착</span>
                    </a>
                </div>
                <div class="infowindow_sepline"></div>
                <div class="infowindow_bt">
                    <a href="./stationdetail/${inputID}/">
                        <i class="fa-solid fa-magnifying-glass blue"></i><br>
                        <span>역 정보</span>
                    </a>
                </div>
            </div>
        `;

        infowindow.style.display = 'block'
        modal.style.display = 'block';

        //document.body.appendChild(infowindow);

        // Get the position of the clicked circle
        var circle = document.getElementById(inputID);
        var cx = circle.getAttribute('cx');

        rect = circle.getBoundingClientRect();

        var rx = rect.x;
        var ry = rect.y;

        infowindow.style.left = (rx-535) + 'px';
        infowindow.style.top = (ry-90) + 'px';
        infowindow.style.display = 'block';

    }
}

function showLine(lineNumber){
        $("#zoomable").children("g").css("visibility", "hidden");
        $(`#${lineNumber}`).css("visibility", "visible");
}

function clearinput(){
    var input = document.getElementById('search_station');
    input.value = '';
}

function clearroute(){
    var ds = document.getElementById('departure_station');
    var as = document.getElementById('arrival_station');

    ds.value = '';
    as.value = '';
}

function routechange(){
    var ds = document.getElementById('departure_station').value;
    var as = document.getElementById('arrival_station').value;

    if(ds==''){
        alert('출발지가 없습니다.')
    }
    if(as==''){
        alert('도착지가 없습니다.')
    }

    var temp = ds;
    ds = as;
    as = temp;

    // 교환된 값을 다시 입력 필드에 설정합니다.
    document.getElementById('departure_station').value = ds;
    document.getElementById('arrival_station').value = as;

}



function searchstation(){
    var searchInput = document.getElementById("search_station").value;

    var stationElements = document.getElementsByTagName("text");
    var stationId = null;

    for (var i = 0; i < stationElements.length; i++) {
        if (stationElements[i].textContent === searchInput) {
            stationId = stationElements[i].previousElementSibling.getAttribute("id");
            break;
        }
    }

    if (stationId) {
        callStation(stationId);
        stationId.scrollIntoView({ behavior: 'smooth', block: 'center' });
    } else {
        // Station not found
        alert("역을 찾을 수가 없습니다.");
    }

}

function stationinfo() {
    var searchInput = document.getElementById("search_station").value;

    // AJAX를 사용하여 서버에 역 정보를 요청합니다.
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/map/searchId/" + searchInput + "/", true);
    xhr.onload = function() {
        if (xhr.status === 200) {
            var stationData = JSON.parse(xhr.responseText);

            if (stationData.stationIds && stationData.stationIds.length > 0) {
                var combinedId;
                if (stationData.stationIds.length === 1) {
                    combinedId = stationData.stationIds[0];
                } else {
                    combinedId = stationData.stationIds.join("x");
                }
                location.href = "/map/stationdetail/" + combinedId + "/";
            } else {
                alert("역을 찾을 수가 없습니다.");
            }
        } else {
            // Error handling
            console.error('Request failed. Status:', xhr.status);
        }
    };
    xhr.send();
}

// $('#search_station').addEventListener('keyup',function(){
//     var stationElements = document.getElementsByTagName("text");
//     var stationArr = [];

//     for (var i = 0; i < stationElements.length; i++) {
//         var stationElement = stationElements[i];
//         var stationName = stationElement.textContent;
//         stationArr.push(stationName);
//     }

//     var arr = [];
//     var searchWord = $('#search_station').value;


// })

// ---- 은나현 추가 (팝업창 외의 부분 클릭하면 닫힘)
document.addEventListener('mouseup', function(e) {
    var infowindow = document.getElementById('subway_infowindow');
    let modal = document.querySelector('.congestion_modal');
    if (!infowindow.contains(e.target) && !modal.contains(e.target)) {
        infowindow.style.display = 'none';
//        modal.style.display = 'none';
    }
});

document.addEventListener('wheel', function(e) {
    var infowindow = document.getElementById('subway_infowindow');
    let modal = document.querySelector('.congestion_modal');
    infowindow.style.display = 'none';
//    modal.style.display = 'none';
});

let buttons = document.querySelectorAll('circle')

buttons.forEach( (button) => {
    button.addEventListener('click',congestion)
})

function congestion() {

    let modal = document.querySelector('.congestion_modal');
    let linebt = document.getElementById('modallinebt');
    let title = document.getElementById('modaltitle');

    var xhr = new XMLHttpRequest();

    xhr.open("GET", "/map/searchStation/" + this.id + "/", true);
    xhr.onload = function() {
        if (xhr.status === 200) {
            let stations = JSON.parse(xhr.responseText);

            let ids = Object.keys(stations)
            modal.id = ids[0];

            linebt.innerHTML = ''

            Object.keys(stations).forEach( (station) => {
                let line = stations[station]['line']
                linebt.insertAdjacentHTML("beforeend",
                    `<button class="station_detail_linebt line-${line}"
                        id="${station}" onclick='changeid(this, ${JSON.stringify(stations[station])})'>${line}</button>` )
            })

            title.innerHTML =  `
                    <hr class="station_detail_line line-${stations[modal.id]['line']}">
                    <div class="station_detail_name line-${stations[modal.id]['line']}-title">
                        <button class="station_detail_linebt line-${stations[modal.id]['line']}" >
                            ${stations[modal.id]['line']}</button>
                        <h2>${stations[modal.id]['name']}</h2>
                    </div>
                    <div class="station_detail_prevnext">
                        <a href="#" class="station_detail_prev">
                            <i class="fa-solid fa-arrow-left blue"></i><span>압구정로데오</span>
                        </a>
                        <a href="#" class="station_detail_next">
                            <span>선정릉</span> <i class="fa-solid fa-arrow-right blue"></i>
                        </a>
                    </div>
                `


        } else {
            // Error handling
            console.error('Request failed. Status:', xhr.status);
        }
    };
    xhr.send();
}

function changeid(e, station){

    let modal = document.querySelector('.congestion_modal');
    let title = document.getElementById('modaltitle');

    modal.id = e.id;

    title.innerHTML =  `
        <hr class="station_detail_line line-${station['line']}">
        <div class="station_detail_name line-${station['line']}-title">
            <button class="station_detail_linebt line-${station['line']}" >
                ${station['line']}</button>
            <h2>${station['name']}</h2>
        </div>
        <div class="station_detail_prevnext">
            <a href="#" class="station_detail_prev">
                <i class="fa-solid fa-arrow-left blue"></i><span>압구정로데오</span>
            </a>
            <a href="#" class="station_detail_next">
                <span>선정릉</span> <i class="fa-solid fa-arrow-right blue"></i>
            </a>
        </div>
    `
}