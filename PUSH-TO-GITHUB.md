# Push this repo to your GitHub

This folder is already a local git repository with your first commit made. You just
need to create the repo on GitHub and push. Pick ONE of the two options below.

Your GitHub username is **okasgreat**. Suggested repo name: **sdlc-ai-pipeline-practice**.

## Option A - GitHub CLI (easiest, one command)

If you have the `gh` CLI installed and logged in:

```bash
gh repo create sdlc-ai-pipeline-practice --public --source=. --remote=origin --push
```

That creates the repo and pushes in one shot. Check login first with `gh auth status`;
if it says you are not logged in, run `gh auth login` once.

## Option B - plain git (works everywhere)

1. On github.com, click **New repository**. Name it `sdlc-ai-pipeline-practice`.
   Leave "Initialize with README" UNCHECKED (you already have one). Create it.
2. Copy the repo URL it shows, then run from this folder:

```bash
git branch -M main
git remote add origin https://github.com/okasgreat/sdlc-ai-pipeline-practice.git
git push -u origin main
```

If git asks for a password, use a **Personal Access Token** (GitHub no longer accepts
your account password here): github.com -> Settings -> Developer settings ->
Personal access tokens -> generate one with `repo` scope, and paste it as the password.

## After you push

Your work on each stage becomes a visible commit history, exactly the kind of thing worth
linking from a LinkedIn post about the lecture.
