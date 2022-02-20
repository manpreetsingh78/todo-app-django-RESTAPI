from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ("OPEN", "OPEN"),
    ("WORKING", "WORKING"),
    ("DONE", "DONE"),
    ("OVERDUE", "OVERDUE"),
)

class ToDoList(models.Model):
    title = models.CharField(max_length=100,blank=False,null=False)
    description = models.TextField(max_length=1000,blank=False,null=False)
    due_date = models.DateField(blank=True,null=True)
    tags = models.CharField(max_length=250,blank=True,null=True)
    status = models.CharField(max_length=20,default='OPEN',choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)



#-------------------JWT AUTH----------------

# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token

# @receiver(post_save,sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender,instance=None,created=False,**kwargs):
#     if created:
#         Token.objects.create(user=instance)
