provider "aws" {
  region = var.aws_region
}

variable "allowed_ingress_cidrs" {
  description = "CIDR blocks allowed to access the service (restrict this!)"
  type        = list(string)
  default     = ["10.0.0.0/8"]
}

resource "aws_security_group" "user_api" {
  name        = "user-api-sg"
  description = "Allow 443 only from trusted CIDRs"

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = var.allowed_ingress_cidrs
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
