import os

batch_size = 1000
lines = []


def process_batch(lines):
    print(lines)

a.
with open('new_location.txt', 'r') as file:
    for i, line in enumerate(file):
        lines.append(line)
        if (i + 1) % batch_size == 0 or i + 1 == os.path.getsize('destination.txt'):
            process_batch(lines)  # 假设这是处理一批数据的函数
            lines = []