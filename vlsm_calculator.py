import ipaddress

def calculate_vlsm(network_input, requirements):
    network = ipaddress.ip_network(network_input, strict=False)

    if not isinstance(network, ipaddress.IPv4Network):
        raise ValueError("Only IPv4 networks are supported.")

    # Allocate the largest subnet first
    requirements = sorted(
        requirements, key=lambda item: item[1], reverse=True
    )

    current = int(network.network_address)
    results = []

    for name, hosts in requirements:
        if not isinstance(hosts, int) or isinstance(hosts, bool) or hosts < 1:
            raise ValueError(f"{name}: host count must be a positive integer.")

        # Reserve one network address and one broadcast address
        block_bits = (hosts + 1).bit_length()
        prefix = 32 - block_bits

        if prefix < network.prefixlen:
            raise ValueError(f"Not enough space for {name}: {hosts} hosts.")

        block_size = 1 << block_bits

        # Align the next subnet to a valid network boundary
        aligned_start = ((current + block_size - 1) // block_size) * block_size
        subnet = ipaddress.ip_network(
            (aligned_start, prefix), strict=True
        )

        if not subnet.subnet_of(network):
            raise ValueError(f"Network capacity exceeded for {name}.")

        results.append((name, hosts, subnet))
        current = int(subnet.broadcast_address) + 1

    return results


def main():
    network = input("Enter network (e.g., 192.168.1.0/24): ")

    count = int(input("How many subnets do you need? "))
    requirements = []

    for i in range(count):
        name = input(f"Subnet {i + 1} name: ")
        hosts = int(input(f"Hosts required for {name}: "))
        requirements.append((name, hosts))

    try:
        results = calculate_vlsm(network, requirements)

        print("\n--- VLSM ALLOCATION PLAN ---")

        for name, hosts, subnet in results:
            print(f"\nSubnet: {name}")
            print(f"Network Address : {subnet.network_address}")
            print(f"CIDR Prefix     : /{subnet.prefixlen}")
            print(f"Subnet Mask     : {subnet.netmask}")
            print(f"First Usable IP : {subnet.network_address + 1}")
            print(f"Last Usable IP  : {subnet.broadcast_address - 1}")
            print(f"Broadcast       : {subnet.broadcast_address}")
            print(f"Hosts Required  : {hosts}")
            print(f"Usable Capacity : {subnet.num_addresses - 2}")

    except ValueError as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()
