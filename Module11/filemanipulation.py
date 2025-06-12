lines=["Hello World\n", "Welcome to Python\n"]
with open("Example.txt","w") as file: #we open the file with premission
    file.writelines(lines)