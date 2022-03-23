from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from dashboard.models import Cars, CarsModel, Company, Feature, FeatureHealth, FeatureTravel, HospitalInfo, LabDiscount, Policy, PolicyHealth, PolicyTravel
from frontend.models import BuyPolicy, BuyPolicyHealth, BuyPolicyTravel, Inquirer
from django.contrib import messages
import json
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.core.paginator import Paginator
from num2words import num2words
# Create your views here.
import pdb;
import json
import random

numGen = ['BS','QV','TF','WA','HX','JZ','SW','QA','RT','OK','OP','ED','GF','LK','PE']

def generateQuotaId(model=BuyPolicyTravel):
    counts = Inquirer.objects.all().count()
    try:     
        ints = random.randint(0,14)   
        obj = model.objects.latest('id')
        id = numGen[ints]
        for i in range(0,5-len(str(obj.pk))):
            id +='0'+str(counts)
        return id+str(obj.pk)+str(counts)
    except:
        return 'bQ00b001'


def index(request):
    
    return render(request, 'frontend/index.html')

def companyProfile(request, pk):
    company = Company.objects.get(pk=pk)
    return render(request, 'frontend/company-profile.html', {'company': company})



def findModel(request):
    brand = request.GET.get('brand')

    # data = {
    #     "Honda"  :["CITY","CIVIC","HONDA ACCORD 1.5L TURBO","BRC I-VTEC MT 1497CC","Accord","Airwave","BR - V","CR-V","CR-Z Hydrid","Cross Road","Fit","Fit Aria","Freed","HR-V","VEZEl"],
    #     "Toyota" :["Allion Toyota","Aqua Toyota","Avanza Toyota","Aygo Toyota","Belta Toyota","C-HR Toyota","Camry Toyota","Celica Toyota","Corolla","Corolla Fielder Toyota","Crown Toyota","Estima Toyota","Fj Cruiser Toyota","Fortuner Toyota","Hiace Toyota","Hilux","IQ Toyota","ISIS Toyota","IST Toyota","Land Crusier Toyota","Mark II Toyota","Mark X Toyota","Passo Toyota","Pixix Epoch Toyota","Pixis Space Toyota","Platz Toyota","Porte Toyota","Prado Toyota","Premio Toyota","Prius Toyota","Prius Alpha Toyota","Probox Toyota","Ractis Toyota","Rav4 Toyota","Roomy Toyota","Rush Toyota","Succeed Toyota","Surf Toyota","Tundra Toyota","Vtiz Toyota","Voxy Toyota","Waish Toyota","Yaris","Hilus","Fortuner"],
    #     "Suzuki" :["Alto","APV","Baleno","Bolan","Carry","Celerio","Cervo","Ciaz","Cultus","Hustler","Jimmy","Kizashi","Liana","Mega Carry Extra","Mehran","MR Wagon","Ravi","Swift","Sx4","Vitara","Wagon","Xbee"],
    #     "Daihatsu" :["Boon","Copen","Cuore","Hijet","Mira","Move","Tanto","Terios"],
    #     "Nissan" :["Clipper","Days","GT-R","Juke","moco","Navara","wingroad"],
    #     "Adam" :["Revo"],
    #     "Audi" :["A3","A4","A5","A6","A7","A8","Q2","Q3","Q5","Q7","R8"],
    #     "BMW" :["2 Series","3 Series","5 Series","7 Series","X1","X2","X4","X5 Series","Z4"],
    #     "Changan" :["2 Series","3 Series","5 Series","7 Series","X1","X2","X4","X5 Series","Z4","Gilgit","Kaghan Xl","Kalam","Kalash","Karvaan","Shahanshah","AlSawin"],
    #     "FAW" :["Carrier","Sirius","V2","X-PV"],
    #     "Hino":["500 Series"],
    #     "Hyundai":["Mighty","Santro","Shehzore","Tucson"],
    #     "Jac":["X200"],
    #     "Jaguar":["XF"],
    #     "Jeep":["Wrangler"],
    #     "JMC":["Vigus"],
    #     "JW Forland":["Bravo"],
    #     "Kia":["Frotier K2700","Grand Carnival","Picanto","Sportage"],
    #     "Land Rover":["Defnder","Discovery 4"],
    #     "Mercedes":["Brabus","C Class","CLA Class","E Class","S Class","SLK Class"],
    #     "Lexus":["CT 200h","LX Series","RX Series"],
    #     "Mazda":["Carol","Rx8"],
    #     "Mitsubishi":["EK Custom","EK Wagon","Fuso","L300","Lancer","Mirage","Outlander","Pajero"],
    #     "Porsche":["911","Boxster","Cayenne","Cayman","Macan","Panamera"],
    #     "Range Rover":["Evoque","Sport","Velar","Vogue"],
    #     "Tesla":["Model 3"],
    #     "United":["Bravo"],
    #     "Prince":["Glory","Pearl"],
    #     "Isuzu":["DMAX"],
    #     "MG":["HS"],
    #     "Proton":["X70"]
    # }
    data = CarsModel.objects.filter(car=brand)
    myData = []
    for model in data:
        myData.append(model.model)
    # data = json.dumps(data)
    return JsonResponse(myData, safe=False)
    
