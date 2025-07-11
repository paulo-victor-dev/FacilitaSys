const body = document.querySelector("body"),

      sidebar = body.querySelector(".sidebar"),
      btn_toggle = body.querySelector(".btn_toggle"),
      dropdown_sidebar = body.querySelector(".submenu_dropdown"),

      user_area = body.querySelector(".user_area"),
      dropdown_menu = body.querySelector(".dropdown_menu"),

      msg = body.querySelector('.message_area'),

      input_doc = body.querySelector('#doc');

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

// Message events
if (msg) {
    msg.classList.add('show');
    setTimeout(() => {
        msg.classList.remove('show');
    }, 3500);
};

// CPF/CNPJ mask
if (input_doc) {
    input_doc.addEventListener('input', () => {
        let v = input_doc.value.replace(/\D/g, '');

        if (v.length <= 11) {
            v = v.replace(/(\d{3})(\d)/, '$1.$2');
            v = v.replace(/(\d{3})(\d)/, '$1.$2');
            v = v.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
        } else {
            v = v.replace(/^(\d{2})(\d)/, '$1.$2');
            v = v.replace(/^(\d{2})\.(\d{3})(\d)/, '$1.$2.$3');
            v = v.replace(/\.(\d{3})(\d)/, '.$1/$2');
            v = v.replace(/(\d{4})(\d)/, '$1-$2');
        }

        input_doc.value = v;
    });
};
