# 🧰 Git Cheat Sheet

A quick reference for everyday Git commands and best practices.

---

## 📦 Getting Started

### Initialize a new repository
```bash
git init
```

### Clone an existing repository
```bash
git clone https://github.com/username/repo.git
```

---

## 🧾 Staging and Committing

### Check status
```bash
git status
```

### Add files to staging
```bash
git add filename.py        # Add specific file
git add .                  # Add all changes
```

### Commit staged changes
```bash
git commit -m "Your commit message"
```

---

## 🔄 Sync with Remote

### Link a remote repository
```bash
git remote add origin https://github.com/username/repo.git
```

### Push to GitHub
```bash
git push origin main       # Push main branch
```

### Pull updates from remote
```bash
git pull origin main
```

---

## 🌿 Branching

### Create a new branch
```bash
git checkout -b feature-branch
```

### Switch branches
```bash
git checkout main
```

### Merge a branch
```bash
git checkout main
git merge feature-branch
```

---

## 🧹 Cleaning Up

### Remove deleted files from Git
```bash
git rm filename.py
```

### Rename a file
```bash
git mv oldname.py newname.py
```

---

## 🔍 History & Diffs

### View commit history
```bash
git log
```

### View file differences
```bash
git diff
```

---

## 🆘 Help

### Get help on any command
```bash
git help <command>
# or
git <command> --help
```

---

## ✅ Best Practices

- Commit often with clear messages.
- Use `.gitignore` to keep sensitive or unnecessary files out of Git.
- Pull before you push.
- Never commit raw data or secrets!

---

