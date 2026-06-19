<div align="center">

# 网络剪贴板(服务端)

**跨设备剪贴板无缝同步**

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/xjyzs/Clipboard_Android?color=orange)](https://github.com/xjyzs/Clipboard/releases)

[English](README.md) · [报告 Bug](https://github.com/xjyzs/Clipboard_Server/issues) · [功能建议](https://github.com/xjyzs/Clipboard_Server/issues)

---

</div>

## ✨ 为什么选择网络剪贴板？

手机上复制，电脑上粘贴。电脑上复制，平板上粘贴。**零操作，即时同步。**

网络剪贴板是一款**免费开源**的软件，能自动将剪贴板内容实时同步到其他设备和 Web 端。

## 🚀 核心特性

| 特性 | 说明 |
|------|------|
| **自动同步** | 任意设备复制，所有已连接设备即时可用 |
| **Web 兼容** | 基于 Socket.IO 协议，可对接 Web、桌面端等 |

## 客户端下载
[Android(自动上传功能需要 Root, 手动上传和同步功能不需要)](https://github.com/xjyzs/Clipboard_Android)


## 📦 工作原理

```
┌──────────────┐     Socket.IO       ┌──────────────┐
│   客户端     │ ◄─────────────────► │   服务端      │
│              │                     │  (Python)    │
└──────┬───────┘                     └──────────────┘
       │
  剪贴板检测                        
```

## 📲 安装指南

### 前置条件

- 拥有一台可运行 Python 代码服务器或电脑

### 安装步骤
#### 创建虚拟环境(可选)
```Shell
python3 -m venv .venv
source .venv/bin/activate
```
#### 安装依赖
```Shell
pip install -r requirements.txt
```
#### 启动程序
```Shell
python clipboard.py
```
地址为`http://你的 IP 地址:11451`
### 变体
clipboard.py(路由为/)
clipboardWithRouteCb.py(路由为/cb)



## 🤝 参与贡献

欢迎参与项目改进！

- 🐛 通过 [Issues](https://github.com/xjyzs/Clipboard_Server/issues) 报告 Bug
- 💡 提出功能建议
- 🔧 提交 Pull Request

## 📄 开源协议

本项目基于 [MIT License](LICENSE) 开源。

---

<div align="center">

**如果觉得这个项目有用，请点个 ⭐ 支持一下吧**

Made with ❤️ by [雪霁银装素](https://github.com/xjyzs)

</div>
