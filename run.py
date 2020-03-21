import unittest
from api_test_framework.lib.HTMLTestReportCN import HTMLTestRunner
from api_test_framework.config.config import *
from api_test_framework.lib.send_email import send_email
import pickle
import sys
from api_test_framework.test.suite.test_suites import *


def discover():  # 发现所有用例
    return unittest.defaultTestLoader.discover(test_case_path)


def save_failures(result, file):  # 从测试结果中找出失败的用例
    suite = unittest.TestSuite()
    for case_result in result.failures:
        suite.addTest(case_result[0])

    with open(file, 'wb') as f:    # 将失败的用例序列化成文件
        pickle.dump(suite, f)


def collect():   # 递归将discover组装的层层嵌套的suite重新组装成一个无嵌套的suite
                 # 即将原来的suite: [suit1(), suite2(case1,case2)..case3] -> suite: [case1, case2,case3]
    suite = unittest.TestSuite()

    def _collect(tests):
        if isinstance(tests, unittest.TestSuite):
            if tests.countTestCases() != 0:
                for i in tests:
                    _collect(i)
        else:
            suite.addTest(tests)

    _collect(discover())
    return suite

# 根据一个用例列表文件组装suite
def makesuite_by_testlist(testlist_file):

    with open(testlist_file) as f:
        testlist = f.readlines()

    testlist = [i.strip() for i in testlist if not i.startswith("#")]

    suite = unittest.TestSuite()
    all_cases = collect()
    for case in all_cases:
        if case._testMethodName in testlist:
            suite.addTest(case)
    return suite

# 根据用例中的tag组装suite
def makesuite_by_tag(tag):
    suite = unittest.TestSuite()
    for case in collect():
        if case._testMethodDoc and tag in case._testMethodDoc:
            suite.addTest(case)

    return suite

# 运行指定suite
def run(suite):
    logging.info("================================== 测试开始 ==================================")

    with open(report_file, 'wb') as f:  # 从配置文件中读取
        result = HTMLTestRunner(stream=f, title="福贝接口自动化测试", description="测试报告", tester="陆庆锋").run(suite)

    if result.failures:
        save_failures(result, last_fails_file)

    if send_email_after_run:
        send_email(report_file)  # 从配置文件中读取
    logging.info("================================== 测试结束 ==================================")

# 只收集用例不允许
def collect_only():
    t0 = time.time()
    i = 0
    for case in collect():
        i += 1
        print("{}.{}".format(str(i), case.id()))
    print("----------------------------------------------------------------------")
    print("Collect {} tests is {:.3f}s".format(str(i),time.time()-t0))


# 运行所有用例
def run_all():
    run(discover())

# 运行suite文件夹下指定名称的suite
def run_suite(suite_name):
    suite = get_suite(suite_name)
    if isinstance(suite, unittest.TestSuite):
        run(suite)
    else:
        print("TestSuite不存在")

# 运行指定列表
def run_by_testlist():
    run(makesuite_by_testlist(testlist_file))

# 运用例行指定tag的
def run_by_tag(tag):
    run(makesuite_by_tag(tag))

# 重跑上次失败的用例
def rerun_fails():
    sys.path.append(test_case_path)
    with open(last_fails_file, 'rb') as f:
        suite = pickle.load(f)
    run(suite)

# 运行总控制入口
def main():
    if options.collect_only:
        collect_only()
    elif options.rerun_fails:
        rerun_fails()
    elif options.testlist:
        run(makesuite_by_testlist(testlist_file))
    elif options.testsuite:
        run_suite(options.testsuite)
    elif options.tag:
        run(makesuite_by_tag(options.tag))
    else:
        run_all()


if __name__ == '__main__':
    main()
