端口扫描器
原理:
使用socket进行连接
能连接上认为是端口开放,否则认为端口关闭
源码中
url 表示目标地址
threadCount 最大线程数
扫描完成以后保存文件到result.txt中