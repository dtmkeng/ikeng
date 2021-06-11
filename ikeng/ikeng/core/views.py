from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework import status
from core.models.profile import Profile
from core.forms import SubscriberForm
from core.models.subscriber import SubscriberModel
from core.serializers import SubscriberSerializer
from rest_framework.response import Response


# Create your views here.
def index(request):
    return render(request, "profile.html")


class IndexView(View):
    def get(self, request):
        p = Profile.objects.get(id=1)
        form = SubscriberForm()
        return render(
            request,
            "profile.html",
            {
                "name": p.name,
                "form": form,
                "age": p.age,
                "birtday": p.birtday,
                "education": p.education,
                "exp": p.exp,
                "github": p.github,
                "github_url": p.github_url,
                "medium": p.medium,
                "twitter": p.twitter,
            },
        )

    def post(self, request):
        form = SubscriberForm(request.POST)
        p = Profile.objects.get(id=1)
        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data.get("email"))
            email = form.cleaned_data.get("email")
            SubscriberModel.objects.create(email=email)
            form = SubscriberForm()

        return render(
            request,
            "profile.html",
            {
                "name": p.name,
                "form": form,
                "age": p.age,
                "birtday": p.birtday,
                "education": p.education,
                "exp": p.exp,
                "github": p.github,
                "github_url": p.github_url,
                "medium": p.medium,
                "twitter": p.twitter,
            },
        )


# list email subscriber
class SubscriberAPIView(APIView):
    def get(self, request):
        subscriber = SubscriberModel.objects.all()
        serializer = SubscriberSerializer(subscriber, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubscriberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
