import azure.functions as func
import openai_client
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_llm_wrapper")
def http_llm_wrapper(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    query = req.params.get('query')
    
    if query:
        llm_response = openai_client.call_openai_api(query)
        return func.HttpResponse(f"This is the LLM response: {llm_response}", status_code=200)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a query in the query string or in the request body for a personalized response.",
             status_code=200
        )