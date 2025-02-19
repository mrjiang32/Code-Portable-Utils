import datetime
import os
import sys
import subprocess
import hashlib

CURRENTTIME = datetime.datetime.now()

def tmexit(code = 0):
    esplasetime = datetime.datetime.now() - CURRENTTIME
    print(f"完成用时：{esplasetime}")
    sys.exit(code)

try:
    import requests
except ModuleNotFoundError:
    print("request导入失败\n")
    tmexit(1)

print("CodePortable-Updater v1.0.1\n简称CPU(bushi\n\n提醒：(CPU)虽然可以更新VSCode，但你需要手动更新(CPU)哦！")
print(f"\n当前时间: GMT {datetime.datetime.now(datetime.UTC)}\n")

# 定义常量
EXTRACT_DIR = os.path.dirname(os.path.abspath(__file__))  

# 请不要修改打包判断代码，否则会执行失败
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)  
    print("打包版本\n")
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
    print("Python文件版本(你居然没打包)\n")

VSCODE_DIR  = os.path.join(BASE_DIR, "app")
VSCODE_BIN  = os.path.join(VSCODE_DIR, "bin", "code-tunnel.exe")
VSCODE_BASH = os.path.join(VSCODE_DIR, "bin", "code")
VSCODE_EXE  = os.path.join(VSCODE_DIR, "Code.exe")
DATA_DIR = os.path.join(VSCODE_DIR, "data")
TMP_DIR = os.path.join(VSCODE_DIR, "tmp")
UPDATES_DIR = os.path.join(EXTRACT_DIR, "updates")
LATEST_URL  = "https://update.code.visualstudio.com/latest/win32-x64-archive/stable"
TEMP_ZIP    = os.path.join(VSCODE_DIR, "vscode_latest.zip")
ZIPPER = os.path.join(UPDATES_DIR, "7z.exe")
BACKUP_DIR = os.path.join(BASE_DIR, "backup")

global version_exe
version_exe = None

print("灵魂拷问：你的Visual Studio Code更新了吗？\n\n让我看看：\n")

def get_vscode_version_from_exe():
    """ 通过 `code-tunnel.exe --version` 获取 VS Code 版本 """
    if os.path.exists(VSCODE_BIN):
        try:
            output = subprocess.check_output([VSCODE_BIN, "--version"], universal_newlines=True).strip()            
            global version_exe
            version_exe = output.replace("(", "").replace(")", "").replace("code","Code").replace("commit","COMMIT")
            print(version_exe)
            return output.split(" ")[1]
        except Exception as e:
            print(f"读取 Code (code-tunnel) 版本失败: {e}")
            version_exe = None
    return "0"

def get_commit_hash_from_sh():
    """ 从 `code.sh` 读取 VS Code COMMIT Hash """
    if os.path.exists(VSCODE_BASH):
        try:
            with open(VSCODE_BASH, "r", encoding="utf-8") as f:
                is_vscode_script = False
                commit_hash = None
                for line in f:
                    line = line.strip()
                    if line.startswith("NAME=") and '"Code"' in line:
                        is_vscode_script = True
                    if line.startswith("COMMIT="):
                        commit_hash = line.split("=")[1].strip().strip('"')
                if is_vscode_script and commit_hash:
                    print(f"从.sh文件的hash:   {commit_hash}")
                    return commit_hash
        except Exception as e:
            print(f"读取 Code (shell 文件) 版本失败: {e}")
    return None

