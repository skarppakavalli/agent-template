from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model():

    # Downloads the model the first time if not cached.
    # This model runs locally on your machine.
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def generate_embeddings(texts):

    model = get_embedding_model()

    # Each text becomes a numerical vector
    vectors = model.embed_documents(texts)

    return vectors
