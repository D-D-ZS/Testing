# 介绍
该工程主要用于作业提交，练习笔记等内容

笔记： NOTE.md

## 作业2
- 补全测试用例【 加减乘除】
- 使用 fixture 装置完成计算机器实例的初始化
- 改造 pytest 的运行规则 ,测试用例命名以 calc_开始，【加， 减 ，乘，除】分别为 calc_add, calc_sub，…
- 自动添加标签(add, sub, mul, div四种)，只运行标签为 add 和 div的测试用例。
- 封装 add, div 测试步骤到 yaml 文件中
涉及到的代码文件：
- src/calc.py 增加减法和乘法 function
- data/sub.yml 减法测试数据
- data/multi.yml 乘法测试数据
- pytest.ini pytest配置文件
- testing/calc_calc.py 符合自定义命名规则的测试模块
- config/steps.yml 执行步骤配置文件（兼测试用例mark文件）
- testing/conftest.py 覆写main.py中的pytest_collection_modifyitems，调整用例执行步骤以及添加标签