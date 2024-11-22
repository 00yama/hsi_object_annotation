import json
import matplotlib.pyplot as plt
from collections import Counter

def load_data(json_file):
    """
    JSONファイルを読み込み、tagsがFalseではないデータを返す。

    :param json_file: JSONファイルのパス
    :return: 有効なデータのリスト
    """
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    # tagsがFalseではないデータのみ取得
    valid_data = [item for item in data if item.get("tags") != False]
    return valid_data

def calculate_category_distribution(data):
    """
    画像ごとのカテゴリ数の分布を計算する。

    :param data: JSONデータのリスト
    :return: カテゴリ数ごとの割合を示す辞書
    """
    # 各画像のカテゴリ数をカウント
    category_counts = [len(item["tags"]) for item in data]
    
    # カテゴリ数ごとの出現頻度をカウント
    count_distribution = Counter(category_counts)
    
    # 全画像数
    total_images = len(category_counts)
    
    # 割合を計算
    percentage_distribution = {k: (v / total_images) * 100 for k, v in count_distribution.items()}
    return percentage_distribution

def plot_category_distribution(distribution):
    """
    カテゴリ数ごとの割合を折れ線グラフとしてプロットする。

    :param distribution: カテゴリ数ごとの割合を示す辞書
    """
    # データをカテゴリ数の昇順にソート
    sorted_distribution = sorted(distribution.items())
    categories = [item[0] for item in sorted_distribution]
    percentages = [item[1] for item in sorted_distribution]
    
    # 折れ線グラフの描画
    plt.figure(figsize=(8, 6))
    plt.plot(categories, percentages, marker='o', color='skyblue', label="Category Distribution")
    plt.xlabel("Number of Categories per Image")
    plt.ylabel("Percentage of Images (%)")
    plt.title("Categories per Image Distribution")
    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()

# メイン処理
json_file = "data-object.json"  # JSONファイル名（例: "data.json"）
data = load_data(json_file)
distribution = calculate_category_distribution(data)
plot_category_distribution(distribution)
