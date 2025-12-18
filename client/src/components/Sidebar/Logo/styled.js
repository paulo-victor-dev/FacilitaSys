import styled from "styled-components";
import { colors } from "../../../styles/colors";

export const Container = styled.div`
    display: flex;
    align-items: center;
    justify-content: start;
    gap: 10px;
    margin-bottom: 40px;

    span {
        font-size: 20px;
        font-weight: 500;
    }
`;

export const ImageContainer = styled.div`
    display: inline-block;
    line-height: 0;
    padding: 10px;
    border-radius: 5px;
    background-color: ${colors.dark};
    
    img {
            display: block;
            width: 20px;
        }
`;