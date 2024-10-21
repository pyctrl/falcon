import falcon


def test_with_default_error_handlers():
    app = falcon.App(default_error_handlers=True)

    assert app._error_handlers == {
        Exception: app._python_error_handler,
        falcon.http_error.HTTPError: app._http_error_handler,
        falcon.http_status.HTTPStatus: app._http_status_handler,
    }


def test_without_default_error_handlers():
    app = falcon.App(default_error_handlers=False)

    assert app._error_handlers == {}
