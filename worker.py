from resonate import Resonate, Context
from threading import Event

resonate = Resonate.remote(group="worker")

@resonate.register
def sleeping_workflow(ctx: Context, wf_id: str, secs: float):
    print(f"Workflow {wf_id} starting, will sleep for {secs} seconds.")
    yield ctx.sleep(secs)
    return f"Workflow {wf_id} completed after sleeping for {secs} seconds."

resonate.start()

print("worker is running...")

Event().wait()
