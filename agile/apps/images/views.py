from rest_framework.views import APIView


class ImageList(APIView):
    def get(self, request, format=None):
        # TODO:
        # check  TTL
        # update image info if its needed
        # return image info 

