from django.test import TestCase
from django.urls import reverse
from .models import menuu, com


class AmericanoViewTest(TestCase):

    def test_americano_page(self):
        # створюємо напій
        item = menuu.objects.create(name="americano")

        # створюємо коментар
        com.objects.create(
            name=item,
            text="test comment"
        )

        # GET-запит
        response = self.client.get(reverse("americano"))

        # 1️⃣ сторінка відкрилась
        self.assertEqual(response.status_code, 200)

        # 2️⃣ правильний шаблон
        self.assertTemplateUsed(
            response,
            "drink/kava/americano.html"
        )

        # 3️⃣ коментар реально є на сторінці
        self.assertContains(response, "test comment")
