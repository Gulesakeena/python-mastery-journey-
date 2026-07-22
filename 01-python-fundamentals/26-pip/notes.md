# 26 - Python PIP

## What is PIP?

PIP (Preferred Installer Program) is Python's official package manager.

It allows you to install, upgrade, remove, and manage third-party Python libraries.

Example libraries:

- NumPy
- Pandas
- Requests
- FastAPI
- Django
- TensorFlow
- OpenCV
- Scikit-learn

---

# Check Python Version

```bash
python --version
```

or

```bash
python3 --version
```

---

# Check PIP Version

```bash
pip --version
```

or

```bash
python -m pip --version
```

---

# Install a Package

```bash
pip install requests
```

Install multiple packages:

```bash
pip install numpy pandas matplotlib
```

Install a specific version:

```bash
pip install pandas==2.2.2
```

---

# Upgrade a Package

```bash
pip install --upgrade requests
```

---

# Uninstall a Package

```bash
pip uninstall requests
```

---

# List Installed Packages

```bash
pip list
```

---

# Show Package Information

```bash
pip show pandas
```

This displays:

- Version
- Location
- Dependencies
- Summary

---

# Freeze Installed Packages

Save installed packages:

```bash
pip freeze
```

Save to a file:

```bash
pip freeze > requirements.txt
```

---

# Install from requirements.txt

```bash
pip install -r requirements.txt
```

This is the standard way to install project dependencies.

---

# Search for a Package

Use the Python Package Index (PyPI):

https://pypi.org

> Note: `pip search` has been removed in recent versions of pip.

---

# Virtual Environments

Create a virtual environment:

```bash
python -m venv .venv
```

Activate (Windows PowerShell):

```powershell
.venv\Scripts\Activate
```

Activate (Linux/macOS):

```bash
source .venv/bin/activate
```

Deactivate:

```bash
deactivate
```

---

# Why Use Virtual Environments?

Without virtual environments:

- Package version conflicts
- Difficult dependency management
- Projects interfere with each other

With virtual environments:

- Each project has isolated dependencies.
- Easier collaboration.
- Reproducible environments.

---

# Best Practices

- Always use a virtual environment.
- Commit `requirements.txt` to Git.
- Do not commit the `.venv` folder.
- Keep packages updated when appropriate.
- Install only the libraries your project needs.

---

# Common Interview Questions

## What is PIP?

Python's package manager.

---

## What does `pip freeze` do?

Lists all installed packages in a format suitable for `requirements.txt`.

---

## Difference between `pip list` and `pip freeze`?

- `pip list` → Human-readable package list.
- `pip freeze` → Exact versions for dependency management.

---

## Why use `requirements.txt`?

To recreate the same Python environment on another machine.

---

## What is PyPI?

The Python Package Index, the official repository of Python packages.

---

# Key Takeaways

- Use `pip install` to install packages.
- Use `pip uninstall` to remove packages.
- Use `pip freeze > requirements.txt` to save dependencies.
- Use `pip install -r requirements.txt` to install project dependencies.
- Always use a virtual environment for real projects.