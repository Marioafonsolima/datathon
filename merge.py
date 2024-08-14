import os
import json
import pandas as pd

def load_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def json_to_dataframe(json_data):
    return pd.DataFrame(json_data)

def main(json_files, merge_keys, output_folder):
    df_list = []
    for file in json_files:
        json_data = load_json_file(file)
        df_list.append(json_to_dataframe(json_data))
    
    merged_df = df_list[0]
    for i in range(1, len(df_list)):
        try: merged_df = pd.merge(merged_df, df_list[i], on=merge_keys[i-1], how='inner')
        except:
            try: merged_df = pd.merge(merged_df, df_list[i], on=merge_keys[0], how='left')
            except: pass
    
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, 'merged_data.csv')
    merged_df.to_csv(output_file, index=False)
    print(f"Merged data saved to {output_file}")

if __name__ == "__main__":
    extracted_folder_path = '.'
    json_files = [
        os.path.join(extracted_folder_path, 'TbAluno.json'),
        os.path.join(extracted_folder_path, 'TbDiarioFrequencia.json'),
        os.path.join(extracted_folder_path, 'TbAlunoTurmaProcedimentoMatricula.json'),
        os.path.join(extracted_folder_path, 'TbFreqAlunoNotificacaoResponsavel.json'),
        os.path.join(extracted_folder_path, 'TbAlunoRotinaEducacaoInfantil.json'),
        os.path.join(extracted_folder_path, 'TbSituacaoAlunoDisciplina.json'),
        os.path.join(extracted_folder_path, 'TbFaseNotaAluno.json'),
        os.path.join(extracted_folder_path, 'TbMensagemCaixaSaida.json'),
        os.path.join(extracted_folder_path, 'TbAlunoTurmaProcedimentoMatriculaHistorico.json'),
        os.path.join(extracted_folder_path, 'TbAlunoTurmaHistorico.json'),
        os.path.join(extracted_folder_path, 'TbAlunoFichaMedica.json'),
        os.path.join(extracted_folder_path, 'TbMetaFaseNotaAluno.json'),
        os.path.join(extracted_folder_path, 'TbMetaSituacaoAlunoDisciplina.json'),
        os.path.join(extracted_folder_path, 'TbAlunoProprioResponsavel.json'),
        os.path.join(extracted_folder_path, 'TbHistorico.json'),
        os.path.join(extracted_folder_path, 'TbHistoricoNotas.json'),
        os.path.join(extracted_folder_path, 'TbDiarioAluno.json'),
        os.path.join(extracted_folder_path, 'TbAlunoTurma.json'),
        os.path.join(extracted_folder_path, 'TbAlunoObs.json'),
    ]

    merge_keys = [
        'IdAluno',
    ]
    
    output_folder = f'{extracted_folder_path}/output'
    main(json_files, merge_keys, output_folder)