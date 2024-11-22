import json
import glob

def calculate_average_tags(json_files):
    """
    JSONファイル群を処理し、data_nameごとのtagsの数の平均を計算する。

    :param json_files: 処理するJSONファイルのリスト
    :return: 平均タグ数（float）
    """
    total_tags = 0
    total_data_names = 0

    for file_path in json_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            # 各エントリのtagsの数をカウント
            for item in data:
                tags = item.get("tags", [])
                total_tags += len(tags)
                total_data_names += 1

    # データがない場合の処理
    if total_data_names == 0:
        return 0

    # 平均を計算
    average_tags = total_tags / total_data_names
    return average_tags

# JSONファイルを自動検出
json_files = glob.glob("data_*.json")  # カレントディレクトリからdata_(日付).jsonを探す

# 平均タグ数を計算
average_tags = calculate_average_tags(json_files)

# 結果を表示
print(f"data_nameあたりの平均tags数: {average_tags:.2f}")
