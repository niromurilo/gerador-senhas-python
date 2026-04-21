# 🔐 Gerador de Senhas Seguras em Python

Este projeto consiste em um gerador de senhas desenvolvido em Python, com foco em boas práticas, segurança e lógica de programação.

## 🚀 Objetivo

Ir além de um exercício básico e construir uma solução mais próxima de um cenário real, garantindo que as senhas geradas sejam seguras, aleatórias e sem padrões previsíveis.

---

## ⚙️ Funcionalidades

- ✅ Geração de senhas com tamanho definido pelo usuário  
- ✅ Inclusão obrigatória de:
  - Letras (maiúsculas e minúsculas)
  - Números
  - Caracteres especiais  
- ✅ Validação de tamanho mínimo da senha  
- ✅ Embaralhamento dos caracteres para evitar padrões previsíveis  
- ✅ Código organizado em função reutilizável  

---

## 🧠 Lógica aplicada

O algoritmo garante que a senha contenha pelo menos:
- 1 letra  
- 1 número  
- 1 caractere especial  

Após isso:
- Os demais caracteres são gerados de forma aleatória  
- A lista final é embaralhada (`shuffle`) para aumentar a segurança  
- A senha é convertida para string e retornada  

---

## 📌 Tecnologias utilizadas

- Python 3  
- Bibliotecas padrão:
  - `random`
  - `string`

---

## ▶️ Como executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/gerador-senhas.git
