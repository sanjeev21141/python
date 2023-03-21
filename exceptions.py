class         GitError(Exception):
    pass

class        RepositoryException(GitError):
    pass

class        RepositoryNotFoundError(RepositoryException):
    message = 'No Repository found'

class        RepositoryEmpty(RepositoryException):
    message = 'No Commits on Repository'

class        StatusError(GitError):
    message = 'Error serializing the status'