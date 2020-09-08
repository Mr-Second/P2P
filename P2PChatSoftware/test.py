import os
name = "郑康"
data = "123.123.123.123"
file_name = "chat_content_text/" + name + ".txt"
with open(file_name, "a") as f:
    f.write(data)

if os.path.exists(file_name):
    print("文件存在")
