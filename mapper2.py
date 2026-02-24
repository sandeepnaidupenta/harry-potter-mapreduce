# DOB: 19-05-2003

import sys
import re
from spellchecker import SpellChecker

spell = SpellChecker()

for line in sys.stdin:
    words = re.findall(r'\b[a-zA-Z]+\b', line.lower())

    for word in words:
        if word not in spell:   # non-English words
            print(f"{word}\t1")