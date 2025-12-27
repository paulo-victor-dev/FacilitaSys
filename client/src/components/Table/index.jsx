import { TableContainer, StatusBadge } from "./styled";

export default function Table({ itensList, tableHeaders }) {
    function formatDate(date) {
        return new Date(date).toLocaleDateString("pt-BR");
    }
    
    return (
        <TableContainer>
            <table>
                <thead>
                    <tr>
                        {tableHeaders.map(header => (
                            <th>{header}</th>
                        ))}
                    </tr>
                </thead>
            
                <tbody>
                    {itensList.map(item => (
                        <tr key={item.id}>
                            <td>{item.company_name}</td>

                            <td>
                                <StatusBadge active={item.is_active}>
                                    {item.is_active ? "Ativo" : "Inativo"}
                                </StatusBadge>
                            </td>
                            
                            <td>{formatDate(item.created_at)}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </TableContainer>
    );
}
