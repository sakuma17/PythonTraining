"""
from math import pi
from math import floor
"""
#まとめてインポート可能
from math import pi,floor
print('円周率は{}です'.format(pi))
print('小数点以下を切り捨てれば{}です'.format(floor(pi)))

"""
↓math自体はインポートしていないのでエラー
print('小数点以下を切り上げれば{}です'.format(math.ceil(math.pi)))
"""
