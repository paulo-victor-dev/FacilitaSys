import { useState, useEffect } from "react";
import MainLayout from "../../layouts/MainLayout";
import { listSupplier } from "../../services/supplier.api";

export default function Supplier() {
    const [supplierList, setSupplierList] = useState([]);
    
    const pageData = {
        title: "Fornecedores",
        
        tableData: {
            objectsList: supplierList,
        },

        filterData: {
            filteredList: "",
            fn: ""
        },

        buttonData: {   
            text: "Fornecedor",
            fn: ()=>console.log("Teste fornecedor")
        }
    }

    useEffect(() => {
        async function fetchSuppliers() {
            const resp = await listSupplier();
            setSupplierList(resp);
        }

        fetchSuppliers();
    }, []);

    return <MainLayout pageData={pageData}/>;
}