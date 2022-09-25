from utils.decorators import debug, register, FUNCTIONS


@debug
@register
def repeater(text : str , repeate : int):
    return text*repeate


@debug
@register
def concatenator(inputs : list):
    return '-'.join(inputs)
