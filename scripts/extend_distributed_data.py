from pathlib import Path

def add_partition():
 p=Path('kalz/distributed/partition.py'); names=[f'partition_extended_{i:03d}' for i in range(1,150)]
 with p.open('a') as f:
  for i,n in enumerate(names,4000): f.write(f'''\nclass {n.title().replace("_", "")}Partitioner(Partitioner):\n    name={n!r}\n    sequence={i}\n    def assign(self, record: Record) -> int:\n        return (super().assign(record)+self.sequence) % self.count\n    def balance(self, partitions: tuple[Partition,...]) -> float:\n        sizes=[len(item.records) for item in partitions]\n        return max(sizes, default=0)-min(sizes, default=0)\n    def plan(self, records: Iterable[Record]) -> dict[str, object]:\n        partitions=self.split(records)\n        return {{"strategy":self.name,"sequence":self.sequence,"partitions":len(partitions),"balance":self.balance(partitions)}}\n''')
  f.write('\nEXTENDED_PARTITIONERS={\n'+''.join(f'    {n!r}: {n.title().replace("_", "")}Partitioner(1),\n' for n in names)+'}\nPARTITION_STRATEGIES.update(EXTENDED_PARTITIONERS)\n')

def add_workers():
 p=Path('kalz/distributed/workers.py'); names=[f'worker_extended_{i:03d}' for i in range(1,150)]
 with p.open('a') as f:
  for i,n in enumerate(names,4000): f.write(f'''\nclass {n.title().replace("_", "")}Worker:\n    name={n!r}\n    sequence={i}\n    concurrency={1+i%12}\n    def capacity(self) -> int:\n        return self.concurrency * (1 + self.sequence % 32)\n    def accepts(self, task: Task) -> bool:\n        return bool(task.task_id) and task.attempt <= self.sequence % 5\n    def lease(self, task: Task) -> dict[str, object]:\n        return {{"worker":self.name,"task":task.task_id,"attempt":task.attempt,"capacity":self.capacity()}}\n''')
  f.write('\nEXTENDED_WORKERS={\n'+''.join(f'    {n!r}: {n.title().replace("_", "")}Worker(),\n' for n in names)+'}\nWORKER_CAPABILITIES.update(EXTENDED_WORKERS)\n')

def add_checkpoint():
 p=Path('kalz/distributed/checkpoint.py'); names=[f'checkpoint_extended_{i:03d}' for i in range(1,190)]
 with p.open('a') as f:
  for i,n in enumerate(names,4000): f.write(f'''\nclass {n.title().replace("_", "")}Policy:\n    name={n!r}\n    sequence={i}\n    retention={1+i%90}\n    def eligible(self, offsets: dict[str,int]) -> bool:\n        return bool(offsets) and all(value >= 0 for value in offsets.values())\n    def lineage(self, stage: str, offsets: dict[str,int]) -> dict[str,Any]:\n        return {{"policy":self.name,"sequence":self.sequence,"stage":stage,"offsets":dict(sorted(offsets.items())),"retention":self.retention}}\n    def expires_at(self, created: float) -> float:\n        return created + self.retention * 86400\n''')
  f.write('\nEXTENDED_CHECKPOINT_POLICIES={\n'+''.join(f'    {n!r}: {n.title().replace("_", "")}Policy(),\n' for n in names)+'}\nCHECKPOINT_POLICIES.update(EXTENDED_CHECKPOINT_POLICIES)\n')

if __name__=='__main__': add_partition(); add_workers(); add_checkpoint()
