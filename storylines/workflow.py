from .circulation import series
from .desk import assignments
from .followers import audience


def report(data):
    return {'series':series(data['reads'],assignments(data['topics'],data['links'])),
            'audience':audience(data['subscriptions'])}
