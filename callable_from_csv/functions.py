from utils.decorators import debug, register, FUNCTIONS

debugging = True


@debug(debugging)
@register
def repeater(text: str, repeat: int):
    return text * repeat


@debug(debugging)
@register
def concatenator(inputs: list):
    return '-'.join(inputs)
