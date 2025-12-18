import styled, { css } from "styled-components";
import { colors } from "../../styles/colors";

export const Container = styled.div`
    display: flex;
    flex-direction: column;

    width: 300px;
    padding: 10px 20px;
    border-right: 1px solid ${colors.shadow};
    background: ${colors.light};

    ul {
        display: flex;
        align-items: start;
        justify-content: start;
        flex: 1;
        flex-direction: column;
        gap: 5px;
        background-color: transparent;
    }

`;

export const SidebarItem = styled.li`
    display: flex;
    align-items: center;
    justify-content: start;
    width: 100%;
    height: 40px;

    a {
        display: flex;
        align-items: center;
        justify-content: start;

        width: 100%;
        height: 100%;

        border-radius: 5px;
        gap: 10px;
        padding: 0 10px;
    }

    a:hover {
        background-color: ${colors.shadow};
    }

    ${({ active }) => 
        active &&
        css`
            a {
                background-color: ${colors.shadow};
            }

            a .sidebar-item-name,
            a .sidebar-icon {
                color: ${colors.primary};
            }
        `
    }

    .sidebar-icon, .sidebar-item-name {
        font-size: 18px;
        font-weight: 500;
        color: ${colors.dark};
    }

    .sidebar-icon {
        font-size: 25px;
    }
`;
