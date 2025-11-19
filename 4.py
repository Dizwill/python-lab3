import os
folder = "texts"
output = "merged.txt"
files = sorted(f for f in os.listdir(folder) if f.endswith(".txt"))
with open(output, "w", encoding="utf-8") as out:
    for i, name in enumerate(files):
        path = os.path.join(folder, name)
        print("Adding:", name)
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                out.write(line)
        if i != len(files) - 1:
            out.write("\n==== end of file ====\n")

print("File created!", output)