[Setup]
AppName=SimplyLang
AppVersion=1.0
DefaultDirName={pf}\SimplyLang
DefaultGroupName=SimplyLang
OutputDir=.\Output
OutputBaseFilename=SimplyLangInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "./dist/simply.exe"; DestDir: "{app}"; Flags: ignoreversion

[Registry]
; Add the install directory to the PATH (for all users)
Root: HKCU; Subkey: "Environment"; ValueName: "Path"; ValueType: string; ValueData: "{app}"; Flags: uninsdeletevalue

[Icons]
Name: "{group}\SimplyLang"; Filename: "{app}\your_script.exe"
