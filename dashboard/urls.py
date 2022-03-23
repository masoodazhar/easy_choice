from django.urls import path, include
from .views import (
    CreateFeature,
    UpdateFeature,
    DeleteFeature,

    CreateFeatureTravel,
    UpdateFeatureTravel,
    DeleteFeatureTravel,

    CreateFeatureHealth,
    UpdateFeatureHealth,
    DeleteFeatureHealth,

    CreatePolicy,
    UpdatePolicy,
    DeletePolicy,

    CreatePolicyTravel,
    UpdatePolicyTravel,
    DeletePolicyTravel,

    CreatePolicyHealth,
    UpdatePolicyHealth,
    DeletePolicyHealth,

    index,
    CreateCompany,
    UpdateCompany,
    DeleteCompany,

    inquiries,
    buyPolicy,
    data_upload,

    CreateCars,
    UpdateCars,
    DeleteCars,


    CreateCarsModel,
    UpdateCarsModel,
    DeleteCarsModel,
    buyPolicyTravel,
    buyPolicyHealths
)


urlpatterns = [
    path('', index, name='dashboard'),
    path('CreateCompany/', CreateCompany.as_view(), name='CreateCompany'),
    path('UpdateCompany/<int:pk>/Update', UpdateCompany.as_view(), name='UpdateCompany'),
    path('DeleteCompany/<int:pk>/Delete', DeleteCompany, name='DeleteCompany'),

    path('CreatePolicy/', CreatePolicy.as_view(), name='CreatePolicy'),
    path('UpdatePolicy/<int:pk>/Update', UpdatePolicy.as_view(), name='UpdatePolicy'),
    path('DeletePolicy/<int:pk>/Delete', DeletePolicy, name='DeletePolicy'),

    path('CreateFeature/', CreateFeature.as_view(), name='CreateFeature'),
    path('UpdateFeature/<int:pk>/Update', UpdateFeature.as_view(), name='UpdateFeature'),
    path('DeleteFeature/<int:pk>/Delete', DeleteFeature, name='DeleteFeature'),

    path('CreateFeatureTravel/', CreateFeatureTravel.as_view(), name='CreateFeatureTravel'),
    path('UpdateFeatureTravel/<int:pk>/Update', UpdateFeatureTravel.as_view(), name='UpdateFeatureTravel'),
    path('DeleteFeatureTravel/<int:pk>/Delete', DeleteFeatureTravel, name='DeleteFeatureTravel'),

    path('CreatePolicyTravel/', CreatePolicyTravel.as_view(), name='CreatePolicyTravel'),
    path('UpdatePolicyTravel/<int:pk>/Update', UpdatePolicyTravel.as_view(), name='UpdatePolicyTravel'),
    path('DeletePolicyTravel/<int:pk>/Delete', DeletePolicyTravel, name='DeletePolicyTravel'),

    path('CreateFeatureHealth/', CreateFeatureHealth.as_view(), name='CreateFeatureHealth'),
    path('UpdateFeatureHealth/<int:pk>/Update', UpdateFeatureHealth.as_view(), name='UpdateFeatureHealth'),
    path('DeleteFeatureHealth/<int:pk>/Delete', DeleteFeatureHealth, name='DeleteFeatureHealth'),

    path('CreatePolicyHealth/', CreatePolicyHealth.as_view(), name='CreatePolicyHealth'),
    path('UpdatePolicyHealth/<int:pk>/Update', UpdatePolicyHealth.as_view(), name='UpdatePolicyHealth'),
    path('DeletePolicyHealth/<int:pk>/Delete', DeletePolicyHealth, name='DeletePolicyHealth'),

    path('Inquiries/', inquiries, name='inquiries'),
    path('BuyPolicy/', buyPolicy, name='buyPolicy'),
    path('buyPolicyTravel/', buyPolicyTravel, name='buyPolicyTravel'),
    path('buyPolicyHealth/', buyPolicyHealths, name='buyPolicyHealth'),
    path('data_upload', data_upload, name='data_upload'),

    path('CreateCars/', CreateCars.as_view(), name='CreateCars'),
    path('UpdateCars/<int:pk>/Update', UpdateCars.as_view(), name='UpdateCars'),
    path('DeleteCars/<int:pk>/Delete', DeleteCars, name='DeleteCars'),

    path('CreateCarsModel/', CreateCarsModel.as_view(), name='CreateCarsModel'),
    path('UpdateCarsModel/<int:pk>/Update', UpdateCarsModel.as_view(), name='UpdateCarsModel'),
    path('DeleteCarsModel/<int:pk>/Delete', DeleteCarsModel, name='DeleteCarsModel'),
]