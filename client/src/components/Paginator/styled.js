import styled, { css } from "styled-components";
import { colors } from "../../styles/colors";

export const Container = styled.div`
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    padding: 15px;
    bottom: 0;

    .previus-btn, .next-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 15px;
        gap: 5px;
        padding: 10px;
        border-radius: 10px;
        transition: background-color 0.2s;

        &:hover {
            background-color: ${colors.shadow};
        }
    }
`; 

export const PaginatorButton = styled.button`
    font-size: 15px;
    border-radius: 10px;
    padding: 10px 15px;
    color: ${props => props.active ? colors.light : colors.dark};
    background-color: ${props => props.active ? colors.primary : "transparent"};
    transition: opacity 0.2s, background-color 0.2s;

    &:hover {
        opacity: ${props => props.active ? 0.8 : 1};
        background-color: ${props => props.active ? colors.primary : colors.shadow};
    }
`;