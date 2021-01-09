from django.test import TestCase


class CredsTestCate(TestCase):
    def test_root_url_is_login(self):
        r = self.client.get('/')
        page_content = r.content.decode('utf8')
        self.assertEquals(r.status_code, 200)
        self.assertTemplateUsed('login.html')
        self.assertInHTML('<title>Login</title>', page_content)

    def test_sign_up_page_uses_correct_template(self):
        r = self.client.get('/signup')
        html = r.content
        self.assertEquals(r.status_code, 200)
        self.assertTemplateUsed('signup.html')
        self.assertEqual(html.find('title'), 'Sign Up')

    def test_reset_password_page_setup(self):
        r = self.client.get('/reset-password')
        self.assertEquals(r.status_code, 200)
        self.assertTemplateUsed('reset-passwrd.html')
