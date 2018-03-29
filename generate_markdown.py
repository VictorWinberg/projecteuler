import os
import subprocess
from sys import stdout
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

def progress(fname, bar_length=50):
    if fname:
        spaces = ' ' * (bar_length - len(fname))
        stdout.write('\rCurrent: {}'.format(fname + spaces))
    else:
        spaces = ' ' * bar_length
        stdout.write('\rDone!{}\n'.format(spaces))
    stdout.flush()

if __name__ == '__main__':
    print('''       _____                           _   _
      / ____|                         | | (_)
     | |  __  ___ _ __   ___ _ __ __ _| |_ _ _ __   __ _
     | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __| | '_ \ / _` |
     | |__| |  __/ | | |  __/ | | (_| | |_| | | | | (_| |
      \_____|\___|_| |_|\___|_| _\__,_|\__|_|_| |_|\__, |
     |  \/  |          | |     | |                  __/ |
     | \  / | __ _ _ __| | ____| | _____      ___ _|___/
     | |\/| |/ _` | '__| |/ / _` |/ _ \ \ /\ / / '_ \\
     | |  | | (_| | |  |   < (_| | (_) \ V  V /| | | |  _ _ _
     |_|  |_|\__,_|_|  |_|\_\__,_|\___/ \_/\_/ |_| |_| (_|_|_)
    ''')
    title = "# Problem solutions\n"
    TOC = ["\n### Table of Contents\n"]
    content = ["\n## Contents"]

    folder = "problems/"
    fnames = sorted(os.listdir(folder))
    for fname in fnames:
        progress(fname)

        content.append("\n### {}".format(fname[:-3]))
        TOC.append("{}. [{}](#{})".format(len(TOC), fname[4:-3], fname[:-3].replace(" ", "-").lower()))
        with open(folder + fname) as f:
            content.append("```python")
            content.append(f.read())
            content.append("```")

        end = float("inf")
        for i in range(5):
            start = time()
            subprocess.run(['python3', folder + fname], stdout=subprocess.PIPE)
            end = min(end, time() - start)
        content.append("Time: `~ {}`.".format(humanize(end)))

    with open("solutions.md", 'w') as f:
        f.write(title + '\n'.join(TOC + content))

    progress(None)
