from libs.glitch.service import glitch_service
from django.http import JsonResponse
from requests.exceptions import HTTPError


# handle typos in URL like reminiscent-steady-albertosaurus does
def error_page(request, exception):
    return JsonResponse({'detail': 'Not found'}, status=404)


def sentence_response(request):
    try:
        adjective, verb, noun = glitch_service.get_all()
    except HTTPError as e:
        return JsonResponse({'detail': 'Unable to fetch data'}, status=e.response.status_code)

    message = f'Quite {adjective} task. I hope that everything {verb}. If not, {noun} will be better next time.'

    return JsonResponse({'detail': message}, status=200)
