from django.views.decorators.csrf import csrf_exempt

from spyne.server.django import DjangoApplication
from spyne.util.django import DjangoComplexModel

from spyne.model.primitive import UnsignedInteger, Unicode
from spyne.protocol.soap import Soap11
from spyne.application import Application
from spyne.service import Service
from spyne.decorator import rpc
from spyne.error import ResourceNotFoundError
from .models import Country, State, City
from spyne.model.complex import ComplexModel, Array

# Create your services here.
class CountryType(DjangoComplexModel):
    class Attributes(DjangoComplexModel.Attributes):
        django_model = Country

class StateType(DjangoComplexModel):
    class Attributes(DjangoComplexModel.Attributes):
        django_model = State

class CityType(DjangoComplexModel):
    class Attributes(DjangoComplexModel.Attributes):
        django_model = City

class CountryService(Service):
    """
    Servicio para obtener paises, estado y ciudades
    """

    @rpc(_returns=Array(CountryType))
    def get_countries(ctx):
        """
        Get a list of countries
        """

        return Country.objects.all()

    @rpc(UnsignedInteger, _returns=Array(StateType))
    def get_states(ctx, country_id):
        """
        Get the states of a country
        """
        return State.objects.filter(country=country_id)


    @rpc(UnsignedInteger, _returns=Array(CityType))
    def get_cities(ctx, state_id):
        """
        Get the cities of a state
        """
        return City.objects.filter(state=state_id)


app = Application([CountryService],
    'django_src.apps.soap',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

country_service = csrf_exempt(DjangoApplication(app))
