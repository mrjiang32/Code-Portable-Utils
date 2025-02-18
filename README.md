## 免责声明 | Disclaimer

本项目使用了 [7-Zip](https://www.7-zip.org/) 作为解压工具。  
7-Zip 是 Igor Pavlov 开发的自由软件，遵循 [GNU LGPL](https://www.gnu.org/licenses/lgpl.html) 许可协议（部分代码遵循 BSD 许可协议）。  

7-Zip 的官方网站：[https://www.7-zip.org/](https://www.7-zip.org/)。  

本项目未对 7-Zip 进行修改，仅用于解压缩功能，版权归原作者所有。  

This project uses [7-Zip](https://www.7-zip.org/) as the extraction tool.  
7-Zip is free software developed by Igor Pavlov, licensed under the [GNU LGPL](https://www.gnu.org/licenses/lgpl.html) (with some parts under BSD License). 

The official website of 7-Zip is [https://www.7-zip.org/](https://www.7-zip.org/).  

No modifications are made to 7-Zip; it is used for extraction purposes only. All copyrights belong to the original author.

---

## Code Portable Utils - VS Code Portable 自动更新程序 | Auto-updater for VS Code Portable

简称 CPU（开玩笑的） | Abbreviated as CPU (just kidding)

---

## 📌 项目介绍 | Project Introduction

本项目用于 **自动更新 VS Code 便携版**。每次运行 `pyupdate.exe` 时，程序会自动检查新版本，若有则下载并解压，确保 VS Code 便携版始终是最新版本。 

This project is designed to **automatically update VS Code Portable**. Each time `pyupdate.exe` is run, it checks for a new version, downloads, and extracts it if needed, ensuring your VS Code Portable is always up-to-date.

---

## 🔧 使用方法 | Usage

### **方法一：使用已有的 exe 文件** | **Method 1: Use Pre-built exe File**

从 GitHub 下载，无需安装即可使用。 

Simply download from GitHub and use without installation.

---

### **方法二：自定义编译 exe 文件** | **Method 2: Build Your Own exe File**

#### 1️⃣ 安装依赖 | Install Dependencies

若为开发者，运行以下命令安装必要的 Python 依赖：

If you're a developer, run the following to install the required Python dependencies:

```
pip install pyinstaller requests
```

#### 2️⃣ 编译可执行文件 (Windows) | Build Executable (Windows)

使用 `build_and_clean.cmd` 一键打包：  

Use `build_and_clean.cmd` to compile the executable:

```
build_and_clean.cmd
```

注意python、pip和pyupdate要在PATH中


📌 打包完成后生成 `pyupdate.exe`，无需 Python 环境即可使用！  

Once built, `pyupdate.exe` is created and can be used without a Python environment!

#### 3️⃣ 启动更新程序 | Run the Updater

直接运行 `pyupdate.exe`：  

Simply run `pyupdate.exe`:

```
pyupdate.exe
```

程序会自动检查并更新 VS Code。  

The program will automatically check for and update VS Code.

---

## 📂 目录结构 | Directory Structure

```
CodePortable
|- PyUpdate.exe        <- Python 版更新器 (Python-based updater)
|- build_and_clean.cmd <- 生成并清理文件 (Build and clean script)
|- app                 <- VS Code 便携版目录 (VS Code Portable directory)
   |- Code.exe
   |- bin
      |- code-tunnel.exe
      |- code(.sh)          
   |- data             <- 便携模式数据存储 (Portable mode data)
|- Updates             <- 存放 `7z` (Stores `7z`)
   |- 7z.exe
   |- 7z.dll
   |- 其他依赖... (Other dependencies...)
```

---

## ❗ 注意事项 | Notes

1. **适用版本** | **Available Versions**  
   该工具仅适用于 Windows 便携版 VS Code，不支持安装版！
   
   This tool is for Windows portable versions of VS Code only, not the installed version!

3. **依赖文件** | **Update Files**  
   请确保 `Updates` 目录内包含 `7z.exe`，否则更新将失败！
   
   Ensure that `Updates` contains `7z.exe` or the update will fail!

4. **自动启动 VS Code** | **Auto-launch VS Code**  
   `pyupdate.exe` 会自动启动 VS Code，若不希望如此，请修改代码。
   
   `pyupdate.exe` will auto-launch VS Code. Modify the script if you want to disable this.

---

## 🛠️ 开发与贡献 | Development & Contribution

本项目由 mrjiang32 及 Copilot、ChatGPT、deepseek 合作完成。  

Developed by mrjiang32, with help from Copilot, ChatGPT, and deepseek.

欢迎提交 Issues 或 Pull Requests 改进本项目！  

Feel free to submit issues or pull requests to improve the project!

---

## 📜 许可证 | License

本项目采用 GPLv3 许可证。  
This project is licensed under the GPL v3.0 License.

---

Made with love by mrjiang32 ❤️

---
