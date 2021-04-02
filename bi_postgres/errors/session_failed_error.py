import json


class SessionFailedError(Exception):
    def __init__(self, code, message):
        super().__init__(
            json.dumps({
                'code': 'PSQL_S002',
                'message': 'Session failed.'
            })
        )
