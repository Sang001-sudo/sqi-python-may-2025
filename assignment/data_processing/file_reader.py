def read_data(file_path:str) -> list:
    with open(file_path, "r") as f:
        file_contents = f.readlines()

    list_of_content_tupul =[]
    for content in file_contents:
        name, age = content.split(",")
        content_tupul = (name, int(age))
        list_of_content_tupul.append(content_tupul)
    return list_of_content_tupul