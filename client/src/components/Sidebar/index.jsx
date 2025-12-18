import { Link, useLocation } from "react-router-dom";
import { ROUTES } from "../../routes/paths";
import Logo from "./Logo";
import { Container, SidebarItem } from "./styled";

export default function Sidebar() {
    const { pathname } = useLocation();
    
    return (
        <Container>
            <Logo />
            <ul>
                <SidebarItem active={pathname === ROUTES.dashboard}>
                    <Link to={ROUTES.dashboard}>
                        <span className="sidebar-icon material-symbols-outlined">dashboard</span>
                        <span className="sidebar-item-name">Dashboard</span>
                    </Link>
                </SidebarItem>

                <SidebarItem active={pathname === ROUTES.users}>
                    <Link to={ROUTES.users}>
                        <span className="sidebar-icon material-symbols-outlined">person</span>
                        <span className="sidebar-item-name">Usuários</span>
                    </Link>
                </SidebarItem>

                <SidebarItem active={pathname === ROUTES.products}>
                    <Link to={ROUTES.products}>
                        <span className="sidebar-icon material-symbols-outlined">package_2</span>
                        <span className="sidebar-item-name">Produtos</span>
                    </Link>
                </SidebarItem>

                <SidebarItem active={pathname === ROUTES.suppliers}>
                    <Link to={ROUTES.suppliers}>
                        <span className="sidebar-icon material-symbols-outlined">factory</span>
                        <span className="sidebar-item-name">Fornecedores</span>
                    </Link>
                </SidebarItem>
            </ul>
        </Container>
    );
}