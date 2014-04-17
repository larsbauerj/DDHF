# -*- coding: UTF-8 -*-
#
from django.db import models
from models import Donators
from models import Files
from models import Sted
from models import Subjects
from models import Pictures
from models import PictureList
from models import Producers
from models import Items
from models import Status
from django.contrib import admin
from django import forms
from django.forms import ModelForm, Textarea, TextInput
from django.contrib.auth.models import User
from widgets import AdminFileWidget
#from widgets import ManyToManyRawIdWidget
#from widgets import ForeignKeyRawIdWidget

class Firstletter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Start bogstav'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'itemheadline'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        s = set( obj.itemheadline[0].upper() for obj  in Items.objects.all())
        return ((c, c) for c in sorted(s) )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value():
          return queryset.filter(itemheadline__istartswith=self.value()) 
        else:
          return queryset

def set_user(request, obj, field_name, change):
  if hasattr(obj, field_name):
    # print "change:", change, getattr(obj, field_name).strip()
    if getattr(obj, field_name) is None or getattr(obj, field_name).strip() == "":
      setattr(obj, field_name, request.user.username)
      change = True
  else:
    setattr(obj, field_name, request.user.username)
    change = True
  return change

class PicturesAdmin(admin.ModelAdmin):
  ordering = '-pictureid',
  list_per_page = 50
  list_max_show_all = list_per_page
  formfield_overrides = {
    models.ImageField: {'widget': AdminFileWidget},
  }
  readonly_fields = ['pictureregisteredby',]
  list_display = ("pictureid",
          "picture_tag",
          "picturetext",
          "pictureregisteredby",
          "pictureoriginal",
           )
  list_display_links = ("pictureid",)
  search_fields =('picturetext', 'pictureid')

  def save_model(self, request, obj, form, change):
    if set_user(request, obj, "pictureregisteredby", change):
      obj.save()

admin.site.register(Pictures, PicturesAdmin)


class PictureListAdmin(admin.ModelAdmin):
  readonly_fields = 'picture_tag',
  ordering = '-item__itemid', 'orden'
  list_display =  'item', 'itemid', 'picture_tag', 'orden',
  extra = 0
admin.site.register(PictureList, PictureListAdmin)


class PictureListInline(admin.TabularInline):
  readonly_fields = 'picture_tag',
  raw_id_fields     = 'picture',
  model         = PictureList
  fieldsets = [
    ( '',
      {
      'fields': ['item', 'orden', ('picture', 'picture_tag'),],
       'classes': ['collapse', 'aligned', 'extrapretty'],
      },
    ),
  ]
  extra = 0


class ItemsForm(forms.ModelForm):
  class Meta:
    model = Items
    widgets = {
       'itemdescription' : Textarea(attrs={'cols' : 70, 'rows' : 3}),
       'itemextrainfo'   : Textarea(attrs={'cols' : 70, 'rows' : 3}),
       'itemreferences'  : Textarea(attrs={'cols' : 70, 'rows' : 3}),
       'itemremarks'     : Textarea(attrs={'cols' : 70, 'rows' : 3}),
       'itemreceivedby'  : TextInput(attrs={'size' : 6}),
       'itemlocation'    : Textarea(attrs={'cols' : 70, 'rows' : 3}),
       'itemusedby'      : Textarea(attrs={'cols' : 70, 'rows' : 3}),
       'itemusedfor'     : Textarea(attrs={'cols' : 70, 'rows' : 3}),
       'itemrestoration' : Textarea(attrs={'cols' : 70, 'rows' : 3}),
    }

