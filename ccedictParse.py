import os
from pathlib import Path


def parse_ccedict(dict_path):
    if os.path.isfile(dict_path):
        with open(dict_path, encoding='UTF8') as f:
            parsed_dict = []
            for line in f:
                english = [e.strip().replace('"', '\\"') for e in line.split('/')[1:] if len(e.strip()) > 0]
                traditional = line.split(' ')[0].strip()
                simplified = line.split(' ')[1].strip()
                if line.startswith('#'):
                    continue

                pinyin = line.split('[')[1].split(']')[0].strip()
                entry = {
                    'traditional': traditional,
                    'simplified': simplified,
                    'pinyin': pinyin,
                    'english': english
                }

                parsed_dict.append(entry)

        return parsed_dict


if __name__ == '__main__':
    ccedictPath = Path('')
    parsed_dict = parse_ccedict(ccedictPath)
