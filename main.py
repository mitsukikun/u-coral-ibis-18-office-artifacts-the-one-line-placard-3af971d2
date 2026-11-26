import os
LINE = "Printer, beige plastic, c. 1998. Oracle of the Paper Age; petitioners fed it paper offerings and waited in silence for its verdict. On permanent loan from IT."
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
