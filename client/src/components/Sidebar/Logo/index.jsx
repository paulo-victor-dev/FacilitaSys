import { Container } from "./styled";

export default function Logo() {
  return (
    <Container>
        <div className="img-bg">
            <img src="public\logo_facilitasys.png" alt="logo_facilitasys" />
        </div>
        <div>
            <span className="logo-init">Facilita</span>
            <span className="logo-last">Sys</span>
        </div>
    </Container>
  );
}