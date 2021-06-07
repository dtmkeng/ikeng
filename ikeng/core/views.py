from django.shortcuts import render
from django.views import View
from core.models import Profile
from core.forms import SubscriberForm


# Create your views here.
def index(request):
    return render(request, 'profile.html')


class IndexView(View):
    def get(self, request):
        p = Profile.objects.get(id=1)
        form =  SubscriberForm()
        return render(request, 'profile.html',
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
            }
        )

    def post(self, request):
        form =  SubscriberForm(request.POST)
        p = Profile.objects.get(id=1)
        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data.get('email'))

        return render(request, 'profile.html',
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
            }
        )
