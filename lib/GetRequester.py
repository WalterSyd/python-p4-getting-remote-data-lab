import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url


    def get_response_body(self):
        #send a GET request to the url
        response = requests.get(self.url)
        #return the content of the response
        return response.content


#pass the response body to the load_json function to convert it to a JSON object
    def load_json(self):
        #send a GET request to the url
        response = requests.get(self.url)
        #return the content of the response in an object form
        return json.loads(response.content)