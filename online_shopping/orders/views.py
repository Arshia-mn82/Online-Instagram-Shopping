from django.http import JsonResponse, HttpResponse
from .models import Order
from products.models import Product
from company.models import CompanyInfo
from django.utils import timezone
import datetime
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def add_to_cart(request, product_id):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            product = Product.objects.get(id=product_id)
            company = CompanyInfo.objects.first()
            requested_quantity = int(data.get("quantity", 1))

            if product.quantity >= requested_quantity:
                product.quantity -= requested_quantity
                product.save()

                Order.objects.create(
                    user=request.user,
                    product=product,
                    quantity=requested_quantity,
                    company=company,
                )
                return HttpResponse("Added to cart.")
            else:
                return HttpResponse("Insufficient quantity available.", status=400)
        except Product.DoesNotExist:
            return HttpResponse("Product not found.", status=404)
        except ValueError:
            return HttpResponse("Invalid quantity.", status=400)
    return HttpResponse("Only POST method is allowed.", status=405)


def cart(request):
    if request.method == "GET":
        orders = Order.objects.filter(user=request.user, paid=False).values(
            "id", "product__name", "quantity", "ordered_at", "paid"
        )
        return JsonResponse(list(orders), safe=False)
    return HttpResponse("Only GET method is allowed.", status=405)


@csrf_exempt
def mark_as_paid(request, order_id):
    if request.method == "POST":
        try:
            order = Order.objects.get(id=order_id, user=request.user, paid=False)
            order.paid = True
            order.delivery_estimate = timezone.now() + datetime.timedelta(days=7)
            order.save()
            return HttpResponse("Payment confirmed and order marked as paid.")
        except Order.DoesNotExist:
            return HttpResponse("Order not found or already paid.", status=404)
    return HttpResponse("Only POST method is allowed.", status=405)


def order_details(request, order_id):
    if request.method == "GET":
        try:
            order = Order.objects.get(id=order_id, user=request.user)
            data = {
                "id": order.id,
                "product_name": order.product.name,
                "quantity": order.quantity,
                "ordered_at": order.ordered_at,
                "paid": order.paid,
                "delivery_estimate": order.delivery_estimate,
                "company_name": order.company.address,
                "company_telephone": order.company.telephone,
            }
            return JsonResponse(data)
        except Order.DoesNotExist:
            return HttpResponse("Order not found.", status=404)
    return HttpResponse("Only GET method is allowed.", status=405)
