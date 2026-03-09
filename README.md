# 🎮 Flask Game Hub

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)]()
[![Flask](https://img.shields.io/badge/Flask-Web_Framework-black)]()

Um **Game Hub web desenvolvido com Python e Flask** que reúne três jogos clássicos em uma única aplicação.  
O usuário pode escolher entre **Jogo da Forca**, **Pedra, Papel e Tesoura** e **Jogo da Velha**, jogando diretamente pelo navegador.

O projeto demonstra conceitos fundamentais de **desenvolvimento web com Flask**, incluindo **rotas, métodos HTTP (GET/POST), formulários HTML, templates Jinja2 e gerenciamento de estado com sessions**.

---

# ⚙️ Instalação
<ol><li>Clone o Repositório</li>


<li>Instale as dependências:</li>
<ul><li>pip install flask</li></ul></ol>

# 📸 Demonstração

<img width="1919" height="870" alt="Captura de tela 2026-03-09 195257" src="https://github.com/user-attachments/assets/0500d0c4-bcc7-4010-9a4c-94255343e8ca" />
<img width="1919" height="869" alt="Captura de tela 2026-03-09 195343" src="https://github.com/user-attachments/assets/75a0089e-4849-446c-8e19-d438f1ce6947" />
<img width="1919" height="868" alt="Captura de tela 2026-03-09 200825" src="https://github.com/user-attachments/assets/5044f897-ce9d-4646-aad1-d8dc4b645d95" />
<img width="1919" height="868" alt="Captura de tela 2026-03-09 195442" src="https://github.com/user-attachments/assets/21e39554-4f50-47c0-9511-f0ddcfe4eeb3" />

# 🚀 Funcionalidades

<ul><li>🎯 Menu principal para seleção de jogos</li>

<li>✏️ Jogo da Forca</li>

<ul><li>Sistema de tentativas</li>

<li>Atualização do estado da palavra</li></ul>

<li>✊✋✌️ Pedra, Papel e Tesoura</li>

<ul><li>Jogador vs computador</li>

<li>Resultado imediato da rodada</li></ul>

<li>❌⭕ Jogo da Velha</li>

<ul><li><i>Em breve</i></li></ul>

<li>💾 Persistência de estado usando Flask Sessions</li>

<li>🔄 Atualização da interface via formulários POST e refresh completo da página</li></ul>

# 📑 Fluxo da Aplicação

<ol><li>O usuário acessa o menu principal</li>

<li>Escolhe um dos jogos disponíveis</li>

<li>Cada jogada envia um formulário POST</li>

<li>O servidor Flask:</li>

<ul><li>Processa a jogada</li>

<li>Atualiza o estado nas sessions</li></ul>

<li>A página é renderizada novamente com o novo estado do jogo</li></ol>

# 🧠 Conceitos Demonstrados

Este projeto foi criado com foco em prática de conceitos importantes de backend web com Flask:

<ul><li> Estrutura de aplicações Flask</li>

<li>Rotas e controle de fluxo</li>

<li>Métodos HTTP GET / POST</li>

<li>Manipulação de formulários HTML</li>

<li>Renderização com Jinja2</li>

<li>Gerenciamento de estado com Flask Sessions</li>

<li>Arquitetura simples request → processamento → renderização</li></ul>

# ✍🏼 Próximas Implementações

<ul>
  <li>Página de Jogo da Velha</li>
  <li><b>Banco de dados SQL</b> para consumo de palavras no Jogo da Forca.</li>
  <li>Página "Database Manager", para administração via cliente.</li>
  <li>Interface mais moderna com Bootstrap ou Tailwind</li>
  <li>Atualizações sem refresh usando JavaScript / Fetch API</li>
</ul>

# 📚 Objetivo do Projeto

Este projeto foi desenvolvido como exercício prático de desenvolvimento web com Flask, explorando a construção de aplicações web simples baseadas em:

<ul><li>Backend Python</li>

<li>Templates server-side</li>

<li>Gerenciamento de estado de aplicação</li></ul>

---

👨‍💻 Desenvolvido por Eybraian B.
