from utils.decorators import time
from csv import reader
from ast import literal_eval
from functions import concatenator, repeater


@time
def main():
    with open("./run.csv", 'r') as file:
        csvreader = reader(file,delimiter=';')
        for row in csvreader:
            callable = getattr(functions,row[0])
            callable(*literal_eval(row[1]))


if __name__ == '__main__':
    main()