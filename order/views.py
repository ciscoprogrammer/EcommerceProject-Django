import io
from django.shortcuts import render
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import FileResponse
from xhtml2pdf import pisa

class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# Create your views here.

from .models import Order  # Ensure the Order model is imported

@api_view(['GET'])
def order_metrics(request):
    today = timezone.now().date()
    orders_today = Order.objects.filter(date_created__date=today).count()
    return Response({'orders_today': orders_today})



@api_view(['GET'])
def download_invoice(request, order_id):
   try:
        order = Order.objects.get(id=order_id)
   except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=404)
    # Create a simple invoice in HTML format
   html_string = """
    <h1>Invoice for Order #{}</h1>
    <p>Order Date: {}</p>
    ...
    """.format(order.id, order.date_created)
    
   result = io.BytesIO()
   pdf = pisa.pisaDocument(io.BytesIO(html_string.encode('UTF-8')), result)
   if not pdf.err:
        return FileResponse(result.getvalue(), content_type='application/pdf')
   else:
        return Response({"error": "Failed to generate PDF"}, status=500)
