import csv
def write_csv(data,file_path):
    keys=data[0].keys()
    with open(file_path,'a',newline="") as file:
        writer=csv.DictWriter(file,fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

