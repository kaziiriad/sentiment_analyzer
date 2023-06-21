from drf_yasg import openapi

swagger_info = openapi.Info(
    title="Sentiment Analyzer API",
    default_version='v1.0',
    description="Text sentiment analyzer using pretrained ML model.",
    terms_of_service="https://analyzer.com/terms/",
    contact=openapi.Contact(email="admin@analyzer.com"),
    license=openapi.License(name="MIT License"),
)
