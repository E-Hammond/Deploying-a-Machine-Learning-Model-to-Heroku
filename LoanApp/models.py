from django.db import models

# Create your models here.


class ModelFeatures(models.Model):
    GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'))
    MARRIED_CHOICES = (('Yes', 'Yes'), ('No', 'No'))
    EDUCATION_CHOICES = (('Graduate', 'Graduate'), ('Not Graduate', 'Not Graduate'))
    SELF_EMPLOYED_CHOICES = (('Yes', 'Yes'), ('No', 'No'))
    CREDIT_HISTORY_CHOICES = (('Yes', 'Yes'), ('No', 'No'))
    PROPERTY_AREA_CHOICES = (('Urban', 'Urban'), ('Rural', 'Rural'), ('SemiUrban', 'SemiUrban'))

    gender = models.CharField(max_length=6,
                              choices=GENDER_CHOICES,
                              default='Male',
                              blank=False)

    married = models.CharField(max_length=3,
                               choices=MARRIED_CHOICES,
                               default='Yes',
                               blank=False)

    dependents = models.IntegerField(blank=False, null=True)

    education = models.CharField(max_length=15,
                                 choices=EDUCATION_CHOICES,
                                 default='Not Graduate',
                                 blank=False, null=True)

    self_employed = models.CharField(max_length=3,
                                     choices=SELF_EMPLOYED_CHOICES,
                                     default='Yes',
                                     blank=False, null=True)

    applicant_income = models.IntegerField(blank=False, null=True)

    co_applicant_income = models.FloatField(max_length=10,
                                            blank=False,
                                            null=True)

    loan_amount = models.FloatField(max_length=10,
                                    blank=False,
                                    null=True)

    loan_term = models.CharField(max_length=5,
                                 choices=CREDIT_HISTORY_CHOICES,
                                 default='Yes',
                                 blank=False,
                                 null=True)

    property_area = models.CharField(max_length=10,
                                     choices=PROPERTY_AREA_CHOICES,
                                     default='Urban',
                                     blank=False,
                                     null=True)

    def __str__(self):
        return self.gender
