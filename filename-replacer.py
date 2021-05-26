import sys
import os

def rename_files(dirPath, src, dest):
    # ファイルとディレクトリに仕分け
    listDir = os.listdir(dirPath)
    files = [file for file in listDir if os.path.isfile(os.path.join(dirPath, file))]
    directories = [directory for directory in listDir if os.path.isdir(os.path.join(dirPath, directory))]
    
    # リネーム
    for file in files:
        if src in file:
            newName = file.replace(src, dest)
            try:
                os.rename(os.path.join(dirPath, file), os.path.join(dirPath, newName))
            except:
                print("Error: " + os.path.join(dirPath, file))
    
    # サブフォルダも再帰的に処理
    for directory in directories:
        rename_files(os.path.join(dirPath, directory), src, dest)

# コマンドライン引数読み取り
args = sys.argv
if len(args) != 4:
    print("Error: 適切にコマンドライン引数を入力してください！")
    print(" - 例: python3 file_renamer.py DirectoryPath a b")
    exit()
dirPath = args[1]
src = args[2]
dest = args[3]

# ディレクトリかどうか判断
if not os.path.isdir(dirPath):
    print("Error: コマンドライン引数にはディレクトリのパスを指定してください！")
    exit()

# 変換開始
print("Target directory: " + dirPath)
print(" - \"" + src + "\" -> \"" + dest + "\"")
rename_files(dirPath, src, dest)
