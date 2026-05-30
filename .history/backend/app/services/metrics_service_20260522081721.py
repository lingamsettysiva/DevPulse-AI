def calculate_repo_metrics(repo_data):
    stars=repo_data["stars"]
    fork=repo_data["forks"]
    open_issues=repo_data["open_issues"]
    watchers=repo_data["watchers"]
    
    popularity_score=stars + forks + watchers
    
    
    if open_issues > 100:
        risk_level="High"
        
    elif open_issues > 30:
        risk_level = "medium"
        
    else:
        risk_level="Low"
        
        
    return {
        "popularity_score": popularity_score
    }