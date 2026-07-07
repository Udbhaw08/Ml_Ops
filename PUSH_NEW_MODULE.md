# How to push a new module folder to Ml_Ops

This documents the actual (safe) process for adding a new course module folder — e.g. a
new folder you create while following along with a course — into the shared repo:
**https://github.com/Udbhaw08/Ml_Ops**

> Note: this supersedes the "fresh repo + force-push" recipe in the root `CLAUDE.md`.
> That recipe replaces the *entire* history of `main` with just one module, which wipes
> out every other module folder already pushed. The steps below merge the new module
> into the existing repo tree instead, so nothing else gets clobbered.

## 1. Prep the module folder locally

Inside your new module folder (e.g. `ML_OPS_UDEMY/<new-module-name>/`):

```bash
cd "e:/Udbhaw_Work/Udbhaw_Work/ML_OPS_UDEMY/<new-module-name>"

# add a .gitignore before the first commit — keep run artifacts, envs, secrets out
cat > .gitignore <<'EOF'
mlruns/
.env
__pycache__/
*.pyc
.venv/
venv/
EOF

git init -q
git checkout -q -b main
git add -A
git commit -q -m "Initial commit: <new-module-name> module"
```

Skip this step if the folder is already its own git repo with commits you're happy with.

## 2. Get a clean copy of the shared repo

```bash
SCRATCH=/path/to/scratch/ml_ops_push
rm -rf "$SCRATCH"
git clone -q https://github.com/Udbhaw08/Ml_Ops.git "$SCRATCH"
```

## 3. Copy the module's tracked files into the shared repo, under its own folder

Using `git archive` exports only tracked, committed files — `.env`, local secrets, and
anything gitignored (like `mlruns/`) never make it in.

```bash
mkdir -p "$SCRATCH/<new-module-name>"
cd "e:/Udbhaw_Work/Udbhaw_Work/ML_OPS_UDEMY/<new-module-name>"
git archive main | tar -x -C "$SCRATCH/<new-module-name>"
```

## 4. Commit and push (no force needed)

```bash
cd "$SCRATCH"
git add -A
git commit -q -m "Add <new-module-name> module"
git push origin main
```

Because this builds on top of the existing history rather than replacing it, a normal
push works — no `--force`, and every previously pushed module folder stays intact.

## Result

The shared repo ends up looking like:

```
Ml_Ops/
  11-End_to_End_project/
    ...
  dsproject/
    ...
  <new-module-name>/
    ...
```

## Secrets checklist before every push

- Never commit MLflow/DagsHub credentials directly in `.py` files — use
  `python-dotenv` + a local `.env` (gitignored).
- DVC remotes pointing at DagsHub's S3-compatible storage need credentials in
  `.dvc/config.local` (gitignored), not `.dvc/config` (committed). Use the DagsHub
  token as both the access key ID and secret access key.
- Double-check `git status` in the module folder before archiving — anything shown as
  untracked or ignored won't make it into the push, which is what you want for secrets
  and run artifacts.
