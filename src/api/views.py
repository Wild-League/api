from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import DeckSerializer, UsersSerializer, DeckCardsSerializer
from .models import Deck, Users

class DeckModelViewSet(viewsets.ModelViewSet):
	queryset = Deck.objects.all()
	serializer_class = DeckSerializer

	def retrieve(self, request, pk):
		try:
			deck = Deck.objects.get(pk=pk)
		except Deck.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serialized_deck = DeckCardsSerializer(deck).data
		return Response(data=serialized_deck, status=status.HTTP_200_OK)


class UsersModelViewSet(viewsets.ModelViewSet):
	queryset = Users.objects.all()
	serializer_class = UsersSerializer
