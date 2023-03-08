def minMeetingRoom(itervals):
    start = sorted([i.start for i in itervals])
    end = sorted([i.end for i in itervals])

    res, count = 0, 0
    s, e = 0, 0

    while s < len(itervals):
        if start[s] < end[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1
        res = max(res, count)

    return res