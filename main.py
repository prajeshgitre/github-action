def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any other content.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_args and 'message' in request_args:
        return 'Hello, {}!'.format(request_args['message'])
    elif request_json and 'message' in request_json:
        return 'Hello, {}!'.format(request_json['message'])
    else:
        return 'Hello World!'
