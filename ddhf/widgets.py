"""
Form Widget classes specific to the Django admin site.
"""

import copy

from django import forms
from django.utils.html import escape
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from django.conf import settings

class AdminFileWidget(forms.FileInput):
  """
  A FileField Widget that shows its current value if it has one.
  """
  def __init__(self, attrs={}):
    super(AdminFileWidget, self).__init__(attrs)

  def render(self, name, value, attrs=None):
    output = []
    if value and hasattr(value, "url"):
        img = ""
        if hasattr(value, "width"):
            img = '<img border="1" src="%s">' % (escape(value.url.replace("original","low")))
        output.append('%s <a target="_blank" href="%s">%s</a><br> %s %s' % \
            (_('Currently:'), escape(value.url), escape(value), _('Change:'), img, ))
    output.append(super(AdminFileWidget, self).render(name, value, attrs))
    return mark_safe(u'\n'.join(output))
