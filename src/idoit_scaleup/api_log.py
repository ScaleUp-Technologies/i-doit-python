

class IDoitApiLog:
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls.log = []
            cls.do_log = False
            # Put any initialization here.
        return cls._instance

    def turn_on(cls):
        cls.do_log = True

    def append_api_log(cls, url: str, payload, response):
        if cls.do_log:
            cls.log.append({
                'url': url,
                'payload': payload,
                'response': response
            })

    def get_api_log(cls):
        return cls.log
