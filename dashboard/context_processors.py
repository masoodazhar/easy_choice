from dashboard.models import Company, Policy, PolicyHealth, PolicyTravel
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User

from frontend.models import BuyPolicy, BuyPolicyHealth, BuyPolicyTravel, Inquirer


def add_variable_to_context(request):
    PolicyCarCount = Policy.objects.all().count()
    PolicyTravelCount = PolicyTravel.objects.all().count()
    PolicyHealthCount = PolicyHealth.objects.all().count()
    totalPackages = PolicyCarCount+PolicyTravelCount+PolicyHealthCount


    BuyPolicyCount = BuyPolicy.objects.all().count()
    BuyPolicyHealthCount = BuyPolicyHealth.objects.all().count()
    BuyPolicyTravelCount = BuyPolicyTravel.objects.all().count()
    totalClients = BuyPolicyCount+BuyPolicyHealthCount+BuyPolicyTravelCount

    InquirerCount = Inquirer.objects.all().count()

    CompanyCount = Company.objects.all().count()

    context = {
        'packages': totalPackages,
        'totalClients': totalClients,
        'Inquirer': InquirerCount,
        'CompanyCount': CompanyCount

    }
    return context

