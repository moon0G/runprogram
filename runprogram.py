import os, sys

exe = {".py": ["py", False], ".cpp": ["clang++", True], ".c": ["clang", True], ".rs": ["cargo run", None]}

try:
    fn = sys.argv[1]
    exten = ""
    isend = False

except:
    print("No Argument Supplied.")
    os.quit()

for x in fn[::-1]:
    if isend == False:
        exten += x

    if x == '.':
        isend = True

exten = exten[::-1]

#print(f"cls; {exec[exten]} {fn}")
if exe[exten][1] == True:
    os.system(f"{exe[exten][0]} {fn} -o {fn[:-len(exten)]}.exe && .\{fn[:-len(exten)]}")

elif exe[exten][1] == False:
    os.system(f"{exe[exten][0]} {fn}")
else:
    os.system(f"{exe[exten][0]}")
