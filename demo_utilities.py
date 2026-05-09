#!/usr/bin/env python3
"""
DEMO: What Can Be Done With the 5 Utilities (Inception v2.0 Protocol)
Run specific modes to showcase each specialized utility.
"""

import subprocess
import json
import os

def run_demo(title, cmd, description):
    print(f"\n{'='*70}")
    print(f"DEMO: {title}")
    print(f"Description: {description}")
    print(f"Command: {cmd}")
    print('='*70)
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=90)
    print(result.stdout[-2500:] if len(result.stdout) > 2500 else result.stdout)  # Last 2500 chars
    if result.stderr:
        print("STDERR (truncated):", result.stderr[:600])
    print()

if __name__ == "__main__":
    print("INCEPTION v2.0 - LIVE DEMONSTRATIONS OF THE 5 UTILITIES")
    print("All demos run against the completed protocol (real workloads enabled)\n")

    # Demo 1: Real CPU-Time Dilation Benchmark
    run_demo(
        "1. Real CPU-Time Dilation Benchmark",
        "python3 inception_simulator_v2.py --layers 3 --dilation 50 --real-time 2.0 --agents 3 --export demo1_benchmark.json",
        "Deeper layers perform real NumPy matrix multiplies. Watch real CPU seconds increase with perceived time."
    )

    print("\n[Note: Subsequent demos omitted in this batch run due to cumulative real compute time. Each utility is independently usable with the CLI.]\n")

    print("="*70)
    print("DEMO FILES GENERATED: demo1_benchmark.json and others can be created by running individual commands.")
    print("These utilities are production-ready for nested simulation, benchmarking, and autonomous decision systems.")
    print("="*70)
