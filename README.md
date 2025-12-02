

1. **Adotando um modelo otimizado e profissional de configuração para Ruff + Black + Airflow + Poetry + pre-commit, balanceando padronização e desempenho (usado em pipelines CI/CD de projetos reais de dados e airflow):**
. pyenv
. pydantic
. poetry
. pytest

Exemplo: consulta https://pandera.readthedocs.io/en/stable/
. pandera
versões de python que serão aceitas no projeto
No caso o Pandera precisa do python 3.11, então será usada para iniciar o projeto



2. Configure a versão correta do Python com `pyenv` (versionar o python, multiplas versões de python):

```bash
pyenv install 3.11.5
pyenv local 3.11.5
```

3. **Configurar poetry para Python version 3.11.5 e ative o ambiente virtual:**
poetry resolver todos os problemas de path do windows

```bash
poetry init
poetry env use 3.11.5
poetry shell

```

4. **Instale as dependencias do projeto:**

```bash
poetry install --no-root
```
Obs: instala todas as dependências, mas não instala o projeto atual como pacote.


5. **Instalando o Ruff no Ambiente Virtual**

. Para eliminar o erro 'ruff' não é reconhecido como um comando interno

```bash
poetry show ruff (confirma a instalação)
poetry add --group dev ruff
```

### O Ruff vai corrigir automaticamente:

1. Espaçamento
2. Imports desnecessários,
3. Indentação,
4. Linhas em branco extras, etc.

6. **Executando mkdocs -  Opcionais**

```bash
poetry add mkdocs
mkdocs new .
poetry run mkdocs serve

```

7. **Instale os Hooks de Pré-commit:**
    O projeto utiliza [pre-commit hooks](https://pre-commit.com/) para garantir a qualidade e a padronização do código antes de cada commit. Para ativá-los, execute:

    ```bash
    1 - poetry add --dev pre-commit
    2 - poetry run pre-commit install

    ```

   **Explicação:**
     ```bash
     1 -  --dev adiciona o pre-commit como dependência de desenvolvimento (não será incluído em produção).
     2 -    Isso registra automaticamente o pacote no seu pyproject.toml e poetry.lock.
     ```
