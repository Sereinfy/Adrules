``` 
更新时间: 2024-11-13 16:12:58 （北京时间） 
插件拦截规则数量: 175281 
DNS拦截规则数量: 45809 
``` 
适用于AdGuard的去广告合并规则，每8个小时更新一次。
个人收藏了不少广告过滤规则，但是每次往新设备添加的时候很是头疼，于是写了这个项目，定时自动获取各规则源更新，生成合并规则库。

## 说明
1. 定时从上游各规则源获取更新，合并去重。
2. 使用国内、国外各 3 组 DNS 服务，分别对上游各规则源拦截的域名进行解析，去除已无法解析的域名。（上游各规则源中存在大量已无法解析的域名，无需加入拦截规则）
3. 本项目仅对上游规则进行合并、去重、去除无效域名，不做任何修改。如发现误拦截情况，可临时添加放行规则（如 `@@||www.example.com^$important`），并向上游规则反馈。
4. 手机推荐使用 [halflife-list](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/sbwml/halflife-list/master/ad.txt&title=halflife-list) + [ADgk](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/banbendalao/ADgk/master/ADgk.txt&title=ADgk) （点击直接导入）

## 订阅链接
1. AdGuard Home 等DNS拦截服务使用规则1
2. AdGuard 等浏览器插件使用规则1 + 规则2

| 规则 | 原始链接 | 加速链接 |
|:-|:-|:-|
| 规则1：DNS 拦截 | [原始链接](https://raw.githubusercontent.com/Sereinfy/Adblock/main/rules/adblockdns.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adblock/main/rules/adblockdns.txt) |
| 规则2：插件拦截 | [原始链接](https://raw.githubusercontent.com/Sereinfy/Adblock/main/rules/adblockfilters.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adblock/main/rules/adblockfilters.txt) |

## 上游规则源
1. 感谢各位广告过滤规则维护大佬们的辛苦付出。

| 规则 | 类型 | 原始链接 | 加速链接 | 更新日期 |
|:-|:-|:-|:-|:-|
| AdGuard Base filters | filter | [原始链接](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_2_Base/filter.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adblock/main/rules/AdGuard_Base_filters.txt) | 2024/11/13 |
| AdGuard Chinese filters | filter | [原始链接](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_224_Chinese/filter.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adblock/main/rules/AdGuard_Chinese_filters.txt) | 2024/11/13 |
| AdGuard Annoyances filter | filter | [原始链接](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_14_Annoyances/filter.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adblock/main/rules/AdGuard_Annoyances_filter.txt) | 2024/11/13 |
| EasyList China | filter | [原始链接](https://easylist-downloads.adblockplus.org/easylistchina.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adblock/main/rules/EasyList_China.txt) | 2024/11/13 |
| EasyPrivacy | filter | [原始链接](https://easylist-downloads.adblockplus.org/easyprivacy.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adblock/main/rules/EasyPrivacy.txt) | 2024/11/13 |
| Fanboy's Annoyance List | filter | [原始链接](https://easylist.to/easylist/fanboy-social.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adblock/main/rules/Fanboy's_Annoyance_List.txt) | 2024/11/13 |
| CJX's Annoyance List | filter | [原始链接](https://raw.githubusercontent.com/cjx82630/cjxlist/master/cjx-annoyance.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adblock/main/rules/CJX's_Annoyance_List.txt) | 2024/09/27 |
| NoAppDownload | filter | [原始链接](https://raw.githubusercontent.com/Noyllopa/NoAppDownload/master/NoAppDownload.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adblock/main/rules/NoAppDownload.txt) | 2024/10/19 |
| Adblock Warning Removal List | filter | [原始链接](https://easylist-downloads.adblockplus.org/antiAdblock.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adblock/main/rules/Adblock_Warning_Removal_List.txt) | 2024/09/27 |
| damengzhu | filter | [原始链接](https://raw.githubusercontent.com/damengzhu/banad/main/jiekouAD.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adblock/main/rules/damengzhu.txt) | 2024/11/13 |
| xinggsf mv | filter | [原始链接](https://raw.githubusercontent.com/xinggsf/Adblock-Plus-Rule/master/mv.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adblock/main/rules/xinggsf_mv.txt) | 2024/11/08 |
| xinggsf rule | filter | [原始链接](https://raw.githubusercontent.com/xinggsf/Adblock-Plus-Rule/master/rule.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adblock/main/rules/xinggsf_rule.txt) | 2024/11/02 |
| SmartTV Blocklist | dns | [原始链接](https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV-AGH.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adblock/main/rules/SmartTV_Blocklist.txt) | 2024/02/15 |
| AWAvenue Ads Rule | dns | [原始链接](https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adblock/main/rules/AWAvenue_Ads_Rule.txt) | 2024/11/08 |
| Urlhaus Malicious URL Blocklist | dns | [原始链接](https://malware-filter.gitlab.io/malware-filter/urlhaus-filter-agh-online.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adblock/main/rules/Urlhaus_Malicious_URL_Blocklist.txt) | 2024/11/13 |
| Nocoin list | host | [原始链接](https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts.txt) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adblock/main/rules/Nocoin_list.txt) | 2024/09/27 |
| 1024 hosts | host | [原始链接](https://raw.githubusercontent.com/Goooler/1024_hosts/master/hosts) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adblock/main/rules/1024_hosts.txt) | 2024/02/15 |
| ad-wars hosts | host | [原始链接](https://raw.githubusercontent.com/jdlingyu/ad-wars/master/hosts) | [加速链接](https://mirror.ghproxy.com/https://raw.githubusercontent.com/Sereinfy/Adblock/main/rules/ad-wars_hosts.txt) | 2024/02/15 |
