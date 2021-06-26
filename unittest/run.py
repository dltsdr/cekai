import unittest
from HTMLTestRunner.HTMLTestRunner_PY3 import HTMLTestRunner

if __name__ == '__main__':
    report_title = 'Example用例执行报告,我的标题'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = './ExampleReport.html'

    test_dir = './testcase'
    discover = unittest.defaultTestLoader.discover(test_dir,pattern="test_*.py")
with open(report_file, 'wb') as report:
    runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
    runner.run(discover)