class ItemsAdmin(admin.ModelAdmin):
  list_per_page = 50
  list_max_show_all = list_per_page
  save_on_top = True
  actions_on_top = True
  actions_on_bottom = True
  save_as = True

  form = ItemsForm
  # admin.site.disable_action('delete_selected')
  actions = [ 'marker_godkendt', 'marker_klar', 'marker_kladde', 'marker_udgaaet', 'marker_intern', ]

  def mesg(self, antal, tekst, request):
    verbose_name =  { 1:self.model._meta.verbose_name, }.get(antal, self.model._meta.verbose_name_plural)
    message_bit = "%s %s blev markeret som %s." % (antal, verbose_name, tekst)
    self.message_user(request, message_bit)

  def marker_godkendt(self, request, queryset):
    self.mesg( queryset.update( itemdeleted=0), "godkendt", request)
  marker_godkendt.short_description = "Godkendt"

  def marker_klar(self, request, queryset):
    self.mesg(queryset.update(itemdeleted=1), "klar", request)
  marker_klar.short_description = "Klar til godkendelse"

  def marker_kladde(self, request, queryset):
    self.mesg(queryset.update(itemdeleted=2), "kladde", request)
  marker_kladde.short_description = "Kladde"

  def marker_udgaaet(self, request, queryset):
    self.mesg(queryset.update(itemdeleted=3), u"udgået", request)
  marker_udgaaet.short_description = u"Udgået"

  def marker_intern(self, request, queryset):
    self.mesg(queryset.update(itemdeleted=4), "intern", request)
  marker_intern.short_description = "Intern"

  readonly_fields = ['itemid', 'itemregisteredby', 'view_pictures',]

  list_filter = Firstletter, 'fileid', 'itemdeleted', 'lastmodified'
  fieldsets = [
    ( '',
      {
      'fields': [
        ('itemheadline', 'itemdescription',),
        ('fileid', 'itemdatingfrom', 'itemdatingto',),
        ('itemdeleted', 'itemacquiretype',),
        'donatorid',
        ('producerid', 'itemmodeltype', 'itemserialno',),
        ('itemreceived', 'itemregistered', 'itemreceivedby', ),
        'itemusedwhereid',
         # ('itemid', 'itempicture', 'view_pictures',),
         ('itemid', 'view_pictures',),
        ('itemextrainfo', 'itemreferences', 'itemremarks',),
         'itemsubject',
      ],
       'classes': ['wide', 'aligned', 'extrapretty'],
      },
    ),
    ( 'admin',
      {
      'fields': [
            ('itemsize', 'itemweight',),
            ('itemdepositeduntil', 'itemoutdated', 'itemborroweduntil',),
            ('itemusedfrom', 'itemusedto',),
            ('itemusedendfrom', 'itemusedendto',),
            ( 'itemregisteredby', 'itemthanksletter',),
            ( 'itemlocation',),
            ( 'itemusedby', 'itemusedfor', ),
            ( 'itemrestoration',),
            ],
       'classes': ['collapse', 'wide', 'aligned'],
      },
      ),
  ]
  # list_display = 'itemid', 'itemheadline', 'get_pictures', 'itemdescription', 'itemregisteredby',
  list_display = 'itemheadline', 'itemid', 'piclist', 'itemdescription', # 'itemregisteredby',
  search_fields =('itemid', 'itemheadline', 'itemdescription', 'itemmodeltype',
          'itemusedby', 'itemusedfor',
          'itemusedwhereid__stednavn',
          'itemextrainfo', 'itemremarks',
          'producerid__producertitle',
          'donatorid__donatorname',
          'fileid__filetitle',
          'itemsubject__subjecttitle',
          'itemserialno',
          'itemreceivedby',
          )
  filter_horizontal = 'itemsubject',
  # raw_id_fields     = 'itempicture',
  raw_id_fields     = 'itemusedwhereid',
  inlines         = [PictureListInline]
  # date_hierarchy    = 'itemdatingfrom'

  class Admin:
    list_filter = 'itemreceived', 'itemreceivedby', 'lastmodified', 'itemregistered'

  def save_model(self, request, obj, form, change):
    if set_user(request, obj, "itemregisteredby", change):
      obj.save()
admin.site.register(Items, ItemsAdmin)


# class ItemsInline(admin.StackedInline):
class ItemsInline(admin.TabularInline):

  model         = Items
  list_display_links = ( 'itemheadline',)
  # raw_id_fields = 'itempicture',
  #readonly_fields = ['get_pictures', 'producerid', 'itemusedwhereid', 'itemsubject', ]
  # readonly_fields = ['itemheadline', 'get_pictures','itemdescription', ]
  readonly_fields = ['itemheadline', 'piclist','itemdescription', ]
  list_per_page = 5
  # list_max_show_all = list_per_page
  can_delete = False

  def has_add_permission(self, request):
    return False


  fieldsets = [
    ( 'genstand',
      {
      # 'fields':[( 'get_pictures','itemdescription', )
      'fields':[( 'piclist','itemdescription', )
        ],
       'classes': ['wide', 'aligned'],
      },
    ),
      # { 'filter_horizontal':['itemsubject'],},
      # { 'filter_vertical':['itempicture'],},
    ]
  extra = 0


