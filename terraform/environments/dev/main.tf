resource "aws_s3_bucket" "terraform_state" {

  bucket = "salary-mlops-tfstate-445411728398"

  tags = {
    Name        = "Terraform State Bucket"
    Environment = "dev"
    Project     = "salary-prediction-mlops"
  }
}

resource "aws_s3_bucket_versioning" "terraform_state_versioning" {

  bucket = aws_s3_bucket.terraform_state.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket" "raw_data" {

  bucket = "salary-mlops-raw-data-445411728398"

  tags = {
    Name        = "Raw Data Bucket"
    Environment = "dev"
    Project     = "salary-prediction-mlops"
  }
}
resource "aws_s3_bucket" "processed_data" {

  bucket = "salary-mlops-processed-data-445411728398"

  tags = {
    Name        = "Processed Data Bucket"
    Environment = "dev"
    Project     = "salary-prediction-mlops"
  }
}
