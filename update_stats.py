import re

with open("README.md", "r") as f:
    content = f.read()

easy = content.count("| Easy |")
medium = content.count("| Medium |")
hard = content.count("| Hard |")

total = easy + medium + hard

stats_block = f"""## Stats

Total Solved: {total}
Easy: {easy}
Medium: {medium}
Hard: {hard}
"""

# 找到 Stats 開頭
start = content.find("## Stats")
end = content.find("## Progress")

new_content = content[:start] + stats_block + "\n" + content[end:]

with open("README.md", "w") as f:
    f.write(new_content)

print("Stats updated!")