#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
from django import forms
class ContactForm(forms.Form):
   subject = forms.CharField(max_length=100)
   message = forms.CharField()
   sender = forms.EmailField()
   subject = forms.CharField(max_length=100)

data = {
    'subject': '',
    'message': 'Hi there',
    'sender': 'invalid email address',
    'cc_myself': True,
    }
f = ContactForm(data)
f.is_valid()
print """<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="da"
      lang="da">

  <head>
    <meta http-equiv="Content-Type"
          content="text/html;charset=utf-8" />
"""
print f
f = ContactForm({'subject': 'hello'})

class CommentForm(forms.Form):
  name = forms.CharField(initial='class')
  url = forms.URLField()
  comment = forms.CharField()
f = CommentForm(initial={'name': 'instance'}, auto_id=False)
print f
print "</html>"
