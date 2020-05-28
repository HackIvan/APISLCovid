from django.db import models

# Create your models here.


class latestUpdateSL(models.Model):
    updatedate = models.CharField(max_length= 30)
    updateTime = models.CharField(max_length=11)
    newCases = models.CharField(max_length=3)
    confirmedCases = models.CharField(max_length=5)
    activeCases = models.CharField(max_length=5)
    recoveredCases = models.CharField(max_length=5)
    death = models.CharField(max_length=5)
    recoveryRate = models.CharField(max_length=6)
    fatalityRate = models.CharField(max_length=6)




class districtCases(models.Model):
    Bo = models.CharField(max_length=20)
    Bonthe = models.CharField(max_length=20)
    Bombali = models.CharField(max_length=20)
    Falaba = models.CharField(max_length=20)
    kailahun = models.CharField(max_length=20)
    Kambia = models.CharField(max_length=20)
    Karene = models.CharField(max_length=20)
    Kono = models.CharField(max_length=20)
    Kenema = models.CharField(max_length=20)
    Koinadugu = models.CharField(max_length=20)
    Moyamba = models.CharField(max_length=20)
    Portloko = models.CharField(max_length=20)
    Pujehun = models.CharField(max_length=20)
    Tonkolili = models.CharField(max_length=20)
    WesternRural = models.CharField(max_length=20)
    WesternUrban = models.CharField(max_length=20)
        
            