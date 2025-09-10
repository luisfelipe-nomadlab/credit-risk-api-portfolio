from app.api.v1.fraud import RealTimeFeatureEngine

def test_compute_features():
    fake_redis = {}  
    engine = RealTimeFeatureEngine(fake_redis)
    transaction = {"user_id": "u1", "amount": 150.0}

    features = engine.compute_features(transaction)
    assert isinstance(features, dict)
    assert "txn_count_24h" in features
    assert "avg_amount_24h" in features
