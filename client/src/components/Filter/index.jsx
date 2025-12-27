import { useState } from "react";
import { Form } from "./styled";
import Dropdown from "./Dropdown";

export default function Filter() {
    const [searchValue, setSearchValue] = useState("");
    
    return (
        <Form>
            <div className="dropdowns-area">
                <Dropdown title={"Status"} itens={["Ativo", "Inativo"]}/>
            </div>

            <div className="search-area">
                <span class="search-icon material-symbols-outlined">search</span>

                <input 
                    className="search-input"
                    type="text"
                    value={searchValue} 
                    onChange={e => setSearchValue(e.target.value)}
                    placeholder="Pesquise na tabela..."
                />
            </div>
        </Form>
    );
}