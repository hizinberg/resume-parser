from djongo import models

class Resume(models.Model):
    skill = models.CharField(max_length=100)

    resume = models.FileField(null=True,blank=True,upload_to='images/')
    
    skillset=models.CharField(null = True ,max_length=500)
    

