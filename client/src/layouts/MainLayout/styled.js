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
    flex-direction: column;
    flex: 1;
    margin: 15px;
    padding: 20px;
    border: 1px solid ${colors.shadow};
    border-radius: 5px;
    box-shadow: 0 0 3px ${colors.shadow};
    background-color: ${colors.light};
`;

export const ContentHeader = styled.div`
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    margin-bottom: 30px;

    .header-title {
        font-size: 20px;
        font-weight: 600;
    }

    button {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 40px;
        gap: 5px;
        padding: 5px 10px;
        border-radius: 5px;
        border: 2px solid ${colors.shadow};
        color: ${colors.dark};
        background-color: ${colors.light}
    }

    .btn-text {
        font-size: 15px;
        font-weight: 600;
    }

    button:hover {
        background-color: ${colors.shadow}
    }
`;

export const ContentBody = styled.div`
    display: flex;
    flex: 1;
    flex-direction: column;
`;

