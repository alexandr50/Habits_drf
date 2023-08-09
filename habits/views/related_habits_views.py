from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import RelatedHabit
from habits.serializers.related_habit_serializers import RelatedHabitSerializers, RelatedHabitCreateSerializers
from users.permissions import IsRelatedhabitOwner


class RelatedHabitListView(generics.ListAPIView):
    queryset = RelatedHabit.objects.all()
    serializer_class = RelatedHabitSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return RelatedHabit.objects.filter(habit__owner=self.request.user)


class RelatedHabitCreateView(generics.CreateAPIView):
    queryset = RelatedHabit.objects.all()
    serializer_class = RelatedHabitCreateSerializers
    permission_classes = [IsAuthenticated]


class RelatedHabitUpdateView(generics.UpdateAPIView):
    queryset = RelatedHabit.objects.all()
    serializer_class = RelatedHabitCreateSerializers
    permission_classes = [IsAuthenticated, IsRelatedhabitOwner]


class RelatedHabitDeleteView(generics.DestroyAPIView):
    queryset = RelatedHabit.objects.all()
    permission_classes = [IsAuthenticated, IsRelatedhabitOwner]
