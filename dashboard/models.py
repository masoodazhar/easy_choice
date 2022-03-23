from django.db import models
from django.urls import reverse

# Create your models here.


class Company(models.Model):
    comapny_name = models.CharField('Company Name',max_length=255)
    logo = models.ImageField(upload_to='companydata')
    redirect_link = models.CharField(default='', max_length=255, blank=True, null=True)
    class meta:
        db_table = 'company'

    def __str__(self):
        return self.comapny_name

    def get_absolute_url(self):
        return reverse('CreateCompany')
    

class FeatureTravel(models.Model):
    # policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=[('1', 'Medical Benefits'), ('2', 'Personal Accident Benefits'), ('3', 'Travel Inconvenience Benefits')])
    feature = models.CharField(max_length=100, unique=True)

    class meta:
        db_table = 'FeatureTravel'

    def __str__(self):
        return str(self.feature)

    def get_absolute_url(self):
        return reverse('CreateFeatureTravel')


class PolicyTravel(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    policy_name = models.CharField(max_length=255)
    instant = models.BooleanField(default=False, blank=True)
    coid19 = models.BooleanField(default=False, blank=True)
    medical_benefits = models.TextField()
    personal_accident_benefits = models.TextField()
    travel_inconvenience_benefits = models.TextField()
    recomended = models.BooleanField(default=False, blank=True)
    off = models.IntegerField('%, if not leave it as 0', default=0, blank=True)

    days_7 = models.IntegerField('',default=7)
    individual_amount_7  = models.FloatField('')
    family_amount_7  = models.FloatField('')

    days_10 = models.IntegerField('',default=10)
    individual_amount_10 = models.FloatField('')
    family_amount_10 = models.FloatField('')

    days_15 = models.IntegerField('',default=15)
    individual_amount_15 = models.FloatField('')
    family_amount_15 = models.FloatField('')

    days_21 = models.IntegerField('',default=21)
    individual_amount_21 = models.FloatField('')
    family_amount_21 = models.FloatField('')
    
    days_31 = models.IntegerField('',default=31)
    individual_amount_31 = models.FloatField('')
    family_amount_31 = models.FloatField('')
    
    days_62 = models.IntegerField('',default=62)
    individual_amount_62 = models.FloatField('')
    family_amount_62 = models.FloatField('')
    
    days_92 = models.IntegerField('',default=92)
    individual_amount_92 = models.FloatField('')
    family_amount_92 = models.FloatField('')
    
    days_122 = models.IntegerField('',default=122)
    individual_amount_122 = models.FloatField('')
    family_amount_122 = models.FloatField('')
    
    days_152 = models.IntegerField('',default=152)
    individual_amount_152 = models.FloatField('')
    family_amount_152 = models.FloatField('')
    
    days_180 = models.IntegerField('',default=180)
    individual_amount_180 = models.FloatField('')
    family_amount_180 = models.FloatField('')
    
    anual_multi_trip = models.CharField('',max_length=50, default='Annual Multi-Trip')
    individual_amount_amt = models.FloatField('')
    family_amount_amt = models.FloatField('')
    
    senior_ages = models.CharField('', max_length=100, default='Senior Age Extension for those aged 65-85')
    individual_amount_sa = models.CharField('', max_length=100)
    family_amount_sa = models.CharField('', max_length=100)

    policy_documents = models.FileField(upload_to='policy_document', default='nodoc.pdf', null=True, blank=True)
    claim_process = models.FileField(upload_to='policy_document', default='nodoc.pdf', null=True, blank=True)

    class meta:
        db_table = 'policytravel'
        
    def __str__(self):
        return self.policy_name

    def get_absolute_url(self):
        return reverse('CreatePolicyTravel')


# NOT IN USED
class PolicyDay(models.Model):
    policy = models.ForeignKey(PolicyTravel, on_delete=models.CASCADE)
    day = models.IntegerField()
    individual_amount = models.FloatField()
    family_amount = models.FloatField()

    class meta:
        db_table = 'policyday'


class Feature(models.Model):
    # policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=[('1', 'Main Coverage'), ('2', 'Third Party Coverage'), ('3', 'Value Added Features')])
    feature = models.CharField(max_length=100, unique=True)

    class meta:
        db_table = 'Feature'

    def __str__(self):
        return str(self.feature)

    def get_absolute_url(self):
        return reverse('CreateFeature')




class Policy(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    policy_name = models.CharField(max_length=255)
    rate = models.FloatField()
    installment_plane = models.IntegerField('Installment Plan (months)',default=0, blank=True)
    off = models.IntegerField('off in %, if not leave it as 0', default=0, blank=True)
    tracking_amount = models.IntegerField(default=0, blank=True)
    instant = models.BooleanField(default=False, blank=True)
    coid19 = models.BooleanField(default=False, blank=True)
    main_coverage = models.TextField()
    recomended = models.BooleanField(default=False, blank=True)
    third_party_coverage = models.TextField()
    value_added_features = models.TextField()
    policy_documents = models.FileField(upload_to='policy_document', default='nodoc.pdf', null=True, blank=True)
    claim_process = models.FileField(upload_to='policy_document', default='nodoc.pdf', null=True, blank=True)
    class meta:
        db_table = 'policy'
        
    def __str__(self):
        return self.policy_name

    def get_absolute_url(self):
        return reverse('CreatePolicy')


# HEALTH
class FeatureHealth(models.Model):
    # policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    # category = models.CharField(max_length=100, choices=[('1', 'Main Coverage'), ('2', 'Third Party Coverage'), ('3', 'Value Added Features')])
    feature = models.CharField(max_length=100, unique=True)
    

    class meta:
        db_table = 'FeatureHealth'

    def __str__(self):
        return str(self.feature)

    def get_absolute_url(self):
        return reverse('CreateFeatureHealth')


class PolicyHealth(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    policy_name = models.CharField(max_length=255)
    self_price = models.FloatField()
    family_price = models.FloatField(default=0, null=True, blank=True)
    family_parent_amount = models.FloatField(default=0, null=True, blank=True)
    family_kids_amount = models.FloatField(default=0, null=True, blank=True)
    parents_price = models.FloatField()
    maternity_cover_price = models.FloatField(default=0)
    off = models.FloatField(default=0)
    instant = models.BooleanField(default=False, blank=True)
    coid19 = models.BooleanField(default=False, blank=True)
    recomended = models.BooleanField(default=False, blank=True)

    hospitalization = models.CharField(max_length=50, choices=(
        ('60k - 2 Lac', '60k - 2 Lac'),
        ('2 Lac - 5 Lac', '2 Lac - 5 Lac'),
        ('5 Lac - 10 Lac', '5 Lac - 10 Lac')
    ))
    
    policy_documents = models.FileField(upload_to='policy_document')
    claim_process = models.FileField(upload_to='policy_document')
    more_features = models.TextField()
    features = models.TextField()

    def get_self(self):
        return self.self_price

    def get_parent(self):
        return self.parents_price

    def get_family_parent(self):
        return self.family_parent_amount*2

    def get_family_kids(self, qty):
        return self.family_kids_amount*qty

    def get_family(self):
        return self.family_price

    class meta:
        db_table = 'policy'
        
    def __str__(self):
        return self.policy_name

    def get_absolute_url(self):
        return reverse('CreatePolicy')



class LabDiscount(models.Model):
    policy = models.ForeignKey(PolicyHealth, on_delete=models.CASCADE)
    hospital_name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    discount = models.CharField(max_length=100)
    address = models.TextField()

    class meta:
        db_table = 'labdiscount'

    def __str__(self):
        return str(self.hospital_name)

class HospitalInfo(models.Model):
    policy = models.ForeignKey(PolicyHealth, on_delete=models.CASCADE)
    hospital_name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    address = models.TextField()

    class meta:
        db_table = 'Hospitalinfo'

    def __str__(self):
        return str(self.hospital_name)


class Cars(models.Model):
    name = models.CharField(max_length=150, unique=True)

    class meta:
        db_table = 'Cars'

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('CreateCars')

class CarsModel(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    model = models.CharField(max_length=255, unique=True)

    class meta:
        db_table = 'Cars'

    def __str__(self):
        return str(self.model)

    def get_absolute_url(self):
        return reverse('CreateCarsModel')