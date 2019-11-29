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


# Create your views here.
