import os

lines_list = []

files_dir = "text_files"

poem_filepath = os.path.join(files_dir, "poem.txt")

with open(poem_filepath, "r", encoding = "utf-8")as file:
    for line in file.readlines():
        if line.endswith(",\n") or line.endswith(","):
            new_line = line.replace(",","")
            lines_list.append(new_line)
        else:
            lines_list.append(line)


print(lines_list)

new_poem_filepath = os.path.join(files_dir, "new_poem.text")

with open("new_poem.txt", "w", encoding = "utf-8")as file:
    poem = "".join(lines_list)
    file.write(poem)

with open("new_poem.txt", "a", encoding = "utf-8")as file:
    file.write("\nЯ")


