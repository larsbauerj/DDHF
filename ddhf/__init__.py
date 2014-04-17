from django.db.models.signals import post_save
import models

def my_callback(sender, **kwargs):
    print "# Your specific logic here"

post_save.connect(my_callback, sender=models)
