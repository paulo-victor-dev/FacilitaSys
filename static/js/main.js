const body = document.querySelector("body"),
      sidebar = body.querySelector(".sidebar"),
      btn_toggle = body.querySelector(".btn_toggle"),
      user_area = body.querySelector(".user_area");

btn_toggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    
});

user_area.addEventListener("click", () => {
    user_area.classList.toggle("active")
});