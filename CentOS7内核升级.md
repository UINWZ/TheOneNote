# CentOS7内核升级
#### 1.导入公钥：
rpm —import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org;
#### 2.添加rpm源:
rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-3.el7.elrepo.noarch.rpm
#### 3.安装最新的稳定版内核:
yum —enablerepo=elrepo-kernel install -y kernel-ml;
#### 4.修改默认启动项，修改 GRUB 配置
打开并编辑 /etc/default/grub 并设置 GRUB_DEFAULT=0;

/* GRUB 初始化页面的第一个内核将作为默认内核。*/;

grub2-mkconfig -o /boot/grub2/grub.cfg
#### other：
#### 1.列出可用的内核版本包列表;
yum —disablerepo=”” —enablerepo=”elrepo-kernel” list available
