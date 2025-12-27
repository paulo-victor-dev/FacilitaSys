import styled from "styled-components";
import { colors } from "../../styles/colors";

export const LayoutContainer = styled.div`
    display: flex;
    height: 100%;

    .divider {
        height: 2px;
        margin: 20px 0;
        background-color: ${colors.shadow};
    }

    main {
        display: flex;
        flex-direction: column;
        flex: 1;
        margin: 20px 20px 20px 0;
        padding: 30px;
        border-radius: 30px;
        box-shadow: 0 0 6px 2px ${colors.shadow};
        background-color: ${colors.light};
    }


`;

