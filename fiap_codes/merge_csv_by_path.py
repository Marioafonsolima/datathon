import os
import pandas as pd


def load_csv_file(file_path):
    return pd.read_csv(file_path)

def main(csv_folder_path, merge_key, output_folder):
    df_list = []
    for file_name in os.listdir(csv_folder_path):
        if file_name.endswith('.csv'):
            file_path = os.path.join(csv_folder_path, file_name)
            df_list.append(load_csv_file(file_path))
    
    if not df_list:
        print("No CSV files found in the specified folder.")
        return
    
    merged_df = df_list[0]
    for i in range(1, len(df_list)):
        try:
            merged_df = pd.merge(merged_df, df_list[i], on=merge_key, how='inner')
        except Exception as e:
            print(f"Error merging file {i} on key {merge_key}: {e}")
            print(f"Error dataframe {df_list[i].columns}: {e}")
            continue
    
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, 'merged_data.csv')
    merged_df.to_csv(output_file, index=False)
    print(f"Merged data saved to {output_file}")


if __name__ == "__main__":
    csv_folder_path = './csv_output_/Tabelas/TbTurma'
    merge_key = 'IdTurma'
    output_folder = os.path.join(csv_folder_path, 'Merge')
    
    main(csv_folder_path, merge_key, output_folder)
