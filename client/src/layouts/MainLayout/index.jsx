import Header from "../../components/Header";
import Sidebar from "../../components/Sidebar";
import { LayoutContainer, Main, Content } from "./styled";

export default function MainLayout({ children }) {
    return (
        <LayoutContainer>
            <Sidebar />
            <Main>
                <Header />
                <Content>
                    {children}
                </Content>
            </Main>
        </LayoutContainer>
    );
}