import hashlib

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager, User, PermissionsMixin
from django.db.models import Q

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
    n_code = models.CharField(max_length=50, unique=True)
    age_category = models.IntegerField(choices=AGE_CHOICES)
    carb = models.FloatField(blank=True)
    prot = models.FloatField(blank=True)
    fat = models.FloatField(blank=True)
    sodium = models.FloatField(blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES)

    class Meta:
        db_table = 'nutri_standard'

    def __str__(self):
        return f'{self.n_code}'


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, user_id, password, **extra_fields):
        if not user_id:
            raise ValueError('The given user_id must be set')

        user_id = self.user_id
        user = self.model(user_id=user_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, user_id, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(user_id, password, **extra_fields)

    def create_superuser(self, user_id, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(user_id, password, **extra_fields)


# class UserManager(BaseUserManager):
#     def create_user(self, user_id, password=None):
#         if not user_id:
#             raise ValueError('Users must have an ID')
#
#         user = self.model(
#             user_id=user_id,
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, user_id, password):
#         user = self.create_user(
#             user_id=user_id,
#             password=password,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user

class User(AbstractBaseUser, PermissionsMixin):
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

    user_id = models.CharField(max_length=20, unique=True, null=False)
    n_code = models.ForeignKey('Standard', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    height = models.FloatField(blank=False)
    weight = models.FloatField(blank=False)
    age_category = models.IntegerField(choices=AGE_CHOICES)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    activity = models.FloatField(choices=ACTIVITY_CHOISES)
    proper_cal = models.FloatField(blank=True)
    create_dt = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'user_id'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return f'{self.n_code, self.user_id, self.gender, self.proper_cal}'

    # def save(self, *args, **kwargs):
    #     gender = self.gender
    #     code = Standard.objects.get(gender=gender)
    #     self.n_code = code.n_code
    #     # if codename:
    #     #     self.codename = codename
    #     super().save(*args, **kwargs)

    # def save2(self, *args, **kwargs):
    #     height = self.height
    #     weight = self.weight
    #     self.proper_cal = 66.47+(13.75*weight)+(5*height)-(6.76*30)
    #     super().save(*args,**kwargs)

    class Meta:
        db_table = 'users'




