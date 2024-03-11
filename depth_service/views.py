from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import depth_by_img
import tempfile
from django.http import HttpResponse

@csrf_exempt
def depth_view(request):
    if request.method == 'POST':
        img_url = request.POST.get('img_url')
        depth_image = depth_by_img(img_url)

        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_image:
            depth_image.save(temp_image, format='PNG')
            temp_image_path = temp_image.name

        with open(temp_image_path, 'rb') as f:
            image_data = f.read()

        response = HttpResponse(image_data, content_type='image/jpeg')
        response['Content-Disposition'] = 'attachment; filename="depth_image.jpg"'
        return response
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)