class DonatorsAdmin(admin.ModelAdmin):
  save_on_top = True
  list_per_page = 20
  list_max_show_all = list_per_page
  list_display = (
         'donatorname',
         'donatorinstitution',
         'donatorposition',
         'donatoraddress',
         'donatorphone',
         'donatoremail',
         'creator',
           )
  search_fields = 'donatorname', 'donatorinstitution', 'donatorposition', 'donatoraddress', 'donatorphone', 'donatoremail',
  list_display_links = 'donatorname',
  readonly_fields = ['creator',]
  # list_filter = [ 'created', 'lastmodified', ]
  fieldsets = [
    ( 'Donator',
      { 'fields': [
        'donatorname',
        'donatorinstitution',
        'donatorposition',
        'donatoraddress',
        'donatorphone',
        'donatoremail',
        'creator'
        ],
       'classes': ['wide', 'aligned'],
      },
    ),
  ]
  inlines = [ItemsInline]

  def save_model(self, request, obj, form, change):
    if set_user(request, obj, "creator", change):
      obj.save()

admin.site.register(Donators, DonatorsAdmin)


class FilesForm(forms.ModelForm):
  class Meta:
    model = Files
    widgets = {
      'filedescription' : Textarea(attrs={'cols' : 70, 'rows' : 3}),
    }

class FilesAdmin(admin.ModelAdmin):
  save_on_top = True
  list_per_page = 20
  list_max_show_all = list_per_page
  form = FilesForm
  list_display = (
    'filetitle',
    'filedescription',
    'datingfrom',
    'datingto',
    'creator',
  )
  search_fields = 'filetitle', 'filedescription',
  list_display_links = ( 'filetitle',)

  # date_hierarchy  = 'datingfrom'
  readonly_fields = ['creator', 'lastmodified']
  # list_filter     = [ 'created', 'lastmodified', ]
  fieldsets = [
    ( 'Sag',
      { 'fields': ['filetitle', 'filedescription', 'datingfrom', 'datingto', 'creator',
        ],
       'classes': ['wide', 'aligned'],
      },
    ),
  ]
  inlines         = [ItemsInline]

  def save_model(self, request, obj, form, change):
    if set_user(request, obj, "creator", change):
      obj.save()

admin.site.register(Files, FilesAdmin)


class StedAdmin (admin.ModelAdmin):
  search_fields = ('stednavn',)
  ordering = 'stednavn',
  # list_per_page = 20
  # list_max_show_all = list_per_page
admin.site.register(Sted, StedAdmin)

class StatusForm(forms.ModelForm):
  class Meta:
    # model = Status
    exclude = [ "block",]

class StatusAdmin (admin.ModelAdmin):
  form = StatusForm
  list_per_page = 20
  list_max_show_all = list_per_page
  list_display = ( "nummer", "block", "status",)
admin.site.register(Status, StatusAdmin)


class ProducersAdmin(admin.ModelAdmin):
  save_on_top = True
  list_display = (
    'producertitle',
    'producerdescription',
    )

  list_display_link = (
    'producertitle',
    )

  # list_filter     = [ 'created', 'lastmodified', ]
  fieldsets = [
    ( 'Producent',
      { 'fields': [ 'producertitle', 'producerdescription', 'creator', ], 
       'classes': ['wide', 'aligned'],
      },
    ),
  ]
  readonly_fields = ['creator',]

  def save_model(self, request, obj, form, change):
    if set_user(request, obj, "creator", change):
      obj.save()

  inlines = [ItemsInline]

admin.site.register(Producers, ProducersAdmin)


class SubjectsAdmin(admin.ModelAdmin):
  list_per_page         = 500
  list_max_show_all     = list_per_page
  list_display          = (
      'subjecttitle',
      'subjectdescription',
  )
  list_display_links    = 'subjecttitle',
  search_fields         = 'subjecttitle', 'subjectdescription',
  # list_filter           = [ 'created', 'lastmodified', ]
  fields                = [ 'subjecttitle', 'subjectdescription', 'creator', ]
  readonly_fields       = ['creator',]

  def save_model(self, request, obj, form, change):
    if set_user(request, obj, "creator", change):
      obj.save()

admin.site.register(Subjects, SubjectsAdmin)
