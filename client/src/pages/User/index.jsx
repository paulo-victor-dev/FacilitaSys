import MainLayout from "../../layouts/MainLayout";

export default function Users() {
    const pageData = {
            title: "Usuários",
        }
        
        return (
            <MainLayout pageData={pageData}/>
        );
}