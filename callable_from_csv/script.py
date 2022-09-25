import functions
from utils.decorators import time
from csv import reader
from ast import literal_eval


@time
def call_functions(csv_path):
    """
    Fetch data about functions and inputs from csv file. Make function calls and print debug info.
    Inputs: csv_path
    """
    with open(csv_path, 'r') as file:
        csvreader = reader(file,delimiter=';')
        for row in csvreader:
            callable = getattr(functions,row[0])
            callable(*literal_eval(row[1]))


if __name__ == '__main__':
    call_functions("./run.csv")
