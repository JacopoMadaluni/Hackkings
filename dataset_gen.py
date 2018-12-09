import random
import csv
def create_dataset1(header):
    a = 2.0
    b = 3.5
    c = 4.0
    d = 600.8

    dataset = [header]
    for _ in range(5000):
        x1 = random.uniform(1, 10000)
        x2 = random.uniform(10000, 100000)
        x3 = random.uniform(10000, 100000)
        x4 = random.uniform(10000, 100000)

        y = a*x1 + b*x2 + c*x3 + d*x4**2
        row = [a*x1, b*x2, c*x3, d*x4, y]
        dataset.append(row)

    with open("5000_Sturtups.csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(dataset)

if __name__ == "__main__":
    create_dataset1(["N_Workers", "Staff", "Infrastructure", "Marketing", "Profit"])
