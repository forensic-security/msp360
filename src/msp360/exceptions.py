from uuid import UUID

class Msp360Exception(Exception): ...


class ClientError(Msp360Exception): ...


class ResourceNotFound(ClientError): ...


# TODO: leverage messages in responses
def check_uuid(value: str, not_found=True, msg=None):
    '''Checks the value is a valid UUID if a resource was not found.
    '''
    try:
        UUID(value)
    except ValueError:
        raise ValueError(value) from None
    if not_found:
        raise ResourceNotFound(msg or value) from None
    else:
        raise ClientError(msg or value) from None
