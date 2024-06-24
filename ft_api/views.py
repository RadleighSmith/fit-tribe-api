from rest_framework.decorators import api_view
from rest_framework.response import Response
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)


@api_view()
def root_route(request):
    """
    Root endpoint of the FitTribe Backend API.

    This endpoint provides a welcome message when accessed.

    Returns:
        Response: A welcome message in JSON format.
    """
    return Response({
        "message": "Welcome to the FitTribe Backend API"
    })


@api_view(['POST'])
def logout_route(request):
    """
    Logout endpoint for the FitTribe Backend API.

    This endpoint clears the JWT authentication and refresh cookies,
    effectively logging the user out.

    Returns:
        Response: An empty response with cookies set to expire immediately.
    """
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response
