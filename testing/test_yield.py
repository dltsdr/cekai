#yield生成器

def fun():
    for i in range(3):
        print(f"i = {i}")
        #yield
        print('end')

f = fun()
next(f)
next(f)
next(f)