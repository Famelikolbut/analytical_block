from drf_yasg import openapi

analytical_list_create_structure = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_UUID, description='UUID of the Analytical'),
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the Analytical', maxLength=254),
    },
    required=['name'],
)
