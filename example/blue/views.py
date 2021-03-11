from django.http import JsonResponse

# Create your views here.

def code(request):

    secret_code =[
        {'code_name': 'thedoctor',
        'secret_code': 'JHgT2xjDi9Xut8dZx8jdFYWi=ahkL*'}
    ]
    return JsonResponse({'secret_code' : secret_code})

def test(request):
    comments = [{
        'status': 'healthy',
        'container':
        'https://hub.docker.com/repository/docker/enochnooli/challenge_project_web',
        'project': 'https://github.com/lexstar1/Challenge_Project'
    }]
    return JsonResponse({'data' : comments})