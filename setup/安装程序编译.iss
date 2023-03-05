; �ű��� Inno Setup �ű��� ���ɣ�
; �йش��� Inno Setup �ű��ļ�����ϸ��������İ����ĵ���

#define MyAppName "modrinth-apiС����"
#define MyAppVersion "1.0.1"
#define MyAppPublisher "GavinCQTD"
#define MyAppURL "https://github.com/gi-b716/modrinth-api-tools"
#define MyAppExeName "modrinth-apiС���� v1.0.1.exe"

[Setup]
; ע: AppId��ֵΪ������ʶ��Ӧ�ó���
; ��ҪΪ������װ����ʹ����ͬ��AppIdֵ��
; (��Ҫ�����µ� GUID�����ڲ˵��е�� "����|���� GUID"��)
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
; ������ȡ��ע�ͣ����ڷǹ���װģʽ�����У���Ϊ��ǰ�û���װ����
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
; ע��: ��Ҫ���κι���ϵͳ�ļ���ʹ�á�Flags: ignoreversion��

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

