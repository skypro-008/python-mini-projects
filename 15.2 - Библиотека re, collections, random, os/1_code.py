import re
from collections import Counter
import random
import os

files = os.listdir()

random_file = random.choice(files)

with open(random_file) as f:
    text = f.read()
    pattern = re.compile(r'\b\w*[aeiou]{3}\w*\b')
    matches = pattern.findall(text)

word_count = Counter(matches)

for word, count in word_count.most_common(5):
    print(word, count)
