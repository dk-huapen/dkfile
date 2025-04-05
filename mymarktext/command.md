# screen

> ```shell
> screen -S session_name    #创建新视窗
> screen -ls                #查看已经创建过的视窗
> screen -r session_name    #恢复session_name s视窗
> screen -d session_name    #将指定视窗离线也可以按下Ctrl+a然后按下d
> ```

# rsync

> ```shell
> rsync file debian_ibm@192.168.1.16:/var/www/html/data/upload_file/tmp/
> 
> rsync -r filedir debian_ibm@192.168.1.16:/var/www/html/data/upload_file/tmp/
> ```

# ssh

> ```shell
> ssh debian_ibm@192.168.1.16 -p 22
> ssh debian_ibm@1dklovelich.iok.la -p 18210
> ```

# latexmk