def nomberToWord(request):
    data = request.GET.get('price')
    data = num2words(data)
    return JsonResponse({"data":data })



def carForm(request):   
    cars = Cars.objects.all().order_by('-id')
    return render(request, 'frontend/form-car.html', {'cars': cars})

coverages = {
    1: 'Main Coverage',
    2: 'Third Party Coverage',
    3: 'Value Added Features'
}


def get_features(policy):
    # features = Feature.objects.filter(policy=policy).order_by('category')
    data = []
    for key, value in coverages.items():
        data.append({
            'category': value,
            'featues': list(map(lambda x: {'feature': x.feature, 'status': x.status}, Feature.objects.filter(feature__category=key) ))
        })
    return data

def listingcar(request):    

    allData = []    
    if request.method == 'GET':
        if not request.session['form_data_car']:
            return redirect('travelForm')
        else:
            form = request.session['form_data_car']

    if request.method == 'POST':
        form = request.POST
        
    
    formData = {}
    for k, v in form.items():
        if k == 'company':
            formData[k] = form.getlist(k) if request.method == 'POST' else v
        else:
            formData[k] = v

    if request.method == 'POST':
        del formData['csrfmiddlewaretoken'] 

    request.session['form_data_car'] = formData
    form = request.session['form_data_car']
    companies = Company.objects.filter(pk__in=list(map(lambda x:x.company.pk, Policy.objects.all())))

    """FILTERS"""
    company = False
    if form.get('company'):
        company = form.get('company')

    sortingSearch = False
    if form.get('sortingSearch'):
        sortingSearch = form.get('sortingSearch')
    

    if company and sortingSearch:
        if sortingSearch == '2':
            all_policies = Policy.objects.filter(company__in=company).order_by('rate')
        elif sortingSearch == '0':
            all_policies = Policy.objects.filter(company__in=company).order_by('-rate')
        elif sortingSearch == '1':
            all_policies = Policy.objects.filter(company__in=company, recomended=True)
        else:
            all_policies = Policy.objects.filter(company__in=company)

        
    elif sortingSearch:
        if sortingSearch == '2':
            all_policies = Policy.objects.order_by('-rate')
        elif sortingSearch == '0':
            all_policies = Policy.objects.order_by('rate')
        elif sortingSearch == '1':
            all_policies = Policy.objects.filter(recomended=True)
        else:
            all_policies = Policy.objects.all()
    
    elif company:
        all_policies = Policy.objects.filter(company__in=company)

    else:
        all_policies = Policy.objects.all()

    # all_policies = Paginator(all_policies, 10) 
    # page_number = request.GET.get('page')
    # page_obj = all_policies.get_page(page_number)

    for plc in all_policies:
        total_amount = (int(form.get('estimated'))/100)*plc.rate
        discount_amount = total_amount-(total_amount/100)*plc.off if plc.off > 0 else 0
        
        installment_amount = 0 
        if plc.installment_plane > 0:
            ...
            # installment_amount = discount_amount/plc.installment_plane if plc.installment_plane > 0 else 0
            installment_amount = discount_amount/plc.installment_plane if plc.off > 0 else (total_amount/plc.installment_plane if plc.installment_plane > 0 else 0)

        allData.append({
            'policy': plc,
            'main_coverage': json.loads(plc.main_coverage),
            'third_party_coverage': json.loads(plc.third_party_coverage),
            'value_added_features': json.loads(plc.value_added_features),
            'discount_amount': discount_amount,
            'installment_amount': installment_amount,
            'total_amount':total_amount,
           
            # 'features': get_features(plc)
        })



    context = {
        'allData': allData,
        'formData': formData,
        'carBrand': Cars.objects.filter(pk=formData.get('brand')).first(),
        'page_obj': all_policies,
        'all_companies': companies,
        'company': company,
        'formDataForSubmission': json.dumps(formData),
        'sortingSearch': sortingSearch,
         'quoteID': generateQuotaId(BuyPolicy)
    }
    # return HttpResponse("%d goes here." % allData)
    return render(request, 'frontend/listing-car.html', context)


