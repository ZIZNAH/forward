**mosdns**
mosdns.yaml

参考大佬(原文)[https://dev.leiyanhui.com/route/mosdns-all-in-one/]

###准备工作###

~~~shell
cd /opt/mosdns/
wget  https://git.ziznah.net/https://raw.githubusercontent.com/IceCodeNew/4Share/master/geoip_china/china_ip_list.txt -O geoip_cn.txt
wget  https://git.ziznah.net/https://raw.githubusercontent.com/Loyalsoldier/v2ray-rules-dat/release/reject-list.txt -O geosite_category-ads-all.txt
wget  https://git.ziznah.net/https://raw.githubusercontent.com/Loyalsoldier/v2ray-rules-dat/release/proxy-list.txt -O 'geosite_geolocation-!cn.txt'
wget  https://git.ziznah.net/https://raw.githubusercontent.com/Loyalsoldier/v2ray-rules-dat/release/direct-list.txt -O geosite_cn.txt
echo "localhost 127.0.0.1"> /opt/mosdns/hosts.txt #注意格式和系统的hosts文件不一样
wget https://www.cloudflare.com/ips-v4 -O cf4.txt #cf ip地址
wget https://www.cloudflare.com/ips-v6 -O cf6.txt
cat cf4.txt  <(echo)  cf6.txt >geoip_cloudflare.txt  #合并
~~~

这里'geosite_geolocation-!cn.txt'加了引号，linux下!识别成bash脚本了

后面直接看配置即可 大佬都贴心上了注释
