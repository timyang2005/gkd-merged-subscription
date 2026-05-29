#!/usr/bin/env python3
import json
import json5
import requests
import os
from typing import Dict, List, Any


SUBSCRIPTION_SOURCES = [
    {
        "name": "奥怪的 GKD 订阅",
        "author": "aoguai",
        "url": "https://registry.npmmirror.com/@aoguai/subscription/latest/files/dist/gkd.json5",
    },
    {
        "name": "甘霖的 GKD 订阅",
        "author": "ganlinte",
        "url": "https://registry.npmmirror.com/@ganlinte/gkd-subscription/latest/files/dist/gkd.json5",
    },
    {
        "name": "AIsouler 的订阅",
        "author": "AIsouler",
        "url": "https://registry.npmmirror.com/@aisouler/gkd_subscription/latest/files/dist/AIsouler_gkd.json5",
    },
    {
        "name": "gujiwuqing 的订阅",
        "author": "gujiwuqing",
        "url": "https://registry.npmmirror.com/@gujiwuqing/gkd_subscription/latest/files/dist/gkd.json5",
    },
]


def fetch_subscription(url: str) -> Dict[str, Any]:
    """获取并解析订阅文件"""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return json5.loads(response.text)
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        raise


def merge_subscriptions(sources: List[Dict[str, Any]]) -> Dict[str, Any]:
    """合并多个订阅"""
    merged = {
        "id": 999001,
        "name": "GKD增强订阅（合并版）",
        "version": 1,
        "author": "Community Merge",
        "mergeInfo": {
            "description": "此订阅由多个订阅合并而成",
            "sources": []
        },
        "categories": [],
        "globalGroups": [],
        "apps": []
    }

    apps_map: Dict[str, Dict] = {}
    categories_map: Dict[int, Dict] = {}
    global_groups_map: Dict[int, Dict] = {}
    rule_count = 0

    for source in sources:
        try:
            print(f"Processing: {source['name']} by {source['author']}")
            sub = fetch_subscription(source["url"])

            merged["mergeInfo"]["sources"].append({
                "author": source["author"],
                "file": f"{source['author'].lower()}_gkd.json5"
            })

            # 合并 categories（去重）
            for cat in sub.get("categories", []):
                key = cat["key"]
                if key not in categories_map:
                    categories_map[key] = cat

            # 合并 globalGroups（去重）
            for gg in sub.get("globalGroups", []):
                key = gg["key"]
                if key not in global_groups_map:
                    global_groups_map[key] = gg
                rule_count += len(gg.get("rules", []))

            # 合并 apps（去重）
            for app in sub.get("apps", []):
                app_id = app["id"]
                if app_id not in apps_map:
                    apps_map[app_id] = app
                else:
                    # 合并 groups
                    existing_groups = {g["key"]: g for g in apps_map[app_id].get("groups", [])}
                    for group in app.get("groups", []):
                        if group["key"] not in existing_groups:
                            existing_groups[group["key"]] = group
                        rule_count += len(group.get("rules", []))
                    apps_map[app_id]["groups"] = list(existing_groups.values())
                rule_count += sum(len(g.get("rules", [])) for g in app.get("groups", []))

        except Exception as e:
            print(f"Error processing {source['name']}: {e}")
            continue

    # 构建最终的合并结果
    merged["categories"] = sorted(categories_map.values(), key=lambda x: x["key"])
    merged["globalGroups"] = sorted(global_groups_map.values(), key=lambda x: x["key"])
    merged["apps"] = sorted(apps_map.values(), key=lambda x: x["id"])

    # 统计信息
    group_count = sum(len(app.get("groups", [])) for app in merged["apps"]) + len(merged["globalGroups"])

    return merged, len(apps_map), group_count, rule_count


def save_files(merged: Dict[str, Any]):
    """保存合并后的文件"""
    # 保存 JSON5 格式
    with open("merged_gkd.json5", "w", encoding="utf-8") as f:
        json5.dump(merged, f, ensure_ascii=False, indent=2)

    # 保存 JSON 格式
    with open("merged_gkd.json", "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)


def main():
    print("开始合并 GKD 订阅...")
    merged, app_count, group_count, rule_count = merge_subscriptions(SUBSCRIPTION_SOURCES)
    save_files(merged)

    json5_size = os.path.getsize("merged_gkd.json5")
    json_size = os.path.getsize("merged_gkd.json")

    print("\n合并完成！")
    print(f"Apps 数量: {app_count}")
    print(f"Groups 数量: {group_count}")
    print(f"规则数量: {rule_count}")
    print(f"JSON5 文件大小: {json5_size / 1024 / 1024:.1f} MB")
    print(f"JSON 文件大小: {json_size / 1024 / 1024:.1f} MB")


if __name__ == "__main__":
    main()
