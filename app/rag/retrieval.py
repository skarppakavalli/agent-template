import math


def cosine_similarity(a, b):

    dot_product = sum(x * y for x, y in zip(a, b))

    magnitude_a = math.sqrt(sum(x * x for x in a))
    magnitude_b = math.sqrt(sum(x * x for x in b))

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (magnitude_a * magnitude_b)


def retrieve(query, chunks, embedding_model, top_k=3):

    # Embed the user's question
    query_vector = embedding_model.embed_query(query)

    # Embed document chunks
    chunk_vectors = embedding_model.embed_documents(
        [chunk.page_content for chunk in chunks]
    )

    scored_results = []

    for chunk, vector in zip(chunks, chunk_vectors):

        score = cosine_similarity(query_vector, vector)

        scored_results.append((score, chunk))

    # Highest similarity first
    scored_results.sort(
        key=lambda item: item[0],
        reverse=True
    )

    return scored_results[:top_k]
