```
更新时间: 2024-06-16 00:25:07  

DNS拦截规则数量: 70860 
Filters规则数量: 170563 
合并规则数量: 241423 

DNS检测已失效域名: 26551 
```
<h1 align='center'>AdBlock Filters</h1> 

## 📣规则说明
1. 合并优质上游规则并去重整理排列。
2. 使用两组国内、两组国外 DNS 服务，分别对上游各规则源拦截的域名进行解析，去除已无法解析的域名。（上游各规则源中存在大量已无法解析的域名，无需加入拦截规则）
3. 本项目仅对上游规则进行合并、去重、去除无效域名，添加少量其他规则。如发现误拦截情况，可临时添加放行规则（如 `@@||www.example.com^$important`），并向上游规则反馈。

4. 手机推荐使用 [halflife-list](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/sbwml/halflife-list/master/ad.txt&title=halflife-list) + [ADgk](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/banbendalao/ADgk/master/ADgk.txt&title=ADgk) （点击直接导入）
## 🎯订阅链接
|    项目    |                             github                              |                           ghproxy                            |
| :-------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|    白名单     | [原始链接](https://raw.githubusercontent.com/Sereinfy/Adrules/main/rule/allow.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adrules/main/rule/allow.txt) |
|   DNS规则    | [原始链接](https://raw.githubusercontent.com/Sereinfy/Adrules/main/rule/adblockdns.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adrules/main/rule/adblockdns.txt) |
|   Filters规则    | [原始链接](https://raw.githubusercontent.com/Sereinfy/Adrules/main/rule/adblockfilters.txt) |[加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adrules/main/rule/adblockfilters.txt) |
|   合并使用    | [原始链接](https://raw.githubusercontent.com/Sereinfy/Adrules/main/rule/rules.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adrules/main/rule/rules.txt) |
## 🆓上游规则

| 规则 | 类型 | 原始链接 | 加速链接 | 更新日期 |
|:-|:-|:-|:-|:-|
| AdGuard Base filters | filter | [原始链接](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_2_Base/filter.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adrules/main/filters/AdGuard_Base_filters.txt) | 2024/06/16 |
| AdGuard Chinese filters | filter | [原始链接](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_224_Chinese/filter.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adrules/main/filters/AdGuard_Chinese_filters.txt) | 2024/06/16 |
| AdGuard Annoyances filter | filter | [原始链接](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_14_Annoyances/filter.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adrules/main/filters/AdGuard_Annoyances_filter.txt) | 2024/06/16 |
| EasyList China | filter | [原始链接](https://easylist-downloads.adblockplus.org/easylistchina.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adrules/main/filters/EasyList_China.txt) | 2024/06/16 |
| EasyPrivacy | filter | [原始链接](https://easylist-downloads.adblockplus.org/easyprivacy.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adrules/main/filters/EasyPrivacy.txt) | 2024/06/16 |
| Fanboy's Annoyance List | filter | [原始链接](https://easylist.to/easylist/fanboy-social.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adrules/main/filters/Fanboy's_Annoyance_List.txt) | 2024/06/16 |
| CJX's Annoyance List | filter | [原始链接](https://raw.githubusercontent.com/cjx82630/cjxlist/master/cjx-annoyance.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adrules/main/filters/CJX's_Annoyance_List.txt) | 2024/04/24 |
| NoAppDownload | filter | [原始链接](https://raw.githubusercontent.com/Noyllopa/NoAppDownload/master/NoAppDownload.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adrules/main/filters/NoAppDownload.txt) | 2024/05/10 |
| Adblock Warning Removal List | filter | [原始链接](https://easylist-downloads.adblockplus.org/antiadblockfilters.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adrules/main/filters/Adblock_Warning_Removal_List.txt) | 2024/06/16 |
| damengzhu | filter | [原始链接](https://raw.githubusercontent.com/damengzhu/banad/main/jiekouAD.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adrules/main/filters/damengzhu.txt) | 2024/06/10 |
| xinggsf mv | filter | [原始链接](https://raw.githubusercontent.com/xinggsf/Adblock-Plus-Rule/master/mv.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adrules/main/filters/xinggsf_mv.txt) | 2024/06/14 |
| xinggsf rule | filter | [原始链接](https://raw.githubusercontent.com/xinggsf/Adblock-Plus-Rule/master/rule.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adrules/main/filters/xinggsf_rule.txt) | 2024/05/17 |
| SmartTV Blocklist | dns | [原始链接](https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV-AGH.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adrules/main/filters/SmartTV_Blocklist.txt) | 2024/02/15 |
| AWAvenue Ads Rule | dns | [原始链接](https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adrules/main/filters/AWAvenue_Ads_Rule.txt) | 2024/06/04 |
| Urlhaus Malicious URL Blocklist | dns | [原始链接](https://malware-filter.gitlab.io/malware-filter/urlhaus-filter-agh-online.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adrules/main/filters/Urlhaus_Malicious_URL_Blocklist.txt) | 2024/06/16 |
| Nocoin list | host | [原始链接](https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adrules/main/filters/Nocoin_list.txt) | 2024/02/15 |
| 1024 hosts | host | [原始链接](https://raw.githubusercontent.com/Goooler/1024_hosts/master/hosts) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adrules/main/filters/1024_hosts.txt) | 2024/02/15 |
| ad-wars hosts | host | [原始链接](https://raw.githubusercontent.com/jdlingyu/ad-wars/master/hosts) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adrules/main/filters/ad-wars_hosts.txt) | 2024/02/15 |

## 🆙上游源码
https://github.com/8680/GOODBYEADS 

https://github.com/217heidai/adblockfilters 

https://github.com/fordes123/ad-filters-subscriber 
