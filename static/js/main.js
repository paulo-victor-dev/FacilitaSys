const body = document.querySelector("body"),
      sidebar = body.querySelector(".sidebar"),
      btn_toggle = body.querySelector(".btn_toggle");

btn_toggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    
});