def submit_inquire(request):
    if request.method == 'GET':
        return redirect('carForm')

    form = request.POST

    inq, created = Inquirer.objects.update_or_create(
        full_name = form.get('full_name'),
        phone = form.get('phone'),
        email = form.get('email'),
        city = form.get('city'),
        qoutId = form.get('qoutId'),
        form_data = json.dumps(json.loads(form.get('form_data'))),
        policy = form.get('policy'),
        policy_type = form.get('policy_type')
    )

    if created:
        messages.success(request, 'Your Inquiry has beed submited, ll contact you as soon as possible')
    else:
        messages.warning(request, 'oops! Something went wrong. Please try again!')
    
    if form.get('policy_type') == 'car':
        return redirect('listingcar')
    elif form.get('policy_type') == 'travel':
        return redirect('listingTravel')
    else:
        return redirect('healthlisting')

def buyPolicy(request, pk, quoteID='BS0012011'):
    allData = {}
    form = request.session['form_data_car']
    plc = Policy.objects.get(pk=pk)

    total_amount = (int(form.get('estimated'))/100)*plc.rate
    discount_amount = total_amount-(total_amount/100)*plc.off if plc.off > 0 else 0
    
    installment_amount = 0 
    if plc.installment_plane > 0:
        ...
        # installment_amount = discount_amount/plc.installment_plane if plc.installment_plane > 0 else 0
        installment_amount = discount_amount/plc.installment_plane if plc.off > 0 else (total_amount/plc.installment_plane if plc.installment_plane > 0 else 0)

    allData.update({
        'policy': plc,
        'total_amount': total_amount,
        'discount_amount': discount_amount,
        'installment_amount': installment_amount
    })

    
    context = {
        'allData': allData,
        'formData': form,
        'generateQuotaId': quoteID,
        'formDataForSubmission': json.dumps(form)
    }

    return render(request, 'frontend/buy.html', context)

def thankyou(request, pk):
    allData = {}
    form = request.session['form_data_car']
    plc = Policy.objects.get(pk=pk)
    
    total_amount = (int(form.get('estimated'))/100)*plc.rate
    discount_amount = total_amount-(total_amount/100)*plc.off if plc.off > 0 else 0
    
    installment_amount = 0 
    if plc.installment_plane > 0:
        ...
        # installment_amount = discount_amount/plc.installment_plane if plc.installment_plane > 0 else 0
        installment_amount = discount_amount/plc.installment_plane if plc.off > 0 else (total_amount/plc.installment_plane if plc.installment_plane > 0 else 0)
    
    allData.update({
        'policy': plc,
        'total_amount': total_amount,
        'discount_amount': discount_amount,
        # 'features': get_features(plc),
        'installment_amount': installment_amount,
        
    })

    context = {
        'allData': allData,
        'formData': form,
        'email': request.session['email'],
        'quoteID': request.session['quoteID']
    }

    return render(request, 'frontend/thanks.html', context)

def submit_buy(request):
    if request.method == 'GET':
        return redirect('carForm')

    form = request.POST
    request.session['email'] = form.get('email')
    request.session['quoteID'] = form.get('quoteID')
    inq, created = BuyPolicy.objects.update_or_create(
        car_owner_name = form.get('car_owner_name'),
        cnic = form.get('cnic'),
        phone = form.get('phone'),
        email = form.get('email'),
        servey_location_address = form.get('servey_location_address'),
        car_registeration_number = form.get('car_registeration_number'),
        date = form.get('date'),
        time = form.get('time'),
        quoteID = form.get('quoteID'),
        form_data = json.dumps(json.loads(form.get('form_data'))),
        policy = Policy.objects.get(pk=form.get('policy'))
    )

    if created:
        return redirect('thankyou', pk=form.get('policy'))
    else:
        messages.warning(request, 'oops! Something went wrong. Please try again!')
    
    return redirect('carForm')


