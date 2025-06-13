const body = document.querySelector("body"),
      sidebar = body.querySelector(".sidebar"),
      btn_toggle = body.querySelector(".btn_toggle"),
      user_area = body.querySelector(".user_area"),
      dropdown_menu = body.querySelector(".dropdown_menu")

btn_toggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    
});

user_area.addEventListener("click", () => {
    user_area.classList.toggle("active")
});


document.addEventListener("click", function(event){
    if (
        user_area.classList.contains("active") &&
        !user_area.contains(event.target) &&
        !dropdown_menu.contains(event.target)
    ) {
        user_area.classList.remove("active")
    }
});