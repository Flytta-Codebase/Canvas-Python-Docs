from chalice import Chalice

app = Chalice(app_name='sedna-hello-world-app')

@app.route('/', methods=['POST'], content_types=['application/json'])
def handle_canvas_request():
    """
    Handles incoming requests from Sedna Canvas.
    For this simple app, it always returns a "Hello World" panel.
    """
    # request_data = app.current_request.json_body # You can access the request data if needed

    # Construct the response based on response.schema.json
    response_payload = {
        "surfaces": [
            {
                "type": "panel",
                "id": "hello_world_panel", # A unique ID for your panel
                "blocks": [
                    {
                        "type": "section",
                        "elements": [
                            {
                                "type": "text",
                                "content": "Hello World" # The text to display
                            }
                        ]
                    }
                ]
            }
        ]
    }
    return response_payload

# To test locally, run: chalice local
# You would then send a POST request (e.g., with an empty JSON body {} or a mock Sedna request)
# to http://127.0.0.1:8000/ 