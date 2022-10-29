let titleArr=[]; //標題arr
let urlArr=[];  //圖片網址arr

function promotion(className,num){
    let img = document.createElement("img");
    img.src=urlArr[num];
    img.style.height="50px";
    document.getElementById(className).appendChild(img);
    let span = document.createElement("span");
    span.textContent=titleArr[num];
    document.getElementById(className).appendChild(span);
}

function titleBlock(idName,num){
    let div0=document.createElement('div');
    div0.setAttribute('class','titleBlock');
    div0.setAttribute('id',idName);
    document.getElementById('titles').appendChild(div0);
    let img=document.createElement('img');
    img.src=urlArr[num];
    img.setAttribute('class','titleImg');
    document.getElementById(idName).appendChild(img); 
    //Uncaught (in promise) TypeError: Cannot read properties of null (reading 'appendChild')
    let div=document.createElement('div');
    div.setAttribute('class','title');
    div.textContent=titleArr[num];
    document.getElementById(idName).appendChild(div);
}

let titleblockNumber=8;

function loadmore(){
    // console.log(titleblockNumber);
    titleblockNumber+=8;
    loadpage(titleblockNumber);
    if(titleblockNumber>=titleArr.length-2){
        let btn=document.getElementById('loadmore');
        btn.style.display='none'
    }
    return titleblockNumber;  
}

function loadpage(nums){
    for(let i=nums-7;i<=nums;i++){
        // console.log(i);
        let idtest=`titleBlock${i}`; //在字串中帶入變數的標準寫法
        // let idtest='titleBlock'+i //這寫法也可以
        // console.log(idtest);
        titleBlock(idtest,i+1)
    }
}


fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json")
.then(response=>{
    return response.json();  //取得 JSON 再轉 JavaScript
}).then(data=>{
    let arr= data['result']['results'];
    // console.log(arr);
    // let titleArr=[]; //標題arr
    // let urlArr=[];  //圖片網址arr
    for(let i=0;i<arr.length;i++){   //完成標題及圖片的Arr
        titleArr.push(arr[i]['stitle']);
        let url = arr[i]['file'].split('http')[1];
        urlArr.push('http'+url)
    };

    promotion('promotion1',0)
    promotion('promotion2',1)
    
    loadpage(titleblockNumber)
})