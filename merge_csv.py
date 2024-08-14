import os
import json
import pandas as pd

def load_csv_file(file_path):
    return pd.read_csv(file_path)

def json_to_dataframe(csv_data):
    return pd.DataFrame(csv_data)

def main(csv_files, merge_keys, output_folder):
    df_list = []
    for file in csv_files:
        csv_data = load_csv_file(file)
        df_list.append(csv_data)
    
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
    csv_files = [
        # './csv_output/Tabelas/TbAluno/Merge/merged_data.csv',
        # './csv_output/Tabelas/TbDiario/Merge/merged_data.csv',
        # './csv_output/Tabelas/TbFase/Merge/merged_data.csv',
        './csv_output/Tabelas/TbDiario/Originais anonimizados/TbDiarioAluno.csv',
        # './csv_output/Tabelas/TbDiario/Merge/TbDiarioFrequencia.csv', # 2
        # './csv_output/Tabelas/TbHistorico/Merge/merged_data.csv', # 2
        # './csv_output/Tabelas/TbMeta/TbMetaFaseNotaAluno.csv', # 1
        # './csv_output/Tabelas/TbMeta/TbMetaSituacaoAlunoDisciplina.csv', # 1
        './csv_output/Tabelas/TbSituacaoAlunoDisciplina/Originais anonimizados/TbSituacaoAlunoDisciplina.csv',
    ]

    merge_keys = [
        'IdAluno',
    ]
    
    output_folder = f'{extracted_folder_path}/output'
    main(csv_files, merge_keys, output_folder)