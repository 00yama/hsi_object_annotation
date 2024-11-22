import json

def compare_data_names(file1, file2, output_file):
    """
    2つのJSONファイルを比較して、一方に存在しないdata_nameを出力する。

    :param file1: JSONファイル1のパス
    :param file2: JSONファイル2のパス
    :param output_file: 見当たらないdata_nameを保存するJSONファイルのパス
    """
    # ファイル1からdata_nameを抽出
    with open(file1, 'r', encoding='utf-8') as f:
        data1 = json.load(f)
        data_names1 = {item['data_name'] for item in data1}

    # ファイル2からdata_nameを抽出
    with open(file2, 'r', encoding='utf-8') as f:
        data2 = json.load(f)
        data_names2 = {item['data_name'] for item in data2}

    # ファイル1に存在するがファイル2に存在しないdata_name
    missing_in_file2 = data_names1 - data_names2

    # ファイル2に存在するがファイル1に存在しないdata_name
    missing_in_file1 = data_names2 - data_names1

    # 結果を辞書にまとめる
    result = {
        "missing_in_file2": list(missing_in_file2),
        "missing_in_file1": list(missing_in_file1)
    }

    # 結果をJSONファイルに書き出す
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"Comparison complete. Results saved in {output_file}")

# 使用例
file1 = "/Users/RINKAOYAMA/033lab/hsi-dataset/hsi_scene_annotation/data_09062024.json"  # ファイル1のパスを指定
file2 = "data_09062024.json"  # ファイル2のパスを指定
output_file = "missing_data_names.json"  # 出力ファイルのパス

compare_data_names(file1, file2, output_file)
