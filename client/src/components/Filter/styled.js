import styled from "styled-components";
import { colors } from "../../styles/colors";

export const Form = styled.form`
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 20px;

    .dropdowns-area {
        display: flex;
        align-items: center;
        gap: 15px;
    }

    .search-area {
        display: flex;
        align-items: center;
        padding: 10px;
        gap: 5px;
        border: 2px solid ${colors.shadow};
        border-radius: 10px;
        transition: all 0.1s;

        &:has(.search-input:focus) {
           box-shadow: 0 0 6px 1px ${colors.shadow};
        }
        &:has(.search-input:focus) .search-icon {
            opacity: 0.4;
        }

        & .search-icon {
            opacity: 0.2;
            transition: opacity 0.1s;
        }

        & .search-input {
            font-size: 14px;
            border: none;

            &:focus {
                outline: none;
            }
        }

        
    }

    
`;