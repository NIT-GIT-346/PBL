import math
import random

random.seed(42)

MODEL_METRICS = [
    {
        "model_name": "Deep RL (DQN)",
        "accuracy": 0.9423,
        "precision": 0.9387,
        "recall": 0.9312,
        "f1_score": 0.9349,
        "auc_roc": 0.9678,
    },
    {
        "model_name": "Random Forest",
        "accuracy": 0.8834,
        "precision": 0.8756,
        "recall": 0.8689,
        "f1_score": 0.8722,
        "auc_roc": 0.9201,
    },
    {
        "model_name": "SVM",
        "accuracy": 0.8567,
        "precision": 0.8498,
        "recall": 0.8423,
        "f1_score": 0.8460,
        "auc_roc": 0.8934,
    },
    {
        "model_name": "Logistic Regression",
        "accuracy": 0.8123,
        "precision": 0.8067,
        "recall": 0.7989,
        "f1_score": 0.8028,
        "auc_roc": 0.8612,
    },
    {
        "model_name": "CNN",
        "accuracy": 0.9156,
        "precision": 0.9098,
        "recall": 0.9045,
        "f1_score": 0.9071,
        "auc_roc": 0.9502,
    },
]


def _generate_training_data():
    data = []
    for episode in range(0, 1001, 10):
        reward = -200 + 700 * (1 - math.exp(-episode / 250))
        reward += random.uniform(-20, 20)
        accuracy = 0.5 + 0.45 * (1 - math.exp(-episode / 300))
        accuracy = min(accuracy, 0.98)
        accuracy += random.uniform(-0.02, 0.02)
        loss = 2.5 * math.exp(-episode / 200) + 0.1
        loss += random.uniform(-0.05, 0.05)
        loss = max(loss, 0.05)
        data.append(
            {
                "episode": episode,
                "reward": round(reward, 2),
                "accuracy": round(accuracy, 4),
                "loss": round(loss, 4),
            }
        )
    return data


DRL_TRAINING_DATA = _generate_training_data()

CONFUSION_MATRIX = {
    "labels": ["Cardiac", "Respiratory", "Metabolic", "Neurological", "General"],
    "matrix": [
        [187, 5, 3, 2, 3],
        [4, 176, 6, 3, 11],
        [2, 4, 183, 1, 10],
        [3, 2, 1, 179, 15],
        [4, 13, 7, 15, 161],
    ],
}
