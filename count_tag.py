import json
import glob
from collections import Counter
import matplotlib.pyplot as plt

def count_tags(json_files):
    """
    JSONファイル群を処理してtagsフィールド内のタグをカウントする。

    :param json_files: 処理するJSONファイルのリスト
    :return: タグの出現頻度を表す辞書
    """
    tag_counter = Counter()
    
    for file_path in json_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            for item in data:
                tags = item.get("tags", [])
                tag_counter.update(tags)
    
    return tag_counter

def plot_bar_chart(tag_counts):
    """
    タグのカウント結果を棒グラフとして表示する。

    :param tag_counts: タグの出現頻度を表す辞書
    """
    # tags = list(tag_counts.keys())
    # counts = list(tag_counts.values())
    # 出現頻度の大きい順に並べ替え
    sorted_tag_counts = tag_counts.most_common()
    tags = [tag for tag, count in sorted_tag_counts]
    counts = [count for tag, count in sorted_tag_counts]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(tags, counts, color='skyblue')
    plt.xlabel("Tags")
    plt.ylabel("Counts")
    # plt.title("Tag Frequencies")
    plt.xticks(rotation=45, ha='right')  # タグが長い場合に対応

    # 各バーの上に数値を記入
    for bar, count in zip(bars, counts):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                 str(count), ha='center', va='bottom', fontsize=10)
                 
    plt.tight_layout()  # レイアウト調整
    plt.show()


# JSONファイルを自動検出
json_files = glob.glob("data_*.json")  # カレントディレクトリからdata_(日付).jsonを探す

# タグをカウント
tag_counts = count_tags(json_files)

# 棒グラフを描画
plot_bar_chart(tag_counts)
