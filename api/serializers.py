from rest_framework import serializers
from advocate.models import Advocate
from company.models import Company

class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = ['name', 'logo', 'summary', 'id',]


class AdvocateSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False)
    class Meta:
        model = Advocate
        fields = ['username', 'name', 'company', 'profile_pic', 'short_bio', 'long_bio', 'advocate_years_of_experience', 'twitter', 'github', 'id',]
