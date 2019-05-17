from django.db import models



class Company(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200,default="")
    email = models.CharField(max_length=200,default="")
    website = models.CharField(max_length=200,default="")

    def __str__(self):
        return self.name


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    industry = models.CharField(max_length=200,default="")
    position = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200,default="")
    description = models.CharField(max_length=1000,default="")
    age=models.IntegerField(default=20)
    educationType = models.CharField(max_length=200,default="")
    placeOfResidence=models.CharField(max_length=200,default="")
    lengthOfService=models.CharField(max_length=200,default="")
    pub_date = models.DateTimeField('date published')
    salary = models.IntegerField(default=0)

    def __str__(self):
        return self.position

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email=models.CharField(max_length=200,default="")
    studyLevel = models.CharField(max_length=200,default="")
    motivLetter = models.CharField(max_length=1000,default="")
    def __str__(self):
        return self.name