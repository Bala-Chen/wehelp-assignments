const jsonUrl ="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

let f = fetch(jsonUrl);

f
.then(function(userData){
    return userData.json();
})
.then(function(jsonData){
    allData = jsonData.result.results;
    return allData;
})
.then(function(allData){
    let mainData = []
    for (i = 0; i < allData.length; i++){
        let stitle = allData[i]["stitle"];
        let img = allData[i]["file"];
        let imgOne = img.split("https://")[1];
        const dict = {"stitle":stitle,"img":"https://" + imgOne};
        mainData.push(dict)
    }
    return mainData;
})
.then(function(mainData){
    createEl(mainData);
    createBtn(); 
    loadMore()
})

function createEl(data){
    for (i = 0; i < data.length; i++){
        let main = document.getElementById("main");
        if(i % 4 == 0){
            divArea = document.createElement('div');
            divArea.className = "div-area";
        };
        let newDiv = document.createElement('div');
        newDiv.className = "main-item";
        let oneImg = document.createElement('img');
        oneImg.src = data[i]["img"];
        newDiv.appendChild(oneImg);
        let stitleH4 = document.createElement('h4');
        stitleH4.textContent = data[i]["stitle"];
        newDiv.appendChild(stitleH4);
        divArea.appendChild(newDiv);
        main.appendChild(divArea);
        if(i >= 8){
            newDiv.style.display = "none"
        }
    }
};

function createBtn(){
    let btnDiv = document.createElement('div');
    btnDiv.className = "btn-area";
    let btn = document.createElement('button');
    btn.className = "btn";
    btn.textContent = "Load More";
    btnDiv.appendChild(btn);
    document.body.appendChild(btnDiv)
};

function loadMore(){
    let items = document.querySelectorAll('.main-item');
    let btn = document.querySelector('button');
    let currentDiv = 8
    btn.addEventListener('click',function(){
        for(i = currentDiv; i < currentDiv + 8;i++){
            if(items[i]){
                items[i].style.display = "block"; 
            }
        }
        currentDiv += 8;
        if(currentDiv >= items.length){
            btn.style.display = "none";
        }
    })
}





