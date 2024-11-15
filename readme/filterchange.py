def modify_filter_file(filename):
    try:
        # 打开文件进行读取
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # 重新打开文件进行写入
        with open(filename, 'w', encoding='utf-8') as file:
            for line in lines:
                # 查找并替换含有特定关键词的整行
                if 'f.write("! Title: AdBlock DNS' in line:
                    file.write('            f.write("! Title: Sereinfy AdBlock DNS\\n")\n')  # 替换整行
                elif 'f.write("! Title: AdBlock Filter' in line:
                    file.write('            f.write("! Title: Sereinfy AdBlock Filter\\n")\n')  # 替换整行
                elif 'f.write("! Description' in line:
                    file.write('            f.write("! Description: 适用于AdGuard的去广告合并规则，每8个小时更新一次。\\n")\n')  # 替换整行
                elif 'f.write("! Homepage' in line:
                    file.write('            f.write("! Homepage: https://github.com/Sereinfy/Adrules\\n")\n')  # 替换整行
                elif 'f.write("! Source' in line:
                    file.write('            f.write("! Source: https://github.com/Sereinfy/Adrules/main/rules\\n")\n')  # 替换整行
                else:
                    file.write(line)  # 保留不包含关键词的原行
        
        print(f'文件 {filename} 修改成功！')

    except FileNotFoundError:
        print(f'文件 {filename} 未找到。')

# 使用示例，替换为您的文件路径
modify_filter_file('filter.py')
