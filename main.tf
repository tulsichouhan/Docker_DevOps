resource "aws_instance" "healthcare_ec2" {
  ami                    = "ami-0c83cb1c664994bbd" # Amazon Linux 2 (Mumbai)
  instance_type          = "t3.micro"
  key_name               = "healthcare-key"
  vpc_security_group_ids = ["sg-0c1d4bf168f589255"]

  user_data = <<-EOF
    #!/bin/bash
    yum update -y
    yum install docker -y
    service docker start
    usermod -aG docker ec2-user
    curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-\$(uname -s)-\$(uname -m)" -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
  EOF

  tags = {
    Name = "Healthcare-App-Server"
  }
}
