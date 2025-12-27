import MainLayout from "../../layouts/MainLayout";

export default function Dashboard() {
    const pageData = {
        title: "Dashboard",
    }
    
    return (
        <MainLayout pageData={pageData}/>
    );
}