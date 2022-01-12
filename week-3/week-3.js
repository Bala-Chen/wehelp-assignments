const jsonUrl ="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

let f = fetch(jsonUrl);

f
.then(function(userData){
    return userData.json();
})
.then(function(jsonData){
    all_data = jsonData.result.results;
    return all_data;
})
.then(function(allData){
    let mainData = []
    for (i = 0; i < allData.length; i++){
        let stitle = allData[i]["stitle"];
        let img = allData[i]["file"];
        let img_one=img.split("https://")[1];
        const dict = {"stitle":stitle,"img":"https://" + img_one};
        mainData.push(dict)
    }
    return mainData;
})
.then(function(main_data){
    create_El(main_data);
    create_btn(); 
    loadMore()
})

function create_El(data){
    for (i = 0; i < data.length; i++){
        let main = document.getElementById("main");
        if(i % 4 == 0){
            var div_area = document.createElement('div');
            div_area.className = "div-area";
        };
        let new_div = document.createElement('div');
        new_div.className = "main-item";
        let one_img = document.createElement('img');
        one_img.src = data[i]["img"];
        new_div.appendChild(one_img);
        let stitle_h4 = document.createElement('h4');
        stitle_h4.textContent = data[i]["stitle"];
        new_div.appendChild(stitle_h4);
        div_area.appendChild(new_div);
        main.appendChild(div_area);
        if(i >= 8){
            new_div.style.display = "none"
        }
    }
};

function create_btn(){
    let btn_div = document.createElement('div');
    btn_div.className = "btn-area";
    let btn = document.createElement('button');
    btn.className = "btn";
    btn.textContent = "Load More";
    btn_div.appendChild(btn);
    document.body.appendChild(btn_div)
};

function loadMore(){
    let items = document.querySelectorAll('.main-item');
    let btn = document.querySelector('button');
    let current_div = 8
    btn.addEventListener('click',function(){
        for(i = current_div; i < current_div + 8;i++){
            if(items[i]){
                items[i].style.display = "block"; 
            }
        }
        current_div += 8;
        if(current_div >= items.length){
            btn.style.display = "none";
        }
    })
}





