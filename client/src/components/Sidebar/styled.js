import styled, { css } from "styled-components";
import { colors } from "../../styles/colors";

export const Container = styled.div`
    display: flex;
    flex-direction: column;
    width: 300px;
    padding: 20px;
    background: none;

    ul {
        display: flex;
        flex-direction: column;
        flex: 1;
        gap: 15px;
        margin-top: 50px;
    } 
`;

export const Li = styled.li`
    display: flex;
    align-items: center;
    height: 50px;
    border-radius: 10px;
    transition: all 0.2s;
    
    a {
        display: flex;
        align-items: center;
        justify-content: start;
        font-weight: 600;
        width: 100%;
        height: 100%;
        gap: 15px;
        padding: 0 10px;
        color: ${colors.dark};
    }

    &:hover {
        background-color: ${colors.light};
        box-shadow: 0 0 6px 1px ${colors.shadow};
    }

    &:hover .sidebar-title {
        color: ${colors.primary};
    }

    &:hover .sidebar-icon {
        color: ${colors.primary};
    }

    ${({active}) => 
        active &&
        css`
           & {
            background-color: ${colors.light};
            box-shadow: 0 0 6px 1px ${colors.shadow};
           }

           .sidebar-title, .sidebar-icon {
            color: ${colors.primary};
           }
        `
    }
`;