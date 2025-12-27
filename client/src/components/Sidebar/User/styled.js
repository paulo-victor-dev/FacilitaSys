import styled from "styled-components";

export const Container = styled.div`
    display: flex;
    align-items: center;
    justify-content: space-between;

    .user-area {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 5px;
    }

    .user-account-icon {
        font-size: 35px;
    }

    .user-info {
        display: flex;
        flex-direction: column;
    }

    .user-name {
        font-size: 15px;
        font-weight: 500;
    }

    .user-role {
        font-size: 13px;
        opacity: 0.5;
    }

    .user-btns {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
    }

    .user-logout-icon, .user-config-icon {
        font-size: 26px;
        cursor: pointer;
        transition: opacity 0.2s;
    }

    .user-logout-icon:hover, .user-config-icon:hover {
        opacity: 0.5;
    }
`;