function NavFunc() {
    var x = document.getElementById("Nav");
    if (x.className === "Nav") {
        x.className += " mobile";
    }
    else {
        x.className = "Nav";
    }
}