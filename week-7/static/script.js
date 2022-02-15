const submitBtn = document.querySelector(".submitBtn")

function getName(){
    const inputEle = document.getElementById("inputQueryStr");
    const inputQueryStr = inputEle.value;
    const f = fetch("/api/members?username="+inputQueryStr);
    f
    .then(function(data){
        return data.json();
    })
    .then(function(jsonData){
        checkData(jsonData)
    })
}

submitBtn.addEventListener("click", getName);

function checkData(jsonData){
    let reset = document.getElementById("output");
    reset.innerText = null
    if(jsonData.data == null){
        let output1 = document.getElementById("output");
        let h2Null = document.createElement("h2");
        h2Null.innerText = "查無此人";
        output1.appendChild(h2Null)
    }else{
        let output2 = document.getElementById("output");
        let h2 = document.createElement("h2");
        let name = jsonData.data.name;
        let userName = jsonData.data.username;
        h2.innerText = name + "(" + userName + ")";
        output2.appendChild(h2)
    }
}

const submitUpBtn = document.querySelector(".submitUpBtn")

function updateName(){
    const newNameEle = document.getElementById("inputNewName");
    let newName = newNameEle.value;
    const requestOptions = {
        method:"POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({name:newName})
    };
    const f = fetch("/api/member",requestOptions);
    
    f
    .then(function(responseData){
        return responseData.json();
    })
    .then(function(jsonData){
        checkNewName(jsonData);
    })

    document.getElementById("inputNewName").value = ""
}

submitUpBtn.addEventListener("click", updateName);

function checkNewName(jsonData){
    let reset = document.getElementById("outputResult");
    reset.innerText = null
    if(jsonData.ok == true){
        let outputOK = document.getElementById("outputResult");
        let h2OK = document.createElement("h2");
        h2OK.innerText = "更新成功";
        outputOK.appendChild(h2OK)
    }else{
        let outputErr = document.getElementById("outputResult");
        let h2Err = document.createElement("h2");
        h2Err.innerText = "更新失敗";
        outputErr.appendChild(h2Err)
    }
}
