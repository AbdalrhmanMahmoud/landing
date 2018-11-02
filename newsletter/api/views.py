# from rest_framework import  generics
# # from .serializers import JoinSerializers
# #
# # from newsletter.models import Join
# # class JoinCreateAPI(generics.CreateAPIView):
# #     qus = Join.objects.all()
# #     ser_class = JoinSerializers
# #     permission_class = []
# #     auth_class = []

from rest_framework import generics


from newsletter.models import Join
from .serializers import JoinSerializer


class JoinCreateAPIView(generics.CreateAPIView):
    queryset = Join.objects.all()
    serializer_class = JoinSerializer
    permission_classes = []
    authentication_classes = []