import Sidebar from "../../components/Sidebar";
import Header from "../../components/Header";
import Filter from "../../components/Filter";
import Table from "../../components/Table";
import Paginator from "../../components/Paginator";
import { LayoutContainer } from "./styled";
import { useState } from "react";

export default function MainLayout({ pageData }) {
    const {title, btnData, itensList, tableHeaders} = pageData;

    const [filteredList, setFilteredList] = useState([]);

    return (
        <LayoutContainer>
            <Sidebar />
            <main>
                <Header title={title} btnData={btnData}/>

                <div className="divider"/>

                <Filter />
        
                <Table itensList={itensList} tableHeaders={tableHeaders}/>

                <Paginator />
            </main>
        </LayoutContainer>
    );
}