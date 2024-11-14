import os

# 读取 rules/black.txt 的行数
with open('rules/black.txt', 'r') as file:
    line_count = sum(1 for _ in file)

# 检查 readme/line.txt 文件是否存在，如果不存在则创建
line_file_path = 'readme/line.txt'

# 如果文件不存在，则创建并写入行数
if not os.path.exists(line_file_path):
    with open(line_file_path, 'w') as file:
        file.write(f"{line_count}\n")
    print(f"文件不存在，已创建并写入行数 {line_count} 到 readme/line.txt")
else:
    # 如果文件已存在，读取第一行并检查是否需要修改
    with open(line_file_path, 'r') as file:
        first_line = file.readline().strip()

    # 如果文件的第一行不是行数，才追加
    if first_line != str(line_count):
        with open(line_file_path, 'r+') as file:
            content = file.read()
            file.seek(0, 0)  # 将文件指针移动到文件开头
            file.write(f"{line_count}\n{content}")
        print(f"已将行数 {line_count} 写入到 readme/line.txt 的第一行。")
    else:
        print(f"行数 {line_count} 已经是 readme/line.txt 的第一行，未做任何修改。")
