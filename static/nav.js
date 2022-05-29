
/*Define a function for closing the side Navbar*/
function CloseNav() {
    document.getElementById("Nav").style.width = "0px";
}
/*Look for the screen size*/
var x = window.matchMedia("(max-width: 700px)")

/*Define a function for opening the side Navbar depending on the screen size*/
function OpenNav() {
    if (x.matches) {
    document.getElementById("Nav").style.width = "150px";
    }
    else {
    document.getElementById("Nav").style.width = "250px";
    }
}