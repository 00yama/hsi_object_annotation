import os
import json
import matplotlib.pyplot as plt

def count_files_in_folder(folder_path):
    """
    指定されたフォルダ内およびサブフォルダ内でファイル名に「Dark」を含まないファイルの数を数える。

    :param folder_path: フォルダのパス
    :return: ファイル数（「Dark」を含まないもの）
    """
    file_count = 0
    
    # os.walkを使って、指定されたフォルダとそのサブフォルダ内を再帰的に探索
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            # ファイル名に「Dark」が含まれていない場合
            if "Dark" not in filename:
                file_count += 1
    
    return file_count

def count_data_in_json(json_file):
    """
    JSONファイル内のdataの数をカウントする。
    tagsがfalseであってもカウントする。

    :param json_file: JSONファイルのパス
    :return: 有効なdataの数
    """
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    valid_data_count = 0
    for item in data:
        # tagsがリストであればカウント
        if isinstance(item.get("tags"), list):
            valid_data_count += 1
    
    return valid_data_count

def plot_pie_chart(file_count, data_count):
    """
    ファイル数とデータ数の割合を円グラフで表示する。

    :param file_count: 「Dark」を含まないファイル数
    :param data_count: JSONファイル内の有効なdata数
    """
    # ファイル数とデータ数が0より小さい場合はエラーメッセージ
    if file_count < 0 or data_count < 0:
        print("Error: file_count or data_count is negative!")
        return
    
    # sizesの計算が負にならないようにする
    sizes = [file_count - data_count, data_count]
    
    # sizesの中に負の数が含まれている場合、エラーを表示
    if any(size < 0 for size in sizes):
        print("Error: One of the sizes is negative. Please check file counts and data counts.")
        return
    
    labels = ['Non-annotated', 'annotated']
    
    # 円グラフを描画
    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'orange'])
    plt.title(f"Percentage of annotation completed")
    plt.axis('equal')  # 円を丸く表示
    plt.show()

# 使用例
folder_path = "/Users/RINKAOYAMA/Library/CloudStorage/Box-Box/033Lab_share/members/21aj/ToyoshigeHATA/HSI-RGB"  # フォルダのパスを指定
json_file = "data.json"  # JSONファイルのパスを指定

# 1. フォルダ内の「Dark」を含まないファイル数をカウント
file_count = count_files_in_folder(folder_path)

# 2. JSONファイル内の有効なdata数をカウント
data_count = count_data_in_json(json_file)

print(f"file_count:{file_count}")
print(f"data_count:{data_count}")
# 3. 円グラフを表示
plot_pie_chart(file_count, data_count)
