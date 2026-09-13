from pathlib import Path

def append_shuffle():
 p=Path('kalz/distributed/shuffle.py'); names=[f'shuffle_extended_{i:03d}' for i in range(1,100)]
 with p.open('a') as f:
  for i,n in enumerate(names,4000): f.write(f'''\nclass {n.title().replace("_", "")}Operator(ShuffleOperator):\n    name={n!r}\n    sequence={i}\n    def map(self, record: Record) -> tuple[str,Any]:\n        return f"{{self.sequence}}:{{record.key}}", record.value\n    def reduce(self, key: str, values: list[Any]) -> Any:\n        return {{"key":key,"count":len(values),"sample":values[:3],"sequence":self.sequence}}\n    def validate(self, batch: ShuffleBatch) -> bool:\n        return bool(batch.batch_id) and batch.partition_id >= 0\n''')
  f.write('\nEXTENDED_SHUFFLE_OPERATORS={\n'+''.join(f'    {n!r}: {n.title().replace("_", "")}Operator(),\n' for n in names)+'}\nSHUFFLE_OPERATORS.update(EXTENDED_SHUFFLE_OPERATORS)\n')

def append_pipeline():
 p=Path('kalz/distributed/pipeline.py'); names=[f'distributed_extended_{i:03d}' for i in range(1,125)]
 with p.open('a') as f:
  for i,n in enumerate(names,4000): f.write(f'''\nclass {n.title().replace("_", "")}Stage:\n    name={n!r}\n    sequence={i}\n    input_stage=''\n    def stage(self) -> Stage:\n        return Stage(self.name, (), (f"{{self.name}}:output",))\n    def watermark(self, timestamp: float) -> float:\n        return max(0.0, timestamp)\n    def fingerprint(self) -> str:\n        return hashlib.sha256(f"{{self.name}}:{{self.sequence}}".encode()).hexdigest()\n    def recovery(self, failed: bool) -> dict[str,object]:\n        return {{"stage":self.name,"sequence":self.sequence,"recoverable":not failed}}\n''')
  f.write('\nEXTENDED_DISTRIBUTED_STAGES=[\n'+''.join(f'    {n.title().replace("_", "")}Stage().stage(),\n' for n in names)+']\n')

if __name__=='__main__': append_shuffle(); append_pipeline()
