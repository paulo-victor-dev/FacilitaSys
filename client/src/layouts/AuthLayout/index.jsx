import { LayoutContainer } from "./styled";

export default function AuthLayout({ children }) {
    return (
        <LayoutContainer>
            {children}
        </LayoutContainer>
    );
}