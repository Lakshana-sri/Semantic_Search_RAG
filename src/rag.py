
import torch
import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from src.hybrid_search import hybrid_search

MODEL_NAME = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)


def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def generate_answer(query):

    results = hybrid_search(query, top_k=3)

    context_parts = []

    for result in results:
        text = clean_text(result["text"])
        context_parts.append(text[:500])

    context = "\n".join(context_parts)

    prompt = f"""
You are an educational AI assistant.

Answer the user's question using the provided context.

Instructions:
1. Give a clear and complete explanation.
2. Use simple English.
3. Explain the main concept and how it works.
4. Include important points from the context.
5. Do not repeat irrelevant information.
6. Do not invent facts.
7. If the context does not contain the answer, say:
   The information is not available in the documents.

Context:
{context}

Question:
{query}

Provide a helpful answer in 3 to 5 sentences.

Answer:
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    with torch.no_grad():

        outputs = model.generate(
            **inputs,
            max_new_tokens=180,
            num_beams=4,
            early_stopping=True,
            repetition_penalty=1.5,
            no_repeat_ngram_size=3
        )

    answer = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return {
        "answer": answer.strip(),
        "sources": results
    }