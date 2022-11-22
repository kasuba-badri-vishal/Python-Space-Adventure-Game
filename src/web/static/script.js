fetch('nav.html')
.then(res => res.text())
.then(text => {
    let oldelem = document.querySelector("script#replace_with_navbar");
    let newelem = document.createElement("div");
    newelem.innerHTML = text;
    oldelem.parentNode.replaceChild(newelem,oldelem);
})

function learnmore1() {
    var hobby = document.getElementById("hobby1");
    var learnmore = document.getElementById("learnmore1");
    if (hobby.checked == true) {
        learnmore.style.display = "block";
    } 
    else{
        learnmore.style.display = "none";
    }
}

function learnmore2() {
    var hobby = document.getElementById("hobby2");
    var learnmore = document.getElementById("learnmore2");
    if (hobby.checked == true) {
        learnmore.style.display = "block";
    } 
    else{
        learnmore.style.display = "none";
    }
}

function learnmore3() {
    var hobby = document.getElementById("hobby3");
    var learnmore = document.getElementById("learnmore3");
    if (hobby.checked == true) {
        learnmore.style.display = "block";
    } 
    else{
        learnmore.style.display = "none";
    }
}