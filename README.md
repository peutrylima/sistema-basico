# 📝 Sistema de Cadastro de Pessoas em Python

## 💻 Sobre o Projeto
Este é o projeto final (Exercício 115) desenvolvido durante o curso de Python do **Curso em Vídeo**, ministrado pelo Professor Gustavo Guanabara. 

Trata-se de um mini sistema interativo via terminal (CLI) que permite o cadastro de pessoas (nome e idade) e a visualização dos usuários cadastrados. O grande diferencial deste projeto é a persistência de dados: todas as informações são salvas automaticamente em um arquivo de texto (`.txt`), garantindo que os registros não sejam perdidos ao fechar o programa.

## 📂 Estrutura do Projeto
Para aplicar boas práticas de desenvolvimento, o código foi construído com base no conceito de **Modularização**. O sistema foi dividido em três arquivos principais, cada um com uma responsabilidade bem definida:

* **`sistema.py`**: É o script principal. Ele inicializa o programa, verifica a existência do banco de dados (arquivo `.txt`) e gerencia o loop de repetição do menu principal.
* **`biblioteca.py`**: Responsável pela interface (UI) do terminal e validação de dados. Contém as funções de formatação de linhas, cabeçalhos, exibição do menu interativo e a função `leiaInt()`, que garante a entrada segura de números inteiros.
* **`arquivo.py`**: Módulo dedicado exclusivamente à manipulação do arquivo de texto. Contém funções para criar, ler e gravar novos dados no arquivo de forma segura.

## 🚀 O que aprendi e quais práticas foram aplicadas
A construção deste projeto foi fundamental para consolidar os seguintes conceitos e práticas de programação:

* **Modularização de Código**: Separação do código em diferentes pacotes para facilitar a manutenção, legibilidade e o reaproveitamento de funções.
* **Tratamento de Erros e Exceções (`try`, `except`, `else`, `finally`)**: O sistema foi construído para ser robusto. Ele trata erros de digitação do usuário (como digitar letras onde se espera a idade) e falhas de sistema (como erro ao tentar abrir ou criar arquivos), evitando que o programa encerre de forma abrupta e mostrando mensagens de erro amigáveis.
* **Manipulação de Arquivos (File I/O)**: 
    * Abertura e leitura de arquivos (`rt`).
    * Criação de novos arquivos caso não existam (`wt+`).
    * Adição de novas linhas de conteúdo sem apagar os dados antigos (`at`).
* **Manipulação e Limpeza de Strings**: Uso de técnicas como `.split(';')` para converter linhas de texto em listas baseadas em um separador, e `.replace('\n', '')` para tratar as quebras de linha indesejadas na leitura.
* **Formatação Avançada de Strings**: Utilização de *f-strings* com parâmetros de alinhamento espacial (ex: `{dado[0]:<30}`) para formatar a saída de dados como uma tabela organizada diretamente no console.

## ⚙️ Como executar

1. Certifique-se de ter o Python 3 instalado em sua máquina.
2. Faça o clone deste repositório ou baixe os arquivos.
3. Abra o terminal na pasta onde os arquivos estão localizados.
4. Execute o arquivo principal com o comando:
   ```bash
   python sistema.py
