class CPU:
    def __init__(self, model, cores):
        self.model = model
        self.cores = cores
    def __str__(self):
        return f"{self.model} ({self.cores} cores)"

class NIC:
    def __init__(self, speed, ip):
        self.speed = speed
        self.ip = ip
    def __str__(self):
        return f"{self.ip} @ {self.speed}"

class Server:
    def __init__(self, hostname):
        self.hostname = hostname
        self.cpu = None
        self.nics = []

    def install_cpu(self, cpu):
        self.cpu = cpu

    def add_nic(self, nic):
        self.nics.append(nic)

    def status(self):
        print(f"Server: {self.hostname}")
        print(f"  CPU: {self.cpu}")
        for nic in self.nics:
            print(f"  NIC: {nic}")

# Build a server through composition
web01 = Server("WEB-01")
web01.install_cpu(CPU("Xeon E5-2680", 16))
web01.add_nic(NIC("10 Gbps", "10.0.1.10"))
web01.add_nic(NIC("1 Gbps", "192.168.1.10"))
web01.status()