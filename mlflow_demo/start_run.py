import mlflow

# Start a new MLflow run
# with mlflow.start_run():
#     mlflow.log_param("param1", 5)
#     mlflow.log_metric("metric1", 0.85)
#     # Log a model
#     # mlflow.log_model(your_model, "model")
    
with mlflow.start_run():
    for epoch in range(0, 3):
        mlflow.log_metric(key="quality", value=2 * epoch, step=epoch)
        
import mlflow

params = {
    "learning_rate": 0.01,
    "batch_size": 32,
    "num_epochs": 10
}

with mlflow.start_run():
    mlflow.log_params(params)