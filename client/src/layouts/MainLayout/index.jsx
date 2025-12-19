import Sidebar from "../../components/Sidebar";
import Header from "../../components/Header";
import Filter from "../../components/Filter";
import Table from "../../components/Table";
import * as styled from "./styled";

export default function MainLayout({ pageData }) {
    const {title, buttonData} = pageData;

    return (
        <styled.LayoutContainer>
            <Sidebar />
            <styled.Main>
                <Header />

                <styled.Content>
                    <styled.ContentHeader>
                        <span className="header-title">{title}</span>

                        <button onClick={buttonData.fn}>
                            <span class="material-symbols-outlined">add</span>

                            <span className="btn-text">
                                {`Novo ${buttonData.text}`}
                            </span>
                        </button>
                    </styled.ContentHeader>

                    <styled.ContentBody>
                        <Filter />
                        <Table />
                    </styled.ContentBody>
                </styled.Content>
            </styled.Main>
        </styled.LayoutContainer>
    );
}