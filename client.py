from resonate import Resonate

resonate = Resonate.remote(group="client")

def main():
    try:
        id = "sleep-workflow-1"
        func = "sleeping_workflow"
        secs = 5.0
        handle = resonate.options(target="poll://any@worker").begin_rpc(id, func=func, wf_id=id, secs=secs)
        result = handle.result()
        print(result)
    except Exception as e:
        print(e)

main()
