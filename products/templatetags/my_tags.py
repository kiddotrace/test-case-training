from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    """
    return encoded URL parameters that are the same as the current
    request's parameters, only with the specified GET parameters added or changed.

    For example, if you're on the page ``/products/?modified=true&page=5``,
    then

    <a href="/products/?{% param_replace page=3 %}">Page 3</a>...

    would expand to

    <a href="/products/?modified=true&page=3">Page 3</a>...
    """
    context_data = context['request'].GET.copy()
    for k, v in kwargs.items():
        context_data[k] = v
    for k in [k for k, v in context_data.items() if not v]:
        del context_data[k]
    return context_data.urlencode()