def submit_buy_travel(request):
    if request.method == 'GET':
        return redirect('travelForm')

    form = request.POST
    request.session['email'] = request.POST.get('email')
    request.session['quoteID'] = form.get('quoteID')
    family_data = []
    for index, family in enumerate(request.POST.getlist('family_first_name')):
        family_data.append({
            'family_relation': request.POST.getlist('family_relation')[index],
            'family_first_name': request.POST.getlist('family_first_name')[index],
            'family_last_name': request.POST.getlist('family_last_name')[index],
            'family_date_of_birth': request.POST.getlist('family_date_of_birth')[index],
            'family_passport': request.POST.getlist('family_passport')[index],
            'family_cnic': request.POST.getlist('family_cnic')[index],
        })
    formData = form.get('form_data')
    print('===================DATA==',form)
    inq, created = BuyPolicyTravel.objects.update_or_create(
        first_name = form.get('first_name'),
        last_name = form.get('last_name'),
        cnic = form.get('cnic'),
        date_of_issue = form.get('date_of_issue'),
        date_of_birth = form.get('date_of_birth'),
        phone = form.get('phone'),
        purpose = form.get('purpose'),
        email = form.get('email'),
        passport = form.get('passport'),
        residance_address = form.get('residance_address'),
        city_residance = form.get('city_residance'),
        travel_from = form.get('travel_from'),
        travel_to = form.get('travel_to'),
        quoteID = form.get('quoteID'),
        
        other_family_members = json.dumps(family_data),
        form_data = json.dumps(json.loads(form.get('form_data'))),
        policy = PolicyTravel.objects.get(pk=form.get('policy'))
    )

    if created:
        return redirect('thankyouTravel', pk=form.get('policy'))
        # return JsonResponse({'data': 'Saved'})
    else:
        messages.warning(request, 'oops! Something went wrong. Please try again!')
        # return JsonResponse({'data': 'error'})
    
    # return redirect('carForm')
    return HttpResponseRedirect('submit_buy_travel')

def thankyouTravel(request, pk):
    allData = {}
    form = request.session['form_data_travel']
    plc = PolicyTravel.objects.get(pk=pk)

    formData = request.session['travel_amounts']
    allData.update({
        'policy': plc,
        'total_amount': formData.get('total_amount'),
        'discount_amount': formData.get('discount_amount'),
        'days': formData.get('days'),
    })

    print(formData)

    context = {
        'allData': allData,
        'formData': formData,
        'email': request.session['email'],
        'quoteID': request.session['quoteID']
    }

    return render(request, 'frontend/thanksTravel.html', context)

def ComparePolicies(request):
    # policies = [28,29]
    policies = json.loads(request.GET.get('policies'))
    print('plcs===========', policies)
    allData = []
    get_unique_features = []
    for plc in Policy.objects.filter(pk__in=policies):
        allData.append({
            'policy': plc,
            'main_coverage': json.loads(plc.main_coverage),
            'third_party_coverage': json.loads(plc.third_party_coverage),
            'value_added_features': json.loads(plc.value_added_features)
            # 'features': Feature.objects.filter(policy=plc)
        })
    print('==================START=================')
    for feature in Feature.objects.all():        
        if feature.feature not in get_unique_features:
            get_unique_features.append(feature.feature)

    context = {
        'allData': allData, 
        'get_unique_features': get_unique_features,
        # 'features': list(map(lambda x: {'feature': x.feature, 'status': x.status}, Feature.objects.filter(policy__in=policies)))
    }
    # news_items = serializers.serialize('json', itemObject)
    # return JsonResponse(allData, safe=False)
    return render(request, 'frontend/compare_temp.html', context)


def ComparePoliciesTravel(request):
    # policies = [2,3]
    policies = json.loads(request.GET.get('policies'))
    print('plcs===========', policies)
    allData = []
    get_unique_features = []
    for plc in PolicyTravel.objects.filter(pk__in=policies):
        allData.append({
            'policy': plc,
            'medical_benefits': json.loads(plc.medical_benefits),
            'personal_accident_benefits': json.loads(plc.personal_accident_benefits),
            'travel_inconvenience_benefits': json.loads(plc.travel_inconvenience_benefits)
            # 'features': Feature.objects.filter(policy=plc)
        })
    print('==================START=================')
    for feature in FeatureTravel.objects.all():        
        if feature.feature not in get_unique_features:
            get_unique_features.append(feature.feature)

    context = {
        'allData': allData, 
        'get_unique_features': get_unique_features,
        # 'features': list(map(lambda x: {'feature': x.feature, 'status': x.status}, Feature.objects.filter(policy__in=policies)))
    }
    # news_items = serializers.serialize('json', itemObject)
    # return JsonResponse(allData, safe=False)
    return render(request, 'frontend/compare_temp_travel.html', context)


