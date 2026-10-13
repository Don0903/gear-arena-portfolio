# Setup leftovers

GitHub's drag-and-drop upload sometimes skips hidden files (names starting with a dot).
If your repo is missing `.gitignore` or `.github/workflows/update-progress.yml`:

1. On your repo page: **Add file → Create new file**.
2. Type the filename exactly: `.gitignore` (or `.github/workflows/update-progress.yml`;
   typing the slashes creates the folders).
3. Paste in the contents of `gitignore.txt` (or `update-progress.yml.txt`) from this folder.
4. **Commit changes**.

Once both exist, you can delete this `setup/` folder.
