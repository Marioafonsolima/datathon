import os
import json
import pandas as pd

def load_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def json_to_dataframe(json_data):
    return pd.DataFrame(json_data)

def convert_json_to_csv(json_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for file_name in os.listdir(json_folder):
        if file_name.endswith('.json'):
            json_file_path = os.path.join(json_folder, file_name)
            json_data = load_json_file(json_file_path)
            df = json_to_dataframe(json_data)
            
            csv_file_name = file_name.replace('.json', '.csv')
            csv_file_path = os.path.join(output_folder, csv_file_name)
            
            df.to_csv(csv_file_path, index=False)
            print(f"Converted {json_file_path} to {csv_file_path}")

if __name__ == "__main__":
    json_folder = '.'
    output_folder = os.path.join(json_folder, 'csv_output')
    
    convert_json_to_csv(json_folder, output_folder)
