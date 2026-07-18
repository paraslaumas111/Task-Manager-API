import csv

def display_population():
    with open(r"C:\Users\Anurag Laumas\Desktop\PGT CS\Ryan International School\12th\Tuition\Vivek (Re-Test)\countries.csv", "r") as f:
        reader = csv.reader(f)

        reader.__next__()
        c=0
        for row in reader:
            c+=1
        print(c)

    # f.close()

display_population()