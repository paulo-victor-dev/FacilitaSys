import { Routes, Route } from "react-router-dom";
import { ROUTES } from "./paths";
import Dashboard from "../pages/Dashboard";
import Users from "../pages/Users";
import Products from "../pages/Products";
import Suppliers from "../pages/Suppliers";

export default function AppRoutes() {
    return (
        <Routes>
            <Route path={ROUTES.dashboard} element={<Dashboard />} />
            <Route path={ROUTES.users} element={<Users />} />
            <Route path={ROUTES.products} element={<Products />} />
            <Route path={ROUTES.suppliers} element={<Suppliers />} />

            <Route path={ROUTES.notFound} element={<p>Not Found</p>} />
        </Routes>
    );
}