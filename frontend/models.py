from django.db import models
from dashboard.models import Policy, PolicyHealth, PolicyTravel
# Create your models here.


class Inquirer(models.Model):
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    form_data = models.TextField()
    policy = models.CharField(max_length=255)
    policy_type = models.CharField(max_length=60)
    qoutId = models.CharField(max_length=100, default='BS000252')

    class meta:
        db_table = 'inquirer'
        
    def __str__(self):
        return self.full_name


class BuyPolicy(models.Model):
    car_owner_name = models.CharField(max_length=150)
    cnic = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    servey_location_address = models.CharField(max_length=25)
    car_registeration_number = models.CharField(max_length=25)
    date = models.CharField(max_length=25)
    time = models.CharField(max_length=25)
    form_data = models.TextField()
    quoteID = models.CharField(max_length=100, default='VF25001441')
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)

    class meta:
        db_table = 'buypolicy'
        
    def __str__(self):
        return self.car_owner_name

class BuyPolicyTravel(models.Model):
    policy = models.ForeignKey(PolicyTravel, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cnic = models.CharField(max_length=100)
    date_of_issue = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    passport = models.CharField(max_length=100)
    residance_address = models.CharField(max_length=100)
    city_residance = models.CharField(max_length=100)
    travel_from = models.CharField(max_length=100)
    travel_to = models.CharField(max_length=100)
    other_family_members = models.TextField()
    quoteID = models.CharField(max_length=100, default='RD25001441')
    form_data = models.TextField()

    class meta:
        db_table = 'buypolicytravel'
        
    def __str__(self):
        return self.first_name

class BuyPolicyHealth(models.Model):
    policy = models.ForeignKey(PolicyHealth, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cnic = models.CharField(max_length=100)
    date_of_issue = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    residance_address = models.CharField(max_length=100)
    city_residance = models.CharField(max_length=100)
    other_family_members = models.TextField()
    form_data = models.TextField()
    quoteID = models.CharField(max_length=100, default='HQ25001441')
    maternity_cover_price = models.BooleanField(default=False)

    class meta:
        db_table = 'buypolicyhealth'
        
    def __str__(self):
        return self.first_name