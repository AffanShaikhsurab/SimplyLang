# Building Instructions for Simply Language

This document provides instructions for building the Simply Language interpreter and creating installers using two different methods: PyInstaller and Inno Setup.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.7+**: Required to run the Simply Language interpreter and build tools
- **pip**: Python package manager
- **Inno Setup**: Required for creating Windows installers (download from [innosetup.com](https://jrsoftware.org/isdl.php))
- **Git**: For version control and obtaining the source code

## Getting the Source Code

1. Clone the repository:

   ```bash
   git clone https://github.com/affanshaikhsurab/Simply-Lang.git
   cd Simply-Lang
   ```
2. Install development dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   If a requirements.txt file doesn't exist, install the following packages:

   ```bash
   pip install pyinstaller pytest
   ```

## Building with PyInstaller

PyInstaller bundles the Simply Language interpreter into a standalone executable.

### Step 1: Prepare Your Environment

1. Navigate to the project root directory:

   ```bash
   cd Simply-Lang
   ```
2. Ensure PyInstaller is installed:

   ```bash
   pip install pyinstaller
   ```

### Step 2: Build the Executable

1. **Option A**: Build using the spec file (recommended):

   ```bash
   # Navigate to the directory containing simply.py (main entry point)
   cd src
   # Copy the spec file to the current directory if needed
   copy ..\builder\installers\simply.spec .
   # Build using the spec file
   pyinstaller simply.spec
   ```
2. **Option B**: Build directly with PyInstaller:

   ```bash
   # Navigate to the directory containing simply.py
   cd src
   # Create a standalone executable
   pyinstaller --onefile --name simply simply.py
   ```

### Step 3: Verify the Build

After building, you should find the executable in the `dist` directory:

```bash
dist\simply.exe
```

Test the executable by running:

```bash
dist\simply.exe example\example.simply
```

## Building with Inno Setup

Inno Setup creates a Windows installer that handles installation, PATH setup, and shortcuts.

### Step 1: Build the Executable with PyInstaller

Complete the PyInstaller steps above to generate the `simply.exe` executable.

### Step 2: Prepare for Inno Setup

1. Ensure the `dist` directory containing `simply.exe` is in the correct location relative to the Inno Setup script.
2. If needed, modify the Inno Setup script (`builder\installers\simplylang_installer.iss`) to include additional files or change settings.

### Step 3: Compile the Installer

1. Open Inno Setup Compiler.
2. Open the script file:

   ```
   File > Open > Navigate to builder\installers\simplylang_installer.iss
   ```
3. Compile the installer:

   ```
   Build > Compile
   ```
4. Alternatively, compile from the command line:

   ```bash
   "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" "builder\installers\simplylang_installer.iss"
   ```

### Step 4: Locate the Installer

After compilation, find the installer in the output directory specified in the script:

```
builder\installers\Output\SimplyLangInstaller.exe
```

## Customizing the Build

### PyInstaller Customization

The `simply.spec` file contains configuration for PyInstaller. Common modifications include:

- Adding data files: Modify the `datas` list in the Analysis section
- Adding hidden imports: Add required modules to `hiddenimports`
- Changing the executable name: Modify the `name` parameter in the EXE section
- Adding an icon: Add `icon='path/to/icon.ico'` to the EXE section

### Inno Setup Customization

The `simplylang_installer.iss` file can be customized in several ways:

- Change application metadata: Modify `AppName`, `AppVersion`, etc.
- Add additional files: Add more `Source:` entries in the `[Files]` section
- Modify installation directory: Change `DefaultDirName`
- Add license agreement: Add a `LicenseFile` directive to the `[Setup]` section
- Customize icons: Modify the `[Icons]` section
- Add uninstaller: Add appropriate entries to create an uninstaller

## Troubleshooting

### PyInstaller Issues

- **Missing modules**: Add them to `hiddenimports` in the spec file
- **Missing files**: Add them to `datas` in the spec file
- **Executable not finding resources**: Use relative paths and ensure all resources are included

### Inno Setup Issues

- **File not found errors**: Ensure paths are correct relative to the .iss file
- **Permission issues**: Run Inno Setup as administrator
- **PATH not updated**: Check the Registry section in the .iss file

## Continuous Integration

For automated builds, consider setting up GitHub Actions or another CI system to:

1. Run tests
2. Build the executable with PyInstaller
3. Create the installer with Inno Setup
4. Upload artifacts to releases

A sample workflow file would be placed in `.github/workflows/build.yml`.

## Additional Resources

- [PyInstaller Documentation](https://pyinstaller.org/en/stable/)
- [Inno Setup Documentation](https://jrsoftware.org/ishelp/)
- [Simply Language Documentation](docs/documentation.md)
