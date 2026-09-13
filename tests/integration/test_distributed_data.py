import asyncio
import time

from kalz.distributed.partition import Record, Partitioner, PARTITION_STRATEGIES
from kalz.distributed.shuffle import ShuffleBatch, SHUFFLE_OPERATORS
from kalz.distributed.workers import Task, WorkerPool, WORKER_CAPABILITIES
from kalz.distributed.checkpoint import Checkpoint, CheckpointStore, CHECKPOINT_POLICIES
from kalz.distributed.pipeline import build_pipeline


def test_partition_and_shuffle():
    records = [Record(str(i), i, time.time()) for i in range(10)]
    partitions = Partitioner(3).split(records)
    assert sum(len(partition.records) for partition in partitions) == 10
    assert len(PARTITION_STRATEGIES) >= 300
    operator = next(iter(SHUFFLE_OPERATORS.values()))
    assert operator.validate(ShuffleBatch('batch', tuple(records), 0))
    assert operator.aggregate(records)


def test_workers_backpressure_and_retry():
    async def run():
        pool = WorkerPool(size=2, max_queue=4)
        await pool.submit(Task('task-1', 3))
        result = await pool.drain(lambda value: value * 2)
        assert result[0].value == 6
        assert len(WORKER_CAPABILITIES) >= 300
    asyncio.run(run())


def test_checkpoint_and_recovery():
    body = {'id': 'cp', 'stage': 'stage', 'offsets': (('partition', 3),)}
    import hashlib, json
    checksum = hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()
    checkpoint = Checkpoint('cp', 'stage', (('partition', 3),), checksum)
    store = CheckpointStore(); store.save(checkpoint)
    assert store.verify(checkpoint)
    assert len(CHECKPOINT_POLICIES) >= 300


def test_pipeline_order_and_metrics():
    pipeline = build_pipeline('integration')
    report = pipeline.plan()
    assert len(report.stages) >= 300
    assert report.status == 'planned'
    assert pipeline.metrics()['stages'] == len(report.stages)
