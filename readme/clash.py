import re

def read_file(file_name):
    """读取文件内容，并返回行列表"""
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

def write_file(file_name, lines):
    """将行列表写入到指定文件中"""
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def convert_line(line):
    """转换单行数据，如果不符合格式则返回空字符串"""
    pattern = r'\|\|([a-zA-Z0-9.-]+)\^'
    match = re.match(pattern, line.strip())
    if match:
        # 使用捕获组进行替换
        new_line = f"  - '{match.group(1)}'\n"
        return new_line
    else:
        # 不符合格式的行返回空字符串
        return ""

def main():
    # 读取原始数据
    original_lines = read_file('rules/adblockdns.txt')
    
    # 转换数据，忽略不符合格式的行
    converted_lines = [convert_line(line) for line in original_lines if convert_line(line)]
    
    # 在输出数据的前一行插入 payload:
    if converted_lines:
        converted_lines.insert(0, "payload:\n")
    
    # 将转换后的数据写入新的文件或覆盖原文件
    write_file('rules/dns_clash.yaml', converted_lines)
    
    print("转换完成，结果已保存至 dns_clash.yaml")

if __name__ == '__main__':
    main()
