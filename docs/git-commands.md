# Git Commands

Your original commands had several spacing/name issues. Use this cleaned version:

```bash
echo "# clash-subscription" >> README.md
git init
git add README.md
git commit -m "第一次提交"
git branch -M main
git remote add origin https://github.com/liyan-lucky/clash-subscription.git
git push -u origin main
```

Common mistakes to avoid:

- `echo"..."` should be `echo "..."`
- `git commit-m` should be `git commit -m`
- `git分支-M` should be `git branch -M`
- `git远程添加源` should be `git remote add origin`
- `git push-u源主` should be `git push -u origin main`
