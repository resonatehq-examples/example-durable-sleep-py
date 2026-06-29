from __future__ import annotations

import asyncio
import os

from resonate.resonate import Resonate


async def main() -> None:
    r = Resonate(url=os.environ.get("RESONATE_URL", "http://localhost:8001"))
    try:
        promise_id = "sleep-workflow-1"
        secs = 5.0
        handle = r.options(target="worker").rpc(
            promise_id, "sleeping_workflow", wf_id=promise_id, secs=secs
        )
        result = await handle.result()
        print(result)
    except Exception as e:
        print(e)
    finally:
        await r.stop()


if __name__ == "__main__":
    asyncio.run(main())
