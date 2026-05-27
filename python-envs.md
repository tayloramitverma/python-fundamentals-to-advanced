# Python Environment Setup

## Global Python (default)
Conda base is your only global Python. Always active by default.

```bash
conda activate base
```

Use this for everything — Hitesh course, scripts, general packages.
Python version: 3.13.9 | Location: /opt/anaconda3

---

## Udemy Project (isolated venv)
Activate only when working on the Udemy course:

```bash
source "/Users/tayloramitverma/Downloads/AI-Learning/Gen AI/Python-Udemy/venv/bin/activate"
```

Go back to global when done:

```bash
deactivate
```

---

## Check which Python is active

```bash
which python3
```

- `/opt/anaconda3/bin/python3` → conda base (global) ✅
- `.../Python-Udemy/venv/bin/python3` → Udemy venv is active

---

## Install a package globally

```bash
conda activate base
pip install <package>
```

---

## Python installations on this machine

| Source       | Version | Notes                        |
|--------------|---------|------------------------------|
| Conda base   | 3.13.9  | Global default — use this    |
| macOS system | 3.9.6   | Apple built-in, leave alone  |
