import os
import json
import pandas as pd

def load_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def json_to_dataframe(json_data):
    return pd.DataFrame(json_data)

def main(json_files, output_folder):
    df_list = []
    all_columns = set()

    for file in json_files:
        json_data = load_json_file(file)
        df = json_to_dataframe(json_data)
        df_list.append(df)
        all_columns.update(df.columns)

    all_columns = list(all_columns)

    for i in range(len(df_list)):
        df_list[i] = df_list[i].reindex(columns=all_columns, fill_value='')

    concatenated_df = pd.concat(df_list, ignore_index=True)

    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, 'concatenated_data.csv')
    concatenated_df.to_csv(output_file, index=False)
    print(f"Concatenated data saved to {output_file}")

if __name__ == "__main__":
    extracted_folder_path = '..'
    json_files = [
        os.path.join(extracted_folder_path, 'TbAluno.json'),
        os.path.join(extracted_folder_path, 'TbDiarioFrequencia.json'),
        os.path.join(extracted_folder_path, 'TbAlunoTurmaProcedimentoMatricula.json'),
        os.path.join(extracted_folder_path, 'TbFreqAlunoNotificacaoResponsavel.json'),
        os.path.join(extracted_folder_path, 'TbAlunoRotinaEducacaoInfantil.json'),
        os.path.join(extracted_folder_path, 'TbSituacaoAlunoDisciplina.json'),
        os.path.join(extracted_folder_path, 'TbFaseNotaAluno.json'),
        os.path.join(extracted_folder_path, 'TbAlunoTurmaHistorico.json'),
        os.path.join(extracted_folder_path, 'TbAlunoFichaMedica.json'),
        os.path.join(extracted_folder_path, 'TbMetaFaseNotaAluno.json'),
        os.path.join(extracted_folder_path, 'TbAlunoProprioResponsavel.json'),
        os.path.join(extracted_folder_path, 'TbHistorico.json'),
        os.path.join(extracted_folder_path, 'TbHistoricoNotas.json'),
        os.path.join(extracted_folder_path, 'TbDiarioAluno.json'),
        os.path.join(extracted_folder_path, 'TbAlunoTurma.json'),
        os.path.join(extracted_folder_path, 'TbAlunoObs.json'),
    ]

    output_folder = f'{extracted_folder_path}/output/aluno'
    main(json_files, output_folder)
