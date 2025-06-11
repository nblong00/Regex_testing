import re

samplefile = open('sample.txt', encoding='utf-8')
data = samplefile.read()
samplefile.close()
print(data)
pattern = re.compile(r'1234')

matches = pattern.finditer(data)

for match in matches:
    print(match)

print(data[161:169])