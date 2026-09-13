from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/'kalz'

def gateway():
 p=ROOT/'gateway'; p.mkdir(exist_ok=True)
 names=[f'route_policy_{i:03d}' for i in range(1,321)]
 out=['from __future__ import annotations','','import hashlib','import time','from dataclasses import dataclass, field','from typing import Any, Iterable','','@dataclass(frozen=True)','class GatewayRequest:','    request_id: str','    method: str','    path: str','    headers: dict[str,str]=field(default_factory=dict)','    body: bytes=b""','','@dataclass(frozen=True)','class GatewayResponse:','    status: int','    body: bytes','    backend: str=""','    headers: dict[str,str]=field(default_factory=dict)','','@dataclass','class Backend:','    name: str','    host: str','    weight: int=1','    healthy: bool=True','    active: int=0','    failures: int=0','    circuit_open_until: float=0.0','','class GatewayError(RuntimeError): pass','','class APIGateway:','    def __init__(self): self.backends: dict[str,Backend]={}; self.routes: dict[str,str]={}; self.requests=0','    def add_backend(self, backend: Backend) -> None: self.backends[backend.name]=backend','    def route(self, path: str, backend: str) -> None:','        if backend not in self.backends: raise GatewayError("backend not found")','        self.routes[path]=backend','    def dispatch(self, request: GatewayRequest) -> GatewayResponse:','        self.requests += 1; name=self.routes.get(request.path)','        if not name: return GatewayResponse(404,b"route not found")','        backend=self.backends[name]','        if not backend.healthy or backend.circuit_open_until > time.time(): return GatewayResponse(503,b"backend unavailable",name)','        backend.active += 1','        try: return GatewayResponse(200,b"gateway planned",name,{"x-request-id":request.request_id})','        finally: backend.active -= 1','    def health(self) -> dict[str,Any]: return {name: backend.healthy and backend.circuit_open_until <= time.time() for name,backend in self.backends.items()}','']
 for i,n in enumerate(names,1):
  c=''.join(x.title() for x in n.split('_'))
  out += [f'class {c}:',f'    name={n!r}',f'    sequence={i}',f'    methods={("GET","POST") if i%2 else ("GET","PUT","DELETE")!r}', '    def accepts(self, request: GatewayRequest) -> bool: return request.method in self.methods and bool(request.path)', '    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"methods":self.methods}', '']
 out += ['ROUTE_POLICIES={',*['    '+repr(n)+': '+''.join(x.title() for x in n.split('_'))+'(),' for n in names],'}','']
 (p/'gateway.py').write_text('\n'.join(out)+'\n')

def balance():
 p=ROOT/'gateway'; names=[f'balancer_strategy_{i:03d}' for i in range(1,321)]
 out=['from __future__ import annotations','','import hashlib','import time','from dataclasses import dataclass','from typing import Any, Iterable','','@dataclass','class Node:','    name: str','    address: str','    weight: int=1','    healthy: bool=True','    latency_ms: float=0.0','    inflight: int=0','','class BalanceError(RuntimeError): pass','','class LoadBalancer:','    def __init__(self, nodes: Iterable[Node]=()): self.nodes={node.name:node for node in nodes}; self.cursor=0','    def add(self,node: Node)->None: self.nodes[node.name]=node','    def healthy(self)->list[Node]: return [node for node in self.nodes.values() if node.healthy]','    def choose_round_robin(self)->Node:','        nodes=self.healthy()','        if not nodes: raise BalanceError("no healthy nodes")','        node=nodes[self.cursor % len(nodes)]; self.cursor += 1; node.inflight += 1; return node','    def choose_least_load(self)->Node:','        nodes=self.healthy()','        if not nodes: raise BalanceError("no healthy nodes")','        node=min(nodes,key=lambda item:(item.inflight,item.latency_ms)); node.inflight += 1; return node','    def release(self,name: str)->None:','        if name in self.nodes: self.nodes[name].inflight=max(0,self.nodes[name].inflight-1)','    def health(self)->dict[str,Any]: return {name:node.__dict__.copy() for name,node in self.nodes.items()}','']
 for i,n in enumerate(names,1):
  c=''.join(x.title() for x in n.split('_'))
  out += [f'class {c}:',f'    name={n!r}',f'    sequence={i}',f'    algorithm={"least-load" if i%3==0 else "round-robin"!r}', '    def score(self,node: Node)->float: return node.inflight + node.latency_ms/1000 + self.sequence/100000', '    def metadata(self)->dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"algorithm":self.algorithm}', '']
 out += ['BALANCER_STRATEGIES={',*['    '+repr(n)+': '+''.join(x.title() for x in n.split('_'))+'(),' for n in names],'}','']
 (p/'load_balancer.py').write_text('\n'.join(out)+'\n')

def defense():
 p=ROOT/'defense'; p.mkdir(exist_ok=True)
 for filename, clsbase, catalog in [('engine.py','DefenseRule','defense_rule'),('hardening.py','HardeningControl','hardening_control')]:
  names=[f'{catalog}_{i:03d}' for i in range(1,421)]
  out=['from __future__ import annotations','','import hashlib','import time','from dataclasses import dataclass','from typing import Any, Iterable','','@dataclass(frozen=True)','class SecurityEvent:','    event_id: str','    kind: str','    source: str','    value: Any','    timestamp: float','','class DefenseError(RuntimeError): pass','','class DefenseEngine:','    def __init__(self): self.rules={}; self.events=[]; self.blocked=set()','    def register(self, rule: Any)->None: self.rules[rule.name]=rule','    def inspect(self,event: SecurityEvent)->dict[str,Any]:','        self.events.append(event); decisions=[rule.evaluate(event) for rule in self.rules.values()]; blocked=any(not decision["allowed"] for decision in decisions)','        if blocked: self.blocked.add(event.source)','        return {"event_id":event.event_id,"blocked":blocked,"decisions":decisions}','    def panic(self)->None: self.blocked.update(event.source for event in self.events)','    def report(self)->dict[str,Any]: return {"rules":len(self.rules),"events":len(self.events),"blocked":len(self.blocked)}','']
  for i,n in enumerate(names,1):
   c=''.join(x.title() for x in n.split('_'))
   out += [f'class {c}({clsbase}):',f'    name={n!r}',f'    sequence={i}',f'    threshold={i%100}', '    def evaluate(self,event: SecurityEvent)->dict[str,Any]:',f'        allowed = event.kind != "blocked" and {str(i%11 != 0)}', '        return {"rule":self.name,"allowed":allowed,"sequence":self.sequence,"reason":"policy evaluation"}', '    def metadata(self)->dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"automatic":True}', '']
  out += [f'{catalog.upper()}S={{',*['    '+repr(n)+': '+''.join(x.title() for x in n.split('_'))+'(),' for n in names],'}','']
  (p/filename).write_text('\n'.join(out)+'\n')

def main(): gateway(); balance(); defense()
if __name__=='__main__': main()
