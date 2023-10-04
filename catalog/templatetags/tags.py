from django import template

register = template.Library()


@register.filter()
def mediapath(i):
    if i:
        return f'/media/{i}'
    return '#'


@register.simple_tag()
def mediapath(i):
    if i:
        return f'/media/{i}'
    return '#'
