from django import template

register = template.Library()

@register.filter
def get_data(dictionary, key):
    return dictionary.get(key)