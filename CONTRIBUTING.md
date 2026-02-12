# 🤝 Contributing Guidelines

Thank you for contributing to the Crop Disease Monitoring & Prediction System.

To maintain clean and structured development, please follow the guidelines below.

---

## 🌿 Branching Strategy

- `main` → Stable production code
- `dev` → Active development branch
- `feature/*` → Individual feature branches

---

## 🔁 Development Workflow

1. Create a new branch from `dev`
2. Work on your assigned issue
3. Commit changes with clear messages
4. Push branch to GitHub
5. Open a Pull Request (PR) to `dev`
6. Wait for review before merging

---

### 📝 Commit Message Convention

To maintain a clean and professional Git history, we follow a structured commit message format.

---

### 📌 Format

git commit -m "type: short description (#issue-number)"


---

### 🔎 What Each Part Means

- **type** → The kind of change you made  
- **short description** → A brief explanation of what you changed  
- **(#issue-number)** → The GitHub issue this commit solves  

---

### 🏷 Common Commit Types

| Type      | Usage |
|-----------|--------|
| feat      | Adding a new feature |
| fix       | Fixing a bug |
| docs      | Updating documentation |
| style     | UI or formatting changes |
| refactor  | Improving existing code |
| chore     | Minor maintenance tasks |

---

### ✅ Real Examples From This Project

If Issue #8 is:

> Setup Flask backend

Then commit like this:

git commit -m "feat: setup Flask backend structure (#8)"


---

If Issue #12 is:

> Create image upload page

Then commit like this:

git commit -m "feat: implemented image upload UI (#12)"


---

If Issue #17 is:

> Fix API response bug

Then commit like this:

git commit -m "fix: corrected API response format (#17)"


---

If you update documentation:

git commit -m "docs: updated README structure"


---

### ❌ Avoid These Commit Messages

done
update
changes
fixed


These messages do not clearly explain what was changed.

---

Following this convention helps:

- Keep project history organized
- Track which issue was solved
- Improve collaboration
- Maintain professional workflow

---

## 📌 Important Rules

- Do NOT push directly to `main`
- Always link commits to issues
- Keep pull requests small and focused
- Follow clean code practices

---

## 👑 Code Review Process

- Project Lead will review all PRs
- Suggestions must be addressed before merging
- Merge only after approval

---

Thank you for contributing 🚀
