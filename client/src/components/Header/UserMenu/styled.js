import styled, { css } from "styled-components";
import { colors } from "../../../styles/colors";

export const Container = styled.div`
    opacity: 0;
    visibility: hidden;
    position: absolute;
    top: 25px;
    right: 0;
    border: 1px solid ${colors.shadow};
    border-radius: 5px;
    background-color: ${colors.light};
    transform: translateY(0);
    transition: opacity 0.2s, visibility 0.2s, transform 0.2s;

    ${({ menuIsOpen }) => 
        menuIsOpen &&
        css`
            opacity: 1;
            visibility: visible;
            transform: translateY(10px);
        `
    }

    ul {
        display: flex;
        align-items: start;
        justify-content: center;
        flex-direction: column;
        gap: 5px;
        padding: 10px;
    }

    li {
        display: flex;
        align-items: center;
        width: 100%;
        height: 30px;
        

        & > a:hover {
            border-radius: 5px;
            background-color: ${colors.shadow};
        }
    }

    a {
        display: flex;
        align-items: center;
        justify-content: start;
        width: 100%;
        height: 100%;
        padding: 0 10px;
        gap: 5px;
        color: ${colors.dark};
    }
`;