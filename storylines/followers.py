from collections import defaultdict


def audience(subscriptions):
    channels = defaultdict(set)
    for row in subscriptions:
        if row['state'] == 'active':
            channels[row['topic']].add(row['person'])
    return {topic: sorted(people) for topic,people in sorted(channels.items())}
