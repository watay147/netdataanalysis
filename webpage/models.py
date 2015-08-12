from django.db import models

# Create your models here.
class BetterCharField(models.Field):
    def __init__(self, length, *args, **kwargs):
        self.length = length
        super(BetterCharField, self).__init__(*args, **kwargs)
    def db_type(self, connection):
        return 'char(%s)' % self.length

class company(models.Model):
    name=models.CharField(max_length=80)
    description=models.CharField(max_length=500)
    stockno=models.CharField(max_length=6)
    creditindex=models.FloatField()
    creditorder=models.IntegerField()
    creditchange=models.IntegerField()
    attention=models.BooleanField()
    attentionreason=models.CharField(max_length=1000)

    def __unicode__(self):  # __str__ on Python 3
        return self.name
        
class statics(models.Model):
    stockno=models.CharField(max_length=6)
    stadate=models.DateField()
    possent=models.IntegerField()
    negsent=models.IntegerField()
    neusent=models.IntegerField()
    creditindex=models.FloatField()
    creditorder=models.IntegerField()
    price=models.FloatField()
    shouldmark=models.BooleanField()
    

    def __unicode__(self):  # __str__ on Python 3
        return str(self.id)

class events(models.Model):
    stockno=models.CharField(max_length=6)
    comname=models.CharField(max_length=80)
    date=models.DateField()
    content=models.TextField()
    title=models.CharField(max_length=100)
    click=models.IntegerField()
    reply=models.IntegerField()
    source=models.CharField(max_length=40)
    hot=models.IntegerField()

    def __unicode__(self):  # __str__ on Python 3
        return self.title

class news(models.Model):
    stockno=models.CharField(max_length=6)
    comname=models.CharField(max_length=80)
    date=models.DateField()
    content=models.TextField()
    title=models.CharField(max_length=100)
    click=models.IntegerField()
    reply=models.IntegerField()
    source=models.CharField(max_length=40)
    hot=models.IntegerField()

    def __unicode__(self):  # __str__ on Python 3
        return self.title
        


