from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.response import Response
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

# Create your views here.
@api_view(['GET', 'POST'])
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def index(request):
    ''' サンプルコード '''
    return Response({"message": "hello world No paramater in request"})
