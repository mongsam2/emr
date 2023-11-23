from django import template

register = template.Library()

@register.filter
def sub(value, arg):
    return value-arg

@register.filter
def back(value):
    ans=''
    if int(value)%2==0:
        ans = '여'
    else:
        ans = '남'
    return ans

@register.filter
def back2(value):
    ans=''
    if int(value)%2==0:
        ans = '여성'
    else:
        ans = '남성'
    return ans

@register.filter
def birth(value):
    birth = value[:4]+'.'+value[4:6]+'.'+value[6:]
    return birth

@register.filter
def birth2(value):
    birth = value[:4]+'년 '+value[4:6]+'월 '+value[6:]+'일'
    return birth

@register.filter
def id_cut(value):
    return value[:8]