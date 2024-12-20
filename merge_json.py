import os
import json
from glob import glob

def merge_json_files(directory, output_file):
    """
    指定したディレクトリ内のdata_YYYYMMDD.json形式のファイルを結合し、
    1つのJSONファイルとして保存する。

    :param directory: JSONファイルが保存されているディレクトリのパス
    :param output_file: 結合結果を保存するファイル名
    """
    all_data = []
    
    # ファイル名がdata_YYYYMMDD.json形式のものを検索
    json_files = glob(os.path.join(directory, "data_*.json"))
    
    for file_path in json_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                # 結合する
                if isinstance(data, list):
                    all_data.extend(data)  # リスト形式の場合
                elif isinstance(data, dict):
                    all_data.append(data)  # 辞書形式の場合
            except json.JSONDecodeError as e:
                print(f"ファイル {file_path} の読み込みエラー: {e}")
    
    # 結果を保存
    with open(output_file, 'w', encoding='utf-8') as output:
        json.dump(all_data, output, ensure_ascii=False, indent=4)
    
    print(f"JSONファイルを結合しました: {output_file}")

# 実行例
input_directory = "./"  # JSONファイルが保存されているフォルダのパス
output_json = "data.json"          # 保存するファイル名

merge_json_files(input_directory, output_json)
