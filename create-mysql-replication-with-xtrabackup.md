# 环境信息:
  * Ubuntu 16.04.5 LTS (output of lsb_relase -a)
  * Mysql  Ver 14.14 Distrib 5.7.23, for Linux (x86_64) using  EditLine wrapper  (Output of mysql -v)
  * xtrabackup version 2.4.12 based on MySQL server 5.7.19 Linux (x86_64) (revision id: 170eb8c) (xtrabackup --version)
# 提示:
 * 整体步骤参考的这篇文章：https://www.digitalocean.com/community/tutorials/how-to-set-up-master-slave-replication-in-mysql 不同的地方就是，这个文章中做backup用的是sqldump, 我们要用xtrabackup做backup.
 
# 步骤:
* 整个操作分两个部分，一个部分就是备份，将主数据库的数据备份，并恢复到从数据库；第二个部分，就是在主数据库和从数据库之间，建立复制会话。
## 第一部分，备份主数据库，并恢复到从数据库
1. 为了主从之间能够远程复制， 在备份主数据库之前，要更改一些配置（如果已经满足这些配置要求，则不需做任何改动。）
```
bind-address            = 0.0.0.0                          # Make sure slave can connect the sql service via TCP/IP. 
server-id               = 1                                # uniq id
log_bin                 = /var/log/mysql/mysql-bin.log     # Enable the bin log. Replication needs it
binlog_do_db            = newdatabase                      # The database you want to sync
```
* 配置改好后，需要重启mysql:`sudo service mysql restart`

2. 备份主数据库
第一条命令的输出可能是不一致的数据, 以，需要第二条的命令，确保数据一致性。 backupdir是个用户指定的目录.
* sudo xtrabackup --backup --user=root --password=123456 --target-dir=backupdir
* sudo xtrabackup --prepare --user=root --password=123456 --target-dir=backupdir
备份的目录中, xtrabackup_info文件包含一些重要信息，在配置远程复制的过程中，需要用到，如下：

```
>sudo cat /var/lib/mysql/xtrabackup_info
...
mysql-bin.000003', position '154'             <<<<注意这条信息
...
```

3. 将数据恢复到从数据库:
* 想办法将主数据库导出的文件夹backupdir， 复制到从数据库的服务器上。下文中，我们假设，已经复制到目录:/home/ubuntu/backupdir
* 停止从数据库的mysql服务: `sudo service mysql stop`
* 创建出一个空的datadir，以便恢复数据，具体方法是:
 * `sudo mv /var/lib/mysql /var/lib/mysql.bak`
 * `sudo mkdir /var/lib/mysql`
* 使用xtrabackup恢复到datadir: /var/lib/mysql. 命令如下：
 * `sudo xtrabackup --copy-back --target-dir=/home/ubuntu/backupdir`
 * `sudo chown -R mysql:mysql /var/lib/mysql`





