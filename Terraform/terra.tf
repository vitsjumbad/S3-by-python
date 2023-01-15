provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "webserver" {
  ami           = "ami-09d95fab7eff77e67" # Amazon Linux 2 LTS
  instance_type = "t2.micro" # low-cost option
  key_name      = "my_key"
  security_groups = ["my_security_group"]

  tags = {
    Name = "webserver"
  }
}

