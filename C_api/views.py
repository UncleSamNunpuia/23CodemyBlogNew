from django.shortcuts import render

# Create your views here.
# added below
from rest_framework import generics
from B_01BaseApp.models import InkhawmInchhiarnaBlogNew
from .serializers import InkhawmInchhiarnaBlogNewSerializer
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from django.shortcuts import get_object_or_404


# we can combine the create view and list view together
class InkhawmInchhiarnaBlogNewListCreateAPIview(generics.ListCreateAPIView):
    queryset = InkhawmInchhiarnaBlogNew.objects.all()
    serializer_class = InkhawmInchhiarnaBlogNewSerializer

    # using below code we can manipulate the data sent cform client and saved the modified value
    # in database
    # def perform_create(self, serializer):
    #     # serializer.save(user= self.request.user)
    #     print("Serializer itself printed: ", serializer)
    #     print("Validated Serializer: ", serializer.validated_data)
    #     mikhual_awmlo = serializer.validated_data.get(
    #         'inkhawm_ni') + " hian chhimtu awm lo"
    #     print(mikhual_awmlo)
    #     mikhual = serializer.validated_data.get('chhimtu1') or None
    #     if mikhual is None:
    #         mikhual = mikhual_awmlo
    #         print("none")
    #     serializer.save(mikhual=mikhual)


InkhawmInchhiarnaBlogNewSerializer_list_create_view = InkhawmInchhiarnaBlogNewListCreateAPIview.as_view()
