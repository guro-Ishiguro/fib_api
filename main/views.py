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
        for i in range(n - 2):
            a, b = b, a + b
            result = b
    return result


class FibViewSet(APIView):
    def get(self, request):
        fib_index = request.GET.get("n", "")
        try:
            fib_index = int(fib_index)
            if fib_index < 1:
                return Response(
                    {"result": "Bad request."}, status=status.HTTP_400_BAD_REQUEST
                )
        except ValueError:
            return Response(
                {"result": "Bad request."}, status=status.HTTP_400_BAD_REQUEST
            )
        result = calc_fbi(fib_index)
        return Response({"result": result})
