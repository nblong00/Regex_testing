import re

pattern = re.compile(r'\d{3}[-\s.]\d{3}[-\s.]\d{4}')

with open('sample.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    matches = pattern.finditer(data)
    # print(data)

    for match in matches:
        print(match)
