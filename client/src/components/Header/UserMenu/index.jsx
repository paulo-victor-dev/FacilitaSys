import { Link } from "react-router-dom";
import { Container } from "./styled";

export default function UserMenu({ menuIsOpen }) {
    return (
        <Container menuIsOpen={menuIsOpen}>
            <ul>
                <li>
                    <Link to={"/"}>
                        <span className="user-menu-icon material-symbols-outlined">logout</span>
                        <span className="user-menu-item">Logout</span>
                    </Link>
                </li>
            </ul>
        </Container>
    );
}