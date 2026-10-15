# Subnet / VLSM Calculator

## Overview
A Python-based tool that allocates IPv4 subnets using
Variable Length Subnet Masking (VLSM).

## Features
- Accepts a parent IPv4 network in CIDR notation
- Takes subnet names and host requirements
- Allocates larger subnets first
- Calculates subnet masks and CIDR prefixes
- Displays network, usable host range and broadcast addresses
- Handles insufficient network capacity

## Technology
- Python 3
- ipaddress module (Python standard library)

## How It Works
1. Accept the parent network and host requirements.
2. Sort the requirements by host count.
3. Calculate the smallest suitable subnet for each group.
4. Align each subnet to a valid network boundary.
5. Check that each subnet fits inside the parent network.
6. Display the allocation plan.

## How to Run
Run `vlsm_calculator.py` using Python 3.

## Example
Network: 192.168.1.0/24

Requirements:
- HR: 100 hosts
- Sales: 50 hosts
- IT: 20 hosts

## Limitations
- Supports IPv4 networks only.
- Assumes conventional subnets with network and broadcast
  addresses reserved.
