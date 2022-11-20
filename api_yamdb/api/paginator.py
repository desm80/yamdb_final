from rest_framework.pagination import PageNumberPagination


class CommentPagination(PageNumberPagination):
    """Пагинатор для представления Comment."""

    page_size = 10
