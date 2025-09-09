![durable sleep banner](/assets/durable-sleep-readme-banner.png)

# Durable sleep

**Resonate Python SDK**

This example application showcases the sleep API that enables a function to reliably sleep for days, weeks, or even years if needed.

## Problem

A business process may need to sleep for a period much longer than the typical lifetime of a process.

Since a process is more likely to crash the longer it is alive, and if a business process needs to suspend (or "sleep") for days, weeks, or even years, then developers are often forced to use cron jobs as a means to reawaken long-sleeping processes.

This leads to complexity that is hard to reason about, test, and rely on.

## Solution

Resonate enables developers to sleep directly in their workflows without leaving the process running idle, reducing implementation complexity while ensuring the business process can survive across process crashes.

## How to run this example

Run a Resonate Server:

```
brew install resonatehq/tap/resonate
resonate dev
```

If you don't have brew, try one of these other [installation options](https://docs.resonatehq.io/operate/server-installation).

Install dependencies:

```shell
uv sync
```

Run the worker

```shell
uv run worker.py
```

Run the client

```shell
uv run client.py
```
