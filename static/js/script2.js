

// Toggle Menu Visibility
document.getElementById("menu-button").addEventListener("click", function () {
    let menu = document.getElementById("menu");
    menu.classList.toggle("hidden");
});

function getDays(){
    let days = document.getElementById("days");
    data = days.value;
    days.textContent = "hey";
}
getDays();
