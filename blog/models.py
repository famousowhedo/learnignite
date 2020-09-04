from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

# Create your models here.


class Course(models.Model):
    rating = models.CharField(max_length=12, blank=True)
    instructor_name = models.CharField(max_length=20)
    instructor_badge = models.CharField(max_length=10, blank=True)
    course_image =  models.ImageField(upload_to='images/', blank=True)
    video_lenght = models.CharField(max_length=30, blank=True)
    date = models.DateTimeField(default=timezone.now)
    Course_Title = models.CharField(max_length=200)
    Course_Subtitle = models.CharField(max_length=300)
    Language = models.CharField(max_length=80, blank=True)
    Requirement_1 = models.CharField(max_length=100, blank=True)
    Requirement_2 = models.CharField(max_length=100,  blank=True)
    Requirement_3 = models.CharField(max_length=100 , blank=True)
    Description = models.TextField()
    What_you_ll_learn_1 = models.CharField(max_length=100 , blank=True)
    What_you_ll_learn_2 = models.CharField(max_length=100, blank=True)
    What_you_ll_learn_3 = models.CharField(max_length=100, blank=True)
    link_to_course = models.URLField()
    admin_approver =models.BooleanField(default=False)
    class Meta:
        ordering = ['date']
   
    def __str__(self):
        return "{}".format( self.instructor_name)
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
      
        

    def save(self):
        super().save()

        img = Image.open(self.course_image.path)

        if img.height > 300 or  img.width > 300:
            output_siz = (300,300)
            img.thumbnail(output_siz)
            img.save(self.course_image.path)
            
        