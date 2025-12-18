import { Container, ImageContainer } from "./styled";

export default function Logo() {
    return (
        <Container>
            <ImageContainer>
                <img src="public/logo_facilitasys.png" alt="logo_facilitasys" />
            </ImageContainer>

            <span>FacilitaSys</span>
        </Container>
    );
}