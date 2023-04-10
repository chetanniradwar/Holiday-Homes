import json
import pytest

from .views import OwnerViewSet


@pytest.mark.usefixtures("request_factory")
class TestHolidayHome:
    @pytest.mark.django_db
    def test_owner_creation(self, request_factory):

        endpoint = '/assessment/assessment-form/'

        view = OwnerViewSet.as_view({'post': 'create'})
        py_data = {

                "name": "owner 1",
                "country_code": "1",
                "primary_phone": 9876543210,
                "email": "abd@gmail.com",
                "country_of_residence": "USA"
        }

        data = json.dumps(py_data)
        request = request_factory.post(endpoint, data, content_type='application/json')
        response = view(request)

        assert response.status_code == 201
