from django.db import models

SET_DAYS = [
    (0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30')
]
HEALTH_CONDITION = [
     (1, 'Excellent'), (2, 'Very good'), (3, 'Good'), (4, 'Fair'), (5, 'Poor')
]
EDUCATION_LEVEL = [
    (1, 'Never attended school or only kindergarten'),
    (2, 'Grades 1 through 8 (Elementary)'),
    (3, 'Grades 9 through 11 (Some high school)'),
    (4, 'Grade 12 or GED (High school graduate)'),
    (5, 'College 1 year to 3 years (Some college or technical school)'),
    (6, 'College 4 years or more (University graduate)')
]

MONTH_INCOME = [
    (1, 'less than 10000 tk'),
    (2, 'less than 15000 tk'),
    (3, 'less than 20000 tk'),
    (4, 'less than 25000 tk'),
    (5, 'less than 35000 tk'),
    (6, 'less than 50000 tk'),
    (7, 'less than 75000 tk'),
    (8, '75,000 tk or more')
]
# Create your models here.
class Diabetic(models.Model):
    HighBP = models.IntegerField()                
    HighChol = models.IntegerField()              
    Height = models.FloatField()   
    Weight = models.FloatField()               
    Smoker = models.IntegerField()               
    Stroke = models.IntegerField()               
    HeartDiseaseorAttack = models.IntegerField() 
    PhysActivity = models.IntegerField()         
    HvyAlcoholConsump = models.IntegerField()    
    NoDocbcCost = models.IntegerField()          
    GenHlth = models.IntegerField(choices=HEALTH_CONDITION)              
    MentHlth = models.IntegerField(choices=SET_DAYS)             
    PhysHlth = models.IntegerField(choices=SET_DAYS)             
    DiffWalk = models.IntegerField()             
    Age = models.FloatField()                  
    Education = models.IntegerField(choices=EDUCATION_LEVEL)            
    Income = models.IntegerField(choices=MONTH_INCOME)              
    Diabetes_binary = models.IntegerField() 