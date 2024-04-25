from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


def calc_fbi(n):
    a, b = 1, 1
    if n == 1:
        result = a
    elif n == 2:
        result = b
    else:
        for i in range(n-2):
            a, b = b, a + b
            result = b
    return result


class FbiViewSet(APIView):
    def get(self, request):
        fbi_index = request.GET.get("n", "")
        fbi_index = int(fbi_index)
        result = calc_fbi(fbi_index)
        return Response({"result": result})
