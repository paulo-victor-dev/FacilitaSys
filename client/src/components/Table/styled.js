import styled from "styled-components";
import { colors } from "../../styles/colors";


export const TableContainer = styled.div`
    width: 100%;
    height: 400px;
    flex: 1;
    padding: 10px 15px;
    border-radius: 10px;
    border: 2px solid ${colors.shadow};

    table {
        width: 100%;
        border-spacing: 0;
        text-align: left;

        thead {
            background-color: ${colors.shadow};

            th {
                font-size: 12px;
                padding: 15px;
                text-transform: uppercase;
                letter-spacing: 1px;
                opacity: 0.6;
            }

            th:first-child {
                border-radius: 10px 0 0 10px;
            }

            th:last-child {
                border-radius: 0 10px 10px 0;
            }
        }

        tbody {
            td {
                font-size: 14px;
                padding: 15px;
                border-bottom: 1px solid ${colors.shadow};
                
                &:first-child {
                    cursor: pointer;
                    font-weight: 500;
                    color: ${colors.primary};

                    &:hover {
                        text-decoration: underline;
                    }
                }
            }
        
            tr:last-child td {
                border: none;
            }
        }
    }
`;

export const StatusBadge = styled.span`
    padding: 5px 10px;
    border-radius: 5px;
    color: ${props => props.active ? colors.success : colors.danger};
    background-color: ${props => props.active ? colors.successBg : colors.dangerBg};
`;