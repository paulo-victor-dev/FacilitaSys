import { Container } from "./styled";

export default function Filter() {
    return (
        <Container>
            <span class="material-symbols-outlined">search</span>
            <input type="search" />
        </Container>
    );
}