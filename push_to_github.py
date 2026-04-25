import os
import subprocess

# ====== CONFIGURE THIS ======
repo_url = ("notepad push_to_github.py"
            "https://github.com/ajmalnavascherada-arch/Experimental-Thermofluid-Data-Analysis-Transient-Heat-Transfer-Study.git")
commit_message = "Initial commit: thermofluid data analysis project"
# ============================

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)

def main():
    print("🚀 Initializing Git repository...")
    run_command("git init")

    print("📦 Adding files...")
    run_command("git add .")

    print("💾 Committing...")
    run_command(f'git commit -m "{commit_message}"')

    print("🔗 Connecting to GitHub...")
    run_command(f"git remote add origin {repo_url}")

    print("🌿 Setting main branch...")
    run_command("git branch -M main")

    print("⬆️ Pushing to GitHub...")
    run_command("git push -u origin main")

    print("✅ Done! Check your GitHub repo.")

if __name__ == "__main__":
    main()