import styled from "styled-components";
import { colors } from "../../../styles/colors";

export const Container = styled.div`
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;

    .img-bg {
        display: flex;
        padding: 10px;
        border-radius: 10px;
        background-color: ${colors.primary};
        box-shadow: 0 0 3px ${colors.primary};
    }

    img {
        width: 30px;
    }

    .logo-init, .logo-last {
        font-family: "Bricolage Grotesque", sans-serif;
        font-size: 25px;
        font-weight: 500;
        
    }

    .logo-init {
        color: ${colors.primary};
        text-shadow: 0 0 0.5px ${colors.primary};
    }

    .logo-last {
        color: ${colors.info};
        text-shadow: 0 0 1px ${colors.info};
    }
`;