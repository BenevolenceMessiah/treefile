# Treefile Documentation

Treefile is a Python package that generates file trees based on a plaintext configuration described in a `.treefile` file. This documentation provides an overview of its features, usage, and integration options.

---

## What is Treefile?

Treefile allows you to define complex directory structures with files and directories in a simple text format. It parses this configuration and creates the corresponding structure in your filesystem. The package also includes support for virtual environments and context menu integration.

---

## Features

### 1. File Tree Generation

Define your project structure using indentation and ASCII tree characters:

```plaintext
project/
├── src/
│   └── main.py
└── README.md
```

Treefile will create all files and directories as specified.

### 2. Virtual Environment Management

Create virtual environments with specified Python versions directly from your `.treefile` configuration:

```plaintext
# !treefile: --venv .venv --py python3.8
project/
└── src/
    └── main.py
```

### 3. Context Menu Integration

Treefile supports right-click context menu integration for `.treefile` files on Windows, macOS, and Linux:

- **Windows**: Use `register_icon.bat`
- **macOS/Linux**: Use `register_icon.sh`

---

## Configuration File

The configuration file (`config.yaml`) allows you to set defaults for virtual environments, Python versions, and output directories:

```yaml
venv: ".venv"
python: "python3.8"
output: "output_dir/"
```

---

## Advanced Usage

### 1. Caching

Treefile caches checksums of `.treefile` files to avoid unnecessary processing when no changes are detected.

### 2. Virtual Environment Activation

After creating a virtual environment, you can activate it directly from the command line:

```bash
treefile --file project.treefile --activate
```

---

## Integration with Operating Systems

### Windows

- File extension association: `.treefile` files will be recognized as Treefile documents.
- Context menu action: "Unpack Treefile"

### macOS/Linux

- Custom file icons for `.treefile` files.
- Desktop entry integration.

---

## Conclusion

Treefile is a versatile tool for managing project structure generation. Its combination of simple configuration files, virtual environment support, and cross-platform context menu integration makes it an essential utility for developers working on complex projects.

For more information or to contribute, visit the [GitHub repository](https://github.com/BenevolenceMessiah/treefile).
