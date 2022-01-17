import sys

print(sys.version)

# a, b = map(int, input().split())
#

import time

lst = ["Как дела?", "Что делаешь?", "Как настроение?"]
for word in lst:
    sys.stdout.write(f"\r{word}...")
    #sys.stdout.flush()
    time.sleep(1)

for i in reversed(range(1, 11)):
    sys.stderr.write(f"{i:2d}\r")
    time.sleep(.5)
