from django.urls import path, include
from .views import (
    index,
    carForm,
    listingcar,
    submit_inquire,
    submit_buy,
    buyPolicy,
    thankyou,
    ComparePolicies,

    # travelForm
    travelForm,
    listingTravel,
    ComparePoliciesTravel,
    buyPolicyTravel,
    submit_buy_travel,
    companyProfile,
    thankyouTravel,

    # healthForm
    healthForm,
    healthlisting,
    get_labs_hotl_ata,
    ComparePoliciesHealth,
    buyPolicyHealth,
    submit_buy_health,
    thankyouHealth,
    findModel,
    nomberToWord
)

urlpatterns = [
    path('', index, name='index'),

    path('Company/<int:pk>/Profile', companyProfile, name='companyProfile'),
    path('car-search/', carForm, name='carForm'),
    path('listingcar/', listingcar, name='listingcar'),
    path('submit_inquire/', submit_inquire, name='submit_inquire'),
    path('submit_buy/', submit_buy, name='submit_buy'),
    path('Buy/<int:pk>/Policy/<str:quoteID>', buyPolicy, name='buyPolicy'),
    path('Thank/<int:pk>/You', thankyou, name='thankyou'),
    path('ComparePolicies/', ComparePolicies, name='ComparePolicies'),
    path('findModel/', findModel, name="findModel"),
    path('nomberToWord/', nomberToWord, name="nomberToWord"),

    # TRAVEL
    path('travel-search/', travelForm, name='travelForm'),
    path('TravelListing/', listingTravel, name='listingTravel'),
    path('ComparePoliciesTravel/', ComparePoliciesTravel, name='ComparePoliciesTravel'),
    path('Buy/PolicyTravel', buyPolicyTravel, name='buyPolicyTravel'),
    path('submit_buy_travel/', submit_buy_travel, name='submit_buy_travel'),
    path('thankyouTravel/<int:pk>/Travel', thankyouTravel, name='thankyouTravel'),

    # Health
    path('health-search/', healthForm, name='healthForm'),
    path('health-listing/', healthlisting, name='healthlisting'),
    path('get_labs_hotl_ata/', get_labs_hotl_ata, name='get_labs_hotl_ata'),
    path('ComparePoliciesHealth/', ComparePoliciesHealth, name='ComparePoliciesHealth'),
    path('buyPolicyHealthDetails/', buyPolicyHealth, name='buyPolicyHealthFront'),
    path('submit_buy_health/', submit_buy_health, name='submit_buy_health'),
    path('thanks/<int:pk>/Health', thankyouHealth, name='thankyouHealth')
]