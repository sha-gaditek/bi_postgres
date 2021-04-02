import json


class SessionNotInitializedError(Exception):
    def __init__(self, code, message):
        super().__init__(
            json.dumps({
                'code': 'PSQL_S001',
                'message': 'Session not initialized before operation.'
            })
        )
