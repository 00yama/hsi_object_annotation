import json
from collections import Counter
import matplotlib.pyplot as plt

with open('data.json', 'r') as f:
    data = json.load(f)

# タグのカウント
labels = []
for entry in data:
    tags = entry.get('tags', [])
    if len(tags) > 2:  # ['tags'][2] が存在する場合
        if len(tags) > 3 and tags[2] == tags[3]:  # ['tags'][3] が存在し、['tags'][2] と一致する場合
            labels.append(tags[2])  # 3番目（インデックス2）のタグを追加
        elif len(tags) > 3:  # ['tags'][3] が存在し、異なる場合
            labels.append(tags[3])  # 4番目（インデックス3）のタグを追加
        else:
            labels.append(tags[2])  # 3番目（インデックス2）のタグを追加

# カウント結果の表示
label_counts = Counter(labels)
label_counts = label_counts.most_common()

# ラベルとカウントを取得
labels, counts = zip(*label_counts)

# グラフを作成
plt.figure(figsize=(12, 8))
plt.barh(labels, counts, color='skyblue')
plt.xlabel('Count')
plt.ylabel('Scene label')
plt.title('Tag Counts by Location')
plt.gca().invert_yaxis()  # ラベルが上から表示されるように反転
plt.tight_layout()

plt.show()
