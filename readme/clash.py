import re
import argparse

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

def is_ipv4(line):
    """检查是否为IPv4格式"""
    pattern = r'^\d{1,3}(\.\d{1,3}){3}$'
    return re.match(pattern, line.strip()) is not None

def main(input_file, output_file):
    # 读取原始数据
    original_lines = read_file(input_file)
    
    # 分离IPv4格式的数据行、数字开头的行和其他行
    ipv4_lines = [line for line in original_lines if line.strip() and is_ipv4(line.strip())]
    # 排除IPv4行后提取数字开头的行
    numeric_lines = [line for line in original_lines if line.strip() and line.strip()[0].isdigit() and not is_ipv4(line.strip())]
    non_numeric_lines = [line for line in original_lines if line.strip() and not line.strip()[0].isdigit() and not is_ipv4(line.strip())]
    
    # 对数字开头的行和其他行按字母顺序排序
    numeric_lines.sort(key=lambda x: x.strip().lower())      # 排序数字开头的行
    non_numeric_lines.sort(key=lambda x: x.strip().lower())  # 排序其他行
    
    # 合并IPv4格式的数据行、数字开头的行和排序后的其他行
    sorted_lines = ipv4_lines + numeric_lines + non_numeric_lines
    
    # 转换数据，忽略不符合格式的行
    converted_lines = [convert_line(line) for line in sorted_lines if convert_line(line)]
    
    # 在输出数据的前一行插入 payload:
    if converted_lines:
        converted_lines.insert(0, "payload:\n")
    
    # 将转换后的数据写入新的文件或覆盖原文件
    write_file(output_file, converted_lines)
    
    print(f"转换完成，结果已保存至 {output_file}")

if __name__ == '__main__':
    # 创建解析器对象
    parser = argparse.ArgumentParser(description="处理adblock文件并转换格式")
    
    # 添加输入和输出文件路径的命令行参数
    parser.add_argument('input_file', help='输入文件路径')
    parser.add_argument('output_file', help='输出文件路径')
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 调用main函数，传入文件路径
    main(args.input_file, args.output_file)
