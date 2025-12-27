import { Container } from "./styled";

export default function Header({ title, btnData }) {
    const {text, btnFn} = btnData;

    return (
        <Container>
            <span className="title">{title}</span>

            <button onClick={btnFn}>
                <span className="material-symbols-outlined">add</span>
                <span>{`Novo ${text}`}</span>
            </button>
        </Container>
    );
}