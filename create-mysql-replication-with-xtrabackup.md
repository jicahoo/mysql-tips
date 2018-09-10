# 环境信息:
  * Ubuntu 16.04.5 LTS (output of lsb_relase -a)
  * Mysql  Ver 14.14 Distrib 5.7.23, for Linux (x86_64) using  EditLine wrapper  (Output of mysql -v)
  * xtrabackup version 2.4.12 based on MySQL server 5.7.19 Linux (x86_64) (revision id: 170eb8c) (xtrabackup --version)
# 提示:
 * 整体步骤参考的这篇文章：https://www.digitalocean.com/community/tutorials/how-to-set-up-master-slave-replication-in-mysql 不同的地方就是，这个文章中做backup用的是sqldump, 我们要用xtrabackup做backup.
 
# 步骤:
1. sudo xtrabackup --backup --user=root --password=123456 --target-dir=backupdir && sudo xtrabackup --prepare --user=root --password=123456 --target-dir=backupdir 

# 
