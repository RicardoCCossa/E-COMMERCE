from django import template

register = template.Library()

@register.filter
def metical(value):
    """
    Formata número para moeda em MT:
    Exemplo: 1500 -> 1.500,00 MT
    """
    try:
        value = float(value)
        return f"{value:,.2f} MT".replace(",", "X").replace(".", ",").replace("X", ".")
    except (ValueError, TypeError):
        return value
