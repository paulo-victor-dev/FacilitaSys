const body = document.querySelector("body"),
      sidebar = body.querySelector(".sidebar"),
      btn_toggle = body.querySelector(".btn_toggle"),
      user_area = body.querySelector(".user_area"),
      dropdown_menu = body.querySelector(".dropdown_menu"),
      add_btn = body.querySelector(".add_btn"),
      modal = body.querySelector(".modal_bg"),
      dropdown_sidebar = body.querySelector(".submenu_dropdown"),
      modal_close_icon = body.querySelector(".modal_close_icon");

// Sidebar events
btn_toggle.addEventListener("click", () => {
    if (dropdown_sidebar.classList.contains("open")) {
        dropdown_sidebar.classList.remove("open");
    };

    sidebar.classList.toggle("close");
});

dropdown_sidebar.addEventListener("click", () => {
    if (sidebar.classList.contains("close")) {
        dropdown_sidebar.classList.remove("open")
    } else {
        dropdown_sidebar.classList.toggle("open")
    };
});
//

// User_area events
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
//

// Search_area events
if (add_btn) {
    add_btn.addEventListener("click", () => {
        modal.classList.toggle("open")
    })
};
//

// Modal events
modal_close_icon.addEventListener("click", () => {
    if (modal.classList.contains("open")) {
        modal.classList.remove("open")
    };
});
//