# 28 - Virtual Environment (venv)

## What is a Virtual Environment?

A Virtual Environment is an isolated Python environment for a single project.

Each project can have:

- Different Python packages
- Different package versions
- Separate dependencies

without affecting other projects.

---

## Why Do We Need Virtual Environments?

Suppose:

Project A needs

```
numpy==1.24
```

Project B needs

```
numpy==2.2
```

Without a virtual environment, these versions would conflict.

With a virtual environment, each project has its own installation.

---

# Create a Virtual Environment

Windows

```bash
python -m venv .venv
```

Linux/macOS

```bash
python3 -m venv .venv
```

---

# Activate

Windows PowerShell

```powershell
.venv\Scripts\Activate
```

Windows CMD

```cmd
.venv\Scripts\activate.bat
```

Linux/macOS

```bash
source .venv/bin/activate
```

After activation you'll see something like:

```
(.venv)
```

at the beginning of the terminal prompt.

---

# Install Packages

```bash
pip install requests
```

```bash
pip install numpy
```

```bash
pip install pandas
```

---

# Check Installed Packages

```bash
pip list
```

---

# Save Dependencies

```bash
pip freeze > requirements.txt
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Deactivate

```bash
deactivate
```

---

# Delete a Virtual Environment

Deactivate it first.

Then simply delete the `.venv` folder.

---

# Project Structure

```
AI-Project/

│── .venv/
│── src/
│── data/
│── requirements.txt
│── README.md
│── .gitignore
```

---

# .gitignore

Never upload

```
.venv/
```

Always upload

```
requirements.txt
```

---

# Common Commands

Create

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\Activate
```

Deactivate

```bash
deactivate
```

Save packages

```bash
pip freeze > requirements.txt
```

Install packages

```bash
pip install -r requirements.txt
```

---

# Best Practices

✅ Create a new virtual environment for every project.

✅ Name it `.venv`.

✅ Commit `requirements.txt`.

✅ Ignore `.venv`.

✅ Use Python's built-in `venv` unless another tool is required.

---

# Common Interview Questions

## Why use a virtual environment?

To isolate project dependencies and prevent package conflicts.

---

## Why shouldn't we upload `.venv` to GitHub?

Because it is machine-specific, large, and can be recreated using `requirements.txt`.

---

## Difference between pip and venv?

- `pip` installs packages.
- `venv` creates an isolated Python environment.

---

## Difference between requirements.txt and pip freeze?

- `requirements.txt` is the dependency file.
- `pip freeze` generates its contents.

---

# Key Takeaways

- One virtual environment per project.
- Activate before installing packages.
- Save dependencies using `pip freeze`.
- Share `requirements.txt`, not `.venv`.