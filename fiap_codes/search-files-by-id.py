import os
import json

extracted_folder_path = '..'
search_id = 'IdAluno'

extracted_files = os.listdir(extracted_folder_path)

def contains_id(file_path, search_id):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        if isinstance(data, list):
            return any(search_id in item for item in data)
        elif isinstance(data, dict):
            return search_id in data
        return False

files_with_id = []
for file in extracted_files:
    if file.endswith('.json'):
        file_path = os.path.join(extracted_folder_path, file)
        if contains_id(file_path, search_id):
            files_with_id.append(file)
            print(f"ID '{search_id}' encontrado no arquivo: {file}")

if not files_with_id:
    print(f"Nenhum arquivo contém o ID '{search_id}'.")

print("Verificação de arquivos concluída.")
