# schedulept.py
# 拉取pt平台流水
import sys

sys.path.append('opt')  #引入opt 目录下的所有py文件
import config

print(config.DATABASE_CONFIG['host'])

print(config.GAME_PT2_CONFIG['SourceUrl'])

print(config.GAME_PT_CONFIG['SourceUrl'])

