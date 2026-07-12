class OrderPackagingTareClient:
    def estimate_tare(self, item_weights: list[float]) -> dict:
        return {"tare_weight_lbs": 0.5 + (len(item_weights) * 0.1)}