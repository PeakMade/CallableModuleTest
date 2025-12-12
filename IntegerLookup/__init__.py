import logging
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    # Hardcoded lookup dictionary
    lookup_map = {
        1: "Cat",
        2: "Dog",
        3: "Unicorn"
    }
    
    # Get the 'value' parameter from query string
    value_param = req.params.get('value')
    
    if not value_param:
        return func.HttpResponse(
            json.dumps({"error": "Please provide a 'value' parameter in the query string"}),
            mimetype="application/json",
            status_code=200
        )
    
    # Validate that the input is an integer
    try:
        input_value = int(value_param)
    except ValueError:
        return func.HttpResponse(
            json.dumps({"error": f"Invalid input: '{value_param}' is not a valid integer"}),
            mimetype="application/json",
            status_code=200
        )
    
    # Look up the value in the dictionary
    if input_value in lookup_map:
        result = lookup_map[input_value]
        return func.HttpResponse(
            json.dumps({"result": result}),
            mimetype="application/json",
            status_code=200
        )
    else:
        return func.HttpResponse(
            json.dumps({"error": f"No value found for input value {input_value}"}),
            mimetype="application/json",
            status_code=200
        )
