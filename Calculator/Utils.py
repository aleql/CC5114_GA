
bin8 = lambda x: ''.join(reversed([str((x >> i) & 1) for i in range(8)]))
int8 = lambda x: int(x, 2)
