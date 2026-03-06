import time
import numpy as np
from tester.tests import *


TESTS = [
    ("list breeds", test_list_all_breeds),
    ("random image", test_random_image),
    ("hound random", test_hound_random),
    ("invalid breed", test_invalid_breed),
    ("json content", test_json_content),
    ("latency", test_latency),
]


def run_tests():

    results = []
    latencies = []

    passed = 0
    failed = 0

    for name, test in TESTS:

        start = time.time()

        try:
            test()

            latency = (time.time() - start) * 1000

            results.append({
                "name": name,
                "status": "PASS",
                "latency_ms": latency
            })

            latencies.append(latency)
            passed += 1

        except Exception as e:

            results.append({
                "name": name,
                "status": "FAIL",
                "details": str(e)
            })

            failed += 1

    avg = np.mean(latencies) if latencies else 0
    p95 = np.percentile(latencies, 95) if latencies else 0

    summary = {
        "passed": passed,
        "failed": failed,
        "error_rate": failed / len(TESTS),
        "latency_ms_avg": avg,
        "latency_ms_p95": p95
    }

    return {
        "summary": summary,
        "tests": results
    }