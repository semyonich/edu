from django import template

register = template.Library()

def color(value):
    return "red"

register.filter('color', color)