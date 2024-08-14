import asyncio
import threading
from concurrent.futures import ThreadPoolExecutor
from collections.abc import Iterable

class FunctionHandler:
    def __init__(self, executor):
        self.executor = executor
        
    def gather(self, fns, args):
        futures = []
        for (i, fn) in enumerate(fns): 
            if args[i] is None:
                futures.append(self.executor.submit(fn))
            elif isinstance(args[i], Iterable):
                futures.append(self.executor.submit(fn, *args[i]))
            else:
                futures.append(self.executor.submit(fn, args[i]))
        return [f.result() for f in futures]

