# AiPdfReader

## Descricao
    - Api em que o usuario ira fazer o upload de um arquivo PDF, e a IA generativa(No projeto esta sendo utilizado o Gemini) irá ler o pdf e poderá fazer uma pergunta sobre o pdf que foi realizado o upload.

    - A api foi contruída utilizando FastApi, MongoDB para armazenar os nomes dos PDFs, conteúdo do pdf, a pergunta feita, e a resposta da Ia.

## Instrução de instalacão

### Pre requisitos
 - Python 3.12.6
 - IDE
 - Docker
 - Git
 - python-dotenv

 ### Guia

 #### Utilize o git clone no seu terminal para clonar o repositorio, e clone dentro da sua pasta desejada.

 ```bash
git clone https://github.com/PedroAntonio2510/AiPdfReader
 ```

 #### Dentro do repositório, inicialize um ambiente virtual e crie um arquivo .env e utilize o comando no terminal:
 ```bash
python3 -m venv venv
source venv/bin/activate
pip install python-dotenv
 ```

 ### Dentro do arquivo .env, crie tres variáveis de ambiente, e dentro delas voce colocará sua Api Key do gemini do google, e seu username e password do mongo cloud atlas(que é o banco onde está hospedado): 

    GOOGLE_API_KEY="<YOUR-API-KEY>"
    DB_USERNAME="<your-username>"
    DB_PASSWORD="<your-password>"
#
    Links para pegar os dados do mongodb e a api do gemini: https://cloud.mongodb.com/v2#/org/66f6e1c60886094f0a351a91/projects
    https://aistudio.google.com/app/prompts/new_chat


 #### Entre na pasta do repositorio pelo terminal utilizando cd AiPdfReader, ou abra direto na sua IDE e acesse pelo terminal da IDE. Utilize os comandos docker na seguinte sequencia:

 ```bash
docker build -t fastapi-aipdf . 

docker run -d -p 8000:8000 fastapi-aipdf

 ```

 ### Acesse a porta: 
  - http://localhost:8000/



 



    