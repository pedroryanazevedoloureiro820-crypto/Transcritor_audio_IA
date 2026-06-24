# Assistente de Transcrição e Resumo de Áudio com IA
Este é um script em Python que automatiza o processo de transcrição e resumo de arquivos de áudio em lote. Ele monitora uma pasta local, faz o upload dos arquivos de áudio para a API do Google Gemini (utilizando o modelo mais recente) e gera relatórios estruturados em formato de texto (`.txt`) automaticamente na pasta de saída.

O projeto demonstra conceitos práticos de **Automação de Processos (RPA)**, **Integração com Modelos de Linguagem de Grande Porte (LLMs)** e **Manipulação de Arquivos de Sistema**.

## Funcionalidades
* **Processamento em Lote:** Varre uma pasta inteira de áudios e processa um por um automaticamente usando estruturas de repetição.
* **Integração com IA:** Utiliza o SDK `google-genai` para enviar arquivos multimídia e receber respostas inteligentes baseadas em prompts customizados.
* **Organização de Arquivos:** Cria automaticamente as pastas necessárias de entrada (`audios`) e saída (`audios resumidos`), isolando os nomes dos arquivos originais e gerando as saídas em texto limpo.
* **Gerenciamento de Armazenamento:** Exclui os arquivos temporários dos servidores da Google após a resposta, garantindo o bom uso das cotas da API.

## Tecnologias Utilizadas

* **Python 3.x**
* **Google GenAI SDK** (Integração com a API do Gemini)
* **OS** 
