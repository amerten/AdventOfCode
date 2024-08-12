import re

j = open(0).read()
print(sum(map(int, re.findall('[\d-]+', j))))