import { createGlobalStyle } from "styled-components";
import { colors } from "./colors";

export const GlobalStyle = createGlobalStyle` 
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    html, body, #root {
        font-family: "Poppins", sans-serif;
        height: 100%;
        background-color: ${colors.secondary};
    }

    button {
        cursor: pointer;
        border: none;
        background: none;
    }

    a {
        text-decoration: none;
    }

    li {
        list-style: none;
    }
`;