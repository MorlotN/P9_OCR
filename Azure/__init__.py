# Import relevant libraries
import logging
from urllib import request
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    # First, log when the function receive an input HTTP trigger
    logging.info('Python HTTP trigger function processed a request.')

    # Grab the user_id from the request parameters
    # user_id will be used by the recommender model to provide recommendations
    user_id = req.params.get('user_id')
    if not user_id:
        return func.HttpResponse("[ERROR] : User ID not provided !")
    else:
        # The Flask API excepts to have the user_id in the URL
        # So, we append the user_id at the end of the URL
        request_url = "http://nicolasm.pythonanywhere.com/get_recommendation/{}".format(user_id)

        # Create and send a POST request to the API
        req = request.Request(request_url, method="POST")
        r = request.urlopen(req)

        # Receive and decode the response
        content = r.read().decode()

        return func.HttpResponse(content)
