import random
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
import time

# --- Mocks for Petals Types ---

@dataclass
class ServerInfo:
    peer_id: str
    start_block: int
    end_block: int
    state: str = "ONLINE" # ONLINE, OFFLINE
    throughput: float = 10.0 # tokens/sec

class DHT:
    def __init__(self):
        self.servers: Dict[str, ServerInfo] = {}

    def announce(self, server: ServerInfo):
        self.servers[server.peer_id] = server

    def get_routing_table(self) -> List[ServerInfo]:
        return list(self.servers.values())

    def find_best_route(self, num_blocks: int) -> List[ServerInfo]:
        # Simple greedy solver: sort by throughput, cover [0, num_blocks)
        # This is the "Golden Nugget" logic simulation
        needed = 0
        route = []
        
        # Filter online
        candidates = [s for s in self.servers.values() if s.state == "ONLINE"]
        # Sort by start block
        candidates.sort(key=lambda s: s.start_block)
        
        current_pos = 0
        while current_pos < num_blocks:
            best_candidate = None
            for s in candidates:
                if s.start_block <= current_pos and s.end_block > current_pos:
                    if best_candidate is None or s.end_block > best_candidate.end_block:
                        best_candidate = s
            
            if best_candidate:
                route.append(best_candidate)
                current_pos = best_candidate.end_block
            else:
                raise Exception(f"Chain broken at block {current_pos}")
                
        return route

class RemoteSequential:
    def __init__(self, dht: DHT, total_blocks: int = 40):
        self.dht = dht
        self.total_blocks = total_blocks

    def forward(self, input_tensor: str) -> str:
        # Simulate distributed inference
        print(f"Plan: Planning route for {self.total_blocks} blocks...")
        try:
            route = self.dht.find_best_route(self.total_blocks)
        except Exception as e:
            return f"FAILURE: {e}"

        result = input_tensor
        for server in route:
            print(f"Step: Routing blocks [{server.start_block}:{server.end_block}] -> {server.peer_id} ({server.state})")
            # Simulate network delay/failure logic
            if server.state != "ONLINE":
                # In robust impl, we'd re-route here. For now, confirm failure is detected.
                return f"FAILURE: Peer {server.peer_id} dead midway"
            
            result += f" -> [Blocks {server.start_block}-{server.end_block} by {server.peer_id}]"
        
        return result

# --- Tests ---

def test_swarm_inference():
    print("--- Petals Swarm Logic Simulation ---")
    
    # 1. Setup DHT with 40 blocks (like Llama-65B)
    dht = DHT()
    
    # 2. Register Servers (Overlapping coverage)
    # Server A: 0-10
    dht.announce(ServerInfo("ServerA", 0, 10))
    # Server B: 10-20
    dht.announce(ServerInfo("ServerB", 10, 20))
    # Server C: 20-40 (Deep)
    dht.announce(ServerInfo("ServerC", 20, 40))
    # Server D: 10-25 (Overlap with B and part of C)
    dht.announce(ServerInfo("ServerD", 10, 25))
    
    print("Swarm Initialized.")
    
    # 3. Client Inference (Normal)
    client = RemoteSequential(dht, total_blocks=40)
    output = client.forward("Input")
    print(f"Result 1: {output}")
    assert "ServerA" in output
    assert "ServerC" in output
    assert "FAILURE" not in output
    print("TEST 1 - Basic Routing: PASS")
    
    # 4. Simulate Failure (Server B goes offline)
    # Server B covered 10-20. Server D covers 10-25, so swarm *should* heal and pick D instead of B.
    # Note: My naive logic above picks 'best_candidate' at planning time.
    print("\nSimulating ServerB Failure...")
    dht.servers["ServerB"].state = "OFFLINE"
    
    output = client.forward("Input")
    print(f"Result 2: {output}")
    
    if "ServerB" in output:
        print("FAIL: Used offline server")
    elif "ServerD" in output:
        print("TEST 2 - Heal Routing (Switched to ServerD): PASS")
    else:
        print(f"FAIL: Unexpected route: {output}")
        
    # 5. Simulate Total Chain Failure
    # Kill Server A (0-10). No one else covers it.
    print("\nSimulating ServerA Failure (Critical)...")
    dht.servers["ServerA"].state = "OFFLINE"
    
    output = client.forward("Input")
    print(f"Result 3: {output}")
    assert "FAILURE" in output
    print("TEST 3 - Broken Chain Detection: PASS")

if __name__ == "__main__":
    test_swarm_inference()
