# 🎬 StreamBox: Avalie Filmes, Ganhe Tokens!

![image](https://github.com/user-attachments/assets/b1c6923a-ec55-429d-9aac-000f77016f0f)

StreamBox: Sua voz vale tokens. Descubra, avalie e seja recompensado!

---

## 📝 Descrição

O **StreamBox** é um projeto inovador que une a paixão por filmes e séries com o universo blockchain. Desenvolvido como parte do programa **Transfero Academy**, nosso objetivo é criar uma plataforma onde os usuários podem descobrir e avaliar seus filmes e séries favoritos, sendo **recompensados com tokens digitais** por suas contribuições.

Acreditamos que a opinião do espectador é valiosa e deve ser reconhecida. Com o CineCritique, cada avaliação se transforma em um ativo, incentivando a participação e construindo uma comunidade engajada e descentralizada de críticos de cinema.

---

## ✨ Funcionalidades (Em Desenvolvimento)

Este projeto está em **desenvolvimento ativo**, com novas funcionalidades sendo implementadas e aprimoradas continuamente. As principais funcionalidades planejadas e em andamento incluem:

* **Autenticação Segura:** Cadastro e login de usuários para acesso personalizado.
* **Catálogo de Filmes e Séries:** Navegação e busca por um vasto acervo de títulos.
* **Detalhes Abrangentes:** Visualização de informações completas sobre cada título (sinopse, elenco, diretores, trailers, etc.).
* **Sistema de Avaliação:** Capacidade de atribuir notas e deixar comentários detalhados sobre filmes e séries.
* **Recompensa em Tokens:** **Recebimento de tokens ERC-20** (a ser definido, ex: `$CRITIQUE`) na carteira do usuário a cada avaliação válida submetida.
* **Perfil do Usuário:** Dashboard pessoal com histórico de avaliações e saldo de tokens.
* **Integração Blockchain:** Interação com um contrato inteligente desenvolvido em Solidity para a emissão e gerenciamento de tokens.

---

## 🛠️ Tecnologias Utilizadas

Este projeto full-stack está sendo construído com uma combinação poderosa de tecnologias:

**Frontend:**
* **HTML5:** Estrutura fundamental das páginas web.
* **CSS3:** Estilização responsiva e design moderno da interface do usuário.
* **JavaScript:** Interatividade dinâmica no lado do cliente.

**Backend:**
* **Python:** Linguagem principal para a lógica de negócio do servidor.
* **Django:** Framework web de alto nível para desenvolvimento rápido e seguro do backend, gerenciando a API e o banco de dados.

**Blockchain/Smart Contracts:**
* **Solidity:** Linguagem para desenvolvimento do contrato inteligente ERC-20 na blockchain Ethereum (ou rede compatível).

**Banco de Dados:**
* **SQL (Sistema Gerenciador de Banco de Dados Relacional):** Para persistência dos dados de usuários, filmes e avaliações.
    

**Outras Ferramentas:**
* **Git:** Sistema de controle de versão distribuído.
* **GitHub:** Plataforma para hospedagem do código-fonte e colaboração.

---

## 🚀 Como Rodar o Projeto Localmente (Em Desenvolvimento)

As instruções abaixo são um guia para configurar e executar o projeto. Como o projeto está em desenvolvimento, alguns passos podem ser aprimorados ou alterados.

### Pré-requisitos

Certifique-se de ter o seguinte software instalado em sua máquina:

* **Python 3.9+**
* **pip** (gerenciador de pacotes do Python)
* **Node.js (LTS)** e **npm** (para ferramentas de blockchain como Hardhat/Truffle, se aplicável, e para o ambiente de desenvolvimento frontend)
* **SQL**
* **Git**

### Instalação e Configuração

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/VictorHLF42/_transfero.git
    cd _transfero
    ```

2.  **Configurar o Ambiente Virtual (Python):**
    ```bash
    python -m venv venv
    source venv/bin/activate # No Linux/macOS
    # venv\Scripts\activate   # No Windows
    ```

3.  **Instalar Dependências do Backend (Django):**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar Variáveis de Ambiente:**
    Crie um arquivo `.env` na raiz do projeto (ou na pasta do backend) e configure as variáveis essenciais, como:
    * `SECRET_KEY=sua_secret_key_aqui`
    * `DATABASE_URL=postgres://user:password@host:port/database_name` (ou variáveis separadas como `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_NAME` se for o caso)
    * `WEB3_PROVIDER_URL=http://localhost:8545` (ou URL da rede blockchain de desenvolvimento/testes, se for necessário para alguma ferramenta)
    * `CONTRACT_ADDRESS=0x...` (endereço do contrato inteligente após o deploy, se for usado)
    * `CONTRACT_ABI_PATH=caminho/para/o/abi.json` (caminho para o arquivo ABI do contrato, se for usado)

5.  **Configurar o Banco de Dados:**
    * Certifique-se de que seu servidor de banco de dados (`[Nome do seu SGBD SQL]`) esteja rodando.
    * Crie um banco de dados vazio com o nome especificado em seu `DATABASE_URL` (ex: `cinecritique_db`).
    * Execute as migrações do Django:
        ```bash
        python manage.py makemigrations
        python manage.py migrate
        ```

6.  **Desenvolvimento e Deploy do Contrato Inteligente (Opcional - para testar a parte blockchain):**
    * Navegue até a pasta do contrato (ex: `contracts/` ou `blockchain/`).
    * Instale as dependências Node.js (se houver): `npm install`
    * Compile o contrato: `npx hardhat compile` (ou comando equivalente para Truffle).
    * Deploy para uma rede de desenvolvimento local (ex: Ganache ou Hardhat Network): `npx hardhat run scripts/deploy.js --network localhost`
    * Atualize o `CONTRACT_ADDRESS` e `CONTRACT_ABI_PATH` (se usados) no seu arquivo `.env` ou em arquivos de configuração do frontend com os dados do contrato recém-implantado.

### Executando o Projeto

1.  **Inicie o servidor de desenvolvimento Django:**
    ```bash
    python manage.py runserver
    ```
    O backend estará acessível em `http://127.0.0.1:8000/`.

---

## 📸 Screenshots (Em Breve!)

_As screenshots serão adicionadas à medida que o desenvolvimento da interface avançar e as funcionalidades visuais forem finalizadas._

* ![Screenshot da Página de Login](assets/screenshot_login.png)
    _Página de Login do CineCritique, o portal de entrada para suas avaliações._

* ![Screenshot da Página de Cadastro](assets/screenshot_cadastro.png)
    _Formulário de Cadastro, sua primeira etapa para se juntar à nossa comunidade._

_Em breve: Imagens do catálogo de filmes, tela de detalhes de um título, e o histórico de avaliações com tokens!_

---

## 🤝 Contribuição

Este projeto está sendo desenvolvido em grupo. Para contribuições externas, por favor, entre em contato com um dos autores. Se você é um membro da equipe, siga o fluxo de trabalho definido no projeto:

1.  Crie uma nova branch para sua feature (`git checkout -b feature/nome-da-feature`).
2.  Faça suas alterações e commit (`git commit -m 'feat: Adiciona nova funcionalidade X'`).
3.  Envie suas alterações para a branch original (`git push origin feature/nome-da-feature`).
4.  Abra um Pull Request para revisão de código.

---

## 📚 Aprendizado na Transfero Academy

O **StreamBox** é um projeto culminante de nosso aprendizado na **Transfero Academy**. Ele nos permitiu aplicar e aprofundar conhecimentos em:

* **Desenvolvimento Web Full-Stack:** Integração robusta de frontend (HTML, CSS, JS) com backend (Python/Django).
* **Bancos de Dados Relacionais (SQL):** Modelagem e gerenciamento de dados persistentes.
* **Desenvolvimento Blockchain (Web3):** Criação de Smart Contracts em Solidity e interação com a blockchain.
* **APIs RESTful:** Construção de interfaces para comunicação entre o frontend, backend e blockchain.
* **Versionamento com Git e GitHub:** Colaboração eficiente em equipe.
* **Metodologias Ágeis:** Práticas de desenvolvimento em um ambiente de equipe.

Este projeto reforça nossa compreensão de como as tecnologias tradicionais e descentralizadas podem se complementar para criar experiências de usuário inovadoras.

---

## 🧑‍💻 Autores

Este projeto está sendo desenvolvido com dedicação e empenho pela turma da **Transfero Academy**, sob a mentoria e auxílio de nosso professor:

* **Professor: William**
* **Membros da Equipe:**
    * **Victor Hugo Lopes Fernandes de Souza** - [Link para seu perfil do GitHub]([https://github.com/seu-usuario](https://github.com/VictorHLF42)) / [Link para seu LinkedIn](https://www.linkedin.com/in/seu-linkedin)
    

---

## ⚖️ Licença

Este projeto está licenciado sob a licença [Nome da Licença, ex: MIT License]. Consulte o arquivo [LICENSE.md](LICENSE/LICENSE.md) para mais detalhes.
