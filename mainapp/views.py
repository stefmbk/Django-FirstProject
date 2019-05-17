from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Job,Company,Application

import datetime
from django.db.models import Q

import pdb


def index(request):
    return render(request, 'mainapp/index.html')
def findjob(request):

    job_list = Job.objects.order_by('-pub_date')
    if request.method == 'POST':
        query=request.POST.get("search",None)
        if query is not None:
            job_list = job_list.filter(Q(position__icontains=query) |
                                       Q(industry__contains=query))


        try:
            min = int(request.POST.get('min'))
            if min is not None:
                job_list = job_list.filter(Q(salary__gte=min))
        except ValueError:
            print('Exception')
        try:
            max = int(request.POST.get('max'))
            if max is not None:
                job_list = job_list.filter(Q(salary__lte=max))
        except ValueError:
            print('Exception')

        studyLevels = request.POST.getlist('checks[]', None)
        if(studyLevels):
            print(studyLevels)
            job_list = job_list.filter(Q(educationType__in=studyLevels))

    else:
        query=request.GET.get("search",None)
        if query is not None:
            job_list=job_list.filter(Q(position__icontains=query) |
                                     Q(industry__contains=query))
    context = {'job_list': job_list}
    return render(request, 'mainapp/findjob.html',context)

def jobdetail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'mainapp/jobdetail.html', {'job': job})
def companydetail(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    return render(request, 'mainapp/companydetail.html', {'company': company})

def addCompany(request):
    company_list = Company.objects.order_by('-name')
    context = {'company_list': company_list}
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email'):
            company = Company()
            job = Job()
            if (Company.objects.filter(name=request.POST.get('name')).count()):
                return render(request, 'mainapp/addCompany.html', {
                    'company': company,
                    'error_message': "Company already exists in database",
                    'company_list': company_list
                })
            else:

                company.name = request.POST.get('name')
                company.address = request.POST.get('address')
                company.email = request.POST.get('email')
                company.website = request.POST.get('website')
                company.save()
                request.session['id']=company.id
                #return HttpResponseRedirect('1/')
        else:
            return render(request, 'mainapp/addCompany.html', {
                'error_message': "Please verify the data entered and try again",'company_list': company_list
            })
    return render(request, 'mainapp/addCompany.html',context)




def postJob(request,company_id):
    if(not(company_id)):
        company_id=request.session['id']

    company = get_object_or_404(Company, pk=company_id)
    if request.method == 'POST':
        if request.POST.get('position') and request.POST.get('studyLevel'):

            job = Job()

            if (Company.objects.filter(name=request.POST.get('name')).count() and Job.objects.filter(name=request.POST.get('position')).count()  ):
                return render(request, 'mainapp/postjob.html', {
                    'company': company,
                    'error_message': "Job already exists in database",
                })
            else:
                job.industry=request.POST.get('industry')
                job.occupation=request.POST.get('occupation')
                job.position = request.POST.get('position')
                job.description = request.POST.get('description')
                job.salary = request.POST.get('salary')
                job.educationType=request.POST.get('studyLevel')
                job.placeOfResidence = request.POST.get('placeOfResidence')
                job.lengthOfService = request.POST.get('lengthOfService')

                job.pub_date=datetime.datetime.now()
                company.job_set.create(description=job.description,salary=job.salary,occupation=job.occupation,industry=job.industry,
                                       position=job.position,pub_date=job.pub_date,educationType=job.educationType,placeOfResidence=job.placeOfResidence)
                company.save()
        else:
            return render(request, 'mainapp/postjob.html', {
                'error_message': "Please verify the data entered and try again (Position and Study level are required)",
            })


    return render(request, 'mainapp/postjob.html',{
                    'company': company,})

def apply(request,job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        app=Application()
        if request.POST.get('name'):
            if (Application.objects.filter(name=request.POST.get('name')).count()):
                return render(request, 'mainapp/apply.html', {
                    'app': app,
                    'error_message': "You aleardy applied for this job",
                })
            else:
                app.name = request.POST.get('name')
                app.email = request.POST.get('email')
                app.studyLevel = request.POST.get('studyLevel')
                app.motivLetter = request.POST.get('motivLetter')
                job.application_set.create(name=app.name, email=app.email, studyLevel=app.studyLevel,motivLetter=app.motivLetter)
                job.save()
        else:
            return render(request, 'mainapp/apply.html', {
                'error_message': "Please verify the data entered and try again (Name field is required)",
            })

    return render(request, 'mainapp/apply.html')

