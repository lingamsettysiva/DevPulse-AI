def predict_repository_risk(metrics):

    popularity_score = metrics["popularity_score"]
    risk_level = metrics["risk_level"]

    # Simple rule-based prediction

    if risk_level == "High":
        prediction = "Repository needs immediate attention"

    elif risk_level == "Medium":
        prediction = "Repository health is moderate"

    else:
        prediction = "Repository looks healthy"

    return {
        "prediction": prediction,
        "score": popularity_score
    }