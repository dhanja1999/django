from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Applicationuser(models.Model):
    choice = (('provider','PROVIDER'),('seeker','SEEKER'))
    
    uid = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,null=True,on_delete=models.SET_NULL)
    user_satus = models.CharField(max_length=10,choices=choice)
    phonenumber = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to='pic/',blank=True,null=True)
    rating = models.IntegerField(default=0)
    rated_user_count = models.IntegerField(default=0)
    address = models.TextField()
    
    
    def __str__(self):
        return self.user.username

class Job(models.Model):
    choice = (('request','REQUEST'),('accept','ACCEPT'))
    
    job_id = models.AutoField(primary_key=True)
    seeker = models.ForeignKey(Applicationuser,null=True,on_delete=models.SET_NULL,related_name='job_seeker')
    provider = models.ForeignKey(Applicationuser,null=True,on_delete=models.SET_NULL,related_name='job_provider')
    status  = models.CharField(max_length=10,choices=choice,default='request')
    
    def __str__(self):
        return self.job_id

class Payment(models.Model):
    choice = (('pending','PENDING'),('done','DONE'))

    payment_id = models.AutoField(primary_key=True)
    job = models.ForeignKey(Job, null=True,on_delete=models.SET_NULL)
    ammount = models.CharField(max_length=10)
    payment_status = models.CharField(max_length=10,choices=choice,default='pending')
    
    def __str__(self):
        return self.payment_id
