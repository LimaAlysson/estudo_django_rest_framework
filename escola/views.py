from django.http import JsonResponse

def estudantes(request):
    
    if request.method == 'GET':
        estudante = {
            'id': '1',
            'nome': 'alysson',
        }
        return JsonResponse(estudante)
