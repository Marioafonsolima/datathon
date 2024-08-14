import os
import json
import pandas as pd


def load_json_file(file_path):
    return pd.read_csv(file_path)

def json_to_dataframe(json_data):
    return pd.DataFrame(json_data)

def convert_csv_to_json(csv_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for file_name in os.listdir(csv_folder):
        if file_name.endswith('.csv'):
            csv_file_path = os.path.join(csv_folder, file_name)
            csv_data = load_json_file(csv_file_path)
            df = json_to_dataframe(csv_data)
            
            json_file_name = file_name.replace('.csv', '.json')
            json_file_path = os.path.join(output_folder, json_file_name)
            
            df.to_json(json_file_path, index=False)
            print(f"Converted {csv_file_path} to {json_file_path}")


if __name__ == "__main__":
    json_folder = '.'
    output_folder = os.path.join(json_folder, 'json_output')

    list_of_paths = [
        'csv_output/Tabelas/Outras tabelas',
        'csv_output/Tabelas/TbAbatimento',
        'csv_output/Tabelas/TbAbatimento/Merge',
        'csv_output/Tabelas/TbAbatimento/Originais anonimizados',
        'csv_output/Tabelas/TbAluno',
        'csv_output/Tabelas/TbAluno/Merge',
        'csv_output/Tabelas/TbAluno/Originais anonimizados',
        'csv_output/Tabelas/TbCampoDinamico',
        'csv_output/Tabelas/TbCampoDinamico/Merge',
        'csv_output/Tabelas/TbCampoDinamico/Originais anonimizados',
        'csv_output/Tabelas/TbCaptacao',
        'csv_output/Tabelas/TbCaptacao/Originais anonimizados',
        'csv_output/Tabelas/TbDiario',
        'csv_output/Tabelas/TbDiario/Merge',
        'csv_output/Tabelas/TbDiario/Originais anonimizados',
        'csv_output/Tabelas/TbFase',
        'csv_output/Tabelas/TbFase/Merge',
        'csv_output/Tabelas/TbFase/Originais anonimizados',
        'csv_output/Tabelas/TbHistorico',
        'csv_output/Tabelas/TbHistorico/Merge',
        'csv_output/Tabelas/TbHistorico/Originais anonimizados',
        'csv_output/Tabelas/TbMeta',
        'csv_output/Tabelas/TbProfessor',
        'csv_output/Tabelas/TbProfessor/Merge',
        'csv_output/Tabelas/TbProfessor/Originais anonimizados',
        'csv_output/Tabelas/TbResponsavel',
        'csv_output/Tabelas/TbResponsavel/Originais anonimizados',
        'csv_output/Tabelas/TbSerie',
        'csv_output/Tabelas/TbSerie/Merge',
        'csv_output/Tabelas/TbSerie/Originais anonimizados',
        'csv_output/Tabelas/TbSituacaoAlunoDisciplina',
        'csv_output/Tabelas/TbSituacaoAlunoDisciplina/Originais anonimizados',
        'csv_output/Tabelas/TbTurma',
        'csv_output/Tabelas/TbTurma/Merge',
        'csv_output/Tabelas/TbTurma/Originais anonimizados',
    ]

    for item in list_of_paths:
        csv_folder = f'./{item}'
        convert_csv_to_json(csv_folder, output_folder)
