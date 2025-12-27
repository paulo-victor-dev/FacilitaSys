import styled from "styled-components";
import { colors } from "../../styles/colors";

export const Container = styled.div`
    display: flex;
    align-items: center;
    justify-content: space-between;

    .title {
        font-size: 22px;
        font-weight: 600;
        color: ${colors.primary};
    }

    button {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 50px;
        gap: 8px;
        padding: 10px;
        border-radius: 10px;

        font-size: 14px;
        font-weight: 600;

        color: ${colors.light};
        background-color: ${colors.primary};
        transition: opacity 0.2s;

        &:hover {
            opacity: 0.8;
        }
    }
`;