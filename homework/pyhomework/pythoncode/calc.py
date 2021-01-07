# 计算器
# 被测文件
class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        try:
            c = a / b
        except IOError:
            print("分母不可为0")
        else:
            return c