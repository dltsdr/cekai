#yield生成器

def fun():
    for i in range(3):
        print(f"i={i}")
        yield  #return 同事相当于暂停并且记住上一次的执行位置
        print('end')

f = fun()
next(f)
next(f)
next(f)