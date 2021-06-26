import unittest


class TestStringMethods(unittest.TestCase):

    # setup和tearDown方法是在篾条测试用例前后分别调用的方法
    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    # setUpClass和tearDownClass是在整个类的前后分别调用的方法
    @classmethod
    def setUpClass(cls) -> None:
        print("set up class")


    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown up class")


    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


    def test_equal(self):
        print("断言相等")
        self.assertEqual(1, 1, "判断 1 == 1")


class TestStringMethods2(unittest.TestCase):

    def test_add(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    report_title = '用例执行报告 我的'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = './ExampleReport.html'
    # 执行方法一:执行当前文件所有的unittest测试用例，全部执行
    # unittest.main()

    # 执行方法二：执行指定的测试用例，将要执行的测试用例添加到测试套件里面，批量执行测试方法
    # suite = unittest.TestSuite()
    # suite.addTest(TestStringMethods("test_upper"))
    # suite.addTest(TestStringMethods("test_isupper"))
    # unittest.TextTestRunner().run(suite)

    # 执行方法三：执行某个测试类，将测试类添加到测试套件里面，批量执行测试类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods2)
    suite = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)
    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
    runner.run(testsuite)
