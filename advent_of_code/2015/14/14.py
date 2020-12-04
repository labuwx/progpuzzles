#!/usr/bin/env python3


def run_for(deer, time):
    round_time = deer['runtime'] + deer['resttime']
    num_whole_runs = time // round_time
    partial_run_time = min(deer['runtime'], time - num_whole_runs * round_time)
    distance = (num_whole_runs * deer['runtime'] + partial_run_time) * deer['speed']
    return distance


def race_for(deers, time):
    state = {
        name: {'dist': 0, 'score': 0, 'running': 1, 'switcht': speed['runtime']}
        for name, speed in deers.items()
    }
    for t in range(1, time + 1):
        dist_max = 0
        for name, st in state.items():
            deer = deers[name]
            st['dist'] += st['running'] * deer['speed']
            dist_max = max(dist_max, st['dist'])
            if t == st['switcht']:
                st['switcht'] = t + (
                    deer['resttime'] if st['running'] else deer['runtime']
                )
                st['running'] = (st['running'] + 1) % 2
        for st in state.values():
            st['score'] += st['dist'] == dist_max

    return state


def main():
    input = open('input').read().strip().split('\n')
    test_time = 2503

    speeds = {
        ls[0]: {'speed': int(ls[3]), 'runtime': int(ls[6]), 'resttime': int(ls[13])}
        for l in input
        for ls in [l.split()]
    }

    results = race_for(speeds, test_time)

    s1 = max(run_for(deer, test_time) for deer in speeds.values())
    s1_alt = max(deer['dist'] for deer in results.values())
    assert s1 == s1_alt

    s2 = max(deer['score'] for deer in results.values())

    print(s1)
    print(s2)


main()
