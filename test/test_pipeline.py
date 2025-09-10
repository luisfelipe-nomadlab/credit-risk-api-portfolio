from app.api.v1.fraud import RealTimeFeatureEngine

def test_amount_zscore():
    engine = RealTimeFeatureEngine({})
    amounts = [100, 200, 300]
    z = engine.compute_amount_zscore(250, amounts)
    assert isinstance(z, float)