def download_latest_version():
    """ 下载最新版本并校验文件 """
    max_retries = 3
    for attempt in range(max_retries):
        try:
            if os.path.exists(TEMP_ZIP):
                os.remove(TEMP_ZIP)
                print("已删除旧的临时下载文件")
            with requests.get(LATEST_URL, stream=True) as r:
                r.raise_for_status()
                with open(TEMP_ZIP, "wb+") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            print(f"已下载最新版本: {latest_version}")
            if os.path.getsize(TEMP_ZIP) > 0:
                print("文件校验成功")
                sha256_hash = hashlib.sha256()
                with open(TEMP_ZIP, "rb") as f:
                    for byte_block in iter(lambda: f.read(4096), b""):
                        sha256_hash.update(byte_block)
                downloaded_hash = sha256_hash.hexdigest()
                expected_hash = response_json["sha256hash"]
                if downloaded_hash == expected_hash:
                    print("文件哈希校验成功")
                    break
                else:
                    print("文件哈希校验失败，重试下载...")
            else:
                print("文件校验失败，重试下载...")
        except requests.RequestException as e:
            print(f"下载失败: {e}")
        except Exception as e:
            print(f"文件校验失败: {e}")
        if attempt == max_retries - 1:
            print("多次下载失败，退出程序")
            tmexit(1)

def backup_directories():
    """ 备份 data 和 tmp 目录 """
    os.makedirs(BACKUP_DIR, exist_ok=True)
    if os.path.exists(DATA_DIR):
        subprocess.run(["move", DATA_DIR, os.path.join(BACKUP_DIR, "data")], check=True, shell=True)
        print("已备份 data 目录")
    if os.path.exists(TMP_DIR):
        subprocess.run(["move", TMP_DIR, os.path.join(BACKUP_DIR, "tmp")], check=True, shell=True)
        print("已备份 tmp 目录")

def extract_and_install():
    """ 解压并安装最新版本 """
    try:
        subprocess.run([ZIPPER, "x", TEMP_ZIP, f"-o{VSCODE_DIR}", "-y"], check=True)
        print(f"版本 {latest_version} 解压成功")
    except subprocess.CalledProcessError as e:
        print(f"解压失败:(7z) \n原因 {e}")
        tmexit(1)
    try:
        os.remove(TEMP_ZIP)
        print("已删除临时下载文件")
    except OSError as e:
        print(f"删除临时文件失败: \n原因 {e}")

