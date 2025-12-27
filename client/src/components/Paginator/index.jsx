import { Container, PaginatorButton } from "./styled";

export default function Paginator() {
    const itensPerPage = 10;
    
    return (
        <Container>
            <button className="previus-btn">
                <span class="material-symbols-outlined">arrow_back</span>
                Anterior
            </button>
            
            <PaginatorButton active={true}>1</PaginatorButton>
            <PaginatorButton active={false}>2</PaginatorButton>
            <PaginatorButton active={false}>3</PaginatorButton>
            
            <button className="next-btn">
                Próxima
                <span class="material-symbols-outlined">arrow_forward</span>
            </button>
        </Container>
    );
}
