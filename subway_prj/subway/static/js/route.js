results = document.querySelectorAll('.route_results');
mintimert = document.getElementById('route_result_mintime');
mintfrt = document.getElementById('route_result_mintf');
mintimebt = document.getElementById('mintimebt');
mintfbt = document.getElementById('mintfbt');
route_pdbts = document.querySelectorAll('.route_pdbt');

function mintime(){
    results.forEach( (result) => {
        result.style.display = 'none';
    })
    mintfbt.classList.remove('clicked')
    mintimebt.classList.add('clicked')

    mintimert.style.display = 'block';
}

function mintf(){

    results.forEach( (result) => {
        result.style.display = 'none';
    })
    mintimebt.classList.remove('clicked')
    mintfbt.classList.add('clicked')
    mintfrt.style.display = 'block';
}