# TRAVEL START HERE
def travelForm(request):
    return render(request, 'frontend/form-travel.html')

no_of_days = [
    'days_7',
    'days_10',
    'days_15',
    'days_21',
    'days_31',
    'days_62',
    'days_62',
    'days_122',
    'days_152',
    'days_180',
    'anual_multi_trip'
]


def listingTravel(request, insurance_companies=False, medical_coverage=False, covid_coverage=False, price_range=False, sort=False):
    duration = 0
    # if request.method == 'POST':        
    if request.method == 'GET' or request.method == 'POST':
        if request.method == 'GET':
            if not request.session['form_data_travel']:
                return redirect('travelForm')
            else:
                form = request.session['form_data_travel']

        if request.method == 'POST':
            form = request.POST

        formData = {}
        for k, v in form.items():            
            if k == 'company':
                formData[k] = form.getlist(k) if request.method == 'POST' else v
            else:
                formData[k] = v

        if request.method == 'POST':
            del formData['csrfmiddlewaretoken'] 

        request.session['form_data_travel'] = formData
        form = request.session['form_data_travel']

        # print(request.POST)
        from datetime import date
        fm, fd, fy = str(form.get('startdate')).split('/')
        em, ed, ey = str(form.get('enddate')).split('/')
        f_date = date(int(fy), int(fm), int(fd))
        l_date = date(int(ey), int(em), int(ed))
        delta = l_date - f_date
        requested_date = delta.days
        selected_type = form.get('type')
        
        """FILTERS"""
        company = False
        if form.get('company'):
            company = form.get('company')

        is_coid19 = False
        if form.get('is_coid19'):
            is_coid19 = form.get('is_coid19')

        
        minValue = False
        maxValue = False
        if form.get('maxValue'):
            minValue = form.get('minValue')
            maxValue = form.get('maxValue')
        
        # print('======================FIND', is_coid19)
        # print(str(form.get('startdate')).split('/'))
        # print('====================FIELDS================')
        # all_fields = [field.name for field in PolicyTravel._meta.get_fields()]
        

        # print('====================POLICIES================')
        all_policies_data = []
        all_prices = []

        if company and is_coid19:
            all_policies = PolicyTravel.objects.filter(company__in=company, coid19=True)
        elif is_coid19:
            all_policies = PolicyTravel.objects.filter(coid19=True)
        elif company:
            all_policies = PolicyTravel.objects.filter(company__in=company)

        else:
            all_policies = PolicyTravel.objects.all()

        # all_policies = Paginator(all_policies, 10) 
        # page_number = request.GET.get('page')
        # page_obj = all_policies.get_page(page_number)

        for policy in all_policies:
            all_policies_data.append({
                'obj': policy,
                'company': policy.company ,
                'policy_name': policy.policy_name ,
                'instant': policy.instant ,
                'coid19': policy.coid19 ,
                
                'days_7': policy.days_7 ,
                'individual_amount_7': policy.individual_amount_7 ,
                'family_amount_7': policy.family_amount_7 ,

                'days_10': policy.days_10 ,
                'individual_amount_10': policy.individual_amount_10 ,
                'family_amount_10': policy.family_amount_10 ,

                'days_15': policy.days_15 ,
                'individual_amount_15': policy.individual_amount_15 ,
                'family_amount_15': policy.family_amount_15 ,

                'days_21': policy.days_21 ,
                'individual_amount_21': policy.individual_amount_21 ,
                'family_amount_21': policy.family_amount_21 ,

                'days_31': policy.days_31 ,
                'individual_amount_31': policy.individual_amount_31 ,
                'family_amount_31': policy.family_amount_31 ,

                'days_62': policy.days_62 ,
                'individual_amount_62': policy.individual_amount_62 ,
                'family_amount_62': policy.family_amount_62 ,

                'days_92': policy.days_92 ,
                'individual_amount_92': policy.individual_amount_92 ,
                'family_amount_92': policy.family_amount_92 ,

                'days_122': policy.days_122 ,
                'individual_amount_122': policy.individual_amount_122 ,
                'family_amount_122': policy.family_amount_122 ,

                'days_152': policy.days_152 ,
                'individual_amount_152': policy.individual_amount_152 ,
                'family_amount_152': policy.family_amount_152 ,

                'days_180': policy.days_180 ,
                'individual_amount_180': policy.individual_amount_180 ,
                'family_amount_180': policy.family_amount_180 ,

                'anual_multi_trip': policy.anual_multi_trip ,
                'individual_amount_amt': policy.individual_amount_amt ,
                'family_amount_amt': policy.family_amount_amt ,

                'senior_ages': policy.senior_ages ,
                'individual_amount_sa': policy.individual_amount_sa ,
                'family_amount_sa': policy.family_amount_sa ,

                'medical_benefits': policy.medical_benefits ,
                'personal_accident_benefits': policy.personal_accident_benefits ,
                'travel_inconvenience_benefits': policy.travel_inconvenience_benefits,
                'off': policy.off,
                'recomended': policy.recomended
            })
            

        """ here now can be the selected area """
        get_final_policy_data = []
        for data in all_policies_data:
            for key, value in data.items():
                _, no_of_day = str(key).split('_') if 'days' in key else ['','0']
                if int(no_of_day) >= requested_date:
                    
                    if maxValue:
                        if float( int(maxValue) > data.get(selected_type+'_amount_'+no_of_day)) and int(minValue) < float(data.get(selected_type+'_amount_'+no_of_day)) :  
                            
                            get_final_policy_data.append({
                                'recomended': data.get('recomended'),
                                'days': data.get(key),
                                'total_amount': float(data.get(selected_type+'_amount_'+no_of_day)),
                                'discount_amount': float(data.get(selected_type+'_amount_'+no_of_day)) if int(data.get('off'))<=1 else (float(data.get(selected_type+'_amount_'+no_of_day))-(float(data.get(selected_type+'_amount_'+no_of_day))/100)*int(data.get('off'))),
                                'policy_obj': data.get('obj'),
                                'top_medical_benefits': list(filter(lambda x:x if x.get('is_active') == '1' else '', json.loads(data.get('obj').medical_benefits))),
                                'medical_benefits': list(filter(lambda x:x if x.get('is_active') == '0' else '', json.loads(data.get('obj').medical_benefits))),
                                'personal_accident_benefits': json.loads(data.get('obj').personal_accident_benefits),
                                'travel_inconvenience_benefits': json.loads(data.get('obj').travel_inconvenience_benefits)                 
                            })
                           
                            break
                    else:
                        get_final_policy_data.append({
                            'recomended': data.get('recomended'),
                            'days': data.get(key),
                            'total_amount': float(data.get(selected_type+'_amount_'+no_of_day)),
                            'discount_amount': float(data.get(selected_type+'_amount_'+no_of_day)) if int(data.get('off'))<=1 else (float(data.get(selected_type+'_amount_'+no_of_day))-(float(data.get(selected_type+'_amount_'+no_of_day))/100)*int(data.get('off'))),
                            'policy_obj': data.get('obj'),
                            'top_medical_benefits': list(filter(lambda x:x if x.get('is_active') == '1' else '', json.loads(data.get('obj').medical_benefits))),
                            'medical_benefits': list(filter(lambda x:x if x.get('is_active') == '0' else '', json.loads(data.get('obj').medical_benefits))),
                            'personal_accident_benefits': json.loads(data.get('obj').personal_accident_benefits),
                            'travel_inconvenience_benefits': json.loads(data.get('obj').travel_inconvenience_benefits)                                     
                        })
                        break
                                    
              
        print('requested_date: ',formData)

    """FILETRS"""  
    all_companies = Company.objects.filter(pk__in=list(map(lambda x:x.company.pk, PolicyTravel.objects.all())))
    
    for data in all_policies_data:
        for key, value in data.items():
            if 'amount' in key and type(value) in [int,float]:
                all_prices.append(value)

    print('forData=============0')
    get_final_policy_data = sorted(get_final_policy_data, key = lambda i: i['discount_amount'])
  
    context = {
        'get_final_policy_data': get_final_policy_data,
        'all_companies': all_companies,
        'all_prices': all_prices,
        'formData': formData,
        'formDataFormSubmission': json.dumps(formData),
        'company': company,
        'is_coid19':is_coid19,
        'duration': requested_date,
        'quoteID': generateQuotaId(),
        'page_obj': all_policies,
        'minValue': minValue,
        'maxValue': maxValue
    }
    return render(request, 'frontend/listing-travel.html', context)




