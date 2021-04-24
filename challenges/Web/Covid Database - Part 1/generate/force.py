from multiprocessing import Process, freeze_support
import jwt
import string
import itertools


def test(token, secret: str):
    try:
        jwt.decode(token, secret, algorithms=['HS256'])
        print(secret)
    except:
        pass
    
    return secret

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MTkxNTkyNjMuMTgyNTQzLCJpYXQiOjE2MTkxNTkxNjMuMTgyNTQzLCJ1c2VyX2lkIjoiODQ2NDAyNzMifQ.lFH2AOkGr7Z8D5ZuUVj5I7goy2fG79gq9u24dhzJc-E"
letters = string.ascii_lowercase
count = 6
tried = 0

# executor = ThreadPoolExecutor(max_workers=10000)

# tried = 0

# def done(result):
#     global tried
#     tried += 1
#     if tried % 100000 == 0:
#         print(tried, result.result())

# for i in range(1, count + 1):
#     for secret in itertools.product(letters, repeat=i):
#         future = executor.submit(test, token, ''.join(secret))
#         future.add_done_callback(done)

# executor.shutdown()

def do(i):
    global tried
    for secret in itertools.product(letters, repeat=i):
        test(token, ''.join(secret))
        tried += 1
        if tried % 100000 == 0:
            print(tried)

processes = []

if __name__ == "__main__":
    for i in range(1, count + 1):
        p = Process(target=do, args=(i,))
        p.start()
        processes.append(p)

# for p in processes:
#     p.join()