import os
import subprocess
from time import time
from math import log10, floor

def significant(x):
    return int(floor(log10(abs(x))))

def round_sig(x):
    return round(x, -significant(x))

def humanize(seconds):
    if significant(seconds) < 0:
        return str(int(round_sig(seconds * 1000))) + " ms"
    else:
        return str(int(round_sig(seconds))) + " s"

title = "# Problem solutions\n"
TOC = ["\n### Table of Contents\n"]
content = ["\n## Contents"]

folder = "problems/"

for fname in sorted(os.listdir(folder)):
    content.append("\n### {}".format(fname[:-3]))
    TOC.append("{}. [{}](#{})".format(len(TOC), fname[4:-3], fname[:-3].replace(" ", "-").lower()))
    with open(folder + fname) as f:
        content.append("```python")
        content.append(f.read())
        content.append("```")

    start = time()
    a = subprocess.run(['python3', folder + fname], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
    content.append("Time: `~ {}`.".format(humanize(time() - start)))

with open("solutions.md", 'w') as f:
    f.write(title + '\n'.join(TOC + content))