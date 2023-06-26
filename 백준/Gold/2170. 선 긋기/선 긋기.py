import sys
from operator import attrgetter

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

N = int(sys.stdin.readline())
lines = []

for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    lines.append(Line(start, end))

lines.sort(key=attrgetter('start'))

x = lines[0].start
y = lines[0].end
ans = 0

for i in range(1, N):
    currLine = lines[i]
    if y >= currLine.start:
        y = max(y, currLine.end)
    else:
        ans += y - x
        x = currLine.start
        y = currLine.end

ans += y - x

print(ans)
