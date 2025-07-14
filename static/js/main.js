const body = document.querySelector("body"),

      sidebar = body.querySelector("aside"),
      btn_toggle = sidebar.querySelector(".btn_toggle"),
      arrow1 = sidebar.querySelector("#arrow1"),
      arrow2 = sidebar.querySelector("#arrow2"),

      submenu_btn1 = sidebar.querySelector("#submenu_btn1"),
      submenu_btn2 = sidebar.querySelector("#submenu_btn2"),

      submenu1 = sidebar.querySelector("#submenu1"),
      submenu2 = sidebar.querySelector("#submenu2"),

      msg = body.querySelector('.message_area'),

      input_doc = body.querySelector('#doc');

// Sidebar close events
btn_toggle.addEventListener("click", () => {
    if (submenu_btn1.classList.contains("open") || submenu_btn2.classList.contains("open")) {
        submenu_btn1.classList.remove("open");
        submenu_btn2.classList.remove("open");
    };

    sidebar.classList.toggle("close");
});

// Sidebar submenus events
submenu_btn1.addEventListener("click", () => {
    submenu1.classList.toggle("open");
    arrow1.classList.toggle("rotate");
});

submenu_btn2.addEventListener("click", () => {
    submenu2.classList.toggle("open");
    arrow2.classList.toggle("rotate");
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
