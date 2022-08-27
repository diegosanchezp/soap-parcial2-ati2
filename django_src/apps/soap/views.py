from django.views.decorators.csrf import csrf_exempt

from spyne.server.django import DjangoApplication
from spyne.util.django import DjangoComplexModel

from spyne.model.primitive import Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.application import Application
from spyne.service import Service
from spyne.decorator import rpc
from spyne.error import ResourceNotFoundError
from .models import Task
from spyne.model.complex import ComplexModel, Array

# Create your services here.
class TaskType(DjangoComplexModel):
    class Attributes(DjangoComplexModel.Attributes):
        django_model = Task

class TaskAndTasks(ComplexModel):
    task = TaskType
    tasks = Array(TaskType)

class TaskService(Service):
    """
    Servicio para obtener tareas
    """
    @rpc(Integer, _returns=TaskAndTasks)
    def get_task(ctx, pk):
        """
        Obtener una tarea especifica y el resto
        """
        try:
            return TaskAndTasks(
                task=Task.objects.get(pk=pk),
                tasks=Task.objects.exclude(pk=pk)
            )
        except Task.DoesNotExist:
            # Mandar una excepcion al cliente si no se encuentra
            # la tarea
            raise ResourceNotFoundError('Tarea')

    @rpc(_returns=Array(TaskType))
    def get_tasks(ctx):
        """
        Obtener el todas las tareas
        """
        return Task.objects.all()


app = Application([TaskService],
    'django_src.apps.soap',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

task_service = csrf_exempt(DjangoApplication(app))
