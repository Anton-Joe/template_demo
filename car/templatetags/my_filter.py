from django import  template

register = template.Library()


# 第一种写法---------------------start
def my_first_filter(value, word):
    return value + word


register.filter('my_first_filter_name', my_first_filter)
# -------------------------------end


# 另外一种写法：
# @register.filter 或者 @register.filter(my_first_filter_name)
# def my_first_filter(value, word):
#     return value + word
