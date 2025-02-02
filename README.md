# Treefile

Treefile is a Python package designed to generate file trees based on a plaintext configuration described in a `.treefile` file. It allows you to create complex directory structures with files and directories, optionally including virtual environments.

This project aims to simplify the process of setting up projects or generating boilerplate code by defining the structure in a simple text file.

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Command Line Arguments](#command-line-arguments)
- [Features](#features)
- [Configuration File](#configuration-file)
- [Context Menu Integration](#context-menu-integration)

---

### Installation

To install Treefile, use pip:

```bash
pip install treefile
```

Alternatively, you can clone the repository and install it manually:

```bash
git clone https://github.com/BenevolenceMessiah/treefile.git
cd treefile
python setup.py install
```

---

## Usage

Treefile reads a `.treefile` configuration file and generates the corresponding directory structure.

### Basic Usage

1. Create a `.treefile` file with your desired structure:

```plaintext
project/
    src/
        main.py
    README.md
```

2. Run Treefile:

```bash
treefile --file project.treefile --output output_dir
```

3. The files and directories will be created in the specified output directory.

---

### Sample `.treefile` File

This sample shows the optional 'tree branches'.

```plaintext
token-itemize/
├── token_itemize/
│   ├── __init__.py
│   ├── cli.py
│   └── main.py
└── tests/
    └── test_main.py
```

Running this with Treefile will create the full directory structure.

---

## Command Line Arguments

Treefile supports the following command line arguments:

```bash
treefile [OPTIONS] --file <PATH>
```

Available options:

- `--file <PATH>`: Path to the `.treefile` file (required)
- `--output <PATH>`: Output directory (default: current directory)
- `--venv <NAME>`: Name for virtual environment (default: .venv)
- `--py <VERSION>`: Python version for virtual environment
- `--activate`: Activate the virtual environment after creation
- `--dry-run`: Preview changes without creating files/directories
- `--force`: Overwrite existing files/directories if conflicts occur
- `--version`: Show package version

---

## Features

### 1. File Tree Generation

Treefile parses a `.treefile` file and creates the corresponding directory structure with files and directories.

### 2. Virtual Environment Management

Treefile can create virtual environments based on specified Python versions. If you include a `venv` section in your configuration, it will automatically handle environment creation.

### 3. Context Menu Integration

Treefile supports right-click context menu integration for `.treefile` files on Windows, macOS, and Linux:

- **Windows**: Register the context menu using `register_icon.bat`
- **macOS/Linux**: Use `register_icon.sh` to set up custom file icons and context menu actions.

### 4. Embedded Configuration

You can embed configuration options directly in your `.treefile` file by adding a comment line starting with `#!treefile:`:

```plaintext
# !treefile: --venv .venv --py python3.8
```

---

## Configuration File

Treefile uses a `config.yaml` file for default settings:

```yaml
venv: ".venv"
python: "python"
output: "."
```

This allows you to set defaults for virtual environments, Python versions, and output directories.

---

## Context Menu Integration

### Windows

Run the following command to register the context menu:

```cmd
scripts/register_icon.bat
```

### macOS/Linux

Make the script executable and run it:

```bash
chmod +x scripts/register_icon.sh && ./scripts/register_icon.sh
```

---

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request.

---

## License

Treefile is distributed under the MIT License. See [LICENSE](LICENSE) for details.
