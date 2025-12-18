import User from "./User";
import { Container } from "./styled";

export default function Header() {
    return (
        <Container>
            <span className="menu-icon material-symbols-outlined">menu</span>
            <User />
        </Container>
    );
}