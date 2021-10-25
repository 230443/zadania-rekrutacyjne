from django.contrib.auth.models import User
from django.db import models


class Cat(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    is_male = models.BooleanField()

    def get_prays_number(self):
        return Prey.objects.filter(hunting__cat=self).count()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if Cat.objects.filter(user=self.user).count() < 4:
            super(Cat, self).save()
        else:
            raise Exception(f'{self.user} has already 4 cats. No more are allowed.')

    def __str__(self):
        return self.name


class Hunting(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    duration = models.DurationField()

    def __str__(self):
        return "{} at {}".format(self.cat.name, self.start_date.strftime("%m/%d/%Y %H:%M:%S"))


class PreyType(models.Model):
    type_name = models.CharField(max_length=20)

    def __str__(self):
        return self.type_name


class Prey(models.Model):
    type = models.ForeignKey(PreyType, on_delete=models.PROTECT)
    hunting = models.ForeignKey(Hunting, on_delete=models.CASCADE)

    def __str__(self):
        return self.type.type_name
