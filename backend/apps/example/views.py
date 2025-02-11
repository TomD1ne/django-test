from django.forms import ValidationError
from django.http import HttpRequest, JsonResponse
from django.views.generic import View
from rest_framework import permissions, viewsets
from .models import Software, Company
from .serializers import SoftwareSerializer, CompanySerializer
import json


"""
To outline the usefulness of DRF (Django REST Framework), the first two classes implement a few endpoints using the built-in way.
Below are examples using DRF, which are the once being used in urls.py
"""


class CompanyByIdView(View):
    """
    This class contains functions for http methods on the "/example/companies" endpoint
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
    This class contains functions for http methods on the "/example/companies" endpoint
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


class CompaniesViewSet(viewsets.ModelViewSet):
    """
    Using DRF.
    This class uses a ViewSet, which is a shortcut for common use cases. The associated endpoints will be created automatically.
    A ModelViewSet creates a get-multiple and a post endpoint, similar to the manual CompanyView class.
    API endpoint that allows Software to be viewed or edited.
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.AllowAny]


class SoftwareViewSet(viewsets.ModelViewSet):
    """
    Using DRF.
    This class uses a ViewSet, which is a shortcut for common use cases. The associated endpoints will be created automatically.
    A ModelViewSet creates a get-multiple and a post endpoint, similar to the manual CompanyView class.
    API endpoint that allows Software to be viewed or edited.
    """

    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
    permission_classes = [permissions.AllowAny]
