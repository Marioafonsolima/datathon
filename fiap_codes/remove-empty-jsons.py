import os
import json

extracted_folder_path = '..'

extracted_files = os.listdir(extracted_folder_path)

def is_json_file_empty(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return len(data) == 0

for file in extracted_files:
    if file.endswith('.json'):
        file_path = os.path.join(extracted_folder_path, file)
        if is_json_file_empty(file_path):
            os.remove(file_path)
            print(f"Arquivo vazio removido: {file}")

print("Verificação e remoção de arquivos vazios concluída.")
