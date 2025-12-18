import { useState } from "react";
import UserMenu from "../UserMenu";
import { Container } from "./styled";

export default function User() {
  const [menuIsOpen, setMenuIsOpen] = useState(false);
  
  function handleMenuIsOpen(e) {
    const newMenuIsOpen = !menuIsOpen;
    setMenuIsOpen(newMenuIsOpen);
  }

  return (
      <Container rotateArrow={menuIsOpen} onClick={e => handleMenuIsOpen(e)}>
        <span className="user-icon material-symbols-outlined">account_circle</span>
        <span className="user-name">Paulo Victor</span>
        <span className="user-arrow material-symbols-outlined">arrow_drop_down</span>

        <UserMenu menuIsOpen={menuIsOpen}/>
      </Container>  
    );
}