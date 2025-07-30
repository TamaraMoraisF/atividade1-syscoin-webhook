# Atividades - Processo Seletivo Syscoin Space 

Repositório criado para armazenar as soluções das duas atividades práticas do processo seletivo para vaga de estágio na Syscoin Space.

---

##  Atividade 1 – Requisição HTTP autenticada

Foi desenvolvido um script em **Python** utilizando a biblioteca `requests` para realizar uma requisição `POST` com autenticação Bearer.

###  Caminho:
`atividade1/syscoin_webhook.py`

###  Detalhes da requisição:
- **Endpoint:** https://webhook.syscoin.com.br/webhook/teste-estagio  
- **Headers:** Authorization: Bearer [token]  
- **Body (JSON):**  
  ```json
  {
    "Name": "Tamara Morais Frigo",
    "Response": "Sou uma pessoa comprometida, com grande interesse em aprender e evoluir constantemente. Tenho certeza de que posso contribuir com dedicação, iniciativa e vontade de crescer junto com a equipe da Syscoin."
  }
  
##  Atividade 2 – Deploy local do Uptime Kuma com Docker

A aplicação open source **[Uptime Kuma](https://github.com/louislam/uptime-kuma)** foi instalada e executada localmente utilizando **Docker**, conforme instruções fornecidas.

### Comando executado:

```bash
docker run -d -p 3001:3001 --name uptime-kuma louislam/uptime-kuma

Após a execução do container, a aplicação ficou acessível via navegador pelo endereço:
http://localhost:3001
