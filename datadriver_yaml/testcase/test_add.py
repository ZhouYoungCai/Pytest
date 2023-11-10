import pytest

from testing.datadriver_yaml.func.operation import my_add

# 用到 yaml文件中的数据时，就需要读取出来

# pip install pyyaml
# 文件或者目录 不可以创建为yaml, 关键字  yaml_demo yaml_aaa
import yaml
def get_data():
  # 如果yaml文件中有中文 ，必须要加上encoding="utf-8"
  with open("../datas/data.yaml",encoding="utf-8") as f :
    data = yaml.safe_load(f)
  return data

def test_get_data():
  print(get_data())



class TestWithYAML:
  @pytest.mark.parametrize('x,y,expected', get_data())
  def test_add(self, x, y, expected):
    assert my_add(int(x), int(y)) == int(expected)
