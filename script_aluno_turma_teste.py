import zipfile
import os
import pandas as pd
import json

extracted_folder_path = '.'
extracted_files = os.listdir(extracted_folder_path)

def load_json_to_df(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return pd.DataFrame(data)

dfs = {}
sample_files = ['TbAluno.json', 'TbDiarioFrequencia.json', 'TbAlunoTurmaProcedimentoMatricula.json', 'TbFreqAlunoNotificacaoResponsavel.json', 'TbAlunoRotinaEducacaoInfantil.json', 'TbSituacaoAlunoDisciplina.json', 'TbFaseNotaAluno.json', 'TbAlunoTurmaHistorico.json', 'TbAlunoFichaMedica.json', 'TbMetaFaseNotaAluno.json', 'TbAlunoProprioResponsavel.json', 'TbHistorico.json', 'TbHistoricoNotas.json', 'TbDiarioAluno.json', 'TbAlunoTurma.json', 'TbAlunoObs.json']
for file in sample_files:
    file_path = os.path.join(extracted_folder_path, file)
    dfs[file] = load_json_to_df(file_path)

for file in sample_files:
    file_path = os.path.join(extracted_folder_path, file)
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        if not data: continue

file_path = os.path.join(extracted_folder_path, 'TbAluno.json')
with open(file_path, 'r', encoding='utf-8') as file:
    aluno_turma_data = json.load(file)
df_aluno_turma = pd.DataFrame(aluno_turma_data)

file_path_turma = os.path.join(extracted_folder_path, 'TbAlunoTurma.json')
df_turma = load_json_to_df(file_path_turma)

df_aluno_turma_completo = pd.merge(df_aluno_turma, df_turma, on='IdAluno', how='inner')

output_folder = f'{extracted_folder_path}/output'
os.makedirs(output_folder, exist_ok=True)
output_file = os.path.join(output_folder, 'merged_data_turma.csv')
df_aluno_turma_completo.to_csv(output_file, index=False)
print(f"Merged data saved to {output_file}")
