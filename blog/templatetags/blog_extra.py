from django import template
from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFill


register = template.Library()

@register.simple_tag
def change_state(value):
	return -value

