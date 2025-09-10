import numpy as np
from datetime import datetime, timedelta

class RealTimeFeatureEngine:
    def __init__(self, redis_client):
        self.redis = redis_client

    def compute_features(self, transaction):
        user_id = transaction["user_id"]

        recent_txns = self.get_recent_transactions(user_id, hours=24)

        features = {
            "txn_count_24h": len(recent_txns),
            "avg_amount_24h": np.mean([t["amount"] for t in recent_txns]) if recent_txns else 0.0,
            "time_since_last_txn": self.time_since_last_transaction(user_id),
            "is_weekend": datetime.now().weekday() >= 5,
            "amount_zscore": self.compute_amount_zscore(transaction["amount"], recent_txns),
        }
        return features

    def compute_amount_zscore(self, amount, recent_txns):
        if not recent_txns:
            return 0.0

        # Aceita lista de dicts {"amount": x} ou lista de números
        if isinstance(recent_txns[0], dict):
            values = [t["amount"] for t in recent_txns]
        else:
            values = recent_txns

        mean, std = np.mean(values), np.std(values)
        return (amount - mean) / std if std > 0 else 0.0

    def get_recent_transactions(self, user_id, hours=24):
        # Mock para testes
        return [{"amount": 100}, {"amount": 200}]

    def time_since_last_transaction(self, user_id):
        # Mock para testes
        return timedelta(minutes=30).total_seconds()
