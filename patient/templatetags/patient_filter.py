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
def birth(value, back):
    if back=='3' or back=='4':
        year = '20'+value[:2]
    else:
        year = '19'+value[:2]
    birth = year+'.'+value[2:4]+'.'+value[4:]
    return birth

@register.filter
def birth2(value, back):
    if back=='3' or back=='4':
        year = '20'+value[:2]
    else:
        year = '19'+value[:2]
    birth = year+'년 '+value[2:4]+'월 '+value[4:]+'일'
    return birth

@register.filter
def id_cut(value):
    return value[:8]