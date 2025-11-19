with open("log.txt", "w") as file:
    file.write("Something here\n")
    file.write("Error connection failed\n")
    file.write("Warning low disk space\n")
    file.write("ERROR file not found\n")
    file.write("Info shutdown complete\n")
with open("log.txt", "r") as file:
    lines = file.readlines()

for index, line in enumerate(lines, start=1):
    if "ERROR" in line:
        print(f"[{index}] {line.strip()}")