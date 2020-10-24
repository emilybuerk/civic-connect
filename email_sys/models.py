from django.db import models

# Create your models here.
class EmailTemplate(models.Model):
    template_text = models.TextField()
    author = models.CharField(max_length = 200)
    rating = models.IntegerField()
    approval = models.BooleanField()
    pub_date = models.DateTimeField('date published')




