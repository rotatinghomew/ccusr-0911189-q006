from collections import defaultdict


def assignments(topics, links):
    known = {row['id'] for row in topics}
    index = defaultdict(set)
    for row in links:
        if row['topic'] not in known:
            raise ValueError('关联引用了未登记专题')
        if row['state'] == 'confirmed':
            index[row['article']].add(row['topic'])
    return index
