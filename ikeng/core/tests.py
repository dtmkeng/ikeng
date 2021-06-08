from django.test import TestCase
from core.models.profile import Profile
from core.models.subscriber import SubscriberModel


class TestProfile(TestCase):
    def test_profile_should_have_defined_fields(self):
        profile = Profile.objects.create(
            name="keng",
            age=24,
            birtday="12/22/11",
            education="test",
            exp="11",
            github="test",
            github_url="git-urk",
            medium="test_mde",
            twitter="test",
        )

        assert profile.name == "keng"
        assert profile.age == 24
        assert profile.birtday == "12/22/11"
        assert profile.education == "test"
        assert profile.exp == "11"
        assert profile.github == "test"
        assert profile.github_url == "git-urk"
        assert profile.medium == "test_mde"
        assert profile.twitter == "test"


class TestIndexView(TestCase):
    def test_index_view_should_see_my_name(self):
        # Given
        Profile.objects.create(
            name="keng",
            age=24,
            birtday="12/22/11",
            education="test",
            exp="11",
            github="test",
            github_url="git-urk",
            medium="test_mde",
            twitter="test",
        )
        # When
        response = self.client.get("/")

        # Then
        assert response.status_code == 200
        assert "keng" in str(response.content)

    def test_index_view_should_save_subcriber_email_when_submit_input_form(self):
        Profile.objects.create(
            name="keng",
            age=24,
            birtday="12/22/11",
            education="test",
            exp="11",
            github="test",
            github_url="git-urk",
            medium="test_mde",
            twitter="test",
        )
        data = {"email": "keng@odds.team"}
        # When
        response = self.client.post("/", data=data)

        # then

        subscriber = SubscriberModel.objects.get(id=1)
        assert response.status_code == 200
        assert subscriber.email == "keng@odds.team"
