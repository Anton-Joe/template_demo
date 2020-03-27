from django import  template

register = template.Library()


def my_first_filter(value, word):
    return value + word


register.filter('my_first_filter_name', my_first_filter)

