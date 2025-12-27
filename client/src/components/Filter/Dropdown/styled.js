import styled from "styled-components";
import { colors } from "../../../styles/colors";

export const Container = styled.div`
    position: relative;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px;
    gap: 20px;
    border: 2px solid ${colors.shadow};
    border-radius: 10px;
    cursor: pointer;
`;

export const DropdownButtons = styled.div`
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 5px;

    .btns-divider {
       color: ${colors.shadow};
    }

    .dropdown-icon-close {
        visibility: ${props => props.menuItem ? "visible" : "hidden"};
        transition: opacity 0.2s;

        &:hover {
            opacity: 0.5;
        }
    }

    .dropdown-icon-arrow {
        transform: ${props => props.menuIsActive ? "rotate(180deg)" : "rotate(0deg)"};
        transition: transform 0.2s;
    }
`;

export const DropdownMenu = styled.div`
    visibility: ${props => props.menuIsActive ? "visible" : "hidden"};
    opacity: ${props => props.menuIsActive ? 1 : 0};
    transform: ${props => props.menuIsActive ? "translateY(10px)" : "translateY(-10px)"};
    
    
    position: absolute;
    z-index: 1000;
    
    display: flex;
    flex-direction: column;
    
    width: 100%;
    gap: 5px;
    padding: 10px;
    border: 2px solid ${colors.shadow};
    border-radius: 10px;
    
    right: 0;
    top: 40px;

    background-color: ${colors.light};

    transition: all 0.1s;
    
    li {
        cursor: pointer;
        padding: 5px;
        border-radius: 10px;
        transition: background-color 0.2s;
        
        &:hover {
            background-color: ${colors.shadow};
        }
    }
    
    
`;