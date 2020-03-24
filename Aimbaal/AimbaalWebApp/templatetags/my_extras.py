from django import template

register = template.Library()
@register.filter(name='cuts')
def cuts(value,arg):
    return value.replace(arg,'')

# register.filter('cut',cut)
