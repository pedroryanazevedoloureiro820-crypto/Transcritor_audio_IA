from google import genai
import os

pasta_projeto = os.getcwd()

pasta_audio = os.path.join(pasta_projeto, "audios")
os.makedirs(pasta_audio, exist_ok=True) 

pasta_saida = os.path.join(pasta_projeto, "audios resumidos")
os.makedirs(pasta_saida, exist_ok=True) 

# Lembrete: Quando for para o GitHub, remova a chave real por segurança!
client = genai.Client(api_key="COLOQUE_AQUI_SUA_CHAVE_DE_API_DO_GEMINI")

arquivos_audio = os.listdir(pasta_audio)
num_arquivos = len(arquivos_audio)
contador = 0

if num_arquivos == 0:
    print("Não há arquivos de áudio na pasta 'audios'.")

while num_arquivos > 0:
    
    nome_audio = arquivos_audio[contador]
    caminho_audio = os.path.join(pasta_audio, nome_audio)
    
    print(f"\nEnviando {nome_audio}...")
    
    # Faz o upload do arquivo
    arquivo_na_ia = client.files.upload(file=caminho_audio)

    print("Processando com a Inteligência Artificial...")
    
    resposta = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=[arquivo_na_ia, "transcreva o audio e resuma"]
    )

    # Pega o nome sem extensão e monta o caminho final de saída
    sem_extensao = os.path.splitext(nome_audio)[0]
    caminho_saida = os.path.join(pasta_saida, f"{sem_extensao}.txt")

    # Escreve o texto gerado na pasta de destino
    with open(caminho_saida, "w", encoding="utf-8") as arquivo_txt:
        arquivo_txt.write(resposta.text)

    # Deleta o arquivo da nuvem para não estourar seu limite de armazenamento
    client.files.delete(name=arquivo_na_ia.name)

    print(f"Sucesso! Resumo salvo em: {sem_extensao}.txt")

    # Atualiza as variáveis do loop
    num_arquivos -= 1
    contador += 1

print("\nTodos os áudios foram processados e salvos com sucesso!")