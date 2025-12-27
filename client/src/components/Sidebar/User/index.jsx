import { Container } from "./styled";

export default function User() {
  function handleLogout() {
    alert("Logout");
  }

  function handleConfig() {
    alert("Configurações");
  }
  
  return (
    <Container>
      <div className="user-area">
        <span className="user-account-icon material-symbols-outlined">account_circle</span>

        <div className="user-info">
          <span className="user-name">Paulo Victor</span>
          <span className="user-role">Administrador</span>
        </div>
      </div>

      <div className="user-btns">
          <span className="user-logout-icon material-symbols-outlined" title="Logout" onClick={handleLogout}>logout</span>
       
          <span className="user-config-icon material-symbols-outlined" title="Configurações" onClick={handleConfig}>settings</span>
      </div>
    </Container>
  );
}