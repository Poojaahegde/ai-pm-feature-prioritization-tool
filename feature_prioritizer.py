"""
AI Feature Prioritization Tool

This script helps AI product managers prioritize features by scoring them based on value, complexity, and risk. Each feature should be provided with scores between 1 and 5 for value, complexity (lower complexity is better), and risk (lower risk is better). The script calculates a weighted score for each feature and ranks them.
"""

from dataclasses import dataclass
from typing import List

@dataclass
class Feature:
    name: str
    value: int  # 1-5
    complexity: int  # 1-5; lower is better
    risk: int  # 1-5; lower is better

    def score(self, value_weight: float = 0.5, complexity_weight: float = 0.3, risk_weight: float = 0.2) -> float:
        normalized_complexity = 6 - self.complexity
        normalized_risk = 6 - self.risk
        return (self.value * value_weight +
                normalized_complexity * complexity_weight +
                normalized_risk * risk_weight)

def prioritize_features(features: List[Feature]) -> List[Feature]:
    """Sort features by their computed score in descending order."""
    return sorted(features, key=lambda f: f.score(), reverse=True)

if __name__ == "__main__":
    # Example usage
    features = [
        Feature("Chat summarization", 5, 3, 2),
        Feature("Voice input", 4, 4, 3),
        Feature("Personalized recommendations", 3, 5, 4),
    ]
    ranked = prioritize_features(features)
    print("Ranked features (highest priority first):")
    for feature in ranked:
        print(f"{feature.name}: {feature.score():.2f}")
