from git import Repo

def push_code(local_path, branch):
    repo = Repo.clone_from("https://github.com/Pankajg3432c/Intern-platform.git", "repo")
    new_branch = repo.create_head(branch)
    new_branch.checkout()
    repo.git.add(all=True)
    repo.index.commit("Intern code submission")
    repo.remote().push(branch)
