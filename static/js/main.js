const body = document.querySelector("body"),

    sidebar = body.querySelector("aside"),
    btn_toggle = sidebar.querySelector(".btn_toggle"),

    msg = body.querySelector('.message_area'),

    input_doc = body.querySelector('#doc');

const submenuButtons = [
    sidebar.querySelector("#submenu_btn1"),
    sidebar.querySelector("#submenu_btn2"),
];

const submenus = [
    sidebar.querySelector("#submenu1"),
    sidebar.querySelector("#submenu2"),
];

const arrows = [
    sidebar.querySelector("#arrow1"),
    sidebar.querySelector("#arrow2"),
];
    

// Sidebar close events
btn_toggle.addEventListener("click", () => {
    if (submenu1.classList.contains("open") || submenu2.classList.contains("open")) {
        submenu1.classList.remove("open");
        submenu2.classList.remove("open");
    };

    if (arrow1.classList.contains("rotate") || arrow2.classList.contains("rotate")) {
        arrow1.classList.remove("rotate");
        arrow2.classList.remove("rotate");
    };

    sidebar.classList.toggle("close");

    const submenus = [submenu1, submenu2];

    submenus.forEach(sub => {
        if (sidebar.classList.contains("close")) {
            sub.style.setProperty("--submenu-duration", "0s");
        };
    });

    if (sidebar.classList.contains("close")) {
        setTimeout(() => {
            submenus.forEach(sub => 
                sub.style.setProperty("--submenu-duration", "0.35s")
            );
        }, 250);
    };
});

// Sidebar submenus events
function closeOthers(currentIndex) {
    submenus.forEach((submenu, i) => {
        if (i !== currentIndex && submenu.classList.contains("open")) {
            submenu.classList.remove("open");
            arrows[i].classList.remove("rotate");
        }
    });
}

submenuButtons.forEach((btn, index) => {
    btn.addEventListener("click", () => {
        closeOthers(index);
        submenus[index].classList.toggle("open");
        arrows[index].classList.toggle("rotate");
    });
});

document.addEventListener("click", (event) => {
    if(
        !sidebar.contains(event.target) &&
        !submenuButtons.some(btn => btn.contains(event.target))
    ) {
        submenus.forEach((submenu, i) => {
            if (submenu.classList.contains("open")) {
                submenu.classList.remove("open");
                arrows[i].classList.remove("rotate");
            }
        });
    }
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

// Input events
document.addEventListener('DOMContentLoaded', () => {
    const form_search = body.querySelector('#form_search');
    const input_search = body.querySelector('#input_search');
    const search_icon = body.querySelector('.search_icon');
    const search_btn = body.querySelector('#search_btn');


    if (form_search && input_search && search_icon) {
        function updateIcon() {
            search_icon.innerText = input_search.value ? 'close' : 'search';
        };
    
        updateIcon();
    
        input_search.addEventListener('input', updateIcon);
    
        search_btn.addEventListener('click', (e) => {
            if (input_search.value) {
                input_search.value = '';
                updateIcon();
            } 
            
            form_search.submit();
        });
    }; 
});