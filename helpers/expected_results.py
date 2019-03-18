class ApiKeyResponse:
    wrong_key = {'error_message': 'The provided API key is invalid.',
                 'html_attributions': [],
                 'results': [],
                 'status': 'REQUEST_DENIED'}
    missing_key = {'error_message': 'You must use an API key to authenticate each request to Google Maps Platform APIs.'
                                    ' For additional information, please refer to http://g.co/dev/maps-no-account',
                   'html_attributions': [],
                   'results': [],
                   'status': 'REQUEST_DENIED'}
