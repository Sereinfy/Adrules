import re
import argparse

def read_file(file_name):
    """读取文件内容，并返回行列表"""
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.readlines()

def write_file(file_name, lines):
    """将行列表写入到指定文件中"""
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def convert_line(line):
    """转换符合格式的行"""
    match = re.match(r'\|\|([a-zA-Z0-9.-]+)\^', line.strip())
    if match:
        return f"  - '{match.group(1)}'\n"
    return ""

def main(input_file, output_file):
    original_lines = read_file(input_file)
    converted_lines = [convert_line(line) for line in original_lines if convert_line(line)]
    
    if converted_lines:
        converted_lines.insert(0, "payload:\n")
    
    write_file(output_file, converted_lines)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="处理adblock文件并转换格式")
    parser.add_argument('input_file', help='输入文件路径')
    parser.add_argument('output_file', help='输出文件路径')
    args = parser.parse_args()
    main(args.input_file, args.output_file)
