; 脚本由 Inno Setup 脚本向导 生成！
; 有关创建 Inno Setup 脚本文件的详细资料请查阅帮助文档！

#define MyAppName "modrinth-api小助手"
#define MyAppVersion "1.0.1"
#define MyAppPublisher "GavinCQTD"
#define MyAppURL "https://github.com/gi-b716/modrinth-api-tools"
#define MyAppExeName "modrinth-api小助手 v1.0.1.exe"

[Setup]
; 注: AppId的值为单独标识该应用程序。
; 不要为其他安装程序使用相同的AppId值。
; (若要生成新的 GUID，可在菜单中点击 "工具|生成 GUID"。)
AppId={{6C897194-4F27-4165-830F-58123E5F83CC}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\ma_tools
DisableProgramGroupPage=yes
LicenseFile=C:\Users\sgany\Desktop-other\python_work\modrinth_api\lasted\LICENSE\LICENSE.txt
InfoBeforeFile=C:\Users\sgany\Desktop-other\python_work\modrinth_api\setup_InfoBeforeFile.txt
; 以下行取消注释，以在非管理安装模式下运行（仅为当前用户安装）。
;PrivilegesRequired=lowest
OutputDir=C:\Users\sgany\Desktop-other\python_work\modrinth_api\r
OutputBaseFilename=ma_setup v1.0.1
SetupIconFile=C:\Users\sgany\Desktop-other\python_work\modrinth_api\lasted\logo.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "chinesesimp"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\sgany\Desktop-other\python_work\modrinth_api\lasted\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\sgany\Desktop-other\python_work\modrinth_api\lasted\Tools\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\sgany\Desktop-other\python_work\modrinth_api\lasted\Scripts\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\sgany\Desktop-other\python_work\modrinth_api\lasted\LICENSE\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\sgany\Desktop-other\python_work\modrinth_api\lasted\libs\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\sgany\Desktop-other\python_work\modrinth_api\lasted\Lib\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\sgany\Desktop-other\python_work\modrinth_api\lasted\include\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\sgany\Desktop-other\python_work\modrinth_api\lasted\DLLs\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\sgany\Desktop-other\python_work\modrinth_api\lasted\logo.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\sgany\Desktop-other\python_work\modrinth_api\lasted\main.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\sgany\Desktop-other\python_work\modrinth_api\lasted\module_connection_test.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\sgany\Desktop-other\python_work\modrinth_api\lasted\module_get_project.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\sgany\Desktop-other\python_work\modrinth_api\lasted\python.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\sgany\Desktop-other\python_work\modrinth_api\lasted\python3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\sgany\Desktop-other\python_work\modrinth_api\lasted\python39.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\sgany\Desktop-other\python_work\modrinth_api\lasted\pythonw.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\sgany\Desktop-other\python_work\modrinth_api\lasted\vcruntime140.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\sgany\Desktop-other\python_work\modrinth_api\lasted\vcruntime140_1.dll"; DestDir: "{app}"; Flags: ignoreversion
; 注意: 不要在任何共享系统文件上使用“Flags: ignoreversion”

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

