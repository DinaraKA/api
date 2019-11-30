import json
from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def api_example(request, *args, **kwargs):
    request_data = None
    if request.body:
        request_data = json.loads(request.body)
    data = {
        'method': request.method,
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'content': request_data
    }
    data_json = json.dumps(data)
    response = HttpResponse(data_json)
    response['Content-Type'] = 'application/json'
    return response

def my_error(message):
    error = JsonResponse({'error': message})
    error.status_code = 400
    return error


@csrf_exempt
def add(request, *args, **kwargs):
    if request.body:
        data = json.loads(request.body)
        a = data.get('A')
        b = data.get('B')
        if type(a) is int and type(b) is int:
             return JsonResponse({'answer': a + b})
        else:
            response = my_error('User input is not number')
            return response
    else:
        response = my_error('No data provided')
        return response


@csrf_exempt
def subtract(request, *args, **kwargs):
    if request.body:
        data = json.loads(request.body)
        a = data.get('A')
        b = data.get('B')
        if type(a) is int and type(b) is int:
             return JsonResponse({'answer': a - b})
        else:
            response = my_error('User input is not number')
            return response
    else:
        response = my_error('No data provided')
        return response


@csrf_exempt
def multiply(request, *args, **kwargs):
    if request.body:
        data = json.loads(request.body)
        a = data.get('A')
        b = data.get('B')
        if type(a) is int and type(b) is int:
             return JsonResponse({'answer': a * b})
        else:
            response = my_error('User input is not number')
            return response
    else:
        response = my_error('No data provided')
        return response


@csrf_exempt
def divide(request, *args, **kwargs):
    if request.body:
        data = json.loads(request.body)
        a = data.get('A')
        b = data.get('B')
        if type(a) is int and type(b) is int:
            if b == 0:
                response = my_error('Division by zero')
                return response
            else:
                return JsonResponse({'answer': a / b})
        else:
            response = my_error('User input is not number')
            return response
    else:
        response = my_error('No data provided')
        return response