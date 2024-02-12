import csv

def getMaxlength(csv_data):
    species = ''
    val = 0
    for row in csv_data:
        len = row[5]
        spec = row[6]
        if len != '' and spec != '': 
            len = float(len[:-1])
            if val < len:
                val = len
                species = spec
    return species

def getLetter(csv_data):
    name_list = []
    processed_name_list = []
    for row in csv_data:
        name = row[0]
        processed_name = list(set([*name]))
        processed_name.sort()
        processed_name = ''.join(processed_name).lower()
        name_list.append(name)
        processed_name_list.append(processed_name)
    
    similar_names_dict = {}
    similar_names_substring_list = []
    for i, value in enumerate(processed_name_list):
        if value in similar_names_dict:
            similar_names_dict[value].append(name_list[i])
        else:
            similar_names_dict[value] = [name_list[i]]
    
    #print(similar_names_dict.values())
    for value in similar_names_dict.values():
        if len(value) > 1:
            similar_names_substring_list.append(value)

    return similar_names_substring_list

def readFile():
    with open(r"/home/skhan/dinosaurs/dinosaurs.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  
        data = list(csv_reader)
        return data

def main():
        csv_data = readFile()
        output_one = getMaxlength(csv_data)
        output_two = getLetter(csv_data)    
        print("Biggest Dinosour is: "+output_one)
        print("list of dinosaurs that can be made using the same letters: " +str(output_two))

if __name__ == "__main__":
    main()     
