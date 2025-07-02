const body = document.querySelector("body"),
      sidebar = body.querySelector(".sidebar"),
      btn_toggle = body.querySelector(".btn_toggle"),
      user_area = body.querySelector(".user_area"),
      dropdown_menu = body.querySelector(".dropdown_menu"),
      add_btn = body.querySelector(".add_btn"),
      modal = body.querySelector(".modal_bg"),
      modal_close_icon = body.querySelector(".modal_close_icon"),
      dropdown_sidebar = body.querySelector(".submenu_dropdown");

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
    };
});

add_btn.addEventListener("click", () => {
    modal.classList.toggle("open")
});

modal_close_icon.addEventListener("click", () => {
    if (modal.classList.contains("open")) {
        modal.classList.remove("open")
    };
});

dropdown_sidebar.addEventListener('click', () => {
    dropdown_sidebar.classList.toggle('open');
});