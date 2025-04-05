# index.html 网站登陆页面

# first.php 网站登陆后首页

# phpmyadmin

+ 数据库web访问脚本，IP/phpmyadmin进入数据库登录界面

# shell

+ 项目shell脚本

> + diary.sh定时生成PDF格式日志并发送至指定邮箱
> 
> + mysql_backup.sh备份数据库并删除7日前备份数据

# mysql_backup

+ mysql_backup.log    数据库备份日志

+ 以日期为文件夹名的备份文件（db_huapen和db_rekong数据库备份）

# images

+ 网站图标

# diary_css 网站CSS格式

# lib 网站公用库

## class 类

### Table.class.php

> ```php
> class dkTable{
>     protected function showTable();
>     public function showStatus($status);
>     public function quickSelect($quick);
>     public function retrievalResult();
> }
> ```

### Ledger.class.php

> ```php
> class Ledger extends dkTable{
>     public function retrievalBox();//检索栏
>     public function addLedger();
>     public function editLedger($ledgerId);
>     public function lookLedger($ledgerId);
>     public function showStrId($strid)
> }
> ```

### Defect.class.php

> ```php
> class Defect extends dkTable{}
> ```

## fpdf PDF文件生成类

## phpqrcode 二维码生成类

> https://phpqrcode.sourceforge.net
