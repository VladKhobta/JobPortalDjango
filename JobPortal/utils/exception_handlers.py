from rest_framework.views import exception_handler
from copy import deepcopy


def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    print(response)

    if response is None:
        print('foof')
        return response

    if 'phone_number' in response.data:
        data = deepcopy(response.data)
        error_text = data.pop('phone_number')
        data['Phone number'] = error_text
        response.data = data

    if 'email' in response.data:
        data = deepcopy(response.data)
        error_text = data.pop('email')
        data['Email'] = error_text
        response.data = data

    if 'non_field_errors' in response.data:
        data = deepcopy(response.data)
        error_text = data.pop('non_field_errors')
        data['Wrong credentials'] = error_text
        response.data = data

    return response
