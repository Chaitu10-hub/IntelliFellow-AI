from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class AnswerGenerator:
    def __init__(self):
        model_name = "microsoft/Phi-3-mini-4k-instruct"

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Load model safely on CPU without accelerate issues
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            dtype=torch.float32,
            device_map=None  # ensures CPU load without accelerate
        )

    def generate_answer(self, question: str, context: str):
        prompt = f"""
You are an AI assistant. Use ONLY the context below to answer the question.

Context:
{context}

Question:
{question}

Answer:
"""

        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=200,
            temperature=0.2
        )

        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)