# Salary Prediction MLOps Project

## Project Objective

Build an end-to-end MLOps pipeline on AWS to predict employee salary based on:

* YearsExperience
* Age

Target Variable:

* Salary

## Tech Stack

### Infrastructure

* Terraform
* AWS IAM
* AWS S3

### Data Engineering

* AWS Glue
* SageMaker Feature Store

### Machine Learning

* SageMaker Studio
* SageMaker Processing Jobs
* SageMaker Training Jobs
* SageMaker Pipelines
* SageMaker Experiments
* SageMaker Model Registry
* SageMaker Clarify

### Deployment

* FastAPI
* Docker
* Amazon ECR
* Amazon EKS

### Monitoring

* CloudWatch
* Prometheus
* Grafana
* SageMaker Model Monitor

### Deployment Strategy

* Canary Deployment using Argo Rollouts

## Project Workflow

Local CSV
→ S3
→ Glue ETL
→ Feature Store
→ Data Validation
→ Train/Test Split
→ Model Training
→ Model Evaluation
→ Model Registry
→ FastAPI
→ Docker
→ ECR
→ EKS
→ Monitoring
→ Drift Detection
→ Retraining
