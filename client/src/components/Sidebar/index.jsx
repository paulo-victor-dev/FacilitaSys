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

                <SidebarItem active={pathname === ROUTES.user}>
                    <Link to={ROUTES.user}>
                        <span className="sidebar-icon material-symbols-outlined">person</span>
                        <span className="sidebar-item-name">Usuários</span>
                    </Link>
                </SidebarItem>

                <SidebarItem active={pathname === ROUTES.product}>
                    <Link to={ROUTES.product}>
                        <span className="sidebar-icon material-symbols-outlined">package_2</span>
                        <span className="sidebar-item-name">Produtos</span>
                    </Link>
                </SidebarItem>

                <SidebarItem active={pathname === ROUTES.supplier}>
                    <Link to={ROUTES.supplier}>
                        <span className="sidebar-icon material-symbols-outlined">factory</span>
                        <span className="sidebar-item-name">Fornecedores</span>
                    </Link>
                </SidebarItem>
            </ul>
        </Container>
    );
}