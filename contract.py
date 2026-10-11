# { "Depends": "py-genlayer:testnet" }
from genlayer import gl

class MyIntelligentContract(gl.Contract):
    greeting: str
    def __init__(self):
        self.greeting = "Hello GenLayer from Indonesia"
    @gl.public.view
    def get_greeting(self) -> str:
        return self.greeting
    @gl.public.write
    def ask_ai(self, prompt: str) -> str:
        ai_result = gl.exec_prompt(f"Answer creatively: {prompt}")
        self.greeting = ai_result
        return ai_result
    @gl.public.write
    def set_greeting(self, new_greeting: str):
        self.greeting = new_greeting
