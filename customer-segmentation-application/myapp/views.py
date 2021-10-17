from django.shortcuts import render
from myapp.segmentation import check
from django.urls import reverse
from django.http import HttpResponseRedirect

import myapp

changer = {'Gender_1': 'Male', 'Gender_0': 'Female', 'Ever_Married_1': 'Yes', 'Ever_Married_0': 'No',
           'Ever_Married_1': 'Yes', 'Graduated_1': 'Yes', 'Graduated_0': 'No', 'Profession_5': 'Healthcare',
		   'Profession_2': 'Engineer', 'Profession_7': 'Lawyer', 'Profession_3': 'Entertainment',
		   'Profession_0': 'Artist', 'Profession_1': 'Doctor', 'Profession_4': 'Executive',
		   'Profession_6': 'Homemaker', 'Profession_8': 'Marketing', 'Var_1_0': 1, 'Var_1_1': 2, 'Var_1_2': 3,
		   'Var_1_3': 4, 'Var_1_4': 5, 'Var_1_5': 6, 'Var_1_6': 7, 'Var_1_7': 8, 'Spending_Score_2': 'Low',
		   'Spending_Score_0': 'Average', 'Spending_Score_1': 'High'}


# Create your views here.
def index(request):
    return render(request, 'index.html')


def service(request):
	if request.method == 'POST':
		segment = check(request.POST)
		customer_id = request.POST.get('ID')
		age = request.POST.get('Age')
		gender = changer[request.POST.get('gender')]
		married = changer[request.POST.get('married')]
		graduated = changer[request.POST.get('graduated')]
		profession = changer[request.POST.get('profession')]
		work_experience = request.POST.get('Work_Experience')
		spending = changer[request.POST.get('spending')]
		family_size = request.POST.get('Family_Size')
		category = changer[request.POST.get('category')]
		ml_model = UserInfo(customer_id=customer_id, age=age, gender=gender, married=married, graduated=graduated,
							profession=profession, work_experience=work_experience, spending=spending, family_size=family_size,
							category=category, segment=segment)
		ml_model.save()
		return HttpResponseRedirect(reverse('result'))
	return render(request, 'services.html')


def result(request):
	data = UserInfo.objects.all().order_by('-id')
	return render(request, 'results.html', {'data': data})


def analytics(request):
    return render(request, 'analytics.html')
