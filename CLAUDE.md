# ML_OPS_UDEMY

This directory contains multiple independent ML/MLOps course modules (`1-MLproject`, `11-End_to_End_project`, `2-Deeplearning`, etc.). The root itself is **not** a git repository — each module folder is its own standalone git repo with its own history, remotes, and (where used) DVC config.

## GitHub target: one shared repo, one subfolder per module

All modules get pushed to a single shared GitHub repo: **https://github.com/Udbhaw08/Ml_Ops**

Each module lands in that repo under a folder named after the module (matching its local folder name here), never flattened at the repo root:

```
Ml_Ops/
  11-End_to_End_project/
    Machine_Learning_pipeline/...
  1-MLproject/
    ...
  2-Deeplearning/
    ...
```

## How to push a module

A module's local git history is often the raw course-template history (e.g. author "Krish Naik", possibly containing an old hardcoded credential in some early commit). Don't push that history as-is. Instead, squash the module's *current* committed state into a single clean commit, nested under `<module-folder-name>/`, then push/force-push it into `Ml_Ops`:

```bash
# from inside the module's own repo (e.g. Machine_Learning_pipeline)
SCRATCH=/path/to/scratch/ml_ops_push
rm -rf "$SCRATCH"
mkdir -p "$SCRATCH/<module-folder-name>"
git archive main | tar -x -C "$SCRATCH/<module-folder-name>"

cd "$SCRATCH"
git init -q && git checkout -q -b main
git add -A
git commit -q -m "Initial commit: <module> module"
git remote add github https://github.com/Udbhaw08/Ml_Ops.git
git push --force github main
```

- `git archive main` exports only the tracked, committed files (respects `.gitignore`), so `.env`, `.dvc/config.local`, and other local secrets never get included.
- Force-push is expected here since each module's history is being replaced/restructured on the shared repo — this repo is meant to hold clean snapshots, not full course-template history.
- Repeat per module, changing the folder name and the `main` ref/source repo each time.

## Secrets

- Never commit MLflow/DagsHub credentials directly in `.py` files. Use `python-dotenv` + a local `.env` (gitignored) — see `11-End_to_End_project/Machine_Learning_pipeline/.env.example` for the pattern.
- DVC remotes pointing at DagsHub's S3-compatible storage need credentials in `.dvc/config.local` (gitignored), **not** `.dvc/config` (committed). For DagsHub S3 auth, use the DagsHub token as *both* `access_key_id` and `secret_access_key` — not the username as the key ID.

## Known cleanup

- A stray top-level `.git` + empty `.dvc` scaffold was previously found directly inside `11-End_to_End_project/` (0 commits, no remote) — likely an accidental `git init`/`dvc init` run one directory too high. It was deleted. If you see a similar stray repo appear in a module's parent folder again, it's safe to delete if it has 0 commits and no remote.
