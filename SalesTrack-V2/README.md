# Versão 2: Aplicação com API REST

O grande salto desta versão foi a separação total entre dados e interface, transformando o backend em uma API robusta e organizada.

### 🛠 Aspectos Técnicos
- **Arquitetura:** Desacoplada (Client-Server) utilizando o padrão REST.
- **Estrutura de Pastas (Organização Profissional):** - `routes/`: Gerenciamento das rotas da API.
  - `services/`: Lógica de negócio isolada.
  - `repositories/`: Camada de interação direta com o banco de dados (MySQL).
- **Configurações (.vscode):** Inclui um arquivo JSON de configuração para o ambiente de desenvolvimento, responsável por limpar e ocultar arquivos de cache (como `__pycache__`) da estrutura de visualização do código, mantendo o workspace limpo.

**Objetivo alcançado:** Criação de um backend escalável e organizado para consumo externo.