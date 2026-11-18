from collections import defaultdict


def series(reads, assignments):
    facts = {}
    totals = defaultdict(set)
    for row in reads:
        dimensions = row['week'], row['article']
        event = row['id']
        if event in facts and dimensions != facts[event]:
            raise ValueError('阅读凭证与不同报道相冲突')
        facts[event] = dimensions
        for subject in assignments.get(row['article'], ()):
            totals[(subject, row['week'])].add(event)
    return [{'topic': key[0], 'week': key[1], 'reads': len(events)} for key,events in sorted(totals.items())]
