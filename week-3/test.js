// $(document).ready(function(){
    fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json")
    .then(response=>{
    return response.json();  //取得 JSON 再轉 JavaScript
    }).then(data=>{
    let arr= data['result']['results'];
    // console.log(arr);
    let titleArr=[]; //標題arr
    let urlArr=[];  //圖片網址arr
    for(let i=0;i<arr.length;i++){   //完成標題及圖片的Arr
    titleArr.push(arr[i]['stitle']);
    let url = arr[i]['file'].split('http')[1];
    urlArr.push('http'+url)
    };
    
    // console.log(titleArr);
    // console.log(urlArr);
    
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
        const img=document.createElement('img');
        img.src=urlArr[num];
        img.setAttribute('class','titleImg');
        document.getElementById(idName).appendChild(img); //Uncaught (in promise) TypeError: Cannot read properties of null (reading 'appendChild')
        let div=document.createElement('div');
        div.setAttribute('class','title');
        div.textContent=titleArr[num];
        document.getElementById(idName).appendChild(div);
    }
    
    for(let i=1;i<9;i++){
    const idtest="'titleBlock"+i+"'";
    titleBlock(idtest,i+1)
    }
    
    promotion('promotion1',0)
    promotion('promotion2',1)
        
    // titleBlock('titleBlock1',2)
    // titleBlock('titleBlock2',3)
    // titleBlock('titleBlock3',4)
    // titleBlock('titleBlock4',5)
    // titleBlock('titleBlock5',6)
    // titleBlock('titleBlock6',7)
    // titleBlock('titleBlock7',8)
    // titleBlock('titleBlock8',9)
    })
    // }