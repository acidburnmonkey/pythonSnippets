'''
this script parses conf file [section] -> content as key value pairs of mega
'''

import re

def main():
    with open('data.txt', 'r') as f:
        text = f.read()

    lines = text.splitlines()
    sections = re.findall(r'\[.*?\]', text)

    mega = {}
    current_key = None

    for line in lines:
        line = line.strip()
        if line in sections:
            current_key = line.strip('[]')
            mega[current_key] = []
        elif current_key:
            mega[current_key].append(line)

    

    print(mega)

if __name__ == '__main__':
    main()
