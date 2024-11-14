# 读取rules/black.txt的行数
with open('rules/black.txt', 'r') as file:
    line_count = sum(1 for _ in file)

# 读取3.txt的第一行并进行判断
with open('3.txt', 'r') as file:
    first_line = file.readline().strip()

# 如果3.txt的第一行不是行数，才追加
if first_line != str(line_count):
    with open('3.txt', 'r+') as file:
        content = file.read()
        file.seek(0, 0)  # 将文件指针移动到文件开头
        file.write(f"{line_count}\n{content}")
    print(f"已将行数 {line_count} 写入到 3.txt 的第一行。")
else:
    print(f"行数 {line_count} 已经是 3.txt 的第一行，未做任何修改。")
