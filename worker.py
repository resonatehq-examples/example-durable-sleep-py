from __future__ import annotations

import asyncio
import os
from typing import TYPE_CHECKING

from resonate.resonate import Resonate

if TYPE_CHECKING:
    from resonate.context import Context


async def sleeping_workflow(ctx: Context, wf_id: str, secs: float) -> str:
    print(f"Workflow {wf_id} starting, will sleep for {secs} seconds.")
    await ctx.sleep(secs)
    return f"Workflow {wf_id} completed after sleeping for {secs} seconds."


async def main() -> None:
    r = Resonate(
        url=os.environ.get("RESONATE_URL", "http://localhost:8001"),
        group="worker",
    )
    r.register(sleeping_workflow)
    print("worker is running...", flush=True)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
