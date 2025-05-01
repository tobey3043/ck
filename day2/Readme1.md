# 🔐 Setting Up SSH for GitHub (Optional but Recommended)

## 0.1 🔍 Check for Existing SSH Keys

```bash
ls -al ~/.ssh
```

Look for files like `id_ed25519.pub` or `id_rsa.pub`. If they exist, you might already have a key.

---

## 0.2 🧾 Generate a New SSH Key

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Press Enter to accept the default file location. Optionally, add a passphrase for security.

---

## 0.3 🧠 Add the Key to the SSH Agent

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

---

## 0.4 📋 Copy the Public Key

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the output.

---

## 0.5 🌐 Add the SSH Key to GitHub

1. Go to GitHub → Profile → **Settings**
2. Navigate to **SSH and GPG Keys**
3. Click **New SSH Key**
4. Paste your public key and save

---

## 0.6 🧪 Test the Connection

```bash
ssh -T git@github.com
```

You should see a success message like:

```bash
Hi your_username! You've successfully authenticated...
```

---

# 🛠️ Contributing to This Project (Step-by-Step)

## 1. 🔱 Fork the Repository

Go to the original repository on GitHub (provided by your instructor) and click the **"Fork"** button in the top-right corner.  
This will create **your own copy** of the repository under your GitHub account.

---

## 2. 💻 Clone Your Fork

Open a terminal and run:

```bash
git clone git@github.com:your-username/repo-name.git
```

Replace `your-username` and `repo-name` with your actual GitHub username and repository name.  
If you're using HTTPS instead of SSH:

```bash
git clone https://github.com/your-username/repo-name.git
```

---

## 3. 📂 Change into the Project Directory

```bash
cd repo-name
```

---

## 4. 🔧 Make Some Changes

Edit one or more files using your favorite code editor (e.g., VSCode, nano, etc.).  
For example:

```bash
nano yourfile.md
```

---

## 5. ✅ Stage and Commit the Changes

```bash
git add .
git commit -m "Made some changes to my file"
```

---

## 6. 🚀 Push to Your Fork (Origin)

```bash
git push origin main
```

Use the branch name you're working on (e.g., `main`, `dev`, or `feature-branch`).

---

## 7. 🔁 Make a Pull Request

1. Go to **your fork** on GitHub.
2. Click **"Compare & pull request"**.
3. Make sure the base repository is the instructor’s original repo.
4. Write a meaningful title and description.
5. Click **"Create pull request"**.

---

That’s it! You've submitted your contribution. 
