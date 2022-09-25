from utils.decorators import timed
from csv import reader
from ast import literal_eval

import functions


@timed
def main():
    with open("./run.csv", 'r') as file:
        csvreader = reader(file,delimiter=';')
        for row in csvreader:
            inputs = literal_eval(row[1])
            print(inputs)
            callable = getattr(functions,row[0])
            output = callable(*inputs)
            print(output)


if __name__ == '__main__':
    main()