const body = document.querySelector("body"),
      sidebar = body.querySelector("nav"),
      menu = body.querySelector("#btn_menu");

menu.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    
});