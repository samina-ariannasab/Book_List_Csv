import csv
#--------------- Read to File----------------
def read_data_csv(filepath="../DB/Book.csv") :
    datalist=[]
    with open(filepath) as book_file :
     reader = csv.reader(book_file)
     for item in reader:
         datalist.append(item)
    return datalist

#--------------- Write to File----------------
def write_data_csv(data,filepath="../DB/Book.csv") :
    with open(filepath, mode="a" ,  newline="") as book_file :
        writer=csv.writer(book_file)
        writer.writerow(data)
