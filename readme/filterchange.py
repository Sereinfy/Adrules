import os

def modify_filter_file(filename):
    try:
        # 打开文件进行读取和写入
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        with open(filename, 'w', encoding='utf-8') as file:
            for line in lines:
                if line.startswith('            f.write("! Title'):
                    file.write('            f.write("! Title: Sereinfy AdBlock DNS\\n")\n')  # 注意这里是 \\n
                elif line.startswith('            f.write("! Description'):
                    file.write('            f.write("! Description: 适用于AdGuard的去广告合并规则，每8个小时更新一次。\\n")\n')
                elif line.startswith('            f.write("! Homepage'):
                    file.write('            f.write("! Homepage: https://github.com/Sereinfy/Adblock\\n")\n')
                elif line.startswith('            f.write("! Source'):
                    file.write('            f.write("! Source: https://raw.githubusercontent.com/Sereinfy/Adblock/main/rules/adblockdns.txt\\n")\n') 
                else:
                    file.write(line)
        
        print(f'文件 {filename} 修改成功！')

    except FileNotFoundError:
        print(f'文件 {filename} 未找到。')

# 使用示例，替换为您的文件路径
modify_filter_file('filter.py')
