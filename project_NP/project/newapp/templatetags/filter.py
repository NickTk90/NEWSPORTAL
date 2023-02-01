from django import template


register = template.Library()

CURRENCIES_SYMBOLS = [
    'тобот',
    'выборы',
    'чемпионат'
]

@register.filter(neme='censor')
def censor(value):
    if not isinstance(value,str):
        raise TypeError (f"не тот тип '{type(value)}' введите строковый")

    for word in value.split():
        if word.lower() in CURRENCIES_SYMBOLS:
            value=value.replace(word, f"{word[0]}{'*' * (len(word)-1)}")
    return value