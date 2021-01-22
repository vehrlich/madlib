from django.test import TestCase, Client
from unittest import mock
from httmock import HTTMock, all_requests, response

from libs.glitch.service import GlitchService


class ServiceTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_response_ok(self):
        with mock.patch.object(GlitchService, 'get_all', return_value=('adjective', 'verb', 'noun')):
            response = self.client.get('/madlib/')

        # used template from madlib.views filled with expected values
        template = 'Quite adjective task. I hope that everything verb. If not, noun will be better next time.'

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['detail'], template)

    def test_adjective_endpoint_fails(self):
        @all_requests
        def _mock_requests(url, request):
            if 'adjective' in url.path:
                return response(404, request=request)

        with HTTMock(_mock_requests):
            res = self.client.get('/madlib/')

        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json()['detail'], 'Unable to fetch data')

    def test_verb_endpoint_fails(self):
        @all_requests
        def _mock_requests(url, request):
            if 'verb' in url.path:
                return response(404, request=request)

        with HTTMock(_mock_requests):
            res = self.client.get('/madlib/')

        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json()['detail'], 'Unable to fetch data')

    def test_noun_endpoint_fails(self):
        @all_requests
        def _mock_requests(url, request):
            if 'noun' in url.path:
                return response(404, request=request)

        with HTTMock(_mock_requests):
            res = self.client.get('/madlib/')

        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json()['detail'], 'Unable to fetch data')