def buyPolicyTravel(request):
    formData = request.POST
    allData = {}
    form = request.session['form_data_travel']
    request.session['travel_amounts'] = formData
    plc = PolicyTravel.objects.get(pk=formData.get('pk'))
    
    allData.update({
        'policy': plc,
        'total_amount': formData.get('total_amount'),
        'discount_amount': formData.get('discount_amount'),
        'days': formData.get('days'),
    })

    context = {
        'allData': allData,
        'formData': form,
        'generateQuotaId': generateQuotaId(PolicyTravel),
        'formDataForSubmission': json.dumps(form)
    }
    return render(request, 'frontend/buy-policy-travel.html',context)

# TRAVEL START HERE
def healthForm(request):
    return render(request, 'frontend/form-health.html')

def healthlisting(request):
    if request.method == 'GET':
        if not request.session['form_data_health']:
            return redirect('travelForm')
        else:
            form = request.session['form_data_health']

    if request.method == 'POST':
        form = request.POST

    formData = {}
    for k, v in form.items():
        if k == 'kids' or k == 'company':
            formData[k] = form.getlist(k) if request.method == 'POST' else v
        else:
            formData[k] = v

    if request.method == 'POST':
        del formData['csrfmiddlewaretoken'] 

    request.session['form_data_health'] = formData
    form = request.session['form_data_health']
    search_type = form.get('type')
    
    """ FILETRS """
    company = False
    
    if form.get('company'):
        company = form.get('company')
    
    limit = form.get('limit')
    
 
    if company:
        policies = PolicyHealth.objects.filter(company__in=company, hospitalization__contains=limit)
    
    else:
        policies = PolicyHealth.objects.filter(hospitalization__contains=limit)

    allData = []

    all_policies = Paginator(policies, 5) 
    page_number = request.GET.get('page')
    page_obj = all_policies.get_page(page_number)
    

    for policy in page_obj:
        total_amount = manage_premium(search_type, policy,form)
        discount_amount = total_amount-(total_amount/100)*policy.off if policy.off > 0 else 0

        allData.append({
            'policy': policy,
            'topFeatures': list(filter(lambda x:x if x.get('is_active') == '1' else '', json.loads(policy.features))),
            'detailFeatures': list(filter(lambda x:x if x.get('is_active') == '0' else '', json.loads(policy.features))),
            'lab': LabDiscount.objects.filter(policy=policy),
            'hospital': HospitalInfo.objects.filter(policy=policy),
            'total_amount': total_amount,
            'discount_amount': discount_amount,
            'kids': len(form.get('kids')) if form.get('kids') else 0,
            'type': form.get('type'),
        })
   
    """ OTHERS """
    companies =  Company.objects.filter(pk__in=[pk.company.pk for pk in PolicyHealth.objects.all()])
    limits = ['60k - 2 Lac', '2 Lac - 5 Lac', '5 Lac - 10 Lac']
    context = {
        'allData': allData,
        'formData': formData,
        'formDataFormSubmission': json.dumps(formData),
        'page_obj': page_obj,
        'all_companies': companies,
        'company': company,
        'limits': limits,
        'limitSearched': limit,
        'quoteID': generateQuotaId(BuyPolicyHealth)
    }
    return render(request, 'frontend/listing-health.html', context)

