## 导入模块
python程序可以调用一组基本的函数，这称为“内建函数”，包括print（），imput（）、len（）等。也包括一组模块，称为“标准库”，例如：math、random等。
#### 导入方式一：
- import关键字
- 模块名称
- 可选的多个模块用，隔开
import random
import random，sys，os，math
这种方式调用函数时必须加上模块名称：print（random.randint（））
#### 导入方式二：
from import语句
from关键字后之后是模块名称，import关键字和一个*号：from random import *
使用from形式调用，函数前不需要加模块.前缀，⚠️使用完整名称会让代码更可读，所以最好使用普通形式的import
Python 学习真的很有趣
#一定要坚持学习下去

