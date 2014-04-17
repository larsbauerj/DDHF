#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.shortcuts import render_to_response
from models import Producers
from models import Files
from models import Items
from models import Donators
from models import Subjects
from models import Pictures
from django.template  import RequestContext
from django.http  import HttpResponse

from django.shortcuts import get_object_or_404

def display_meta(request):
    html = []
    html.append('<tr><td>%s</td></tr>' % request.user)
    values = request.META.items()
    values.sort()
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def ItemsView(request, itemid):
    item = get_object_or_404(Items, pk=itemid)
    c = RequestContext(request, { 'pic': True, "item": item, })
    return render_to_response("admin/base_site.html", c)

def AboutView(request):
    return render_to_response("admin/about.html")
