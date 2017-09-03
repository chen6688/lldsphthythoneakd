from django.db import models
from datetime import datetime
# Create your models here.
class errorLog(models.Model) :
    name = models.CharField(max_length=100, verbose_name="name")
    group = models.CharField(max_length=255, verbose_name="group")
    path = models.CharField(max_length=1000, verbose_name="path")
    createTime = models.DateTimeField(default=datetime.now, verbose_name="create_time")