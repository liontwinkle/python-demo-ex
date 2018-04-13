import datetime
import pytest

from django_dynamic_fixture import G

from api.v1.stylist.serializers import StylistSerializer
from core.models import User
from salon.models import Salon, Stylist


@pytest.fixture
def stylist_data() -> Stylist:
    salon = G(
        Salon,
        name='Test salon', address='2000 Rilma Lane', city='Los Altos', state='CA',
        zip_code='94022', latitude=37.4009997, longitude=-122.1185007
    )

    stylist_user = G(
        User,
        is_staff=False, is_superuser=False, email='test_stylist@example.com',
        first_name='Fred', last_name='McBob', phone='(650) 350-1111'
    )
    stylist = G(
        Stylist,
        salon=salon, user=stylist_user,
        work_start_at=datetime.time(8, 0), work_end_at=datetime.time(15, 0),
    )

    return stylist


class TestStylistSerializer(object):
    @pytest.mark.django_db
    def test_stylist_serializer_representation(self, stylist_data: Stylist):
        serializer = StylistSerializer(instance=stylist_data)
        data = serializer.data
        assert(data['first_name'] == 'Fred' and data['last_name'] == 'McBob')
        assert(data['salon_name'] == 'Test salon')
        assert(data['id'] == stylist_data.id)

    @pytest.mark.django_db
    def test_stylist_serializer_update(self, stylist_data: Stylist):
        data = {
            'first_name': 'Jane',
            'salon_name': 'Janes beauty',
        }
        serializer = StylistSerializer(instance=stylist_data, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        stylist = serializer.save()
        assert(stylist.user.first_name == 'Jane')
        assert(stylist.salon.name == 'Janes beauty')
