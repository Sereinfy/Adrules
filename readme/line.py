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
    # 如果文件已存在，读取所有行
    with open(line_file_path, 'r') as file:
        lines = file.readlines()

    first_line = lines[0].strip() if lines else None

    # 如果文件的第一行不是行数，才追加
    if first_line != str(line_count):
        with open(line_file_path, 'r+') as file:
            # 如果行数大于50行，只保留前50行
            content = lines[:50]
            content.insert(0, f"{line_count}\n")  # 将行数写入第一行
            file.seek(0, 0)  # 将文件指针移动到文件开头
            file.writelines(content)
        print(f"已将行数 {line_count} 写入到 readme/line.txt 的第一行。")
    else:
        print(f"行数 {line_count} 已经是 readme/line.txt 的第一行，未做任何修改。")

    # 如果文件行数超过50行，删除超过部分
    if len(lines) > 50:
        with open(line_file_path, 'w') as file:
            # 只写入前50行，删除超过50行的数据
            file.writelines(lines[:50])
        print("line.txt 文件行数超过50行，已删除超过50行的部分。")
