terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  # For production, uncomment and configure S3 backend
  backend "s3" {
    bucket         = "movie-app-backend-tf-state-1767376687"
    key            = "movie-app/terraform.tfstate"
    region         = "ap-south-1"
    dynamodb_table = "movie-app-backend-tf-lock"
  }
}

provider "aws" {
  region = var.aws_region
}
