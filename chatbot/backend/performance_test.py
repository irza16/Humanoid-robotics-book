import time
import asyncio
import aiohttp
import statistics
from typing import List, Dict, Any

async def performance_test(base_url: str, num_requests: int = 10):
    """
    Performance test to verify response times for the chat endpoint
    """
    print(f"Running performance test with {num_requests} requests to {base_url}")

    response_times = []
    successful_requests = 0
    failed_requests = 0

    async with aiohttp.ClientSession() as session:
        for i in range(num_requests):
            try:
                start_time = time.time()

                # Send a test request
                async with session.post(
                    f"{base_url}/chat",
                    json={
                        "question": "What is this book about?",
                        "selected_text": None
                    },
                    headers={"Content-Type": "application/json"}
                ) as response:
                    response_time = time.time() - start_time
                    response_times.append(response_time)

                    if response.status == 200:
                        successful_requests += 1
                        data = await response.json()
                        print(f"Request {i+1}: Success in {response_time:.2f}s")
                    else:
                        failed_requests += 1
                        print(f"Request {i+1}: Failed with status {response.status}")

            except Exception as e:
                failed_requests += 1
                print(f"Request {i+1}: Exception - {str(e)}")

    # Calculate performance metrics
    if response_times:
        avg_response_time = statistics.mean(response_times)
        median_response_time = statistics.median(response_times)
        p95_response_time = sorted(response_times)[int(0.95 * len(response_times))] if len(response_times) > 0 else 0
        max_response_time = max(response_times)
        min_response_time = min(response_times)

        print("\n--- Performance Results ---")
        print(f"Total requests: {num_requests}")
        print(f"Successful requests: {successful_requests}")
        print(f"Failed requests: {failed_requests}")
        print(f"Success rate: {(successful_requests/num_requests)*100:.2f}%")
        print(f"Average response time: {avg_response_time:.2f}s")
        print(f"Median response time: {median_response_time:.2f}s")
        print(f"95th percentile response time: {p95_response_time:.2f}s")
        print(f"Max response time: {max_response_time:.2f}s")
        print(f"Min response time: {min_response_time:.2f}s")

        # Check if 95% of requests meet the <5s requirement
        fast_enough = sum(1 for rt in response_times if rt < 5.0) / len(response_times)
        print(f"Percentage of requests under 5s: {fast_enough*100:.2f}%")

        if fast_enough >= 0.95:
            print("✅ Performance requirement met: 95% of requests under 5s")
        else:
            print("❌ Performance requirement not met: Less than 95% of requests under 5s")
    else:
        print("No successful requests to analyze")


def run_performance_test_sync(base_url: str, num_requests: int = 10):
    """
    Synchronous wrapper for the performance test
    """
    asyncio.run(performance_test(base_url, num_requests))


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        base_url = sys.argv[1]
    else:
        base_url = "http://localhost:8000"

    num_requests = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    run_performance_test_sync(base_url, num_requests)