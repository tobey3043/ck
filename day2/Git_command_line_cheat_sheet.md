# 🧠 Git Command Cheat Sheet

A quick reference for essential Git commands like `pull`, `push`, `merge`, `fetch`, resolving merge conflicts, and merge strategies like `rebase` and `--ff`.

---

## 🔄 git pull

Fetches changes from a remote repository and merges them into your current branch.

```bash
git pull origin main
```

➡️ Equivalent to:
```bash
git fetch origin main
git merge origin/main
```

---

## 📤 git push

Sends your committed changes to a remote repository.

```bash
git push origin main
```

📝 Use after `git commit` to publish your changes.

---

## 🔀 git merge

Combines changes from one branch into another.

```bash
git checkout main        # Switch to target branch
git merge feature-branch
```

🎯 Use this to bring in changes from a feature or topic branch.

---

## 🚀 git merge --ff (Fast-Forward)

If the current branch has no new commits since it diverged from the branch being merged, Git will **fast-forward** — simply moving the pointer forward without creating a new commit.

```bash
git checkout main
git merge --ff feature-branch
```

✅ Pros:
- Keeps history linear
- No extra merge commits

❌ Not possible if both branches have diverged

### Force a merge commit (even when fast-forward is possible):

```bash
git merge --no-ff feature-branch
```

---

## 📥 git fetch

Downloads changes from the remote but **does not merge** them.

```bash
git fetch origin
```

🔎 Good for checking what's new before merging:
```bash
git log HEAD..origin/main
```

---

## ⚔️ Resolving Merge Conflicts

Git marks conflicts like this:

```
<<<<<<< HEAD
Your changes
=======
Incoming changes
>>>>>>> branch-name
```

1. Edit the file to resolve the conflict  
2. Stage the file with `git add`  
3. Finish the merge with `git commit`

Or abort with:
```bash
git merge --abort
```

---

## 🧬 Merge Strategies

### 🔁 git merge
Preserves full history with a new merge commit:
```bash
git merge feature-branch
```

### 🔃 git rebase
Rewrites history for a linear timeline:
```bash
git checkout feature-branch
git rebase main
```

Then:
```bash
git checkout main
git merge feature-branch  # fast-forward if possible
```

Avoid rebasing shared/public branches!

---

## ✨ Bonus Commands

- Create a branch: `git checkout -b feature-name`
- Stage + commit: `git add . && git commit -m "Message"`
- Check status: `git status`
- View history: `git log --oneline --graph --all`

---

🧩 Tip: Use `merge --no-ff` for clearer history when merging feature branches.
