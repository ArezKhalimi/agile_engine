from django.contrib.postgres.search import SearchVector
from rest_framework import generics

from .models import Image
from .serializers import ImageSerializer


class ImageView(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = 'pcid'


class SearchView(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = 'search_term'
    search_vector = SearchVector(
        'pcid', 'title', 'camera', 'author', 'hashtags__tag_name'
    )

    def get_queryset(self):
        # just full_text search
        # TODO: add trigram search via pcid
        # TODO: add indexes
        search_term = self.kwargs['search_term']
        qs = (
            Image.objects
            .annotate(search=self.search_vector)
            .filter(search=search_term)
        )
        return qs
