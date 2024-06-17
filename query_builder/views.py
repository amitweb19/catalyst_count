from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.http import JsonResponse
from .models import Country, State, City, Company


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Company
from .serializers import CompanyFilterSerializer


@login_required(login_url="/login/")
def QueryBuilder(request):
    return render(request, 'builder.html')

class FilteredCompaniesCountAPIView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = CompanyFilterSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        country_id = serializer.validated_data.get('country')
        state_id = serializer.validated_data.get('state')
        city_id = serializer.validated_data.get('city')
        current_employee_estimate_from = serializer.validated_data.get('current_employee_estimate_from')
        current_employee_estimate_to = serializer.validated_data.get('current_employee_estimate_to')

        # Filter companies based on selected criteria
        companies = Company.objects.all()

        if country_id:
            companies = companies.filter(country_id=country_id)
        if state_id:
            companies = companies.filter(state_id=state_id)
        if city_id:
            companies = companies.filter(city_id=city_id)
        if current_employee_estimate_from:
            companies = companies.filter(current_employee_estimate__gte=current_employee_estimate_from)
        if current_employee_estimate_to:
            companies = companies.filter(current_employee_estimate__lte=current_employee_estimate_to)

        # Get the count of filtered companies
        filtered_count = companies.count()

        return Response({'filtered_count': filtered_count})

def get_states(request):
    country_id = request.GET.get('country_id')
    states = State.objects.filter(country_id=country_id).values('id', 'name')
    return JsonResponse(list(states), safe=False)

def get_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id).values('id', 'name')
    return JsonResponse(list(cities), safe=False)

def filter_options(request):
    countries = Country.objects.all()
    context = {
        'countries': countries
    }
    return render(request, 'filter_options.html', context)