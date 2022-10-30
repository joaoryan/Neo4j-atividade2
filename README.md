# Exercícios

## Questão 01

1. Busque pelo professor `“Teacher”` cujo nome seja **“Renzo”**, retorne o **ano_nasc** e o **CPF**.
2. Busque pelos professores `“Teacher”` cujo nome comece com a letra **“M”**, retorne o **name** e o **cpf**.
3. Busque pelos nomes de todas as cidades `“City”` e retorne-os.
4. Busque pelas escolas `“School”`, onde o number seja maior ou igual a 150 e menor ou igual a 550, retorne o nome da escola, o endereço e o número.

---

## Questão 02

1. Encontre o ano de nascimento do professor mais jovem e do professor mais velho.
2. Encontre a média aritmética para os habitantes de todas as cidades, use a propriedade **“population”**.
3. Encontre a cidade cujo **CEP** seja igual a **“37540-000”** e retorne o nome com todas as letras **“a”** substituídas por **“A”** .
4. Para todos os professores, retorne um caractere, iniciando a partir da 3ª letra do
nome.

---

## Questão 03

1. Crie a classe `TeacherCRUD()` que tenha uma relação de **composição** com a classe `Graph()` e apresente funções de CRUD na entidade `“Teacher”` do banco de dados, utilizando o `name` para fazer os MATCH’s.
    
    <aside>
    💡 Cada função da classe `TeacherCRUD()` deve criar um JSON com seu retorno por meio da função `write_a_json()`.
    
    </aside>
    
    - `create(self, name, ano_nasc, cpf) # cria um Teacher`
    - `read(self, name) # retorna apenas um Teacher`
    - `update(self, name, newCpf) # atualiza cpf com base no name`
    - `delete(self, name) # deleta Teacher com base no name`
2. Utilizando a classe `TeacherCRUD()` crie um `Teacher` com as seguintes características:
    
    ```jsx
    name: 'Chris Lima',
    ano_nasc:1956,
    cpf: '189.052.396-66'
    ```
    
3. Utilizando a classe `TeacherCRUD()` pesquise o professor com o name de `"Chris Lima"` .
4. Utilizando a classe `TeacherCRUD()` altere o cpf do `“Teacher”` de name `"Chris Lima"` para `"162.052.777-77"` .

---

## Como executar?
1. Instale as dependências:
    ```sh
    python -m pip install -r requirements.txt
    ```
2. execute o arquivo `main.py`
    ```sh
    python main.py
    ```
