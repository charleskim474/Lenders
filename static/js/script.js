let intro = document.getElementById("greet");

function setTime(){
    let now = new Date();
    let time = now.getHours();
    
    if(time < 12){
        intro.textContent = "Good Morning there, Welcome to Kimtech records. \n Please login to gain access to your records."
    }
    else if(time >= 12 && time < 16){
        intro.textContent = "Good Afternoon there, Welcome to Kimtech records. \n Please login to gain access to your records."
    }
    else{
        intro.textContent = "Good Evening there, Welcome to Kimtech records. \n Please login to gain access to your records."
    }
}
setTime();


function show(){
    let pw = document.getElementById("inputPw");
    if(pw.type == "password"){
        pw.type = "text";
    }
    else{
        pw.type = "password";
    }
}
