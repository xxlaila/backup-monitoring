1、脚本存放目录
/usr/lib/zabbix/alertscripts，脚本的权限是zabbix 账户，具有可执行权限
2、重要参数介绍：
toparty："2" 这个参数是在企业微信里面部门的id
Corpid：企业的CorpID标示
Secret：管理组的密钥凭证
Agentid：新建应用的id
只需要求修改以上参数即可
![image]()
以上部门没有新建，只是在这个应用中新增加了几个用户。最好的方式是增加一个部门组，用户添加到部门组里面，这种方式最科学
3、登陆zabbix 进行配置
3.1、创建一个媒介类型
![image]()
3.2、创建一个告警类别
![image]()
![image]()
服务器:{HOST.NAME}发生: {TRIGGER.NAME}故障!

告警主机:{HOST.NAME}
告警地址:{HOST.IP}
监控项目:{ITEM.NAME}
监控取值:{ITEM.LASTVALUE}
告警等级:{TRIGGER.SEVERITY}
当前状态:{TRIGGER.STATUS}
告警信息:{TRIGGER.NAME}
告警时间:{EVENT.DATE} {EVENT.TIME}
事件ID:{EVENT.ID}
![image]()
服务器:{HOST.NAME}: {TRIGGER.NAME}已恢复!

告警主机:{HOST.NAME}
告警地址:{HOST.IP}
监控项目:{ITEM.NAME}
监控取值:{ITEM.LASTVALUE}
告警等级:{TRIGGER.SEVERITY}
当前状态:{TRIGGER.STATUS}
告警信息:{TRIGGER.NAME}
告警时间:{EVENT.DATE} {EVENT.TIME}
恢复时间:{EVENT.RECOVERY.DATE} {EVENT.RECOVERY.TIME}
持续时间:{EVENT.AGE}
事件ID:{EVENT.ID}
![image]()
服务器:{HOST.NAME}: 报警确认

确认人:{USER.FULLNAME} 
时间:{ACK.DATE} {ACK.TIME} 
确认信息如下:
"{ACK.MESSAGE}"
问题服务器IP:{HOSTNAME1}
问题ID:{EVENT.ID}
当前的问题是: {TRIGGER.NAME}
3.3、为用户添加告警类型
![image]()
这里为admin用户添加的 告警方式。注意一下send to 这个参数，这里一定要是@all。否则不成功
4、企业微信测试
![image]()
