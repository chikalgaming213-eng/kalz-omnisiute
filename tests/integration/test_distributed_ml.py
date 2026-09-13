import time

from kalz.ml.features import FeatureRecord, FeatureStore, FEATURE_TRANSFORMS
from kalz.ml.models import ModelArtifact, ModelRegistry, MODEL_ARCHITECTURES
from kalz.ml.training import TrainingBatch, TRAINING_STRATEGIES
from kalz.ml.inference import InferenceRequest, InferenceServer, INFERENCE_RUNTIMES
from kalz.ml.evaluation import Evaluator, EVALUATION_METRICS


def test_feature_store_and_transforms():
    store = FeatureStore()
    version = store.put(FeatureRecord('entity-1', (('x', 1.0),), time.time(), 'test'))
    assert version and store.get('entity-1').entity_id == 'entity-1'
    assert len(FEATURE_TRANSFORMS) >= 300
    assert next(iter(FEATURE_TRANSFORMS.values())).apply({'x': 1.0})


def test_model_registry_and_architecture():
    registry = ModelRegistry()
    artifact = ModelArtifact('model', '1', (1.0,), 'checksum')
    registry.register(artifact); registry.promote('model', '1')
    assert registry.resolve('model').version == '1'
    assert len(MODEL_ARCHITECTURES) >= 300


def test_training_and_evaluation():
    strategy = next(iter(TRAINING_STRATEGIES.values()))
    report = strategy.fit([TrainingBatch('batch', ((1.0,),), (1.0,))], epochs=2)
    assert report.epochs == 2
    evaluator = Evaluator(); result = evaluator.evaluate([1.0, 2.0], [1.0, 1.0])
    assert result.samples == 2
    assert len(EVALUATION_METRICS) >= 300


def test_inference_runtime():
    registry = ModelRegistry()
    registry.register(ModelArtifact('model', '1', (1.0,), 'checksum')); registry.promote('model', '1')
    server = InferenceServer(registry)
    response = server.predict(InferenceRequest('request', 'model', (1.0, 2.0), time.time()))
    assert response.status == 'ok' and response.model == 'model'
    assert len(INFERENCE_RUNTIMES) >= 300
