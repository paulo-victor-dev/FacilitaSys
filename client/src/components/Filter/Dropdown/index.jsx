import { useState } from "react";
import { Container, DropdownMenu, DropdownButtons } from "./styled";

export default function Dropdown({ title, itens }) {
    const [menuIsActive, setMenuIsActive] = useState(false);
    const [menuItem, setMenuItem] = useState("");

    function handleRemove(e) {
        e.stopPropagation();
        setMenuItem("");
    }

    return (
        <Container onClick={() => setMenuIsActive(!menuIsActive)}>
            <span className="dropdown-title">
                {menuItem ? `${title}: ${menuItem}` : title}
            </span>

            <DropdownButtons menuItem={menuItem} menuIsActive={menuIsActive}>
                <span className="dropdown-icon-close material-symbols-outlined" onClick={handleRemove}>close</span>
                  
                <span className="btns-divider">|</span>

                <span className="dropdown-icon-arrow material-symbols-outlined">keyboard_arrow_down</span>
            </DropdownButtons>

            <DropdownMenu menuIsActive={menuIsActive}>
                {itens.map((item, i) => (
                    <li key={i} onClick={() => setMenuItem(item)}>
                        <span>{item}</span>
                    </li>
                ))}
            </DropdownMenu>
        </Container>
    );
}