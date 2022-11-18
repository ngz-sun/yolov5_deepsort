def get_classes(classes_path):
    with open(classes_path, encoding='utf-8') as f:
        class_names = f.readlines()
    class_names = [c.strip() for c in class_names]
    print(class_names)
    return class_names, len(class_names)

get_classes("./model_data/my_voc_classes.txt")