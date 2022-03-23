from django import forms

from frontend.models import BuyPolicyTravel
from .models import Policy, PolicyHealth, PolicyTravel


class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = ('company','recomended','policy_name','rate','installment_plane','off','tracking_amount','instant','coid19','policy_documents','claim_process')

class PolicyTravelForm(forms.ModelForm):
    class Meta:
        model = PolicyTravel
        fields = [
            'company',
            'policy_name',
            'instant',
            'coid19',
            'recomended',
            

            'days_7',
            'individual_amount_7',
            'family_amount_7',

            'days_10',
            'individual_amount_10',
            'family_amount_10',

            'days_15',
            'individual_amount_15',
            'family_amount_15',

            'days_21',
            'individual_amount_21',
            'family_amount_21',

            'days_31',
            'individual_amount_31',
            'family_amount_31',

            'days_62',
            'individual_amount_62',
            'family_amount_62',

            'days_92',
            'individual_amount_92',
            'family_amount_92',

            'days_122',
            'individual_amount_122',
            'family_amount_122',

            'days_152',
            'individual_amount_152',
            'family_amount_152',

            'days_180',
            'individual_amount_180',
            'family_amount_180',

            'anual_multi_trip',
            'individual_amount_amt',
            'family_amount_amt',
            
            'senior_ages',
            'individual_amount_sa',
            'family_amount_sa',
            'off',
            'policy_documents',
            'claim_process',
            
            ]

class BuyPolicyTravelFrom(forms.ModelForm):
    class Meta:
        model = BuyPolicyTravel
        fields = '__all__'

class PolicyHealthForm(forms.ModelForm):
    class Meta:
        model = PolicyHealth
        fields = ('company', 'policy_name', 'recomended', 'self_price','family_price','parents_price','instant','coid19','hospitalization','policy_documents','claim_process','more_features','off','maternity_cover_price','family_parent_amount','family_kids_amount')