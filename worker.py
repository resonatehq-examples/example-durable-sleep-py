from resonate import Resonate, Context
from threading import Event

resonate = Resonate.remote(group="worker")

@resonate.register
def sleeping_workflow(ctx: Context, wf_id: str, dur: int):
    print(f"Workflow {wf_id} starting, will sleep for {dur} seconds.")
    yield ctx.sleep(dur)
    return f"Workflow {wf_id} completed after sleeping for {dur} seconds."

resonate.start()

print("worker is running...")

Event().wait()