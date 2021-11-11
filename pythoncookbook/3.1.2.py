from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=5)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)
