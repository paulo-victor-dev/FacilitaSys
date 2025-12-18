import styled, { css } from "styled-components";

export const Container = styled.div`
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;

    .user-icon {
        font-size: 26px;
        margin-right: 5px;
    }

    .user-arrow {
        transition: transform 0.2s;
    }

    ${({ rotateArrow }) => 
        rotateArrow && 
        css`
            .user-arrow {
                transform: rotate(180deg);
            }
        `
    }
`;