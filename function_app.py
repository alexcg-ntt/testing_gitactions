import azure.functions as func
import logging
import os
#from openai_access import try_openai

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="test_githubactions_func")
def test_githubactions_func(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    #app_setting_test = os.getenv("my_test_app_setting")
    subscription_key = os.getenv("OpenAIAPIKey")
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        #answer = try_openai(str(subscription_key))
        return func.HttpResponse(
             "Back to previous version. Subscription key: " + str(subscription_key),
             status_code=200
        )