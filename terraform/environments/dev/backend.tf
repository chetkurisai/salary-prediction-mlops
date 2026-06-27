terraform {
  backend "s3" {
    bucket = "salary-mlops-tfstate-445411728398"
    key    = "dev/terraform.tfstate"
    region = "us-east-2"
  }
}
