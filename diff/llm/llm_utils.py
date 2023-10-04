import csv
import threading
from autogpt.llm.base import Message
import asyncio
from typing import List, Literal, Optional

import threading

def save_to_csv(file_name, data):
    print("SAVING!!!!!!!!\n\n\n")
    thread_id = threading.get_ident()
    with open(f"logs/{thread_id}_{file_name}", 'a', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in data:
            csv_writer.writerow(row)

def create_chat_completion(
    messages: List[Message],  # type: ignore
    model: Optional[str] = None,
    temperature: float = None,
    max_tokens: Optional[int] = None,
) -> str:
    print("HERE!!!!!!!!\n\n\n")
    result="TEST"
    #result=autogpt_create_chat_completion(messages,model,temperature,max_tokens)

    data_to_save = []
    data_to_save.append(model,temperature,max_tokens,messages, result)
    save_to_csv('chat.csv', data_to_save)
    return result

########NEW METHOD WITH ASYNC AND STREAMING#########
        ######NEEDS CHAIN CACHING#############
""" 
def save_to_csv(file_name, data):
    thread_id = threading.get_ident()
    with open(f"logs/{thread_id}_{file_name}", 'a', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in data:
            csv_writer.writerow(row)

async def generate_chat_stream(
    messages: List[Message],
    model: Optional[str] = None,
    temperature: float = None,
    max_tokens: Optional[int] = None,
    async_mode: bool = False,
) -> str:
    data_to_save = []
    data_to_save.append([model, temperature, max_tokens, messages, "START"])
    save_to_csv('chat.csv', data_to_save)

    for i in range(5):
        # Simulate generating chat completions, you can replace this with your actual logic
        completion = f"Partial Completion {i}"
        yield completion

    data_to_save = []
    data_to_save.append([model, temperature, max_tokens, messages, "END"])
    save_to_csv('chat.csv', data_to_save)

# Usage example
async def main():
    async for partial_completion in generate_chat_stream(
        messages=[Message(content="Hello"), Message(content="How are you?")],
        model="my_model",
        temperature=0.7,
        max_tokens=50,
        async_mode=True,
    ):
        print(partial_completion)


if __name__ == "__main__":
    #testing purpous
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main()) """