from django.db import models

# Create your models here.

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

MARRIED_CHOICES = [
    ('No', 'No'),
    ('Yes', 'Yes'),
]

SPENDING_CHOICES = [
    ('Low', 'Low'),
    ('Average', 'Average'),
    ('High', 'High'),
]

GRADUATED_CHOICES = [
    ('No', 'No'),
    ('Yes', 'Yes'),
]

PROFESSION_CHOICES = [
    ('Healthcare', 'Healthcare'),
    ('Engineer', 'Engineer'),
    ('Lawyer', 'Lawyer'),
    ('Doctor', 'Doctor'),
    ('Entertainment', 'Entertainment'),
    ('Artist', 'Artist'),
    ('Executive', 'Executive'),
    ('Homemaker', 'Homemaker'),
    ('Marketing', 'Marketing'),
]

CATEGORY_CHOICES = [
    ('Var_1_0', '1'),
    ('Var_1_1', '2'),
    ('Var_1_2', '3'),
    ('Var_1_3', '4'),
    ('Var_1_4', '5'),
    ('Var_1_5', '6'),
    ('Var_1_6', '7'),
    ('Var_1_7', '8'),
    ('Var_1_8', '8'),
]


class UserInfo(models.Model):
    customer_id = models.CharField(max_length=6)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES)
    age = models.CharField(max_length=4)
    married = models.CharField(max_length=4, choices=MARRIED_CHOICES)
    graduated = models.CharField(max_length=4, choices=GRADUATED_CHOICES)
    profession = models.CharField(max_length=15, choices=PROFESSION_CHOICES)
    work_experience = models.CharField(max_length=3)
    spending = models.CharField(max_length=8, choices=SPENDING_CHOICES)
    family_size = models.CharField(max_length=3)
    category = models.CharField(max_length=8, choices=CATEGORY_CHOICES, default='None')
    segment = models.CharField(max_length=4, blank=True, default='None')

    def __str__(self):
        return self.customer_id