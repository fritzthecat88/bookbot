def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main(y):
    x = get_book_text(y) 
    z = x.split()
    counter = 0
    for i in range(0, len(z)):
        counter += 1
    return counter

def number_characters(text):
    low_case = text.lower()
    count_dic = {}
    for i in low_case:
        if i not in count_dic:
            count_dic[i] = 1
        else:
            count_dic[i] += 1
    return count_dic

def print_report(dict):
    list = []
    for i in dict:
        list.append({"char": i, "num": dict[i]})
    return list

def sort_on(items):
    return items["num"]