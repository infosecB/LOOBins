from pyloobins.models import Detection, ExampleUseCase, LOOBin, LOOBinsGroup, Resource
from polyfactory.factories.pydantic_factory import ModelFactory

class DetectionFactory(ModelFactory[Detection]):
    __model__ = Detection

class ExampleUseCaseFactory(ModelFactory[ExampleUseCase]):
    __model__ = ExampleUseCase

class ResourceFactory(ModelFactory[Resource]):
    __model__ = Resource

class LOOBinFactory(ModelFactory[LOOBin]):
    __model__ = LOOBin