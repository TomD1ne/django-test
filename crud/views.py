from django.forms import ValidationError
from django.http import HttpRequest, JsonResponse
from django.views.generic import View
from rest_framework import permissions, viewsets
from .models import Software, Company
from .serializers import SoftwareSerializer
import json


"""
For the Company crud endpoints I've used the built in way to do it in Django
This requires a lot of manual conversions and error handling
A better way may be achievable using DRF, which I will explore for the Software table
https://www.django-rest-framework.org/
"""


class CompanyByIdView(View):
    """
    This class contains functions for http methods on the "/crud/companies" endpoint
    The endpoints take one argument, a company_id : int
    """

    def get(self, _, company_id):
        try:
            company = Company.objects.get(pk=company_id)
        except Company.DoesNotExist:
            return JsonResponse({"error": "Object not found"}, status=404)
        return JsonResponse(
            {
                "company_name": company.name,
                "company_score": company.score,
            }
        )

    def put(self, request: HttpRequest, company_id):
        try:
            try:
                Company.objects.get(pk=company_id)
            except Company.DoesNotExist:
                return JsonResponse({"error": "Object not found"}, status=404)

            if not request.body:
                return JsonResponse({"error": "Request body is empty"}, status=400)

            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                return JsonResponse({"error": "Invalid JSON data"}, status=400)

            required_fields = ["company_name", "company_score"]
            for field in required_fields:
                if field not in data:
                    return JsonResponse(
                        {"error": f"Missing required field: {field}"}, status=400
                    )

            try:
                company = Company(
                    id=company_id,
                    name=data["company_name"],
                    score=data["company_score"],
                )
                company.full_clean()  # Validate the model instance
            except ValidationError as e:
                return JsonResponse({"error": str(e)}, status=400)

            company.save()

            return JsonResponse({"result": "success"})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


class CompanyView(View):
    """
    This class contains functions for http methods on the "/crud/companies" endpoint
    Unlike the above class, these functions don't take a company_id : int argument
    """

    def get(self, _):
        companies = Company.objects.all()
        data = list(companies.values("id", "name", "score"))
        return JsonResponse(data, safe=False)

    def post(self, request: HttpRequest):
        try:
            if not request.body:
                return JsonResponse({"error": "Request body is empty"}, status=400)

            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                return JsonResponse({"error": "Invalid JSON data"}, status=400)

            required_fields = ["company_name", "company_score"]
            for field in required_fields:
                if field not in data:
                    return JsonResponse(
                        {"error": f"Missing required field: {field}"}, status=400
                    )

            try:
                company = Company(
                    name=data["company_name"],
                    score=data["company_score"],
                )
                company.full_clean()  # Validate the model instance
            except ValidationError as e:
                return JsonResponse({"error": str(e)}, status=400)

            company.save()

            return JsonResponse({"result": "success"})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


def exampleError(_: HttpRequest):
    """
    Showcases what an error response looks like
    """
    raise NotImplementedError


class SoftwareViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Software to be viewed or edited.
    """

    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
    permission_classes = [permissions.AllowAny]
