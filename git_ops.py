import os
import re
import datetime

from python_git_lib.git_service import GitService


class GitOps:
    _service = GitService.instance()

    def __init__(self, path: str):
        self.path = path
        self._global_args = ['-C', self.path]

    def execute(self, command: str, *args) -> str:
        response = self._service.run_git_command(*self._global_args,
                                                 *command.split(' '), *args)
        return response.stdout.decode('utf8')

    def clone(self, url: str, name: str = 'origin'):
        self.execute(f'clone {url}')
        return ("Cloned")

    def git_add(self, files: str = "."):
        self.execute(f'add {files}')
        return ("added")

    def git_commit(self, message: str = "default commit msg from gitops"):
        self.execute(f'commit -m {message}')
        return ("Commited")

    def git_push(self, remote: str = "origin", branch: str = "main"):
        self.execute(f'push {remote} {branch}')
        return ("Pushed")

    def git_pull(self, remote: str = "origin", branch: str = "main"):
        self.execute(f'pull {remote} {branch}')
        return ("pulled")