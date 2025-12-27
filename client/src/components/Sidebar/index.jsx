import { Link, useLocation } from "react-router-dom";
import Logo from "./Logo";
import User from "./User";
import { ROUTES } from "../../routes/paths";
import { Container, Li } from "./styled";

export default function Sidebar() {
  const location = useLocation();
  
  return (
    <Container>
        <Logo />

        <ul>
          <Li active={location.pathname === ROUTES.dashboard}>
            <Link to={ROUTES.dashboard}>
              <span class="sidebar-icon material-symbols-outlined">dashboard</span>
              <span className="sidebar-title">Dashboard</span>
            </Link>
          </Li>

          <Li active={location.pathname === ROUTES.user}>
            <Link to={ROUTES.user}>
              <span class="sidebar-icon material-symbols-outlined">group</span>
              <span className="sidebar-title">Usuários</span>
            </Link>
          </Li>

          <Li active={location.pathname === ROUTES.product}>
            <Link to={ROUTES.product}>
              <span class="sidebar-icon material-symbols-outlined">package_2</span>
              <span className="sidebar-title">Produtos</span>
            </Link>
          </Li>

          <Li active={location.pathname === ROUTES.supplier}>
            <Link to={ROUTES.supplier}>
              <span class="sidebar-icon material-symbols-outlined">factory</span>
              <span className="sidebar-title">Fornecedores</span>
            </Link>
          </Li>
        </ul>

        <User />
    </Container>
  );
}