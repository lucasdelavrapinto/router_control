# Automação Web

Essa foi feita para automatizar o processo de configuração do meu roteador, habilitando ou desabilitando o bloqueio de acesso a internet.

# Utilização

Inicialmente, é recomendado criar um ambiente virtual no linux para o projeto:
`python3 -m venv .venv && source .venv/bin/activate`

Para rodar, basta executar o comando `python3 index.py on` ou `python3 index.py off` e aguardar.

# Como funciona

O script utiliza o Playwright para acessar a página de login do roteador e executar os comandos necessários para habilitar o bloqueio de acesso a internet.

# Como instalar

Instale com o pip:

`python3 -m pip install -r requirements.txt`

# CRON

Para executar o script automaticamente, você pode usar o CRON, como exemplo:

`59 23 * * * python3 index.py` que irá executar o script todos dias as 23:59.

Para maiores informações sobre o CRON, consulte a documentação oficial: https://man7.org/linux
Se precisar de auxilio para configurar o CRON, consulte: https://crontab.guru/.

# Observações importantes

- Certifique-se de ter as credenciais corretas do roteador no arquivo `credentials.py`.
- O endereço IP do roteador pode variar, então ajuste a variável `LOGIN_URL_ROUTER
` conforme necessário.
- O script foi testado com um modelo específico de roteador, então pode ser necessário ajustar os seletores de elementos para funcionar com outros modelos.
- O script é assíncrono, então certifique-se de ter o ambiente configurado para rodar código assíncrono.
- O script envia uma mensagem para o Telegram após a execução, então certifique-se de ter as credenciais do Telegram configuradas corretamente no arquivo `credentials.py`.
