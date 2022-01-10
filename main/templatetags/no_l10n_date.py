from django import template
from django.utils import formats

register = template.Library()


@register.filter
def no_l10n_date(value, arg=None):
    """
    Using this template filter instead of the builtin 'date' filter ensures date formating will follow the DATE_FORMAT
    and DATETIME_FORMAT formats defined in settings ignoring localized formats.

    This is equivalent to calling the bultin 'date' filter with settings.USE_L10N=False in Django 4, see
    https://github.com/django/django/blob/4.0.1/django/template/defaultfilters.py#L746.
    The Django 4 builtin 'date' filter uses localization over settings when used with setting 'USE_L10N=True' (which is
    the default, see https://docs.djangoproject.com/en/4.0/ref/settings/#date-format.
    The USE_L10N setting is deprecated. Starting with Django 5.0, localized formatting of data will always be enabled.
    Using this filter instead of the builtin 'date' filter ensures we can upgrade to Django 5 without changing date
    formating in templates and avoids the deprecation warnings relative to the setting 'USE_L10N=False'.
    """
    if value in (None, ''):
        return ''
    try:
        return formats.date_format(value, arg, use_l10n=False)
    except AttributeError:
        try:
            return format(value, arg)
        except AttributeError:
            return ''
