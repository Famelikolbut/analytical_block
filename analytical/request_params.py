from drf_yasg import openapi


class SearchAnalyticalParams:
    search = openapi.Parameter(
        "search",
        openapi.IN_QUERY,
        description="Search by name",
        type=openapi.TYPE_STRING,
    )
