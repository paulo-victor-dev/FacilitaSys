const body = document.querySelector("body"),

      sidebar = body.querySelector(".sidebar"),
      btn_toggle = body.querySelector(".btn_toggle"),
      dropdown_sidebar = body.querySelector(".submenu_dropdown"),

      user_area = body.querySelector(".user_area"),
      dropdown_menu = body.querySelector(".dropdown_menu"),

      add_btn = body.querySelector(".add_btn"),

      msg = body.querySelector('.message_area');

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

// Search_area events
if (add_btn) {
    add_btn.addEventListener("click", () => {
        modal.classList.toggle("open")
    })
};

// Message events
if (msg) {
    msg.classList.add('show');
    setTimeout(() => {
        msg.classList.remove('show');
    }, 3000);
};
