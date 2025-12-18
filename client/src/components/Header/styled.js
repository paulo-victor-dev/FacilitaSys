import styled from "styled-components";
import { colors } from "../../styles/colors";

export const Container = styled.div`
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 50px;
    padding: 0 20px;
    border-bottom: 1px solid ${colors.shadow};
    background-color: ${colors.light};
`;