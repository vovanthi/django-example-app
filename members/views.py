import django_filters
from rest_framework import viewsets, filters, generics

from .models import Members
from .serializer import MembersSerializer

# Create your views here.
class MemberViewSet(viewsets.ModelViewSet):
    """
    Member Modelに紐づくViewsets
    """
    serializer_class = MembersSerializer
    queryset = Members.objects.all()
    # filter_backends = (filters.SearchFilter,)
    search_fields = ('member_id', 'member_name', 'joined_at')

class MemberListViewSet(generics.ListAPIView):
    serializer_class = MembersSerializer
    model = serializer_class.Meta.model
    def get_queryset(self):
        member_id = self.kwargs['member_id']
        queryset = self.model.objects.filter(member_id=member_id)
        return queryset
