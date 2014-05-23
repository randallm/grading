from django import template
from lessons.models import Response

register = template.Library()

@register.filter
def response_to_q(question, user):
    try:
        return question.response_set.get(answerer=user).text
    except Response.DoesNotExist:
        return ''

@register.filter
def response_comment(question, user):
    try:
        return question.response_set.get(answerer=user).comment
    except Response.DoesNotExist:
        return None