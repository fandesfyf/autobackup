# autobackup
一个用python写的自动备份文件的小工具,在写毕业论文的时候害怕丢档,因此写了这个工具检测到文件更改时自动备份,还有保存历史记录的作用.

# 用法
有python环境的可以直接用
```
python autobackup.py [任何目录下的文件名]
```
进行启动

没有python环境的window小伙伴可以直接使用我打包好的exe程序,可以exe的路径放在环境变量里面(这种教程百度谷歌一下就有一大堆),或者放在要备份文件相同目录,然后在资源管理器备份文件目录按住shift右键打开powershell(当然也可以打开cmd手动cd到该目录),将要备份的文件名作为输入即可,其实无需放在相同目录也可以对其他目录的文件进行自动备份
```
 .\autobackup.exe [xx路径/文件名]
```

# 依赖
文件更改检测依赖watchdog包`pip install watchdog`即可
