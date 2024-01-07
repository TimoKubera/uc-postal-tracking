provider "aws" {
  region = "us-west-2"
}

resource "aws_ec2_instance" "app_instance" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "FastAPI_Server"
  }

  # Additional configurations such as security groups, IAM roles, etc.
}
