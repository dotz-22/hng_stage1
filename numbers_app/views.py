from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NumberSerializer
from .classifier import classify_number, get_fun_fact
from rest_framework.views import APIView

class ClassifyView(APIView):
    def get (self, request):
      
        serializer = NumberSerializer(data=request.GET)

        if not serializer.is_valid():
            return Response({"error": True, "message": "Invalid input. Provide a valid integer."}, status=400)

        number = serializer.validated_data['number']
        
        classification = classify_number(number)
        
        fun_fact = get_fun_fact(number)

        response_data = {
            "number": number,
            "is_prime": classification.get("is_prime", False),
            "is_perfect": classification.get("is_perfect", False),
            "properties": classification.get("properties", []),
            "digit_sum": classification.get("digit_sum", 0),
            "fun_fact": fun_fact or "No fun fact available."
        }

        

        return Response(response_data, status=200)