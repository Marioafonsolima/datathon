import os
import json

extracted_folder_path = '.'

extracted_files = os.listdir(extracted_folder_path)

def find_ids(file_path):
    ids_found = set()
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        if isinstance(data, list):
            for item in data:
                ids_found.update(key for key in item.keys() if key.startswith('Id'))
        elif isinstance(data, dict):
            ids_found.update(key for key in data.keys() if key.startswith('Id'))
    return ids_found

all_ids = set()
files_with_ids = {}
for file in extracted_files:
    if file.endswith('.json'):
        file_path = os.path.join(extracted_folder_path, file)
        ids_in_file = find_ids(file_path)
        if ids_in_file:
            files_with_ids[file] = ids_in_file
            all_ids.update(ids_in_file)
            print(f"IDs encontrados no arquivo {file}: {ids_in_file}")

if not files_with_ids:
    print("Nenhum arquivo contém IDs que começam com 'Id'.")

print("Verificação de arquivos concluída.")
print(f"Todos os IDs encontrados: {all_ids}")
