from django.test import TestCase
from ikeng.core.models.profile import Profile
from ikeng.core.models.subscriber import SubscriberModel
from ikeng.core.admin import ProfileAdmin, SubscriberAdmin
from django.contrib import admin


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


class TestSubcriberModel(TestCase):
    def test_subscriber_should_have_defined_fields(self):
        expected_email = "phumai@odds.team"

        subscriber = SubscriberModel.objects.create(
            email=expected_email
        )

        assert subscriber.email == expected_email


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

    def test_index_view_should_not_see_my_name(self):
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
        response = self.client.get("/test")

        # Then
        assert response.status_code == 404

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


class ProfileTest(TestCase):
    def test_admin_should_be_registered(self):
        self.assertTrue(isinstance(admin.site._registry[Profile], ProfileAdmin))

    def test_admin_should_set_list_display(self):
        expected = (
            'name',
        )
        assert ProfileAdmin.list_display == expected

    def test_admin_should_set_list_search_fields(self):
        expected = [
            'name',
        ]
        assert ProfileAdmin.search_fields == expected


class SubscriberTest(TestCase):
    def test_admin_should_be_registered(self):
        self.assertTrue(isinstance(admin.site._registry[SubscriberModel], SubscriberAdmin))

    def test_admin_should_set_list_display(self):
        expected = (
            'email',
        )
        assert SubscriberAdmin.list_display == expected

    def test_admin_should_set_list_search_fields(self):
        expected = [
            'email',
        ]
        assert SubscriberAdmin.search_fields == expected


class SubscriberAPIViewTest(TestCase):
    def test_view_get_subscriber_should_be_accessible(self):

        response = self.client.get('/subscribers/')

        assert response.status_code == 200

    def test_view_get_subscriber_should_be_return_data(self):
        SubscriberModel.objects.create(email="test@test.com")
        expected = [
            {
                'email': "test@test.com"
            }
        ]

        response = self.client.get('/subscribers/')

        assert response.status_code == 200
        assert response.data == expected

    def test_view_get_subscriber_should_be_return_empty_array_when_not_found_data(self):
        expected = []

        response = self.client.get('/subscribers/')

        assert response.status_code == 200
        assert response.data == expected

    def test_view_post_subscriber_should_be_save_subscriber_email(self):
        expected = {
            "email": "new@test.com"
        }

        response = self.client.post('/subscribers/', data=expected)

        subscriber = SubscriberModel.objects.get(id=1)
        assert response.status_code == 201
        assert response.data == expected
        assert subscriber.email == expected["email"]

    def test_view_post_subscriber_not_should_be_save_subscriber_email_invaild_body(self):
        expected = {
            "emails": "new@test.com"
        }

        response = self.client.post('/subscribers/', data=expected)

        assert response.status_code == 400


class ProfileAPIViewTest(TestCase):
    def test_view_get_profile_should_be_accessible(self):

        response = self.client.get('/profile/')

        assert response.status_code == 200

    def test_view_get_profile_should_be_return_data(self):
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
        expected = {
            "name": "keng",
            "age": 24,
            "birtday": "12/22/11",
            "education": "test",
            "exp": "11",
            "github": "test",
            "github_url": "git-urk",
            "medium": "test_mde",
            "twitter": "test",
        }

        response = self.client.get('/profile/')

        assert response.status_code == 200
        assert response.data["name"] == expected["name"]
        assert response.data["age"] == expected["age"]
        assert response.data["birtday"] == expected["birtday"]
        assert response.data["education"] == expected["education"]
        assert response.data["exp"] == expected["exp"]
        assert response.data["github"] == expected["github"]
        assert response.data["github_url"] == expected["github_url"]
        assert response.data["medium"] == expected["medium"]
        assert response.data["twitter"] == expected["twitter"]

    def test_view_get_profile_should_be_return_empty_array_when_not_found_data(self):
        expected = {
            "name": "",
            "age": None,
            "birtday": "",
            "education": "",
            "exp": "",
            "github": "",
            "github_url": "",
            "medium": "",
            "twitter": "",
        }

        response = self.client.get('/profile/')

        assert response.status_code == 200
        assert response.data == expected

    def test_view_post_should_be_created_new_profile(self):
        expected = {
            "name": "keng",
            "age": 24,
            "birtday": "12/22/11",
            "education": "test",
            "exp": "11",
            "github": "test",
            "github_url": "git-urk",
            "medium": "test_mde",
            "twitter": "test",
        }

        response = self.client.post('/profile/', data=expected)

        profile = Profile.objects.get(id=1)
        assert response.status_code == 201
        assert profile.name == expected["name"]
        assert profile.age == expected["age"]
        assert profile.birtday == expected["birtday"]
        assert profile.education == expected["education"]
        assert profile.exp == expected["exp"]
        assert profile.github == expected["github"]
        assert profile.github_url == expected["github_url"]
        assert profile.medium == expected["medium"]
        assert profile.twitter == expected["twitter"]

    def test_view_post_should_not_be_created_new_profile_because_invaild_body(self):
        expected = {
            "test": "keng",
        }

        response = self.client.post('/profile/', data=expected)

        assert response.status_code == 400
