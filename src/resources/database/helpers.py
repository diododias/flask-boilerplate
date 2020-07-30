from uuid import UUID


def validate_uuid(uuid):
    try:
        uuid_obj = UUID(uuid, version=4)
        if uuid_obj:
            return True
        else:
            return False
    except ValueError:
        return False
