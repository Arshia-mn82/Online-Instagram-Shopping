from django.http import JsonResponse, HttpResponse
from .models import Product

def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all().values('id', 'name', 'description', 'price')
        return JsonResponse(list(products), safe=False)
    return HttpResponse("Only GET method is allowed.", status=405)

def product_detail(request, pk):
    if request.method == 'GET':
        try:
            product = Product.objects.values('id', 'name', 'description', 'price').get(pk=pk)
            return JsonResponse(product)
        except Product.DoesNotExist:
            return HttpResponse("Product not found.", status=404)
    return HttpResponse("Only GET method is allowed.", status=405)
