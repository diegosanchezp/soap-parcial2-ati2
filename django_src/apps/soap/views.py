from django.views.decorators.csrf import csrf_exempt
from spyne.server.django import DjangoApplication
from spyne.model.primitive import Unicode, Integer
from spyne.protocol.soap import Soap11
from spyne.application import Application
from spyne.service import Service
from spyne.decorator import rpc
from spyne.model.complex import Iterable

# Create your services here.
class HelloWorldService(Service):
    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(ctx, name, times):
        for i in range(times):
            yield 'Hello, %s' % name

app = Application([HelloWorldService],
    'django_src.apps.soap',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

hello_world_service = csrf_exempt(DjangoApplication(app))
