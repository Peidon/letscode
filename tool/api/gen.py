import re


def analyze_protobuf(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Regular expression to match service definitions and their RPCs
    service_pattern = re.compile(r'service\s+(\w+)\s*{([^}]+)}')
    rpc_pattern = re.compile(r'rpc\s+(\w+)\s*\((\w+)\)\s*returns\s*\((\w+)\)')

    services = service_pattern.findall(content)

    for service in services:
        service_name, rpcs = service
        print(f"Service (API) Name: {service_name}")
        for rpc in rpc_pattern.findall(rpcs):
            method_name, request, response = rpc
            print(f"\tMethod Name: {method_name}")
            print(f"\t\tRequest: {request}")
            print(f"\t\tResponse: {response}")


if __name__ == "__main__":
    # Replace 'your_protobuf_file.proto' with the path to your protobuf file
    analyze_protobuf('your_protobuf_file.proto')