def manage_premium(seach_type, policy,form, from_method=True):
    if seach_type == 'self':
        return policy.get_self()

    elif seach_type == 'family':        
        if from_method:
            qty = len(form.get('kids'))
        else:
            qty = int(form.get('kids'))
        
        total = float(policy.get_family_kids(qty))+float(policy.get_family_parent())            
        if total > 0:
            return total
        else:
            return policy.get_family()

    elif seach_type == 'parents':
        return policy.get_parent()



def buyPolicyHealth(request):
    formData = request.POST
    allData = {}
    form = request.session['form_data_health']
    plc = PolicyHealth.objects.get(pk=formData.get('pk'))


    print('==========formData========')
    print(formData)

    allData.update({
        'policy': plc,
        'total_amount': formData.get('total_amount'),
        'discount_amount': formData.get('discount_amount'),
        'maternity_cover_price': formData.get('maternity_cover_price'),
        'off': plc.off,
    })

    context = {
        'allData': allData,
        'formData': form,
        'formDataForForm': json.dumps(form),
        'generateQuotaId': generateQuotaId(BuyPolicyHealth),
        'has_maternity': formData.get('has_maternity'),
    }
    return render(request, 'frontend/buy-policy-health.html',context)


def submit_buy_health(request):
    if request.method == 'GET':
        return redirect('travelForm')

    form = request.POST
    request.session['email'] = form.get('email')
    request.session['quoteID'] = form.get('quoteID')

    family_data = []
    for index, family in enumerate(request.POST.getlist('family_first_name')):
        family_data.append({
            'family_relation': request.POST.getlist('family_relation')[index],
            'family_first_name': request.POST.getlist('family_first_name')[index],
            'family_last_name': request.POST.getlist('family_last_name')[index],
            'family_date_of_birth': request.POST.getlist('family_date_of_birth')[index],
        })
    formData = form.get('form_data')
    print('===================DATA HEALTH==',form)

    myFormData = []
    for i in json.loads(form.get('form_data')):
        print('===========TESTING FRM DATA========')
        print(i)

    inq, created = BuyPolicyHealth.objects.update_or_create(
        first_name = form.get('first_name'),
        last_name = form.get('last_name'),
        cnic = form.get('cnic'),
        date_of_issue = form.get('date_of_issue'),
        date_of_birth = form.get('date_of_birth'),
        phone = form.get('phone'),
        email = form.get('email'),
        residance_address = form.get('residance_address'),
        city_residance = form.get('city_residance'),
        other_family_members = json.dumps(family_data),
        form_data = json.dumps(json.loads(form.get('form_data'))),
        policy = PolicyHealth.objects.get(pk=form.get('policy')),
        maternity_cover_price = form.get('maternity'),
        quoteID = form.get('quoteID')
    )

    if created:

        return redirect('thankyouHealth', pk=form.get('policy'))
        # return JsonResponse({'data': 'Saved'})
    else:
        messages.warning(request, 'oops! Something went wrong. Please try again!')
        # return JsonResponse({'data': 'error'})
    
    # return redirect('carForm')
    # return JsonResponse({'data': 'default'})
    return redirect('submit_buy_health')


