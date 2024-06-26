
# 整合常用的shell脚本

**自用**

**replace_token.sh**

token使用xiaoya默认位置：/etc/xiaoya

获取地址：

[mytoken](https://alist.nn.ci/zh/guide/drivers/aliyundrive.html)  
[myopentoken](https://alist.nn.ci/tool/aliyundrive/request.html)  
[temp_transfer_folder_id](https://www.aliyundrive.com/drive/file/resource)  
[转存](https://www.aliyundrive.com/s/rP9gP3h9asE)

一把梭：

~~~bash
wget -N --no-check-certificate https://raw.githubusercontent.com/ZIZNAH/forward/master/replace_token.sh && chmod +x replace_token.sh && bash replace_token.sh
~~~

------------------------------------------------------------------------------------------

**mosdnsv5.yaml**

确保mosdns文件夹已创建：/etc/mosdns

一把梭：
~~~bash
wget -N --no-check-certificate -qO /etc/mosdns/config.yaml https://git.ziznah.net/https://raw.githubusercontent.com/ZIZNAH/forward/master/mosdnsv5.yaml && chmod +x /etc/mosdns/config.yaml
~~~

------------------------------------------------------------------------------------------

**mosdns v5**

确保安装unzip： apt install unzip

1、下载对应版本

~~~bash
wget https://git.ziznah.net/https://github.com/IrineSistiana/mosdns/releases/download/v5.3.1/mosdns-linux-amd64.zip && unzip mosdns-linux-amd64.zip && chmod +x mosdns
~~~

2、运行mosdns（确保config.yaml已经存在）
~~~bash
mosdns start -c config_file -d working_dir​
~~~

3、使用 systemd 来管理 mosdns 服务

	1.安装 systemd

	如果您的 Linux 服务器上尚未安装 systemd，可以使用包管理器如 yum（适用于 CentOS/RHEL）或 apt（适用于 Debian/Ubuntu）来安装它：

	# 使用 yum 安装 systemd（CentOS/RHEL）
	yum install systemd
	# 使用 apt 安装 systemd（Debian/Ubuntu）
	apt install systemd

	2.创建mosdns.service 文件

	使用文本编辑器 (如 vim) 在 /etc/systemd/system 目录下创建一个 mosdns.service 文件，用于配置 mosdns 服务。

	sudo vim /etc/systemd/system/mosdns.service

	写入内容

	[Unit]
	# 服务名称，可自定义
	Description = mosdns server
	After = network.target syslog.target
	Wants = network.target

	[Service]
	Type = simple
	# 启动frps的命令，需修改为您的mosdns的安装路径
	ExecStart = /path/to/mosdns start -c config_file -d working_dir​

	[Install]
	WantedBy = multi-user.target

	3.使用 systemd 命令管理 mosdns 服务

	# 启动mosdns
	sudo systemctl start mosdns
	# 停止mosdns
	sudo systemctl stop mosdns
	# 重启mosdns
	sudo systemctl restart mosdns
	# 查看mosdns状态
	sudo systemctl status mosdns

	4.设置 mosdns 开机自启动

	sudo systemctl enable mosdns




------------------------------------------------------------------------------------------
**感谢并致敬这些作者**
------------------------------------------------------------------------------------------
### **1、socat.sh**

系统要求：支持CentOS 6+ 、Debian 7+、Ubuntu 14+。
脚本说明：脚本默认开启UDP、TCP转发，带开机自启功能，且一次只能转发单个端口，如果想转发多个端口请重复运行本脚本。
提示：该脚本在Vultr各个系统均测试通过，包括最新的Ubuntu 18.04

来源：[Socat一键安装脚本](https://www.moerats.com/archives/621/)

------------------------------------------------------------------------------------------

### **2、cf-v4-ddns.sh**

API key, see https://www.cloudflare.com/a/account/my-account,
这里填写上一步获取的CFKEY
CFKEY=
输入你需要解析用来DDNS解析的根域名 eg: example.com，比如我的域名是123.com，那么此处填写123.com
CFZONE=
登陆CF的Username, eg: user@example.com(即CF的登录邮箱)
CFUSER=
填写用来DDNS解析的二级域名，与上面设置的要一致, eg: ddns.yourdomain.com（例 ddns.123.com）
CFHOST=

下载安装:
~~~
wget -N --no-check-certificate https://raw.githubusercontent.com/ZIZNAH/forward/master/cf-v4-ddns.sh && chmod +x && cf-v4-ddns.sh 
~~~
设置定时任务
~~~
crontab -e
*/2 * * * * /root/cf-v4-ddns.sh >/dev/null 2>&1
~~~
# 如果需要日志，替换上一行代码
~~~
*/2 * * * * /root/cf-v4-ddns.sh >> /var/log/cf-ddns.log 2>&1
~~~
来源：[Cloudflare API v4一键安装脚本](https://github.com/yulewang/cloudflare-api-v4-ddns)

------------------------------------------------------------------------------------------

### **3、brook-pf.sh**

脚本说明: Brook 端口转发 一键安装管理脚本
系统支持: CentOS6+ / Debian6+ / Ubuntu14+

来源：[Brook 端口转发 一键安装管理脚本](https://github.com/ToyoDAdoubiBackup/doubi)

------------------------------------------------------------------------------------------

### **4、iptables-pf.sh**

- 脚本说明: iptables 端口转发 一键安装管理脚本
- 系统支持: CentOS6+ / Debian6+ / Ubuntu14+
- 使用方法: https://doub.io/wlzy-20/

下载安装:
~~~
wget -N --no-check-certificate https://raw.githubusercontent.com/ZIZNAH/forward/master/iptables-pf.sh && chmod +x iptables-pf.sh && bash iptables-pf.sh
~~~
来源：[iptables-pf.sh 一键安装脚本](https://github.com/ToyoDAdoubiBackup/doubi#iptables-pfsh)

------------------------------------------------------------------------------------------

### **5、natcfg.sh**

- 推荐！！！
- 脚本说明: natcfg.sh 端口转发 一键安装管理脚本
- 系统支持: CentOS6+ / Debian6+ / Ubuntu14+
- 使用方法: https://github.com/arloor/iptablesUtils/

下载安装:
~~~
wget --no-check-certificate -qO natcfg.sh https://raw.githubusercontent.com/ZIZNAH/forward/master/natcfg.sh && bash natcfg.sh
~~~
来源：[natcfg.sh 一键安装脚本](https://github.com/arloor/iptablesUtils/)

------------------------------------------------------------------------------------------

### **6、mosdns_geodata_download.sh**

- 推荐！！！
- 脚本说明: mosdns geodata_download
- 系统支持: linux
- 使用方法: https://github.com/xukecheng/scripts/
- 备注:原版添加CDN

下载安装:
~~~
wget https://git.ziznah.net/https://raw.githubusercontent.com/ZIZNAH/forward/master/mosdns_geodata_download.sh -O mosdns_geodata_download.sh && chmod +x mosdns_geodata_download.sh && mosdns_geodata_download.sh
~~~
来源：[mosdns_geodata_download.sh]([https://github.com/arloor/iptablesUtils/](https://raw.githubusercontent.com/xukecheng/scripts/main/mosdns_geodata_download.sh)https://raw.githubusercontent.com/xukecheng/scripts/main/mosdns_geodata_download.sh)
