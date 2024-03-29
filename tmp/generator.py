def consumer():
    r = ''
    while True:
        print(r,'---------------------')
        s = yield r
        print(s,'+++++++++++++++++++++')
        if not s:
            return
        print('[CONSUMER] Consuming %s...' % s)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print(r,'*********************')
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)