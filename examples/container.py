"""This example showcases how to run a container, rather than a Python, function, as the payload of a task in Hera"""

from hera import Task, Workflow, WorkflowService

# TODO: replace the domain and token with your own
ws = WorkflowService(host='https://my-argo-server.com', token='my-auth-token')
w = Workflow('container', ws)

t = Task('cowsay', image='docker/whalesay', command=['cowsay', 'foo'])
w.add_task(t)
w.create()
