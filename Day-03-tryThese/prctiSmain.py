from prctiSmodel_utils import (
    calculate_total_requests,
    count_requests,
    most_used_model,
)

requests = ["GPT", "Claude", "GPT", "Gemini", "gpt"]

while True:
    try:
        token_count = int(input("Enter token count: "))
        if token_count < 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid token count. Enter a non-negative integer.")

counts = count_requests(requests)
total_requests = calculate_total_requests(counts)
most_used = most_used_model(counts)

print("Counts:", counts)
print("Total requests:", total_requests)
print("Most used:", most_used)
print("Token count:", token_count)