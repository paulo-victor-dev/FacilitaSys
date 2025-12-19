import { Routes, Route } from "react-router-dom";
import { ROUTES } from "./paths";
import Dashboard from "../pages/Dashboard";
import User from "../pages/User";
import Product from "../pages/Product";
import Supplier from "../pages/Supplier";

export default function AppRoutes() {
    return (
        <Routes>
            <Route path={ROUTES.dashboard} element={<Dashboard />} />
            <Route path={ROUTES.user} element={<User />} />
            <Route path={ROUTES.product} element={<Product />} />
            <Route path={ROUTES.supplier} element={<Supplier />} />

            <Route path={ROUTES.notFound} element={<p>Not Found</p>} />
        </Routes>
    );
}