try:
    current_version = "0"
    fault = False
    print("初步检测：")
    current_version1 = get_vscode_version_from_exe()
    if version_exe != None:
        commit_hash1 = version_exe.split(" ")[3].strip()
    else:
        commit_hash1 = None
    commit_hash2 = get_commit_hash_from_sh()
    print(f"\n比较hash:\ncode-tunnel        {commit_hash1}\ncode-shell         {commit_hash2}")

    os.system("cls")

    hash_only = False
    if commit_hash1 == commit_hash2 and commit_hash1 != None and commit_hash2 != None:
        if current_version1 != 0 and current_version1 != "0": 
            current_version = current_version1
            print(f"\n检测版本一致: \nVS Code 版本名称   {current_version}\nVS Code 提交哈希   {commit_hash1}")
    elif commit_hash1 == None and commit_hash2 != None:
        print(f"用hash检测版本：\n{commit_hash1}")
        current_version = commit_hash1
        hash_only = True
    else:
        confirm = input("你似乎没有安装Code，是否从现有版本制作[y/N]")
        if confirm.lower().strip() == "y":
            try:
                if not os.path.exists(VSCODE_DIR):
                    os.makedirs(VSCODE_DIR)
                if not os.path.exists(DATA_DIR):
                    os.makedirs(DATA_DIR)
                user_data_src = os.path.join(os.getenv('APPDATA'), 'Code')
                user_data_dst = os.path.join(DATA_DIR, 'user-data')
                if os.path.exists(user_data_src):
                    subprocess.run(["xcopy", user_data_src, user_data_dst, "/E", "/I", "/EXCLUDE:cache,logs"], check=True)
                    print("已复制用户数据目录到便携模式")
                extensions_src = os.path.join(os.getenv('USERPROFILE'), '.vscode', 'extensions')
                extensions_dst = os.path.join(DATA_DIR, 'extensions')
                if os.path.exists(extensions_src):
                    subprocess.run(["xcopy", extensions_src, extensions_dst, "/E", "/I", "/EXCLUDE:cache,logs"], check=True)
                    print("已复制扩展目录到便携模式")
                current_version = "Need Installing"
            except Exception as e:
                print(f"移植到便携模式失败: {e}")   
            tmexit(0)
        else:
            tmexit(0)

    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(TMP_DIR):
        os.makedirs(TMP_DIR)

    if not fault:
        print(f"\n+------------------------------+\n o((>ω< ))o Code版本是：{current_version}\n+------------------------------+\n")
        try:
            response = requests.get("https://update.code.visualstudio.com/api/update/win32-x64-archive/stable/latest", timeout=10)
            response_json = response.json()
            latest_version = response_json["name"].strip()
            latest_hash    = response_json["version"].strip()
            print(f"获得最新版本成功！")
            print(f"VS Code 版本名称   {latest_version}\nVS Code 提交哈希   {latest_hash}\n")
        except Exception as e:
            print(f"无法获取最新版本信息，跳过更新: {e}")
            latest_version = current_version

        if latest_version.strip() != current_version.strip() or (hash_only and current_version.strip() != latest_hash):
            os.makedirs(VSCODE_DIR, exist_ok=True)
            try:
                for proc in subprocess.check_output(['tasklist'], universal_newlines=True).splitlines():
                    if "Code.exe" in proc:
                        pid = int(proc.split()[1])
                        proc_path = subprocess.check_output(['wmic', 'process', 'where', f'ProcessId={pid}', 'get', 'ExecutablePath'], universal_newlines=True).splitlines()
                        if len(proc_path) > 1 and VSCODE_EXE in proc_path[1]:
                            os.kill(pid, 9)
                            print(f"已结束进程 Code.exe (PID: {pid}) 位于 {proc_path[1]}")
            except Exception as e:
                print(f"结束进程失败: {e}")
            download_latest_version()
            if not os.path.exists(ZIPPER):
                print("没有找到7z.exe，我们无法解压更新包\n但是你可以手动解压（那就不叫自动化了")
                tmexit(1)
            try:
                backup_directories()
                app_old_zip = os.path.join(BASE_DIR, "app.old.7z")
                subprocess.run([ZIPPER, "a", app_old_zip, VSCODE_DIR], check=True)
                print("已将原来的 app 目录打包成 app.old.7z")
            except subprocess.CalledProcessError as e:
                print(f"打包失败:(7z) \n原因 {e}")
                tmexit(1)
            extract_and_install()
            print(f"安装成功！:)\n")
            current_version = latest_version
        else:
            print(f"你已是最新版本！无需更新:)\n")
    if os.path.exists(VSCODE_EXE):
        try:
            print("原神~启动（bushi\n")
            print(f"启动Code {current_version}")
            vscode_process = subprocess.Popen([VSCODE_EXE], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
            print("启动成功！( •̀ ω •́ )✧\n.")
            print("(╯▽╰ )~~按Enter键退出程序")
        except OSError as e:
            print(f"启动失败: {e}")
    else:
        print(f"未找到 Code 可执行文件: {VSCODE_EXE}")
except KeyboardInterrupt:
    print("^C\n退出")
except Exception as e:
    print(f"哎呀！程序失败了！别担心，Code还会继续启动。\n\n原因：{e}\n\n不过如果这是一个bug，请反馈给我\n链接[https://github.com/mrjiang32/CodePortable-Updater]！\n祝你使用愉快！(❁´◡`❁)")
    if os.path.exists(VSCODE_EXE):
        try:
            print(f"启动Code {current_version}")
            os.system("pause")
            vscode_process = subprocess.Popen([VSCODE_EXE], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
            print("启动成功！（你发issue了吗")
            print("(╯▽╰ )~~按Enter键退出程序")
        except OSError as e:
            print(f"启动失败: {e}")
    else:
        print(f"未找到 Code 可执行文件: {VSCODE_EXE}")