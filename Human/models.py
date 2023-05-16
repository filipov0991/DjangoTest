from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=99)
    last_name = models.CharField(max_length=99)
    blood_type = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    unemployed = models.BooleanField()
    married = models.BooleanField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Marriage(models.Model):
    person1 = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person1')
    person2 = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person2')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.person1} and {self.person2}"
    

class Action(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    rating = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.person} {self.description}"