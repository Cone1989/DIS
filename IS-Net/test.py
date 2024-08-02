import os

if __name__ == "__main__":
    model_path = "../saved_models/Test"
    if(not os.path.exists(model_path)):
        os.mkdir(model_path)
    text = "Hello, World!"

    # 使用 'w' 模式打开文件，如果文件不存在，将会创建文件
    with open(model_path + "/" + "example.txt", 'w') as file:
        file.write(text)
 
