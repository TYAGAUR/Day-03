from model_utils import count_requests, most_used_model

requests = ["GPT", "Claude", "GPT", "Gemini", "gpt"]

counts = count_requests(requests)
most_used = most_used_model(counts)

print("Counts:", counts)
print("Most used:", most_used)