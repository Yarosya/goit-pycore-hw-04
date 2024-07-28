def get_cats_info(path):
    cats_info = []
    try:
        with open(path, encoding='utf-8') as f:
            for line in f:
                info = line.strip().split(',')
                if len(info) == 3:
                    cats_info.append({
                        'id': info[0],
                        'name': info[1],
                        'age': info[2]
                    })
                else:
                    raise ValueError("Incorrect line format: {}".format(line))
    except FileNotFoundError:
        print("File not found: {}".format(path))
    except Exception as e:
        print(f"An error occurred: {e}")
    return cats_info

cats_info = get_cats_info("secondTask/cat.txt")
print(cats_info)
