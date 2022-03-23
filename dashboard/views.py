from django.db.models import Q
from django.db import models
from django.forms import widgets
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.forms import PolicyForm, PolicyHealthForm, PolicyTravelForm
from dashboard.models import Cars, CarsModel, Company, Feature, FeatureHealth, FeatureTravel, HospitalInfo, LabDiscount, Policy, PolicyHealth, PolicyTravel
from frontend.models import BuyPolicy, BuyPolicyTravel, Inquirer, BuyPolicyHealth
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django import forms
import pdb
import json
import csv, io
from django.contrib import messages


# Create your views here.

@login_required
def index(request):
    return render(request, 'backend/index.html')


class CreateCompany(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'dashboard.add_company'
    model = Company
    fields = '__all__'
    template_name = 'backend/Company.html'

    def get_context_data(self, **kwargs):
        context = super(CreateCompany, self).get_context_data(**kwargs)
        context['CompanyList'] = Company.objects.all() 
        return context

class UpdateCompany(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'dashboard.change_company'
    model = Company
    fields = '__all__'
    login_url = 'login'
    template_name = 'backend/Company.html'   

    def get_context_data(self, **kwargs):
        context = super(UpdateCompany, self).get_context_data(**kwargs)
        context['CompanyList'] = Company.objects.all() 
        return context

@login_required
@permission_required('dashboard.delete_company', raise_exception=True)
def DeleteCompany(request, pk):
    model = Company.objects.get(pk=pk)
    model.delete()
    return redirect('CreateCompany')


# POLICY
coverages = {
    1: 'Main Coverage',
    2: 'Third Party Coverage',
    3: 'Value Added Features'
}
class CreatePolicy(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'dashboard.add_policy'
    model = Policy
    fields = '__all__'
    template_name = 'backend/Policy.html'

    def get_form(self, **kwargs):            
        form = super(CreatePolicy, self).get_form(**kwargs)
        # form.fields['main_coverage'] = forms.ModelChoiceField(queryset=Feature.objects.filter(category='1'))
        # form.fields['third_party_coverage'] = forms.ModelChoiceField(queryset=Feature.objects.filter(category='2'))
        # form.fields['value_added_features'] = forms.ModelChoiceField(queryset=Feature.objects.filter(category='3'))
        # form.fields['date'].widget = forms.TextInput(attrs={'type': 'date'})
        return form

    def post(self, *args, **kwargs):
        form = self.request.POST

        policyForm = PolicyForm(form, self.request.FILES)
        all_features_with_status_1 = []
        all_features_with_status_2 = []
        all_features_with_status_3 = []
        for i,values in enumerate(form.getlist('feature')):
            if form.getlist('category')[i] == '1':
                all_features_with_status_1.append({
                    'feature': values, 
                    'status': form.getlist('status')[i]
                })

            if form.getlist('category')[i] == '2':
                all_features_with_status_2.append({
                    'feature': values, 
                    'status': form.getlist('status')[i]
                })
            if form.getlist('category')[i] == '3':
                all_features_with_status_3.append({
                    'feature': values, 
                    'status': form.getlist('status')[i]
                })
        
        print('==================================TEST')
        print(all_features_with_status_3)
        print('==================================TEST')
        # if policyForm.is_valid():
        saveObj = policyForm.save(commit=False)
        saveObj.main_coverage = json.dumps(all_features_with_status_1)
        saveObj.third_party_coverage = json.dumps(all_features_with_status_2)
        saveObj.value_added_features = json.dumps(all_features_with_status_3)
        saveObj.save()
        messages.success(self.request, 'Successfully saved')
        return redirect('CreatePolicy')


    def get_context_data(self, **kwargs):
        context = super(CreatePolicy, self).get_context_data(**kwargs)
        context['PolicyList'] = Policy.objects.all() 
        
        featureBoxes = []
        for key, value in coverages.items():
            featureBoxes.append({
                'category': key,
                'name': value.replace(' ','_').lower(),
                'feature_name': value,
                'boxes': Feature.objects.filter(category=key)
            })

        context['featureBoxes'] = featureBoxes
        return context

class UpdatePolicy(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    permission_required = 'dashboard.change_policy'
    model = Policy
    fields = '__all__'
    login_url = 'login'
    template_name = 'backend/Policy.html'   

    def post(self, *args, **kwargs):
        obj = Policy.objects.get(pk=self.kwargs.get('pk', None))
        form = self.request.POST

        policyForm = PolicyForm(form, self.request.FILES, instance=obj)
        all_features_with_status_1 = []
        all_features_with_status_2 = []
        all_features_with_status_3 = []
        for i,values in enumerate(form.getlist('feature')):
            if form.getlist('category')[i] == '1':
                all_features_with_status_1.append({
                    'feature': values, 
                    'status': form.getlist('status')[i]
                })

            if form.getlist('category')[i] == '2':
                all_features_with_status_2.append({
                    'feature': values, 
                    'status': form.getlist('status')[i]
                })
            if form.getlist('category')[i] == '3':
                all_features_with_status_3.append({
                    'feature': values, 
                    'status': form.getlist('status')[i]
                })
        
        print('==================================TEST')
        print(all_features_with_status_3)
        print('==================================TEST')
        # if policyForm.is_valid():
        saveObj = policyForm.save(commit=False)
        saveObj.main_coverage = json.dumps(all_features_with_status_1)
        saveObj.third_party_coverage = json.dumps(all_features_with_status_2)
        saveObj.value_added_features = json.dumps(all_features_with_status_3)
        saveObj.save()
        messages.success(self.request, 'Successfully saved')
        return redirect('CreatePolicy')


    def get_context_data(self, **kwargs):
        obj = Policy.objects.get(pk=self.kwargs.get('pk', None))
        context = super(UpdatePolicy, self).get_context_data(**kwargs)
        context['PolicyList'] = Policy.objects.all() 
        context['main_coverage'] = json.loads(Policy.objects.get(pk=obj.pk).main_coverage)
        context['third_party_coverage'] = json.loads(Policy.objects.get(pk=obj.pk).third_party_coverage)
        context['value_added_features'] = json.loads(Policy.objects.get(pk=obj.pk).value_added_features)
        context['is_update'] = True
        return context

@login_required
@permission_required('dashboard.delete_policy', raise_exception=True)
def DeletePolicy(request, pk):
    model = Policy.objects.get(pk=pk)
    model.delete()
    return redirect('CreatePolicy')



# Feature
class CreateFeature(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'dashboard.add_feature'
    model = Feature
    fields = '__all__'
    template_name = 'backend/Feature.html'

    def get_context_data(self, **kwargs):
        context = super(CreateFeature, self).get_context_data(**kwargs)
        context['FeatureList'] = Feature.objects.all() 
        return context

class UpdateFeature(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    permission_required = 'dashboard.change_feature'
    model = Feature
    fields = '__all__'
    login_url = 'login'
    template_name = 'backend/Feature.html'   

    def get_context_data(self, **kwargs):
        context = super(UpdateFeature, self).get_context_data(**kwargs)
        context['FeatureList'] = Feature.objects.all() 
        return context


@login_required
@permission_required('dashboard.delete_feature', raise_exception=True)
def DeleteFeature(request, pk):
    model = Feature.objects.get(pk=pk)
    model.delete()
    return redirect('CreateFeature')


@login_required
@permission_required('dashboard.view_inquirer', raise_exception=True)
def inquiries(request):
    inq = Inquirer.objects.all()
    
    data = []

    for i in inq:
        data.append({
            'full_name': i.full_name,
            'phone': i.phone,
            'email': i.email,
            'city': i.city,
            'form_data': json.loads(i.form_data),
            'policy': i.policy,
            'quoteid': i.qoutId,
            'policy_type': i.policy_type
        })
    context = {
        'inq': data
    }
    return render(request, 'backend/inquiries.html', context)

@login_required
@permission_required('dashboard.view_buypolicy', raise_exception=True)
def buyPolicy(request):
    inq = BuyPolicy.objects.all()

    data = []

    for i in inq:
        data.append({
            'car_owner_name': i.car_owner_name,
            'cnic': i.cnic,
            'phone': i.phone,
            'email': i.email,
            'form_data': json.loads(i.form_data),
            'servey_location_address': i.servey_location_address,
            'car_registeration_number': i.car_registeration_number,
            'date': i.date,
            'time': i.time,
            'quoteID': i.quoteID,
            'policy': i.policy,
            'date': i.date,
            'date': i.date,
        })

    context = {
        'inq': data
    }
    return render(request, 'backend/buy.html', context)


@login_required
@permission_required('dashboard.view_buypolicy', raise_exception=True)
def buyPolicyTravel(request):
    inq = BuyPolicyTravel.objects.all()
    data = []
    for i in inq:
        data.append({
            'policy': i.policy,
            'first_name': i.first_name,
            'last_name': i.last_name,
            'cnic': i.cnic,
            'date_of_issue': i.date_of_issue,
            'date_of_birth': i.date_of_birth,
            'phone': i.phone,
            'purpose': i.purpose,
            'email': i.email,
            'passport': i.passport,
            'residance_address': i.residance_address,
            'city_residance': i.city_residance,
            'travel_from': i.travel_from,
            'travel_to': i.travel_to,
            'quoteID': i.quoteID,
            'other_family_members': json.loads(i.other_family_members),
            'form_data': json.loads(i.form_data)            
        })

    context = {
        'inq': data
    }
    return render(request, 'backend/buytravel.html', context)



@login_required
@permission_required('dashboard.view_buypolicy', raise_exception=True)
def buyPolicyHealths(request):
    inq = BuyPolicyHealth.objects.all()
    data = []
    for i in inq:
        data.append({
            'policy': i.policy,
            'first_name': i.first_name,
            'last_name': i.last_name,
            'cnic': i.cnic,
            'date_of_issue': i.date_of_issue,
            'date_of_birth': i.date_of_birth,
            'phone': i.phone,
            'email': i.email,
            'residance_address': i.residance_address,
            'city_residance': i.city_residance,
            'quoteID': i.quoteID,
            'other_family_members': json.loads(i.other_family_members)[0],
            'form_data': json.loads(i.form_data)            
        })

    print('============================')
    print(data)

    context = {
        'inq': data
    }
    return render(request, 'backend/buyhealth.html', context)



# FeatureTravel
class CreateFeatureTravel(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'dashboard.add_feature_travel'
    model = FeatureTravel
    fields = '__all__'
    template_name = 'backend/FeatureTravel.html'

    def get_context_data(self, **kwargs):
        context = super(CreateFeatureTravel, self).get_context_data(**kwargs)
        context['FeatureTravelList'] = FeatureTravel.objects.all() 
        return context

class UpdateFeatureTravel(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    permission_required = 'dashboard.change_feature_travel'
    model = FeatureTravel
    fields = '__all__'
    login_url = 'login'
    template_name = 'backend/FeatureTravel.html'   

    def get_context_data(self, **kwargs):
        context = super(UpdateFeatureTravel, self).get_context_data(**kwargs)
        context['FeatureTravelList'] = FeatureTravel.objects.all() 
        return context

@login_required
@permission_required('dashboard.delete_feature_travel', raise_exception=True)
def DeleteFeatureTravel(request, pk):
    model = FeatureTravel.objects.get(pk=pk)
    model.delete()
    return redirect('CreateFeatureTravel')


# POLICY
coverages_travel = {
    1: 'Medical Benefits',
    2: 'Personal Accident Benefits',
    3: 'Travel Inconvenience Benefits'
}

class CreatePolicyTravel(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'dashboard.add_policy_travel'
    model = PolicyTravel
    fields = '__all__'
    template_name = 'backend/PolicyTravel.html'

    def get_form(self, **kwargs):            
        form = super(CreatePolicyTravel, self).get_form(**kwargs)
        form.fields['days_7'].widget = forms.TextInput(attrs={'readonly':'readonly'})
        form.fields['days_10'].widget = forms.TextInput(attrs={'readonly':'readonly'})
        form.fields['days_15'].widget = forms.TextInput(attrs={'readonly':'readonly'})
        form.fields['days_21'].widget = forms.TextInput(attrs={'readonly':'readonly'})
        form.fields['days_31'].widget = forms.TextInput(attrs={'readonly':'readonly'})
        form.fields['days_62'].widget = forms.TextInput(attrs={'readonly':'readonly'})
        form.fields['days_92'].widget = forms.TextInput(attrs={'readonly':'readonly'})
        form.fields['days_122'].widget = forms.TextInput(attrs={'readonly':'readonly'})
        form.fields['days_152'].widget = forms.TextInput(attrs={'readonly':'readonly'})
        form.fields['days_180'].widget = forms.TextInput(attrs={'readonly':'readonly'})
        form.fields['anual_multi_trip'].widget = forms.TextInput(attrs={'readonly':'readonly'})
        form.fields['senior_ages'].widget = forms.TextInput(attrs={'readonly':'readonly'})
        
        return form

    def post(self, *args, **kwargs):
        form = self.request.POST
        
        policyTravelForm = PolicyTravelForm(form, self.request.FILES)
        all_features_with_status_1 = []
        all_features_with_status_2 = []
        all_features_with_status_3 = []
        for i,values in enumerate(form.getlist('feature')):
            if form.getlist('category')[i] == '1':
                all_features_with_status_1.append({
                    'feature': values, 
                    'status': form.getlist('status')[i],
                    'is_active': form.getlist('is_active')[i]
                })

            if form.getlist('category')[i] == '2':
                all_features_with_status_2.append({
                    'feature': values, 
                    'status': form.getlist('status')[i],
                    # 'is_active': form.getlist('is_active')[i]
                })
            if form.getlist('category')[i] == '3':
                all_features_with_status_3.append({
                    'feature': values, 
                    'status': form.getlist('status')[i],
                    # 'is_active': form.getlist('is_active')[i]
                })
        
        print('==================================TEST')
        print(all_features_with_status_3)
        print('==================================TEST')
        # pdb.set_trace()
        # if PolicyTravelForm.is_valid():
        saveObj = policyTravelForm.save(commit=False)
        saveObj.medical_benefits = json.dumps(all_features_with_status_1)
        saveObj.personal_accident_benefits = json.dumps(all_features_with_status_2)
        saveObj.travel_inconvenience_benefits = json.dumps(all_features_with_status_3)
        saveObj.save()
        messages.success(self.request, 'Successfully saved')
        return redirect('CreatePolicyTravel')


    def get_context_data(self, **kwargs):
        context = super(CreatePolicyTravel, self).get_context_data(**kwargs)
        context['PolicyTravelList'] = PolicyTravel.objects.all() 
        
        featureBoxes = []
        for key, value in coverages_travel.items():
            featureBoxes.append({
                'category': key,
                'name': value.replace(' ','_').lower(),
                'feature_name': value,
                'boxes': FeatureTravel.objects.filter(category=key)
            })

        context['featureBoxes'] = featureBoxes
        return context

class UpdatePolicyTravel(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    permission_required = 'dashboard.change_policy_travel'
    model = PolicyTravel
    fields = '__all__'
    login_url = 'login'
    template_name = 'backend/PolicyTravel.html'   
    
    def post(self, *args, **kwargs):

        obj = PolicyTravel.objects.get(pk=self.kwargs.get('pk'))
        form = self.request.POST
        
        policyTravelForm = PolicyTravelForm(form, self.request.FILES, instance=obj)
        all_features_with_status_1 = []
        all_features_with_status_2 = []
        all_features_with_status_3 = []
        for i,values in enumerate(form.getlist('feature')):
            if form.getlist('category')[i] == '1':
                all_features_with_status_1.append({
                    'feature': values, 
                    'status': form.getlist('status')[i],
                    'is_active': form.getlist('is_active')[i]
                })

            if form.getlist('category')[i] == '2':
                all_features_with_status_2.append({
                    'feature': values, 
                    'status': form.getlist('status')[i],
                    # 'is_active': form.getlist('is_active')[i]
                })
            if form.getlist('category')[i] == '3':
                all_features_with_status_3.append({
                    'feature': values, 
                    'status': form.getlist('status')[i],
                    # 'is_active': form.getlist('is_active')[i]
                })
        
        print('==================================TEST')
        print(all_features_with_status_3)
        print('==================================TEST')
        # pdb.set_trace()
        # if PolicyTravelForm.is_valid():
        saveObj = policyTravelForm.save(commit=False)
        saveObj.medical_benefits = json.dumps(all_features_with_status_1)
        saveObj.personal_accident_benefits = json.dumps(all_features_with_status_2)
        saveObj.travel_inconvenience_benefits = json.dumps(all_features_with_status_3)
        saveObj.save()
        messages.success(self.request, 'Successfully saved')
        return redirect('CreatePolicyTravel')


    def get_context_data(self, **kwargs):
        obj = PolicyTravel.objects.get(pk=self.kwargs.get('pk'))
        context = super(UpdatePolicyTravel, self).get_context_data(**kwargs)
        context['PolicyTravelList'] = PolicyTravel.objects.all() 
   
        context['medical'] = json.loads(PolicyTravel.objects.get(pk=obj.pk).medical_benefits)
        context['personal'] = json.loads(PolicyTravel.objects.get(pk=obj.pk).personal_accident_benefits)
        context['travel'] = json.loads(PolicyTravel.objects.get(pk=obj.pk).travel_inconvenience_benefits)
      

        context['is_update'] = True
        return context

@login_required
@permission_required('dashboard.delete_policy_travel', raise_exception=True)
def DeletePolicyTravel(request, pk):
    model = PolicyTravel.objects.get(pk=pk)
    model.delete()
    return redirect('CreatePolicyTravel')


# HEALTH
# FeatureTravel
class CreateFeatureHealth(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'dashboard.add_feature_health'
    model = FeatureHealth
    fields = '__all__'
    template_name = 'backend/FeatureHealth.html'

    def get_context_data(self, **kwargs):
        context = super(CreateFeatureHealth, self).get_context_data(**kwargs)
        context['FeatureHealthList'] = FeatureHealth.objects.all() 
        return context

class UpdateFeatureHealth(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    permission_required = 'dashboard.change_feature_health'
    model = FeatureHealth
    fields = '__all__'
    login_url = 'login'
    template_name = 'backend/FeatureHealth.html'   

    def get_context_data(self, **kwargs):
        context = super(UpdateFeatureHealth, self).get_context_data(**kwargs)
        context['FeatureHealthList'] = FeatureHealth.objects.all() 
        return context

@login_required
@permission_required('dashboard.delete_feature_health', raise_exception=True)
def DeleteFeatureHealth(request, pk):
    model = FeatureHealth.objects.get(pk=pk)
    model.delete()
    return redirect('CreateFeatureHealth')



class CreatePolicyHealth(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'dashboard.add_policy_health'
    model = PolicyHealth
    fields = '__all__'
    template_name = 'backend/PolicyHealth.html'

    def post(self, *args, **kwargs):
        obj = super(CreatePolicyHealth, self).post(*args, **kwargs)

        form = self.request.POST
        
        self.form = PolicyHealthForm(form, self.request.FILES)
        all_features_with_status_1 = []
        for i,values in enumerate(form.getlist('feature')):
            all_features_with_status_1.append({
                'feature': values, 
                'status': form.getlist('status')[i],
                'is_active': form.getlist('is_active')[i]
            })

        
        print('==================================TEST')
        print(all_features_with_status_1)
        print('==================================TEST')
        # pdb.set_trace()
        if self.form.is_valid():
            saveObj = self.form.save(commit=False)
            saveObj.features = json.dumps(all_features_with_status_1)
            saveObj.save()
            return redirect('CreatePolicyHealth')
        else:
            print("====ERROR =====")
            print(self.form.errors)
        messages.success(self.request, 'Successfully saved')
        return obj

    def get_context_data(self, **kwargs):
        context = super(CreatePolicyHealth, self).get_context_data(**kwargs)
        context['PolicyHealthList'] = PolicyHealth.objects.all() 
        context['featureBoxes'] = FeatureHealth.objects.all()
        return context

class UpdatePolicyHealth(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    permission_required = 'dashboard.change_policy_health'
    model = PolicyHealth
    fields = '__all__'
    login_url = 'login'
    template_name = 'backend/PolicyHealth.html'   
    
    def post(self, *args, **kwargs):

        obj = PolicyHealth.objects.get(pk=self.kwargs.get('pk'))
        form = self.request.POST
        
        policyHealthForm = PolicyHealthForm(form, self.request.FILES, instance=obj)
        all_features_with_status_1 = []
        for i,values in enumerate(form.getlist('feature')):
            all_features_with_status_1.append({
                'feature': values, 
                'status': form.getlist('status')[i],
                'is_active': form.getlist('is_active')[i]
            })

        print('==================================TEST')
        print(all_features_with_status_1)
        print('==================================TEST')
        # pdb.set_trace()
        # if PolicyHealthForm.is_valid():
        saveObj = policyHealthForm.save(commit=False)
        saveObj.features = json.dumps(all_features_with_status_1)
        saveObj.save()
        messages.success(self.request, 'Successfully saved')
        return redirect('CreatePolicyHealth')


    def get_context_data(self, **kwargs):
        obj = PolicyHealth.objects.get(pk=self.kwargs.get('pk'))
        context = super(UpdatePolicyHealth, self).get_context_data(**kwargs)
        context['PolicyHealthList'] = PolicyHealth.objects.all() 
        context['featureBoxes'] = json.loads(PolicyHealth.objects.get(pk=obj.pk).features)      
        context['is_update'] = True
        return context

@login_required
@permission_required('dashboard.delete_policy_health', raise_exception=True)
def DeletePolicyHealth(request, pk):
    model = PolicyHealth.objects.get(pk=pk)
    model.delete()
    return redirect('CreatePolicyHealth')


def data_upload(request):
    # declaring template
    # template = "profile_upload.html"
    # data = LabDiscount.objects.all()

    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    policy = PolicyHealth.objects.get(pk=request.POST.get('policy'))
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        if request.POST.get('type') == 'lab':
            _, created = LabDiscount.objects.update_or_create(
                policy=policy,
                hospital_name=column[0],
                city=column[1],
                discount=column[2],
                address=column[3]
            )
        else:
            _, created = HospitalInfo.objects.update_or_create(
                policy=policy,
                hospital_name=column[0],
                city=column[1],
                address=column[2]
            )
        if created:
            messages.success(request,'Data has beed uploaded successfully')
        else:
            messages.warning(request,'Somehing went wrong. please try again!')
    return redirect('CreatePolicyHealth')


# Cars
class CreateCars(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'dashboard.add_cars'
    model = Cars
    fields = '__all__'
    template_name = 'backend/Cars.html'

    def get_context_data(self, **kwargs):
        context = super(CreateCars, self).get_context_data(**kwargs)
        context['CarsList'] = Cars.objects.all() 
        return context

class UpdateCars(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'dashboard.change_cars'
    model = Cars
    fields = '__all__'
    login_url = 'login'
    template_name = 'backend/Cars.html'   

    def get_context_data(self, **kwargs):
        context = super(UpdateCars, self).get_context_data(**kwargs)
        context['CarsList'] = Cars.objects.all() 
        return context

@login_required
@permission_required('dashboard.delete_cars', raise_exception=True)
def DeleteCars(request, pk):
    model = Cars.objects.get(pk=pk)
    model.delete()
    return redirect('CreateCars')


# CarsModel
class CreateCarsModel(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'dashboard.add_cars_model'
    model = CarsModel
    fields = '__all__'
    template_name = 'backend/CarsModel.html'

    def get_context_data(self, **kwargs):
        context = super(CreateCarsModel, self).get_context_data(**kwargs)
        context['CarsModelList'] = CarsModel.objects.all() 
        return context

class UpdateCarsModel(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    permission_required = 'dashboard.change_cars_model'
    model = CarsModel
    fields = '__all__'
    login_url = 'login'
    template_name = 'backend/CarsModel.html'   

    def get_context_data(self, **kwargs):
        context = super(UpdateCarsModel, self).get_context_data(**kwargs)
        context['CarsModelList'] = CarsModel.objects.all() 
        return context

@login_required
@permission_required('dashboard.delete_cars_model', raise_exception=True)
def DeleteCarsModel(request, pk):
    model = CarsModel.objects.get(pk=pk)
    model.delete()
    return redirect('CreateCarsModel')