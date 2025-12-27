import { useState, useEffect } from "react";
import * as supplierApi from "../../services/supplier.api";
import MainLayout from "../../layouts/MainLayout";

export default function Supplier() {
    const [itensList, setItensList] = useState([]);
    
    const pageData = {
        title: "Fornecedores",
        btnData: {
            text: "Fornecedor",
            btnFn: () => alert("Clicou"),
        },
        itensList: itensList,
        tableHeaders: ["Nome", "Status", "Data Criação"]
    }

    useEffect(() => {
        async function fetchSupllierApi() {
            const resp = await supplierApi.listSupplier();
            setItensList(resp);
        }

        fetchSupllierApi();
    }, [])
        
    return <MainLayout pageData={pageData}/>;
}