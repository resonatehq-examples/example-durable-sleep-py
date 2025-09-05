![Resonate example app Readme banner](/assets/resonate-example-app-readme-banner.png)

# Durable sleep

![durable sleep banner](/assets/durable-sleep-readme-banner.png)

**Resonate Python SDK**

This example application showcases the Context.sleep() function API that enables a function to reliably sleep for days, weeks, or even years if needed.

## Problem

A business process may need to sleep for a period of time that is much longer than the probable lifetime of a process.

In other words, a process is likely to crash the longer it is alive, and if a business process needs to "suspend", or "sleep", for days or weeks, or even years, then developers are often forced to use cron jobs as a means to reawaken long sleeping processes.

This leads to complexity that is hard to reason about, test, and rely on.

## Solution

Resonate enables developers to handle that sleep directly in their workflows, reducing the complexity of the implemntation while also knowing that it can survive process crashes.
