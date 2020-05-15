[TOC]
# 介绍
自动化测试练习

# pytest
## 基础使用
- 直接执行pytest，会运行当前目录下 以Test开头的类以及test_\* 或 \*_test格式的function。也可以通过配置文件修改该匹配格式
- 通过 raises 方法断言已知异常。raises详细用法，参考之后章节
- pytest有很多装饰器或方法参数，比如tmpdir, 为每一次测试创建唯一的临时目录
```
def test_needsfiles(tmpdir):
    print(tmpdir)
    assert True
# print的输出
C:\Users\shaun\AppData\Local\Temp\pytest-of-shaun\pytest-0\test_needsfiles0
```
- pytest --fixtures 查看 pytest 有哪些内建函数和常用装饰器

## pytest 参数说明
- pytest --version 查看版本
- pytest --fixtures 查看可用的内建函数和常用的装饰器
- pytest -h | --help 查看帮助信息
- pytest -x 第一次失败后停止运行
- pytest --maxfail=2 第二次失败后停止运行
### 运行指定模块
- pytest test_calc.py 运行当前目录下test_calc.py文件中的用例
### 运行指定目录
- pytest testing/ 运行testing 目录下所有用例
### 运行匹配关键字规则的用例
- pytest -k "TestCalc and not add" 运行符合规则的case，当前这个命令的意思是，运行 TestCalc 类下 除了包含 add 名字的其他所有测试用例，匹配规则可以使用文件名，类名以及方法名。
### 运行指定节点ID的用例
pytest 获取到的每一个test都是有一个 nodeid，由模块文件名后跟类名、函数名和参数化参数等说明符组成，以::字符分隔。
- pytest test_calc.py::TestCalc::test_add 运行test_calc.py文件下TestCalc类下test_add的函数。
### 运行指定mark的用例
通过@pytest.mark.label 可以给函数添加不同的标签，执行时可以使用-m指定需要运行的标签名称
- pytest test_calc.py -m add 运行 add 标签的用例
- pytest test_calc.py -m "not add" 运行 add 标签之外的其他用例
### 运行指定package的用例
- pytest --pyargs testing.test_calc 运行testing包下的test_calc.py模块

## pytest 执行流程

## pytest API 
### Function
#### pytest.approx(expected, rel=None, abs=None, nan_ok=False)
判断两个数字或者两组数字在一定公差内相等。
- expected 期望值
- rel 相对公差（精度）默认 1e-6
- abs 绝对公差（精度）默认 1e-12
- nan_ok 

由于浮点数计算精度问题，直接比较可能会得到意外的结果，比如 
```python
0.1 + 0.2 == 0.3
# 结果
False
```
通过approx方法可以解决这个问题
```python
from pytest import approx
0.1 + 0.2 == approx(0.3)
# 结果
True
```
默认情况下，approx认为其期望值的1e-6(即百万分之一)范围内的数字是相等的。
如果期望值是0.0，那么这种处理将会导致令人惊讶的结果，因为除了0.0本身之外，其他的都比较接近0.0。
为了处理这种情况，approx还认为在1e-12的期望值的绝对公差范围内的数字是相等的。
无穷大和NaN是特殊情况。无穷大只被认为是等于它自己的，而不考虑它的相对容限。
默认情况下，NaN并不等于任何值，但是可以通过将nan_ok参数设置为True使其等于自身。(这是为了方便比较使用NaN表示“无数据”的数组。)

相对公差和绝对公差都可以通过参数调整。
```python
1.0001 == approx(1)
# 结果
False
1.0001 == approx(1, rel=1e-3)
# 结果
True
1.0001 == approx(1, abs=1e-3)
# 结果
True
```
当只设置了abs参数，没有设置rel时，比较时将不会考虑相对公差。如果两个都设置了，则任意一个满足则表示相等
```python
>>> 1 + 1e-8 == approx(1, rel=1e-12)
False
```
#### pytest.fail
使用给定消息显式地使执行测试失败（即使断言的结果是成功的也会失败）。

`fail(msg: str = '', pytrace: bool = True) → NoReturn`
- msg 失败信息内容
- pytrace 如果 False，显示msg失败信息，并且不会报告python traceback
```python
import pytest
def test_demo1(self):
    assert 1 == 1
    pytest.fail(msg="预期失败", pytrace=False)
```

#### pytest.skip
`skip(msg[, allow_module_level=False])`

使用给出的msg信息跳过测试执行。



### Marks

### Fixtures

### Hooks

### Objects

### Special Variables

### Environment Variables

### Exceptions

### Configuration Options


## pytest 测试场景实现

## 使用skip 和 xfail处理确定无法成功的用例
对于一些特殊情况，比如不同系统运行用例，或者其他原因，我们确定测试用例肯定是失败的，
但又不是产品的bug，因此我们不想因为这种情况导致测试结果出现red。对于这种情况可以使用skip跳过用例
或者使用 xfail 预期测试会因为某些原因失败。


## 调整测试用例执行顺序
pytest_collection_modifyitems

## 根据用例名称添加标签
pytest_collection_modifyitems




# allure


# 参考链接
pytest: https://docs.pytest.org/en/latest/contents.html

allure: http://allure.qatools.ru/