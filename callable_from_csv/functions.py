from utils.decorators import debug


@debug
def repeater(text : str , repeate : int):
    return text*repeate


@debug
def concatenator(inputs : list):
    return '-'.join(inputs)