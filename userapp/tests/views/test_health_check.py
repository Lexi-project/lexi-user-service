import pytest
from rest_framework.test import APIClient
from rest_framework import status

client = APIClient()


@pytest.mark.django_db
def test_health_check():
    response = client.post('/api/user/health-check')
    assert response.status_code == status.HTTP_200_OK
