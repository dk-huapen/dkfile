# 1、安装Debian12

## 1.1、磁盘分区

## 2、设置个人偏好

### 1.2.1、设置为多用户（命令行）启动

```shell
sudo systemctl get-default
graphical.target      //图形化界面
sudo systemctl set-default multi-user.targer    //为多用户（命令行）

systemctl isolate multi-user.targer    #启动多用户（命令行）单元
systemctl isolate graphical.targer     #启动图形化界面单元
```

### 1.2.2、设置startx默认启动X Server(Gnome)

```shell
update-alternatives --config x-session-manager
```

## 1.2.3、安装常用软件

+ marktext

+ latex

+ logwatch
  
  > ```shell
  > apt-get install logwatch
  > ```
- fzf 
  
  > ```shell
  > apt-get install fzf               \\命令行搜索工具
  > ```

- screen
  
  > ```shell
  > apt-get install screen             \\全屏窗口管理器
  > ```

### 更新软件源

# 2、搭建LAMP平台

## 2.1、安装mySQL

+ 安装MariaDB
  
  > ```shell
  > sudo apt-get install mariadb-server mariadb-client
  > ```

+ 初始化MariaDB
  
  > ```shell
  > mysql_secure_installation
  > 
  > Enter current password for root (enter for none):
  > #输入当前用户的密码，即空，直接回车
  > 
  > Change the root password? [Y/n] y        #修改密码吗？
  > New password:                        #新密码
  > Re-enter new password:                #再输入一次
  > 
  > Remove anonymous users? [Y/n] y        #移除匿名用户
  >  ... Success!
  > 
  > Disallow root login remotely? [Y/n] n    #禁用root远程,需要远程访问
  > 
  > Remove test database and access to it? [Y/n] y
  > #移除test数据库?
  > 
  > Reload privilege tables now? [Y/n] y
  >     #重新加载
  >  ... Success!
  > ```

+ 数据库常用操作
  
  + 备份数据库
    
    > ```shell
    > mysql -u user
    > mysqldump -u user abc > abc.sql    #备份abc数据库(表结构和表数据)
    > mysqldump -u user -d abc > abc.sql    #备份abc数据库(仅备份表结构)
    > ```
  
  + 恢复数据库
    
    > ```sql
    > > create database abc;    #新建数据库
    > > use abc;                #选择数据库
    > > set names utf8;         #设置数据库编码
    > > source abc.sql          #导入备份的数据库
    > ```

## 2.2、 安装PHP及相关包

### 2.2.1、PHP安装注意事项：必须安装PHP7

+ 安装PHP7
  
  > ```shell
  > sudo apt update
  > sudo apt install software-properties-common ca-certificates lsb-release apt-transport-https
  > sudo sh -c 'echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/php.list'
  > wget -qO - https://packages.sury.org/php/apt.gpg | sudo apt-key add -
  > sudo apt update
  > sudo apt-get install libapache2-mod-php7.4 php7.4 php7.4-gd php7.4-opcache php7.4-mbstring php7.4-xml php7.4-json php7.4-zip php7.4-curl php7.4-imap php7.4-mysql php7.4-fpm
  > ```

+ 切换PHP版本
  
  > ```shell
  > sudo update-alternatives --config php
  > ```

+ 设置上传文件大小限制
  
  > ```shell
  > vim /etc/php/7.4/apache2/php.ini
  > 
  > 
  > upload_max_filessize = 4M #默认为2M
  > ```

## 2.2.2、安装ImageMagick以及imagick PHP扩展

+ 安装依赖库
  
  > ```shell
  > sudo apt-get install build-essential 
  > 
  > sudo apt-get install libjpeg-dev libpng-dev libtiff-dev libgif-dev libwebp-dev 
  > 
  > sudo apt-get install webp
  > 
  > apt-get install libmagickwand-dev
  > ```

+ 源码编译安装ImageMagick
  
  > 官网地址： https://www.imagemagick.org/download/ImageMagick.tar.gz
  > 
  > github下载： https://github.com/ImageMagick/ImageMagick
  > 
  > ```shell
  > wget https://www.imagemagick.org/download/ImageMagick.tar.gz
  > tar xf ImageMagick-xx.tar.xz
  > ./configure --prefix=/usr/local/imagemagick
  > make
  > make install
  > ```

+ imagick扩展地址 https://pecl.php.net/package/imagick
  
  > ```shell
  > wget http://pecl.php.net/get/imagick-3.4.4.tgz
  > tar xf imagick-xx.tgz
  > /usr/local/php/bin/phpize
  > ./configure --with-php-config=/usr/local/php/bin/php-config --with-imagick=/usr/local/imagemagick/
  > make
  > make install
  > ```

# 3.搭建Postfix系统

## 3.1、mailutils

+ 安装mailutils
  
  > ```shell
  > apt-get install mailutils              \\Debian下mail
  > ```

+ 发送带附件的邮件
  
  > ```shell
  > mail -s diary -A 2024-01-02.pdf 18803555056@163.com
  > ```

## 3.2、Postfix

+ 安装Postfix，安装过程中选择**<mark><u>inter选项?</u></mark>**
  
  > ```shell
  > apt-get install postfix              \\安装postfix
  > ```

## 3.3、接收外界邮件？
