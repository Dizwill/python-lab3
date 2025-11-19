with open("article.txt", "w", encoding="utf-8") as f:
    f.write("Hello!\n"
            "This is the first paragraph of the text.\n\n"
            "This is the second paragraph.\n"
            "It also contains something.\n\n"
            "And finally the third paragraph.")

with open("article.txt", "r", encoding="utf-8") as f:
    content = f.read()
paragraphs = content.split("\n\n")
for i, paragraph in enumerate(paragraphs, start=1):
    filename = f"part_{i}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(paragraph)
    print(f"File created: {filename}")

print(f"Ready. Files created: {len(paragraphs)}")