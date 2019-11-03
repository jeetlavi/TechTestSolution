# TechTestSolution
Tech Test Solution This solution contains YAML based AWS cloud formation template that luanches a Network load balancer which feeds into an Application load baalancer and then into to web servers. The webservers are using Apache to present output from MySql database as a backend. The DB itself has a read replica based out in two AZs.

Requirements: Windows command prompt with AWS CLI profile setup. Use 'AWS configure' cmdlet to setup a new default profile.

Here are the pre-requisites/assumption made in the case:

    The account from which CF template is being executed has access to luanch VPC,Subnets, EC2 instances and so on.
    For the sake of this example long list ogf mapping has not been done with AMI in all different regions. The template works (on basis od AMI) on us-west-1 region by default. Please enter an "Ubuntu" AMI of your region if required.
    UBUNTU has been selected as OS for this solution.

Steps:
1) Execute template - basic-network.yml.
2) Secondly, execute template - infrastructure.yml.
