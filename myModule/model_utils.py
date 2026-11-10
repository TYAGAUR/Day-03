def count_requests(model_requests):
    counts = {}

    for model in model_requests:
        model = model.lower()

        if model in counts:
            counts[model] += 1
        else:
            counts[model] = 1

    return counts


def most_used_model(counts):
    if not counts:
        return None

    return max(counts, key=counts.get)