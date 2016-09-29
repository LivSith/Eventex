from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Lívia Mendes', cpf='12345678901',
                    email='liviasithmendes@gmail.com', phone='11-948583889')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]


    def test_subscrition_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'liviasithmendes@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Lívia Mendes',
                    '12345678901',
                    'liviasithmendes@gmail.com',
                    '11-948583889',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

