# 介绍
自动化测试练习

# pytest + allure
## pytest
### 基础使用
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

### pytest 参数说明
- pytest --version 查看版本
- pytest --fixtures 查看可用的内建函数和常用的装饰器
- pytest -h | --help 查看帮助信息
- pytest -x 第一次失败后停止运行
- pytest --maxfail=2 第二次失败后停止运行
#### 运行指定模块
- pytest test_calc.py 运行当前目录下test_calc.py文件中的用例
#### 运行指定目录
- pytest testing/ 运行testing 目录下所有用例
#### 运行匹配关键字规则的用例
- pytest -k "TestCalc and not add" 运行符合规则的case，当前这个命令的意思是，运行 TestCalc 类下 除了包含 add 名字的其他所有测试用例，匹配规则可以使用文件名，类名以及方法名。
#### 运行指定节点ID的用例
pytest 获取到的每一个test都是有一个 nodeid，由模块文件名后跟类名、函数名和参数化参数等说明符组成，以::字符分隔。
- pytest test_calc.py::TestCalc::test_add 运行test_calc.py文件下TestCalc类下test_add的函数。
#### 运行指定mark的用例
通过@pytest.mark.label 可以给函数添加不同的标签，执行时可以使用-m指定需要运行的标签名称
- pytest test_calc.py -m add 运行 add 标签的用例
- pytest test_calc.py -m "not add" 运行 add 标签之外的其他用例
#### 运行指定package的用例
- pytest --pyargs testing.test_calc 运行testing包下的test_calc.py模块

### raises
raises使用有两种方式，一种直接使用，另一种通过 pytest.mark.parametrize，适用于一些用例引起异常，一些不会引起异常。

### 装饰器 
@pytest.fixture()

### conftest
### yield

yield + 函数 == 生成器


### 参数化 
- @pytest.mark.parametrize()
- yaml

使用 @pytest.mark.parametrize() 传入参数 yaml 定义的参数

### 用例添加模块标记
可通过复写pytest的源码中的方法，获取全部用例list，然后遍历用例进行统一添加标签操作



### 用例排序 pytest-order

### pytest配置文件pytest.ini
全局配置

通过pytest配置文件，将一些固化的内容添加到配置文件中，比如运行命令参数

## allure


# 参考链接
pytest: https://docs.pytest.org/en/latest/contents.html

allure: http://allure.qatools.ru/