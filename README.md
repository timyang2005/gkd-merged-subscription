# GKD 增强订阅（合并版）

这是一个合并了多个优质 GKD 第三方订阅的规则集合，帮助你一站式跳过各种应用的开屏广告、弹窗等。

## 📦 订阅信息

| 项目 | 详情 |
|------|------|
| 订阅名称 | GKD增强订阅（合并版） |
| 订阅 ID | 999001 |
| 文件大小 | 1.7 MB |
| Apps 数量 | 816 个 |
| 规则数量 | 34,805 条 |

## 🔗 导入链接

### 方法1：直接导入（推荐）

在 GKD 应用中使用"从链接导入"功能，输入以下链接之一：

**JSON5 格式（推荐）：**
```
https://raw.githubusercontent.com/timyang2005/gkd-merged-subscription/main/merged_gkd.json5
```

**JSON 格式（兼容性更好）：**
```
https://raw.githubusercontent.com/timyang2005/gkd-merged-subscription/main/merged_gkd.json
```

### 方法2：使用国内镜像（国内用户推荐）

如果你在国内，可以使用以下镜像链接获得更快的下载速度：

**通过 jsDelivr：**
```
https://cdn.jsdelivr.net/gh/timyang2005/gkd-merged-subscription@main/merged_gkd.json5
```

**通过 gitmirror：**
```
https://raw.gitmirror.com/timyang2005/gkd-merged-subscription/main/merged_gkd.json5
```

## 📋 合并来源

本订阅合并了以下 4 个仍在维护的优质订阅：

| 订阅名称 | 作者 | 原始 Apps 数 | 状态 |
|---------|------|-------------|------|
| 奥怪的 GKD 订阅 | aoguai | 72 | ✅ 维护中 |
| 甘霖的 GKD 订阅 | ganlinte | 607 | ✅ 维护中 |
| 梦念逍遥の订阅 | 梦念逍遥 | 285 | ✅ 维护中 |
| Mrlc 的订阅 | Mrlc | 689 | ✅ 维护中 |

**合并后统计：**
- ✅ 去重后共 **816** 个 Apps
- ✅ 共 **2,048** 个 Groups
- ✅ 共 **34,805** 条规则

## 🚀 使用步骤

### 1. 打开 GKD 应用
确保你的手机已安装 [GKD](https://github.com/gkd-kit/gkd) 应用

### 2. 导入订阅
- 点击底部「订阅」标签
- 点击右上角「+」按钮
- 选择「从链接导入」
- 复制粘贴上述链接之一
- 点击确认导入

### 3. 启用规则
- 导入成功后，在订阅列表中找到「GKD增强订阅（合并版）」
- 点击进入，根据需要启用/禁用各个分组
- 建议先启用「开屏广告」分组测试效果

## 🔄 更新订阅

本订阅会定期更新，更新方法：

1. 在 GKD 的订阅列表中找到本订阅
2. 点击订阅名称进入详情
3. 点击右上角菜单，选择「检查更新」
4. 如有新版本，按提示更新即可

## ⚙️ 合并逻辑

- **Apps 去重**：按包名（`id`）自动去重，保留第一个遇到的版本
- **Groups 合并**：同一 App 的多个订阅中的 groups 会合并，按 `key` 去重
- **GlobalGroups 去重**：按 `key` 去重
- **Categories 去重**：按 `key` 去重

## ⚠️ 注意事项

1. **订阅 ID**：本订阅 ID 为 `999001`，如有冲突请手动修改文件
2. **规则冲突**：不同订阅可能有重复或冲突的规则，建议导入后测试并调整
3. **自动更新**：本订阅支持自动更新检查
4. **规则优先级**：当前保留第一个遇到的规则，如需调整请手动修改

## 🐛 问题反馈

如果在使用过程中遇到问题：
- 规则相关 issue 请到各原始订阅仓库反馈
- 合并相关 issue 可以在本仓库提交

## 📜 许可证

本订阅合并自多个开源订阅，遵循各原始订阅的许可证。
- [GKD 第三方订阅收录名单](https://github.com/Adpro-Team/GKD_THS_List)

## 🙏 致谢

感谢以下订阅作者的辛勤维护：
- [aoguai](https://github.com/aoguai/subscription) - 奥怪的 GKD 订阅
- [ganlinte](https://github.com/ganlinte/GKD-subscription) - 甘霖的 GKD 订阅  
- [梦念逍遥](https://github.com/MengNianxiaoyao/gkd-subscription) - 梦念逍遥の订阅
- [Mrlc](https://github.com/mrlctate/gkd-mrlc) - Mrlc 的订阅

---

**⭐ 如果这个项目对你有帮助，欢迎 Star！**