def thankyouHealth(request, pk):
    allData = {}
    form = request.session['form_data_health']
    plc = PolicyHealth.objects.get(pk=pk)

    total_amount = manage_premium(form.get('type'), plc,form)
    discount_amount = total_amount-(total_amount/100)*plc.off if plc.off > 0 else 0
    allData.update({
        'policy': plc,
        'total_amount': total_amount,
        'discount_amount': discount_amount
    })

    print(form)

    context = {
        'allData': allData,
        'formData': form,
        'email': request.session['email'],
        'quoteID': request.session['quoteID']
    }

    return render(request, 'frontend/thanksHealth.html', context)

def get_labs_hotl_ata(request):
    pk = request.GET.get('pk')
    search_type = request.GET.get('type')
    if search_type == 'hospitals':
        data = HospitalInfo.objects.filter(policy=PolicyHealth.objects.get(pk=pk))
        return render(request, 'frontend/hospitals.html', {'data': data})
    if search_type == 'labs':
        data = LabDiscount.objects.filter(policy=PolicyHealth.objects.get(pk=pk))
        return render(request, 'frontend/labs.html', {'data': data})


def ComparePoliciesHealth(request):
    # policies = [2,3]
    policies = json.loads(request.GET.get('policies'))
    form = {
        'kids': request.GET.get('kids')
    }
    search_type = request.GET.get('type')

    allData = []
    get_unique_features = []
    for plc in PolicyHealth.objects.filter(pk__in=policies):
        allData.append({
            'policy': plc,
            'features': json.loads(plc.features),
            'lab': LabDiscount.objects.filter(policy=plc),
            'hospital': HospitalInfo.objects.filter(policy=plc),
            'premium': manage_premium(search_type, plc,form, False)
            # 'features': Feature.objects.filter(policy=plc)
        })
        
    for feature in FeatureHealth.objects.all():        
        if feature.feature not in get_unique_features:
            get_unique_features.append(feature.feature)

    context = {
        'allData': allData, 
        'get_unique_features': get_unique_features,
        'policies': len(policies)
        # 'features': list(map(lambda x: {'feature': x.feature, 'status': x.status}, Feature.objects.filter(policy__in=policies)))
    }
    # news_items = serializers.serialize('json', itemObject)
    # return JsonResponse(allData, safe=False)
    return render(request, 'frontend/compare_health.html', context)