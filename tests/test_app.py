import unittest
import re
from app import create_app
from app.main import get_response

class FlaskAppTestCase(unittest.TestCase):

    #Set the app for testing.
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

    #Test if the response is successful.
    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Chatbot', response.data)  

    #Test if the first response from the LLM is valid.
    def test_chat_route_post(self):
        response = self.client.post('/get', data=dict(msg="Hello, chatbot!"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello! How can I assist you today?', response.data)  

    #Test if the response is correctly retrieved from custom data.
    def test_student_visa_cost(self):
        prompt = "What's the cost of a student visa?"

        response = get_response(prompt)

        self.assertIn("490", response)

    #Test if the chatbot correctly only answers about the domain which is UK visas.
    def test_usa_visa_cost(self):
        prompt = "What's the cost of visas in the USA?"

        response = get_response(prompt)

        # Check if the response does not contain any numbers (indicating the bot doesn't know)
        self.assertIsNone(re.search(r'\d+', response))

if __name__ == '__main__':
    unittest.main()
