# Projeto Django - Cotação de Euro e Dólar

## Descrição do Projeto

Este é um projeto Django simples que exibe a cotação do Euro e do Dólar frente ao Real. A aplicação faz uso de uma API de câmbio para fornecer informações atualizadas sobre as taxas de câmbio dessas moedas.

## Funcionalidades

- **Exibição da Cotação**: A página inicial do projeto exibe a cotação atual do Euro e do Dólar em relação ao Real.

- **Atualização Automática**: As taxas de câmbio são automaticamente atualizadas em intervalos regulares para garantir que os usuários tenham acesso às informações mais recentes.

## Pré-requisitos

Certifique-se de ter os seguintes requisitos instalados em seu ambiente de desenvolvimento:

- Python 3.x
- Django
- Requests (biblioteca para fazer requisições HTTP)

Instale as dependências executando o seguinte comando:

```bash
pip install -r requirements.txt
```

## Configuração

1. Clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/sam-dev97/COT_MOEDAS.git
cd pj_cotacao
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv myenv
#  Windows
myenv\Scripts\activate
#  Linux/Mac
source myenv/bin/activate
```

3. Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

4. Configure a API de câmbio:
   - Registre-se em uma API de câmbio (por exemplo, [Open Exchange Rates](https://openexchangerates.org/)).
   - Obtenha sua chave de API.
   - Crie um arquivo `.env` no diretório do projeto e adicione a chave da API:

   ```env
   API_KEY=sua-chave-de-api
   ```

5. Execute as migrações para criar o banco de dados:

```bash
python manage.py migrate
```

6. Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

Acesse a aplicação em [http://localhost:8000/](http://localhost:8000/).

## Uso

Acesse a página principal para visualizar as cotações atualizadas do Euro e do Dólar.

## Autor

Samuel Santos vivatecnosams@gmail.com
