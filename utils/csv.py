from csv import writer

def generate(header,values,filename="data.csv"):
    with open(filename,"w") as file:
        csv_writer = writer(file)
        csv_writer.writerow(header)
        csv_writer.writerows(values)