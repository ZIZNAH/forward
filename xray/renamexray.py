#!/usr/bin/env python3
"""Print an Xray node share URL with a user supplied display name.

Uses 233boy/Xray's existing `url <config-file>` command to produce the
protocol-correct URL, then changes only its display name (VMess `ps` or URI
fragment). It does not modify server configuration files.
"""

import argparse
import base64
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


ANSI = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]")
URL = re.compile(r"(?:vmess|vless|trojan|ss|socks|hy|hysteria2?)://[^\s\x1b]+")


def rename_url(url: str, name: str) -> str:
    if url.startswith("vmess://"):
        payload = url[len("vmess://"):]
        payload += "=" * (-len(payload) % 4)
        try:
            data = json.loads(base64.urlsafe_b64decode(payload).decode("utf-8"))
        except (ValueError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ValueError("无法解码 VMess 链接中的配置") from exc
        data["ps"] = name
        encoded = base64.b64encode(
            json.dumps(data, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        ).decode("ascii")
        return "vmess://" + encoded

    # The text after # is the connection name in standard share URIs.
    from urllib.parse import quote

    base = url.split("#", 1)[0]
    return base + "#" + quote(name, safe="-._~")


def main() -> int:
    parser = argparse.ArgumentParser(description="为 233boy/Xray 节点链接设置自定义名称")
    parser.add_argument("--xray", default="/usr/local/bin/xray", help="233boy/Xray 管理命令路径")
    args = parser.parse_args()

    conf_dir = Path("/etc/xray/conf")
    if not conf_dir.is_dir():
        print(f"找不到配置目录: {conf_dir}", file=sys.stderr)
        return 1
    files = sorted(p for p in conf_dir.iterdir()
                   if p.is_file() and p.name.endswith(".json")
                   and not re.search(r"dynamic-port-.*-link", p.name))
    if not files:
        print(f"{conf_dir} 中没有可用的 JSON 节点配置", file=sys.stderr)
        return 1

    print("选择节点配置：")
    for i, path in enumerate(files, 1):
        print(f"  {i}) {path.name}")
    while True:
        choice = input("请输入序号: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(files):
            config = files[int(choice) - 1]
            break
        print("序号无效，请重试。")

    name = input("请输入自定义名称: ").strip()
    if not name:
        print("名称不能为空。", file=sys.stderr)
        return 1

    xray = args.xray
    if not Path(xray).exists():
        found = shutil.which(xray)
        if not found:
            print(f"找不到 233boy/Xray 命令: {xray}", file=sys.stderr)
            return 1
        xray = found

    # This calls the script's same URL-generation path as menu option 3.
    result = subprocess.run([xray, "url", config.name], cwd=str(conf_dir.parent.parent),
                            text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ANSI.sub("", result.stdout)
    if result.returncode != 0:
        print(output, end="", file=sys.stderr)
        return result.returncode
    matches = URL.findall(output)
    if not matches:
        print("原脚本没有生成可分享的 URL。原始输出：", file=sys.stderr)
        print(output, file=sys.stderr)
        return 1

    try:
        customized = rename_url(matches[-1].rstrip(".,;"), name)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print("\n自定义名称链接：")
    print(customized)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
