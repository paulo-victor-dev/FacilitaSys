import styled from "styled-components";
import { colors } from "../../styles/colors";

export const LayoutContainer = styled.div`
    display: flex;
    height: 100%;
`;

export const Main = styled.div`
    display: flex;
    flex-direction: column;
    width: 100%;
`;

export const Content = styled.div`
    display: flex;
    flex: 1;
    margin: 15px;
    padding: 10px;
    border: 1px solid ${colors.shadow};
    border-radius: 5px;
    box-shadow: 0 0 3px ${colors.shadow};
    background-color: ${colors.light};
`;

