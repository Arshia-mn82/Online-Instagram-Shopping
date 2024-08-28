from django.http import JsonResponse,HttpResponse
from .models import CompanyInfo

def get_company_info(request):
    if request.method == 'GET':
        try:
            company_info = CompanyInfo.objects.first()  
            data = {
                "address": company_info.address,
                "telephone": company_info.telephone,
            }
            return JsonResponse(data)
        except CompanyInfo.DoesNotExist:
            return JsonResponse({"error": "Company information not available."}, status=404)
    return HttpResponse("Only GET method is allowed.", status=405)
