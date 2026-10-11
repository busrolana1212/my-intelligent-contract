# { "Depends": "py-genlayer:testnet" }
from genlayer import *
class MyContract(gl.Contract):
 @gl.public.write
 def ask(self,q:str):
  self.v=gl.nondet.exec_prompt(q)
  return self.v
