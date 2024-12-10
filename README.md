# Registro de Incidentes - Back-end

Este é o back-end da aplicação de registro e monitoramento de incidentes. A API foi desenvolvida em **Python** utilizando o framework **Flask**, com suporte a banco de dados **SQLite**.

---

## **Descrição**
A API fornece suporte para operações CRUD (Create, Read, Delete) para gerenciar incidentes. Também inclui suporte a documentação interativa via **Swagger**.

---

## **Instalação**

### **Pré-requisitos**
- **Python 3.8** ou superior instalado.
- **pip** (gerenciador de pacotes do Python).

### **Passos para Configuração**
1. Clone este repositório no seu computador:
   ```bash
   git clone https://github.com/vitorvmonteiro/mvp-devfullstackb-backend.git
   ```

2. Navegue até o diretório clonado:
   ```bash
   cd mvp-devfullstackb-backend
   ```

3. Crie um ambiente virtual para o Python (recomendado):
   ```bash
   python -m venv venv
   ```

4. Ative o ambiente virtual:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/macOS**:
     ```bash
     source venv/bin/activate
     ```

5. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Como executar**
1. Inicie o servidor:
   ```bash
   python app.py
   ```

2. Acesse a API no navegador:
   - **Base URL**: [http://127.0.0.1:5000](http://127.0.0.1:5000)
   - **Swagger UI**: [http://127.0.0.1:5000/apidocs](http://127.0.0.1:5000/apidocs)

---

## **Estrutura do Projeto**
- `app.py`: Arquivo principal da API.
- `database/`: Contém a lógica do banco de dados SQLite.
  - `__init__.py`: Configuração do banco.
  - `incidentes.py`: Modelo de dados.
- `requirements.txt`: Dependências do projeto.

---

## **Licença**
Este projeto é de uso interno e acadêmico. Modificações são bem-vindas, mas devem ser mencionadas ao autor.
