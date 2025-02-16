# Code Portable Updater - VS Code Portable 自动更新程序

*A simple auto-updater for VS Code Portable*

简称 CPU (bushi)
Abbreviated as CPU (just kidding)

------

## 📌 项目介绍 | Project Introduction

本项目用于 **自动更新 VS Code 便携版**。每次启动 `pyupdate.exe` 时，程序会自动检查是否有新版本，若有则自动下载并解压，确保你的 VS Code 便携版始终保持最新状态。
This project is designed to **automatically update VS Code Portable**. Every time `pyupdate.exe` is launched, it checks for a new version and downloads & extracts it if needed, ensuring your VS Code Portable is always up-to-date.

------

## 🔧 使用方法 | Usage

### **方法一：使用已有的 exe 文件**

### **Method 1: Use Pre-built exe File**

直接从 Github 下载即可，无需安装即可使用（这不是绿色版么）。
Simply download it from Github and use it directly without installation (isn't this a portable version?).

------

### **方法二：导出你自己的 exe 文件**

### **Method 2: Build Your Own exe File**

#### 1️⃣ 安装依赖 | Install Dependencies

如果你是开发者，运行以下命令安装必要的 Python 依赖：
If you are a developer, run the following command to install the required Python dependencies:

powershell

复制

```
pip install pyinstaller requests  # pyinstaller and requests
```

#### 2️⃣ 编译可执行文件 (Windows) | Build Executable

使用 `build_and_clean.cmd` 一键打包：
Use `build_and_clean.cmd` to compile the executable:

powershell

复制

```
build_and_clean.cmd
```

📌 打包完成后，将生成 `pyupdate.exe`，无需 Python 运行环境即可使用！
📌 Once built, `pyupdate.exe` will be created and can run without a Python environment!

#### 3️⃣ 启动更新程序 | Run the Updater

直接运行 `pyupdate.exe`：
Simply launch `pyupdate.exe`:

powershell

复制

```
pyupdate.exe
```

程序会自动检测新版本并更新 VS Code。
It will automatically check for updates and update VS Code if necessary.

------

## 📂 目录结构 | Directory Structure

bash

复制

```
CodePortable
|- Entry.exe           <- 启动入口 (Entry script)
|- PyUpdate.exe        <- Python 版更新器 (Python-based updater)
|- LegacyUpdate.exe    <- 备用批处理更新器 (Fallback batch script updater)
|- build_and_clean.cmd <- 生成并清理文件 (Build and clean script)
|- App <- [dir]        <- VS Code 便携版目录 (VS Code Portable directory)
   |- Code.exe
   |- bin/code-tunnel.exe
   |- data <- [dir]    <- 便携模式数据存储 (Portable mode data)
|- Updates <- [dir]    <- 存放 `curl` 和 `7z` (Stores `curl` & `7z`)
   |- curl.exe
   |- 7z.exe
   |- 7z.dll
   |- 其他依赖... (Other dependencies...)
```

------

## ❗ 注意事项 | Notes

1. **适用版本**
   此工具仅适用于 Windows 便携版 VS Code，不支持官方安装版！
   This tool is for Windows portable versions of VS Code and does not support installed versions.
2. **依赖文件**
   确保 `Updates` 目录内包含 `curl.exe` 和 `7z.exe`，否则更新将失败！
   Ensure that `Updates` contains `curl.exe` and `7z.exe`, or the update will fail!
3. **自动启动 VS Code**
   `PyUpdate.exe` 运行后会自动启动 VS Code。如果你不希望立即启动，可以修改代码。
   `pyupdate.exe` will auto-launch VS Code after updating. Modify the script if you want to disable this behavior.

------

## 🛠️ 开发与贡献 | Development & Contribution

全是 mrjiang32 的功劳（当然还有 Copilot、ChatGPT 和 deepseek）。
All credits go to mrjiang32 (and of course, Copilot, ChatGPT, and deepseek).

欢迎提交 Issue 或 Pull Request 来改进本项目！
Feel free to submit issues or pull requests to improve this project!

------

## 📜 许可证 | License

本项目采用 GPLv3 许可证。
This project is licensed under the GPL version 3.0 License.

------

Made with love by mrjiang32
