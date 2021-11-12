from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager
from django.db.models import Q

class User(models.Model):
    objects = UserManager()
    """ Custom User Model """

    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Femail'),
    )

    AGE_1929 = 1929
    AGE_3049 = 3049
    AGE_5064 = 5064

    AGE_CHOICES = (
        (AGE_1929, '19~29'),
        (AGE_3049, '30~49'),
        (AGE_5064, '50~64'),
    )

    ACTIVITY_1 = 1.2
    ACTIVITY_2 = 1.375
    ACTIVITY_3 = 1.55
    ACTIVITY_4 = 1.725
    ACTIVITY_5 = 1.9
    ACTIVITY_CHOISES = (
        (ACTIVITY_1, '거의 없음'),
        (ACTIVITY_2, '활동량 조금있다.(주1~2회 운동)'),
        (ACTIVITY_3, '활동량 많다.(주3~5회 운동)'),
        (ACTIVITY_4, '활동량 꽤 많다.(주6~7회 운동)'),
        (ACTIVITY_5, '활동량 아주 많다.(매일 2번 운동)'),
    )


    user_id = models.CharField(max_length=20, unique=True, primary_key=True)
    n_code = models.ForeignKey("Standard", on_delete=models.CASCADE, db_column='n_code')
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    height = models.FloatField(blank=False)
    weight = models.FloatField(blank=False)
    age_category = models.IntegerField(choices=AGE_CHOICES)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    activity = models.FloatField(choices=ACTIVITY_CHOISES)
    proper_cal = models.FloatField(blank=True)
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name, self.gender, self.height, self.weight}'

    def save(self, *args, **kwargs):
        gender = self.gender
        code = Standard.objects.get(gender=gender)
        self.n_code = code.n_code
        # if codename:
        #     self.codename = codename
        super().save(*args, **kwargs)

    # def save2(self, *args, **kwargs):
    #     height = self.height
    #     weight = self.weight
    #     self.proper_cal = 66.47+(13.75*weight)+(5*height)-(6.76*30)
    #     super().save(*args,**kwargs)

    class Meta:
        db_table = 'users'

class Standard(models.Model):
    """ Custom User Model """

    GENDER_MALE = 1
    GENDER_FEMALE = 2

    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
    )

    AGE_1929 = 1929
    AGE_3049 = 3049
    AGE_5064 = 5064

    AGE_CHOICES = (
        (AGE_1929, '19~29'),
        (AGE_3049, '30~49'),
        (AGE_5064, '50~64'),
    )
    n_code = models.CharField(max_length=50, unique=True, primary_key=True)
    age_category = models.IntegerField(choices=AGE_CHOICES)
    carb = models.FloatField(blank=True)
    prot = models.FloatField(blank=True)
    fat = models.FloatField(blank=True)
    sodium = models.FloatField(blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES)

    def __str__(self):
        return f'{self.n_code}'

    class Meta:
        db_table = 'nutri_standard'


