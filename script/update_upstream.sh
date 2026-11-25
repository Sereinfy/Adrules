#!/bin/bash
set -euo pipefail

# 导入工具函数
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/utils.sh"

# 项目根目录
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
TMP_DIR="${ROOT_DIR}/tmp"
FAILED_LOG="${ROOT_DIR}/download_failed.log"

# 检查依赖
check_deps curl sed xargs

# 准备目录
mkdir -p "${TMP_DIR}/content" "${TMP_DIR}/dns"
> "$FAILED_LOG"

# 下载任务处理函数
do_download() {
    local url="$1"
    local target_dir="$2"

    # 为重名文件添加缓解措施：使用 URL 的 MD5 哈希作为前缀
    local url_hash=$(echo -n "$url" | md5sum | cut -d' ' -f1 | cut -c1-8)
    local original_filename=$(basename "$url")
    local filename="${url_hash}_${original_filename}"

    local filepath="${target_dir}/${filename}"
    local tmp_filepath="${filepath}.tmp"

    if download_file "$url" "$tmp_filepath"; then
        # 插入来源注释
        sed -i "1i\\! url: $url" "$tmp_filepath"
        # 换行符转换
        sed -i 's/\r$//' "$tmp_filepath"
        # 原子性移动，确保文件完整
        mv "$tmp_filepath" "$filepath"
    else
        rm -f "$tmp_filepath"
        echo "$url" >> "$FAILED_LOG"
    fi
}

export -f do_download
export -f download_file
export -f log_info
export -f log_warn
export -f log_error
export NC GREEN YELLOW RED

# 规则链接
content_urls=(
  #--lite
  #awavenue
  "https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/Filters/AWAvenue-Ads-Rule-Adblock.txt"
  #adguard-mobile
  "https://filters.adtidy.org/extension/ublock/filters/11.txt"
  #easylist-china
  "https://easylist-downloads.adblockplus.org/easylistchina.txt"
  #--normal
  #easylist
  "https://easylist.to/easylist/easylist.txt"
  #easyprivacy
  "https://easylist.to/easylist/easyprivacy.txt"
  #anti-ad
  "https://anti-ad.net/easylist.txt"
  #ublock-privacy
  "https://ublockorigin.github.io/uAssets/filters/privacy.txt"
  #adguard-annoyances
  "https://filters.adtidy.org/extension/ublock/filters/14.txt"
  #easylist-cookie
  "https://secure.fanboy.co.nz/fanboy-cookiemonster.txt"
  #nocoin
  "https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/nocoin.txt"
  #--plus
  #adguard-base
  "https://filters.adtidy.org/extension/ublock/filters/2_without_easylist.txt"
  #adguard-chinese
  "https://filters.adtidy.org/extension/ublock/filters/224.txt"
  #cjx-annoyance
  "https://raw.githubusercontent.com/cjx82630/cjxlist/master/cjx-annoyance.txt"
)

dns_urls=(
  #awavenue
  "https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/Filters/AWAvenue-Ads-Rule-Adblock.txt"
  #adguard-mobile
  "https://filters.adtidy.org/extension/ublock/filters/11.txt"
  #easylist-china
  "https://easylist-downloads.adblockplus.org/easylistchina.txt"
  #easylist
  "https://easylist.to/easylist/easylist.txt"
  #easyprivacy
  "https://easylist.to/easylist/easyprivacy.txt"
  #anti-ad
  "https://anti-ad.net/easylist.txt"
  #ublock-privacy
  "https://ublockorigin.github.io/uAssets/filters/privacy.txt"
  #nocoin
  "https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/nocoin.txt"
  #adguard-base
  "https://filters.adtidy.org/extension/ublock/filters/2_without_easylist.txt"
  #adguard-Social
  "https://filters.adtidy.org/windows/filters/4.txt"
  #Fuck Tracking
  "https://easylist-downloads.adblockplus.org/easyprivacy.txt"
  "https://filters.adtidy.org/windows/filters/3.txt"
  #xinggsf
  "https://raw.githubusercontent.com/xinggsf/Adblock-Plus-Rule/master/mv.txt"
  #uBO
  "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances-others.txt"
  "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt"
  "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt"
  "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt"
  #Me
  "https://raw.githubusercontent.com/Cats-Team/dns-filter/main/abp.txt"
)

log_info "开始并发下载规则..."

# 使用 xargs 控制并发数为 8
printf "%s\n" "${content_urls[@]}" | xargs -I {} -P 8 bash -c "do_download '{}' '${TMP_DIR}/content'"
printf "%s\n" "${dns_urls[@]}" | xargs -I {} -P 8 bash -c "do_download '{}' '${TMP_DIR}/dns'"

if [ -s "$FAILED_LOG" ]; then
    log_error "以下链接下载失败:"
    cat "$FAILED_LOG"
fi

log_info "下载任务完成。"
