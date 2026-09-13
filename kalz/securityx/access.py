from __future__ import annotations

import base64
import hashlib
import json
import secrets
import time
from dataclasses import dataclass, field
from typing import Any, Iterable

# Capability-based access control, roles, scopes, and audit decisions

@dataclass(frozen=True)
class Principal:
    principal_id: str
    roles: frozenset[str]=frozenset()
    capabilities: frozenset[str]=frozenset()

@dataclass(frozen=True)
class AccessDecision:
    allowed: bool
    principal_id: str
    resource: str
    action: str
    reason: str

class AccessController:
    def __init__(self): self.roles: dict[str,set[str]]={}; self.audit: list[AccessDecision]=[]
    def grant_role(self, role: str, capabilities: Iterable[str]) -> None: self.roles[role]=set(capabilities)
    def decide(self, principal: Principal, resource: str, action: str) -> AccessDecision:
        granted=set(principal.capabilities)
        for role in principal.roles: granted.update(self.roles.get(role,set()))
        allowed=action in granted or f"{resource}:{action}" in granted
        decision=AccessDecision(allowed,principal.principal_id,resource,action,"capability matched" if allowed else "capability missing"); self.audit.append(decision); return decision
    def enforce(self, principal: Principal, resource: str, action: str) -> None:
        if not self.decide(principal,resource,action).allowed: raise PermissionError("access denied")
    def report(self) -> dict[str,Any]: return {"decisions":len(self.audit),"allowed":sum(item.allowed for item in self.audit)}


class AccessPolicy001:
    name='access_policy_001'
    sequence=1
    default_scope="scope:1"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy002:
    name='access_policy_002'
    sequence=2
    default_scope="scope:2"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy003:
    name='access_policy_003'
    sequence=3
    default_scope="scope:3"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy004:
    name='access_policy_004'
    sequence=4
    default_scope="scope:4"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy005:
    name='access_policy_005'
    sequence=5
    default_scope="scope:5"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy006:
    name='access_policy_006'
    sequence=6
    default_scope="scope:6"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy007:
    name='access_policy_007'
    sequence=7
    default_scope="scope:7"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy008:
    name='access_policy_008'
    sequence=8
    default_scope="scope:8"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy009:
    name='access_policy_009'
    sequence=9
    default_scope="scope:9"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy010:
    name='access_policy_010'
    sequence=10
    default_scope="scope:10"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy011:
    name='access_policy_011'
    sequence=11
    default_scope="scope:11"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy012:
    name='access_policy_012'
    sequence=12
    default_scope="scope:12"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy013:
    name='access_policy_013'
    sequence=13
    default_scope="scope:13"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy014:
    name='access_policy_014'
    sequence=14
    default_scope="scope:14"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy015:
    name='access_policy_015'
    sequence=15
    default_scope="scope:15"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy016:
    name='access_policy_016'
    sequence=16
    default_scope="scope:0"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy017:
    name='access_policy_017'
    sequence=17
    default_scope="scope:1"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy018:
    name='access_policy_018'
    sequence=18
    default_scope="scope:2"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy019:
    name='access_policy_019'
    sequence=19
    default_scope="scope:3"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy020:
    name='access_policy_020'
    sequence=20
    default_scope="scope:4"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy021:
    name='access_policy_021'
    sequence=21
    default_scope="scope:5"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy022:
    name='access_policy_022'
    sequence=22
    default_scope="scope:6"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy023:
    name='access_policy_023'
    sequence=23
    default_scope="scope:7"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy024:
    name='access_policy_024'
    sequence=24
    default_scope="scope:8"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy025:
    name='access_policy_025'
    sequence=25
    default_scope="scope:9"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy026:
    name='access_policy_026'
    sequence=26
    default_scope="scope:10"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy027:
    name='access_policy_027'
    sequence=27
    default_scope="scope:11"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy028:
    name='access_policy_028'
    sequence=28
    default_scope="scope:12"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy029:
    name='access_policy_029'
    sequence=29
    default_scope="scope:13"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy030:
    name='access_policy_030'
    sequence=30
    default_scope="scope:14"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy031:
    name='access_policy_031'
    sequence=31
    default_scope="scope:15"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy032:
    name='access_policy_032'
    sequence=32
    default_scope="scope:0"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy033:
    name='access_policy_033'
    sequence=33
    default_scope="scope:1"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy034:
    name='access_policy_034'
    sequence=34
    default_scope="scope:2"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy035:
    name='access_policy_035'
    sequence=35
    default_scope="scope:3"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy036:
    name='access_policy_036'
    sequence=36
    default_scope="scope:4"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy037:
    name='access_policy_037'
    sequence=37
    default_scope="scope:5"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy038:
    name='access_policy_038'
    sequence=38
    default_scope="scope:6"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy039:
    name='access_policy_039'
    sequence=39
    default_scope="scope:7"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy040:
    name='access_policy_040'
    sequence=40
    default_scope="scope:8"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy041:
    name='access_policy_041'
    sequence=41
    default_scope="scope:9"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy042:
    name='access_policy_042'
    sequence=42
    default_scope="scope:10"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy043:
    name='access_policy_043'
    sequence=43
    default_scope="scope:11"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy044:
    name='access_policy_044'
    sequence=44
    default_scope="scope:12"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy045:
    name='access_policy_045'
    sequence=45
    default_scope="scope:13"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy046:
    name='access_policy_046'
    sequence=46
    default_scope="scope:14"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy047:
    name='access_policy_047'
    sequence=47
    default_scope="scope:15"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy048:
    name='access_policy_048'
    sequence=48
    default_scope="scope:0"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy049:
    name='access_policy_049'
    sequence=49
    default_scope="scope:1"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy050:
    name='access_policy_050'
    sequence=50
    default_scope="scope:2"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy051:
    name='access_policy_051'
    sequence=51
    default_scope="scope:3"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy052:
    name='access_policy_052'
    sequence=52
    default_scope="scope:4"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy053:
    name='access_policy_053'
    sequence=53
    default_scope="scope:5"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy054:
    name='access_policy_054'
    sequence=54
    default_scope="scope:6"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy055:
    name='access_policy_055'
    sequence=55
    default_scope="scope:7"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy056:
    name='access_policy_056'
    sequence=56
    default_scope="scope:8"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy057:
    name='access_policy_057'
    sequence=57
    default_scope="scope:9"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy058:
    name='access_policy_058'
    sequence=58
    default_scope="scope:10"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy059:
    name='access_policy_059'
    sequence=59
    default_scope="scope:11"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy060:
    name='access_policy_060'
    sequence=60
    default_scope="scope:12"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy061:
    name='access_policy_061'
    sequence=61
    default_scope="scope:13"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy062:
    name='access_policy_062'
    sequence=62
    default_scope="scope:14"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy063:
    name='access_policy_063'
    sequence=63
    default_scope="scope:15"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy064:
    name='access_policy_064'
    sequence=64
    default_scope="scope:0"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy065:
    name='access_policy_065'
    sequence=65
    default_scope="scope:1"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy066:
    name='access_policy_066'
    sequence=66
    default_scope="scope:2"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy067:
    name='access_policy_067'
    sequence=67
    default_scope="scope:3"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy068:
    name='access_policy_068'
    sequence=68
    default_scope="scope:4"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy069:
    name='access_policy_069'
    sequence=69
    default_scope="scope:5"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy070:
    name='access_policy_070'
    sequence=70
    default_scope="scope:6"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy071:
    name='access_policy_071'
    sequence=71
    default_scope="scope:7"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy072:
    name='access_policy_072'
    sequence=72
    default_scope="scope:8"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy073:
    name='access_policy_073'
    sequence=73
    default_scope="scope:9"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy074:
    name='access_policy_074'
    sequence=74
    default_scope="scope:10"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy075:
    name='access_policy_075'
    sequence=75
    default_scope="scope:11"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy076:
    name='access_policy_076'
    sequence=76
    default_scope="scope:12"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy077:
    name='access_policy_077'
    sequence=77
    default_scope="scope:13"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy078:
    name='access_policy_078'
    sequence=78
    default_scope="scope:14"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy079:
    name='access_policy_079'
    sequence=79
    default_scope="scope:15"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy080:
    name='access_policy_080'
    sequence=80
    default_scope="scope:0"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy081:
    name='access_policy_081'
    sequence=81
    default_scope="scope:1"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy082:
    name='access_policy_082'
    sequence=82
    default_scope="scope:2"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy083:
    name='access_policy_083'
    sequence=83
    default_scope="scope:3"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy084:
    name='access_policy_084'
    sequence=84
    default_scope="scope:4"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy085:
    name='access_policy_085'
    sequence=85
    default_scope="scope:5"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy086:
    name='access_policy_086'
    sequence=86
    default_scope="scope:6"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy087:
    name='access_policy_087'
    sequence=87
    default_scope="scope:7"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy088:
    name='access_policy_088'
    sequence=88
    default_scope="scope:8"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy089:
    name='access_policy_089'
    sequence=89
    default_scope="scope:9"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy090:
    name='access_policy_090'
    sequence=90
    default_scope="scope:10"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy091:
    name='access_policy_091'
    sequence=91
    default_scope="scope:11"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy092:
    name='access_policy_092'
    sequence=92
    default_scope="scope:12"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy093:
    name='access_policy_093'
    sequence=93
    default_scope="scope:13"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy094:
    name='access_policy_094'
    sequence=94
    default_scope="scope:14"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy095:
    name='access_policy_095'
    sequence=95
    default_scope="scope:15"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy096:
    name='access_policy_096'
    sequence=96
    default_scope="scope:0"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy097:
    name='access_policy_097'
    sequence=97
    default_scope="scope:1"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy098:
    name='access_policy_098'
    sequence=98
    default_scope="scope:2"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy099:
    name='access_policy_099'
    sequence=99
    default_scope="scope:3"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy100:
    name='access_policy_100'
    sequence=100
    default_scope="scope:4"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy101:
    name='access_policy_101'
    sequence=101
    default_scope="scope:5"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy102:
    name='access_policy_102'
    sequence=102
    default_scope="scope:6"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy103:
    name='access_policy_103'
    sequence=103
    default_scope="scope:7"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy104:
    name='access_policy_104'
    sequence=104
    default_scope="scope:8"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy105:
    name='access_policy_105'
    sequence=105
    default_scope="scope:9"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy106:
    name='access_policy_106'
    sequence=106
    default_scope="scope:10"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy107:
    name='access_policy_107'
    sequence=107
    default_scope="scope:11"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy108:
    name='access_policy_108'
    sequence=108
    default_scope="scope:12"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy109:
    name='access_policy_109'
    sequence=109
    default_scope="scope:13"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy110:
    name='access_policy_110'
    sequence=110
    default_scope="scope:14"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy111:
    name='access_policy_111'
    sequence=111
    default_scope="scope:15"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy112:
    name='access_policy_112'
    sequence=112
    default_scope="scope:0"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy113:
    name='access_policy_113'
    sequence=113
    default_scope="scope:1"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy114:
    name='access_policy_114'
    sequence=114
    default_scope="scope:2"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy115:
    name='access_policy_115'
    sequence=115
    default_scope="scope:3"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy116:
    name='access_policy_116'
    sequence=116
    default_scope="scope:4"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy117:
    name='access_policy_117'
    sequence=117
    default_scope="scope:5"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy118:
    name='access_policy_118'
    sequence=118
    default_scope="scope:6"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy119:
    name='access_policy_119'
    sequence=119
    default_scope="scope:7"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy120:
    name='access_policy_120'
    sequence=120
    default_scope="scope:8"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy121:
    name='access_policy_121'
    sequence=121
    default_scope="scope:9"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy122:
    name='access_policy_122'
    sequence=122
    default_scope="scope:10"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy123:
    name='access_policy_123'
    sequence=123
    default_scope="scope:11"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy124:
    name='access_policy_124'
    sequence=124
    default_scope="scope:12"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy125:
    name='access_policy_125'
    sequence=125
    default_scope="scope:13"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy126:
    name='access_policy_126'
    sequence=126
    default_scope="scope:14"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy127:
    name='access_policy_127'
    sequence=127
    default_scope="scope:15"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy128:
    name='access_policy_128'
    sequence=128
    default_scope="scope:0"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy129:
    name='access_policy_129'
    sequence=129
    default_scope="scope:1"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy130:
    name='access_policy_130'
    sequence=130
    default_scope="scope:2"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy131:
    name='access_policy_131'
    sequence=131
    default_scope="scope:3"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy132:
    name='access_policy_132'
    sequence=132
    default_scope="scope:4"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy133:
    name='access_policy_133'
    sequence=133
    default_scope="scope:5"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy134:
    name='access_policy_134'
    sequence=134
    default_scope="scope:6"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy135:
    name='access_policy_135'
    sequence=135
    default_scope="scope:7"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy136:
    name='access_policy_136'
    sequence=136
    default_scope="scope:8"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy137:
    name='access_policy_137'
    sequence=137
    default_scope="scope:9"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy138:
    name='access_policy_138'
    sequence=138
    default_scope="scope:10"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy139:
    name='access_policy_139'
    sequence=139
    default_scope="scope:11"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy140:
    name='access_policy_140'
    sequence=140
    default_scope="scope:12"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy141:
    name='access_policy_141'
    sequence=141
    default_scope="scope:13"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy142:
    name='access_policy_142'
    sequence=142
    default_scope="scope:14"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy143:
    name='access_policy_143'
    sequence=143
    default_scope="scope:15"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy144:
    name='access_policy_144'
    sequence=144
    default_scope="scope:0"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy145:
    name='access_policy_145'
    sequence=145
    default_scope="scope:1"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy146:
    name='access_policy_146'
    sequence=146
    default_scope="scope:2"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy147:
    name='access_policy_147'
    sequence=147
    default_scope="scope:3"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy148:
    name='access_policy_148'
    sequence=148
    default_scope="scope:4"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy149:
    name='access_policy_149'
    sequence=149
    default_scope="scope:5"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy150:
    name='access_policy_150'
    sequence=150
    default_scope="scope:6"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy151:
    name='access_policy_151'
    sequence=151
    default_scope="scope:7"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy152:
    name='access_policy_152'
    sequence=152
    default_scope="scope:8"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy153:
    name='access_policy_153'
    sequence=153
    default_scope="scope:9"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy154:
    name='access_policy_154'
    sequence=154
    default_scope="scope:10"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy155:
    name='access_policy_155'
    sequence=155
    default_scope="scope:11"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy156:
    name='access_policy_156'
    sequence=156
    default_scope="scope:12"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy157:
    name='access_policy_157'
    sequence=157
    default_scope="scope:13"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy158:
    name='access_policy_158'
    sequence=158
    default_scope="scope:14"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy159:
    name='access_policy_159'
    sequence=159
    default_scope="scope:15"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy160:
    name='access_policy_160'
    sequence=160
    default_scope="scope:0"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy161:
    name='access_policy_161'
    sequence=161
    default_scope="scope:1"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy162:
    name='access_policy_162'
    sequence=162
    default_scope="scope:2"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy163:
    name='access_policy_163'
    sequence=163
    default_scope="scope:3"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy164:
    name='access_policy_164'
    sequence=164
    default_scope="scope:4"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy165:
    name='access_policy_165'
    sequence=165
    default_scope="scope:5"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy166:
    name='access_policy_166'
    sequence=166
    default_scope="scope:6"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy167:
    name='access_policy_167'
    sequence=167
    default_scope="scope:7"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy168:
    name='access_policy_168'
    sequence=168
    default_scope="scope:8"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy169:
    name='access_policy_169'
    sequence=169
    default_scope="scope:9"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy170:
    name='access_policy_170'
    sequence=170
    default_scope="scope:10"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy171:
    name='access_policy_171'
    sequence=171
    default_scope="scope:11"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy172:
    name='access_policy_172'
    sequence=172
    default_scope="scope:12"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy173:
    name='access_policy_173'
    sequence=173
    default_scope="scope:13"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy174:
    name='access_policy_174'
    sequence=174
    default_scope="scope:14"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy175:
    name='access_policy_175'
    sequence=175
    default_scope="scope:15"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy176:
    name='access_policy_176'
    sequence=176
    default_scope="scope:0"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy177:
    name='access_policy_177'
    sequence=177
    default_scope="scope:1"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy178:
    name='access_policy_178'
    sequence=178
    default_scope="scope:2"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy179:
    name='access_policy_179'
    sequence=179
    default_scope="scope:3"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy180:
    name='access_policy_180'
    sequence=180
    default_scope="scope:4"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy181:
    name='access_policy_181'
    sequence=181
    default_scope="scope:5"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy182:
    name='access_policy_182'
    sequence=182
    default_scope="scope:6"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy183:
    name='access_policy_183'
    sequence=183
    default_scope="scope:7"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy184:
    name='access_policy_184'
    sequence=184
    default_scope="scope:8"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy185:
    name='access_policy_185'
    sequence=185
    default_scope="scope:9"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy186:
    name='access_policy_186'
    sequence=186
    default_scope="scope:10"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy187:
    name='access_policy_187'
    sequence=187
    default_scope="scope:11"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy188:
    name='access_policy_188'
    sequence=188
    default_scope="scope:12"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy189:
    name='access_policy_189'
    sequence=189
    default_scope="scope:13"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy190:
    name='access_policy_190'
    sequence=190
    default_scope="scope:14"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy191:
    name='access_policy_191'
    sequence=191
    default_scope="scope:15"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy192:
    name='access_policy_192'
    sequence=192
    default_scope="scope:0"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy193:
    name='access_policy_193'
    sequence=193
    default_scope="scope:1"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy194:
    name='access_policy_194'
    sequence=194
    default_scope="scope:2"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy195:
    name='access_policy_195'
    sequence=195
    default_scope="scope:3"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy196:
    name='access_policy_196'
    sequence=196
    default_scope="scope:4"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy197:
    name='access_policy_197'
    sequence=197
    default_scope="scope:5"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy198:
    name='access_policy_198'
    sequence=198
    default_scope="scope:6"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy199:
    name='access_policy_199'
    sequence=199
    default_scope="scope:7"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy200:
    name='access_policy_200'
    sequence=200
    default_scope="scope:8"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy201:
    name='access_policy_201'
    sequence=201
    default_scope="scope:9"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy202:
    name='access_policy_202'
    sequence=202
    default_scope="scope:10"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy203:
    name='access_policy_203'
    sequence=203
    default_scope="scope:11"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy204:
    name='access_policy_204'
    sequence=204
    default_scope="scope:12"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy205:
    name='access_policy_205'
    sequence=205
    default_scope="scope:13"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy206:
    name='access_policy_206'
    sequence=206
    default_scope="scope:14"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy207:
    name='access_policy_207'
    sequence=207
    default_scope="scope:15"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy208:
    name='access_policy_208'
    sequence=208
    default_scope="scope:0"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy209:
    name='access_policy_209'
    sequence=209
    default_scope="scope:1"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy210:
    name='access_policy_210'
    sequence=210
    default_scope="scope:2"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy211:
    name='access_policy_211'
    sequence=211
    default_scope="scope:3"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy212:
    name='access_policy_212'
    sequence=212
    default_scope="scope:4"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy213:
    name='access_policy_213'
    sequence=213
    default_scope="scope:5"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy214:
    name='access_policy_214'
    sequence=214
    default_scope="scope:6"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy215:
    name='access_policy_215'
    sequence=215
    default_scope="scope:7"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy216:
    name='access_policy_216'
    sequence=216
    default_scope="scope:8"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy217:
    name='access_policy_217'
    sequence=217
    default_scope="scope:9"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy218:
    name='access_policy_218'
    sequence=218
    default_scope="scope:10"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy219:
    name='access_policy_219'
    sequence=219
    default_scope="scope:11"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy220:
    name='access_policy_220'
    sequence=220
    default_scope="scope:12"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy221:
    name='access_policy_221'
    sequence=221
    default_scope="scope:13"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy222:
    name='access_policy_222'
    sequence=222
    default_scope="scope:14"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy223:
    name='access_policy_223'
    sequence=223
    default_scope="scope:15"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy224:
    name='access_policy_224'
    sequence=224
    default_scope="scope:0"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy225:
    name='access_policy_225'
    sequence=225
    default_scope="scope:1"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy226:
    name='access_policy_226'
    sequence=226
    default_scope="scope:2"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy227:
    name='access_policy_227'
    sequence=227
    default_scope="scope:3"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy228:
    name='access_policy_228'
    sequence=228
    default_scope="scope:4"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy229:
    name='access_policy_229'
    sequence=229
    default_scope="scope:5"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy230:
    name='access_policy_230'
    sequence=230
    default_scope="scope:6"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy231:
    name='access_policy_231'
    sequence=231
    default_scope="scope:7"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy232:
    name='access_policy_232'
    sequence=232
    default_scope="scope:8"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy233:
    name='access_policy_233'
    sequence=233
    default_scope="scope:9"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy234:
    name='access_policy_234'
    sequence=234
    default_scope="scope:10"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy235:
    name='access_policy_235'
    sequence=235
    default_scope="scope:11"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy236:
    name='access_policy_236'
    sequence=236
    default_scope="scope:12"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy237:
    name='access_policy_237'
    sequence=237
    default_scope="scope:13"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy238:
    name='access_policy_238'
    sequence=238
    default_scope="scope:14"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy239:
    name='access_policy_239'
    sequence=239
    default_scope="scope:15"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy240:
    name='access_policy_240'
    sequence=240
    default_scope="scope:0"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy241:
    name='access_policy_241'
    sequence=241
    default_scope="scope:1"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy242:
    name='access_policy_242'
    sequence=242
    default_scope="scope:2"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy243:
    name='access_policy_243'
    sequence=243
    default_scope="scope:3"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy244:
    name='access_policy_244'
    sequence=244
    default_scope="scope:4"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy245:
    name='access_policy_245'
    sequence=245
    default_scope="scope:5"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy246:
    name='access_policy_246'
    sequence=246
    default_scope="scope:6"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy247:
    name='access_policy_247'
    sequence=247
    default_scope="scope:7"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy248:
    name='access_policy_248'
    sequence=248
    default_scope="scope:8"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy249:
    name='access_policy_249'
    sequence=249
    default_scope="scope:9"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy250:
    name='access_policy_250'
    sequence=250
    default_scope="scope:10"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy251:
    name='access_policy_251'
    sequence=251
    default_scope="scope:11"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy252:
    name='access_policy_252'
    sequence=252
    default_scope="scope:12"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy253:
    name='access_policy_253'
    sequence=253
    default_scope="scope:13"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy254:
    name='access_policy_254'
    sequence=254
    default_scope="scope:14"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy255:
    name='access_policy_255'
    sequence=255
    default_scope="scope:15"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy256:
    name='access_policy_256'
    sequence=256
    default_scope="scope:0"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy257:
    name='access_policy_257'
    sequence=257
    default_scope="scope:1"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy258:
    name='access_policy_258'
    sequence=258
    default_scope="scope:2"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy259:
    name='access_policy_259'
    sequence=259
    default_scope="scope:3"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy260:
    name='access_policy_260'
    sequence=260
    default_scope="scope:4"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy261:
    name='access_policy_261'
    sequence=261
    default_scope="scope:5"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy262:
    name='access_policy_262'
    sequence=262
    default_scope="scope:6"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy263:
    name='access_policy_263'
    sequence=263
    default_scope="scope:7"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy264:
    name='access_policy_264'
    sequence=264
    default_scope="scope:8"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy265:
    name='access_policy_265'
    sequence=265
    default_scope="scope:9"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy266:
    name='access_policy_266'
    sequence=266
    default_scope="scope:10"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy267:
    name='access_policy_267'
    sequence=267
    default_scope="scope:11"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy268:
    name='access_policy_268'
    sequence=268
    default_scope="scope:12"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy269:
    name='access_policy_269'
    sequence=269
    default_scope="scope:13"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy270:
    name='access_policy_270'
    sequence=270
    default_scope="scope:14"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy271:
    name='access_policy_271'
    sequence=271
    default_scope="scope:15"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy272:
    name='access_policy_272'
    sequence=272
    default_scope="scope:0"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy273:
    name='access_policy_273'
    sequence=273
    default_scope="scope:1"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy274:
    name='access_policy_274'
    sequence=274
    default_scope="scope:2"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy275:
    name='access_policy_275'
    sequence=275
    default_scope="scope:3"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy276:
    name='access_policy_276'
    sequence=276
    default_scope="scope:4"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy277:
    name='access_policy_277'
    sequence=277
    default_scope="scope:5"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy278:
    name='access_policy_278'
    sequence=278
    default_scope="scope:6"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy279:
    name='access_policy_279'
    sequence=279
    default_scope="scope:7"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy280:
    name='access_policy_280'
    sequence=280
    default_scope="scope:8"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy281:
    name='access_policy_281'
    sequence=281
    default_scope="scope:9"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy282:
    name='access_policy_282'
    sequence=282
    default_scope="scope:10"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy283:
    name='access_policy_283'
    sequence=283
    default_scope="scope:11"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy284:
    name='access_policy_284'
    sequence=284
    default_scope="scope:12"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy285:
    name='access_policy_285'
    sequence=285
    default_scope="scope:13"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy286:
    name='access_policy_286'
    sequence=286
    default_scope="scope:14"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy287:
    name='access_policy_287'
    sequence=287
    default_scope="scope:15"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy288:
    name='access_policy_288'
    sequence=288
    default_scope="scope:0"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy289:
    name='access_policy_289'
    sequence=289
    default_scope="scope:1"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy290:
    name='access_policy_290'
    sequence=290
    default_scope="scope:2"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy291:
    name='access_policy_291'
    sequence=291
    default_scope="scope:3"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy292:
    name='access_policy_292'
    sequence=292
    default_scope="scope:4"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy293:
    name='access_policy_293'
    sequence=293
    default_scope="scope:5"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy294:
    name='access_policy_294'
    sequence=294
    default_scope="scope:6"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy295:
    name='access_policy_295'
    sequence=295
    default_scope="scope:7"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy296:
    name='access_policy_296'
    sequence=296
    default_scope="scope:8"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy297:
    name='access_policy_297'
    sequence=297
    default_scope="scope:9"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy298:
    name='access_policy_298'
    sequence=298
    default_scope="scope:10"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy299:
    name='access_policy_299'
    sequence=299
    default_scope="scope:11"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy300:
    name='access_policy_300'
    sequence=300
    default_scope="scope:12"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy301:
    name='access_policy_301'
    sequence=301
    default_scope="scope:13"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy302:
    name='access_policy_302'
    sequence=302
    default_scope="scope:14"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy303:
    name='access_policy_303'
    sequence=303
    default_scope="scope:15"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy304:
    name='access_policy_304'
    sequence=304
    default_scope="scope:0"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy305:
    name='access_policy_305'
    sequence=305
    default_scope="scope:1"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy306:
    name='access_policy_306'
    sequence=306
    default_scope="scope:2"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy307:
    name='access_policy_307'
    sequence=307
    default_scope="scope:3"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy308:
    name='access_policy_308'
    sequence=308
    default_scope="scope:4"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy309:
    name='access_policy_309'
    sequence=309
    default_scope="scope:5"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy310:
    name='access_policy_310'
    sequence=310
    default_scope="scope:6"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy311:
    name='access_policy_311'
    sequence=311
    default_scope="scope:7"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy312:
    name='access_policy_312'
    sequence=312
    default_scope="scope:8"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy313:
    name='access_policy_313'
    sequence=313
    default_scope="scope:9"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy314:
    name='access_policy_314'
    sequence=314
    default_scope="scope:10"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy315:
    name='access_policy_315'
    sequence=315
    default_scope="scope:11"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy316:
    name='access_policy_316'
    sequence=316
    default_scope="scope:12"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy317:
    name='access_policy_317'
    sequence=317
    default_scope="scope:13"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy318:
    name='access_policy_318'
    sequence=318
    default_scope="scope:14"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy319:
    name='access_policy_319'
    sequence=319
    default_scope="scope:15"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

class AccessPolicy320:
    name='access_policy_320'
    sequence=320
    default_scope="scope:0"
    def allows(self, principal: Principal, action: str) -> bool: return action in principal.capabilities or self.default_scope in principal.capabilities
    def metadata(self) -> dict[str,Any]: return {"name":self.name,"sequence":self.sequence,"default_scope":self.default_scope}

ACCESS_POLICIES={
    'access_policy_001': AccessPolicy001(),
    'access_policy_002': AccessPolicy002(),
    'access_policy_003': AccessPolicy003(),
    'access_policy_004': AccessPolicy004(),
    'access_policy_005': AccessPolicy005(),
    'access_policy_006': AccessPolicy006(),
    'access_policy_007': AccessPolicy007(),
    'access_policy_008': AccessPolicy008(),
    'access_policy_009': AccessPolicy009(),
    'access_policy_010': AccessPolicy010(),
    'access_policy_011': AccessPolicy011(),
    'access_policy_012': AccessPolicy012(),
    'access_policy_013': AccessPolicy013(),
    'access_policy_014': AccessPolicy014(),
    'access_policy_015': AccessPolicy015(),
    'access_policy_016': AccessPolicy016(),
    'access_policy_017': AccessPolicy017(),
    'access_policy_018': AccessPolicy018(),
    'access_policy_019': AccessPolicy019(),
    'access_policy_020': AccessPolicy020(),
    'access_policy_021': AccessPolicy021(),
    'access_policy_022': AccessPolicy022(),
    'access_policy_023': AccessPolicy023(),
    'access_policy_024': AccessPolicy024(),
    'access_policy_025': AccessPolicy025(),
    'access_policy_026': AccessPolicy026(),
    'access_policy_027': AccessPolicy027(),
    'access_policy_028': AccessPolicy028(),
    'access_policy_029': AccessPolicy029(),
    'access_policy_030': AccessPolicy030(),
    'access_policy_031': AccessPolicy031(),
    'access_policy_032': AccessPolicy032(),
    'access_policy_033': AccessPolicy033(),
    'access_policy_034': AccessPolicy034(),
    'access_policy_035': AccessPolicy035(),
    'access_policy_036': AccessPolicy036(),
    'access_policy_037': AccessPolicy037(),
    'access_policy_038': AccessPolicy038(),
    'access_policy_039': AccessPolicy039(),
    'access_policy_040': AccessPolicy040(),
    'access_policy_041': AccessPolicy041(),
    'access_policy_042': AccessPolicy042(),
    'access_policy_043': AccessPolicy043(),
    'access_policy_044': AccessPolicy044(),
    'access_policy_045': AccessPolicy045(),
    'access_policy_046': AccessPolicy046(),
    'access_policy_047': AccessPolicy047(),
    'access_policy_048': AccessPolicy048(),
    'access_policy_049': AccessPolicy049(),
    'access_policy_050': AccessPolicy050(),
    'access_policy_051': AccessPolicy051(),
    'access_policy_052': AccessPolicy052(),
    'access_policy_053': AccessPolicy053(),
    'access_policy_054': AccessPolicy054(),
    'access_policy_055': AccessPolicy055(),
    'access_policy_056': AccessPolicy056(),
    'access_policy_057': AccessPolicy057(),
    'access_policy_058': AccessPolicy058(),
    'access_policy_059': AccessPolicy059(),
    'access_policy_060': AccessPolicy060(),
    'access_policy_061': AccessPolicy061(),
    'access_policy_062': AccessPolicy062(),
    'access_policy_063': AccessPolicy063(),
    'access_policy_064': AccessPolicy064(),
    'access_policy_065': AccessPolicy065(),
    'access_policy_066': AccessPolicy066(),
    'access_policy_067': AccessPolicy067(),
    'access_policy_068': AccessPolicy068(),
    'access_policy_069': AccessPolicy069(),
    'access_policy_070': AccessPolicy070(),
    'access_policy_071': AccessPolicy071(),
    'access_policy_072': AccessPolicy072(),
    'access_policy_073': AccessPolicy073(),
    'access_policy_074': AccessPolicy074(),
    'access_policy_075': AccessPolicy075(),
    'access_policy_076': AccessPolicy076(),
    'access_policy_077': AccessPolicy077(),
    'access_policy_078': AccessPolicy078(),
    'access_policy_079': AccessPolicy079(),
    'access_policy_080': AccessPolicy080(),
    'access_policy_081': AccessPolicy081(),
    'access_policy_082': AccessPolicy082(),
    'access_policy_083': AccessPolicy083(),
    'access_policy_084': AccessPolicy084(),
    'access_policy_085': AccessPolicy085(),
    'access_policy_086': AccessPolicy086(),
    'access_policy_087': AccessPolicy087(),
    'access_policy_088': AccessPolicy088(),
    'access_policy_089': AccessPolicy089(),
    'access_policy_090': AccessPolicy090(),
    'access_policy_091': AccessPolicy091(),
    'access_policy_092': AccessPolicy092(),
    'access_policy_093': AccessPolicy093(),
    'access_policy_094': AccessPolicy094(),
    'access_policy_095': AccessPolicy095(),
    'access_policy_096': AccessPolicy096(),
    'access_policy_097': AccessPolicy097(),
    'access_policy_098': AccessPolicy098(),
    'access_policy_099': AccessPolicy099(),
    'access_policy_100': AccessPolicy100(),
    'access_policy_101': AccessPolicy101(),
    'access_policy_102': AccessPolicy102(),
    'access_policy_103': AccessPolicy103(),
    'access_policy_104': AccessPolicy104(),
    'access_policy_105': AccessPolicy105(),
    'access_policy_106': AccessPolicy106(),
    'access_policy_107': AccessPolicy107(),
    'access_policy_108': AccessPolicy108(),
    'access_policy_109': AccessPolicy109(),
    'access_policy_110': AccessPolicy110(),
    'access_policy_111': AccessPolicy111(),
    'access_policy_112': AccessPolicy112(),
    'access_policy_113': AccessPolicy113(),
    'access_policy_114': AccessPolicy114(),
    'access_policy_115': AccessPolicy115(),
    'access_policy_116': AccessPolicy116(),
    'access_policy_117': AccessPolicy117(),
    'access_policy_118': AccessPolicy118(),
    'access_policy_119': AccessPolicy119(),
    'access_policy_120': AccessPolicy120(),
    'access_policy_121': AccessPolicy121(),
    'access_policy_122': AccessPolicy122(),
    'access_policy_123': AccessPolicy123(),
    'access_policy_124': AccessPolicy124(),
    'access_policy_125': AccessPolicy125(),
    'access_policy_126': AccessPolicy126(),
    'access_policy_127': AccessPolicy127(),
    'access_policy_128': AccessPolicy128(),
    'access_policy_129': AccessPolicy129(),
    'access_policy_130': AccessPolicy130(),
    'access_policy_131': AccessPolicy131(),
    'access_policy_132': AccessPolicy132(),
    'access_policy_133': AccessPolicy133(),
    'access_policy_134': AccessPolicy134(),
    'access_policy_135': AccessPolicy135(),
    'access_policy_136': AccessPolicy136(),
    'access_policy_137': AccessPolicy137(),
    'access_policy_138': AccessPolicy138(),
    'access_policy_139': AccessPolicy139(),
    'access_policy_140': AccessPolicy140(),
    'access_policy_141': AccessPolicy141(),
    'access_policy_142': AccessPolicy142(),
    'access_policy_143': AccessPolicy143(),
    'access_policy_144': AccessPolicy144(),
    'access_policy_145': AccessPolicy145(),
    'access_policy_146': AccessPolicy146(),
    'access_policy_147': AccessPolicy147(),
    'access_policy_148': AccessPolicy148(),
    'access_policy_149': AccessPolicy149(),
    'access_policy_150': AccessPolicy150(),
    'access_policy_151': AccessPolicy151(),
    'access_policy_152': AccessPolicy152(),
    'access_policy_153': AccessPolicy153(),
    'access_policy_154': AccessPolicy154(),
    'access_policy_155': AccessPolicy155(),
    'access_policy_156': AccessPolicy156(),
    'access_policy_157': AccessPolicy157(),
    'access_policy_158': AccessPolicy158(),
    'access_policy_159': AccessPolicy159(),
    'access_policy_160': AccessPolicy160(),
    'access_policy_161': AccessPolicy161(),
    'access_policy_162': AccessPolicy162(),
    'access_policy_163': AccessPolicy163(),
    'access_policy_164': AccessPolicy164(),
    'access_policy_165': AccessPolicy165(),
    'access_policy_166': AccessPolicy166(),
    'access_policy_167': AccessPolicy167(),
    'access_policy_168': AccessPolicy168(),
    'access_policy_169': AccessPolicy169(),
    'access_policy_170': AccessPolicy170(),
    'access_policy_171': AccessPolicy171(),
    'access_policy_172': AccessPolicy172(),
    'access_policy_173': AccessPolicy173(),
    'access_policy_174': AccessPolicy174(),
    'access_policy_175': AccessPolicy175(),
    'access_policy_176': AccessPolicy176(),
    'access_policy_177': AccessPolicy177(),
    'access_policy_178': AccessPolicy178(),
    'access_policy_179': AccessPolicy179(),
    'access_policy_180': AccessPolicy180(),
    'access_policy_181': AccessPolicy181(),
    'access_policy_182': AccessPolicy182(),
    'access_policy_183': AccessPolicy183(),
    'access_policy_184': AccessPolicy184(),
    'access_policy_185': AccessPolicy185(),
    'access_policy_186': AccessPolicy186(),
    'access_policy_187': AccessPolicy187(),
    'access_policy_188': AccessPolicy188(),
    'access_policy_189': AccessPolicy189(),
    'access_policy_190': AccessPolicy190(),
    'access_policy_191': AccessPolicy191(),
    'access_policy_192': AccessPolicy192(),
    'access_policy_193': AccessPolicy193(),
    'access_policy_194': AccessPolicy194(),
    'access_policy_195': AccessPolicy195(),
    'access_policy_196': AccessPolicy196(),
    'access_policy_197': AccessPolicy197(),
    'access_policy_198': AccessPolicy198(),
    'access_policy_199': AccessPolicy199(),
    'access_policy_200': AccessPolicy200(),
    'access_policy_201': AccessPolicy201(),
    'access_policy_202': AccessPolicy202(),
    'access_policy_203': AccessPolicy203(),
    'access_policy_204': AccessPolicy204(),
    'access_policy_205': AccessPolicy205(),
    'access_policy_206': AccessPolicy206(),
    'access_policy_207': AccessPolicy207(),
    'access_policy_208': AccessPolicy208(),
    'access_policy_209': AccessPolicy209(),
    'access_policy_210': AccessPolicy210(),
    'access_policy_211': AccessPolicy211(),
    'access_policy_212': AccessPolicy212(),
    'access_policy_213': AccessPolicy213(),
    'access_policy_214': AccessPolicy214(),
    'access_policy_215': AccessPolicy215(),
    'access_policy_216': AccessPolicy216(),
    'access_policy_217': AccessPolicy217(),
    'access_policy_218': AccessPolicy218(),
    'access_policy_219': AccessPolicy219(),
    'access_policy_220': AccessPolicy220(),
    'access_policy_221': AccessPolicy221(),
    'access_policy_222': AccessPolicy222(),
    'access_policy_223': AccessPolicy223(),
    'access_policy_224': AccessPolicy224(),
    'access_policy_225': AccessPolicy225(),
    'access_policy_226': AccessPolicy226(),
    'access_policy_227': AccessPolicy227(),
    'access_policy_228': AccessPolicy228(),
    'access_policy_229': AccessPolicy229(),
    'access_policy_230': AccessPolicy230(),
    'access_policy_231': AccessPolicy231(),
    'access_policy_232': AccessPolicy232(),
    'access_policy_233': AccessPolicy233(),
    'access_policy_234': AccessPolicy234(),
    'access_policy_235': AccessPolicy235(),
    'access_policy_236': AccessPolicy236(),
    'access_policy_237': AccessPolicy237(),
    'access_policy_238': AccessPolicy238(),
    'access_policy_239': AccessPolicy239(),
    'access_policy_240': AccessPolicy240(),
    'access_policy_241': AccessPolicy241(),
    'access_policy_242': AccessPolicy242(),
    'access_policy_243': AccessPolicy243(),
    'access_policy_244': AccessPolicy244(),
    'access_policy_245': AccessPolicy245(),
    'access_policy_246': AccessPolicy246(),
    'access_policy_247': AccessPolicy247(),
    'access_policy_248': AccessPolicy248(),
    'access_policy_249': AccessPolicy249(),
    'access_policy_250': AccessPolicy250(),
    'access_policy_251': AccessPolicy251(),
    'access_policy_252': AccessPolicy252(),
    'access_policy_253': AccessPolicy253(),
    'access_policy_254': AccessPolicy254(),
    'access_policy_255': AccessPolicy255(),
    'access_policy_256': AccessPolicy256(),
    'access_policy_257': AccessPolicy257(),
    'access_policy_258': AccessPolicy258(),
    'access_policy_259': AccessPolicy259(),
    'access_policy_260': AccessPolicy260(),
    'access_policy_261': AccessPolicy261(),
    'access_policy_262': AccessPolicy262(),
    'access_policy_263': AccessPolicy263(),
    'access_policy_264': AccessPolicy264(),
    'access_policy_265': AccessPolicy265(),
    'access_policy_266': AccessPolicy266(),
    'access_policy_267': AccessPolicy267(),
    'access_policy_268': AccessPolicy268(),
    'access_policy_269': AccessPolicy269(),
    'access_policy_270': AccessPolicy270(),
    'access_policy_271': AccessPolicy271(),
    'access_policy_272': AccessPolicy272(),
    'access_policy_273': AccessPolicy273(),
    'access_policy_274': AccessPolicy274(),
    'access_policy_275': AccessPolicy275(),
    'access_policy_276': AccessPolicy276(),
    'access_policy_277': AccessPolicy277(),
    'access_policy_278': AccessPolicy278(),
    'access_policy_279': AccessPolicy279(),
    'access_policy_280': AccessPolicy280(),
    'access_policy_281': AccessPolicy281(),
    'access_policy_282': AccessPolicy282(),
    'access_policy_283': AccessPolicy283(),
    'access_policy_284': AccessPolicy284(),
    'access_policy_285': AccessPolicy285(),
    'access_policy_286': AccessPolicy286(),
    'access_policy_287': AccessPolicy287(),
    'access_policy_288': AccessPolicy288(),
    'access_policy_289': AccessPolicy289(),
    'access_policy_290': AccessPolicy290(),
    'access_policy_291': AccessPolicy291(),
    'access_policy_292': AccessPolicy292(),
    'access_policy_293': AccessPolicy293(),
    'access_policy_294': AccessPolicy294(),
    'access_policy_295': AccessPolicy295(),
    'access_policy_296': AccessPolicy296(),
    'access_policy_297': AccessPolicy297(),
    'access_policy_298': AccessPolicy298(),
    'access_policy_299': AccessPolicy299(),
    'access_policy_300': AccessPolicy300(),
    'access_policy_301': AccessPolicy301(),
    'access_policy_302': AccessPolicy302(),
    'access_policy_303': AccessPolicy303(),
    'access_policy_304': AccessPolicy304(),
    'access_policy_305': AccessPolicy305(),
    'access_policy_306': AccessPolicy306(),
    'access_policy_307': AccessPolicy307(),
    'access_policy_308': AccessPolicy308(),
    'access_policy_309': AccessPolicy309(),
    'access_policy_310': AccessPolicy310(),
    'access_policy_311': AccessPolicy311(),
    'access_policy_312': AccessPolicy312(),
    'access_policy_313': AccessPolicy313(),
    'access_policy_314': AccessPolicy314(),
    'access_policy_315': AccessPolicy315(),
    'access_policy_316': AccessPolicy316(),
    'access_policy_317': AccessPolicy317(),
    'access_policy_318': AccessPolicy318(),
    'access_policy_319': AccessPolicy319(),
    'access_policy_320': AccessPolicy320(),
}


class AdvancedPolicy001AccessPolicy:
    name='advanced_policy_001'
    sequence=6000
    scope='advanced_policy_001'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy002AccessPolicy:
    name='advanced_policy_002'
    sequence=6001
    scope='advanced_policy_002'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy003AccessPolicy:
    name='advanced_policy_003'
    sequence=6002
    scope='advanced_policy_003'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy004AccessPolicy:
    name='advanced_policy_004'
    sequence=6003
    scope='advanced_policy_004'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy005AccessPolicy:
    name='advanced_policy_005'
    sequence=6004
    scope='advanced_policy_005'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy006AccessPolicy:
    name='advanced_policy_006'
    sequence=6005
    scope='advanced_policy_006'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy007AccessPolicy:
    name='advanced_policy_007'
    sequence=6006
    scope='advanced_policy_007'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy008AccessPolicy:
    name='advanced_policy_008'
    sequence=6007
    scope='advanced_policy_008'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy009AccessPolicy:
    name='advanced_policy_009'
    sequence=6008
    scope='advanced_policy_009'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy010AccessPolicy:
    name='advanced_policy_010'
    sequence=6009
    scope='advanced_policy_010'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy011AccessPolicy:
    name='advanced_policy_011'
    sequence=6010
    scope='advanced_policy_011'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy012AccessPolicy:
    name='advanced_policy_012'
    sequence=6011
    scope='advanced_policy_012'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy013AccessPolicy:
    name='advanced_policy_013'
    sequence=6012
    scope='advanced_policy_013'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy014AccessPolicy:
    name='advanced_policy_014'
    sequence=6013
    scope='advanced_policy_014'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy015AccessPolicy:
    name='advanced_policy_015'
    sequence=6014
    scope='advanced_policy_015'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy016AccessPolicy:
    name='advanced_policy_016'
    sequence=6015
    scope='advanced_policy_016'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy017AccessPolicy:
    name='advanced_policy_017'
    sequence=6016
    scope='advanced_policy_017'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy018AccessPolicy:
    name='advanced_policy_018'
    sequence=6017
    scope='advanced_policy_018'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy019AccessPolicy:
    name='advanced_policy_019'
    sequence=6018
    scope='advanced_policy_019'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy020AccessPolicy:
    name='advanced_policy_020'
    sequence=6019
    scope='advanced_policy_020'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy021AccessPolicy:
    name='advanced_policy_021'
    sequence=6020
    scope='advanced_policy_021'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy022AccessPolicy:
    name='advanced_policy_022'
    sequence=6021
    scope='advanced_policy_022'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy023AccessPolicy:
    name='advanced_policy_023'
    sequence=6022
    scope='advanced_policy_023'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy024AccessPolicy:
    name='advanced_policy_024'
    sequence=6023
    scope='advanced_policy_024'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy025AccessPolicy:
    name='advanced_policy_025'
    sequence=6024
    scope='advanced_policy_025'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy026AccessPolicy:
    name='advanced_policy_026'
    sequence=6025
    scope='advanced_policy_026'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy027AccessPolicy:
    name='advanced_policy_027'
    sequence=6026
    scope='advanced_policy_027'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy028AccessPolicy:
    name='advanced_policy_028'
    sequence=6027
    scope='advanced_policy_028'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy029AccessPolicy:
    name='advanced_policy_029'
    sequence=6028
    scope='advanced_policy_029'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy030AccessPolicy:
    name='advanced_policy_030'
    sequence=6029
    scope='advanced_policy_030'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy031AccessPolicy:
    name='advanced_policy_031'
    sequence=6030
    scope='advanced_policy_031'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy032AccessPolicy:
    name='advanced_policy_032'
    sequence=6031
    scope='advanced_policy_032'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy033AccessPolicy:
    name='advanced_policy_033'
    sequence=6032
    scope='advanced_policy_033'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy034AccessPolicy:
    name='advanced_policy_034'
    sequence=6033
    scope='advanced_policy_034'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy035AccessPolicy:
    name='advanced_policy_035'
    sequence=6034
    scope='advanced_policy_035'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy036AccessPolicy:
    name='advanced_policy_036'
    sequence=6035
    scope='advanced_policy_036'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy037AccessPolicy:
    name='advanced_policy_037'
    sequence=6036
    scope='advanced_policy_037'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy038AccessPolicy:
    name='advanced_policy_038'
    sequence=6037
    scope='advanced_policy_038'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy039AccessPolicy:
    name='advanced_policy_039'
    sequence=6038
    scope='advanced_policy_039'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy040AccessPolicy:
    name='advanced_policy_040'
    sequence=6039
    scope='advanced_policy_040'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy041AccessPolicy:
    name='advanced_policy_041'
    sequence=6040
    scope='advanced_policy_041'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy042AccessPolicy:
    name='advanced_policy_042'
    sequence=6041
    scope='advanced_policy_042'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy043AccessPolicy:
    name='advanced_policy_043'
    sequence=6042
    scope='advanced_policy_043'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy044AccessPolicy:
    name='advanced_policy_044'
    sequence=6043
    scope='advanced_policy_044'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy045AccessPolicy:
    name='advanced_policy_045'
    sequence=6044
    scope='advanced_policy_045'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy046AccessPolicy:
    name='advanced_policy_046'
    sequence=6045
    scope='advanced_policy_046'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy047AccessPolicy:
    name='advanced_policy_047'
    sequence=6046
    scope='advanced_policy_047'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy048AccessPolicy:
    name='advanced_policy_048'
    sequence=6047
    scope='advanced_policy_048'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy049AccessPolicy:
    name='advanced_policy_049'
    sequence=6048
    scope='advanced_policy_049'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy050AccessPolicy:
    name='advanced_policy_050'
    sequence=6049
    scope='advanced_policy_050'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy051AccessPolicy:
    name='advanced_policy_051'
    sequence=6050
    scope='advanced_policy_051'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy052AccessPolicy:
    name='advanced_policy_052'
    sequence=6051
    scope='advanced_policy_052'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy053AccessPolicy:
    name='advanced_policy_053'
    sequence=6052
    scope='advanced_policy_053'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy054AccessPolicy:
    name='advanced_policy_054'
    sequence=6053
    scope='advanced_policy_054'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy055AccessPolicy:
    name='advanced_policy_055'
    sequence=6054
    scope='advanced_policy_055'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy056AccessPolicy:
    name='advanced_policy_056'
    sequence=6055
    scope='advanced_policy_056'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy057AccessPolicy:
    name='advanced_policy_057'
    sequence=6056
    scope='advanced_policy_057'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy058AccessPolicy:
    name='advanced_policy_058'
    sequence=6057
    scope='advanced_policy_058'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy059AccessPolicy:
    name='advanced_policy_059'
    sequence=6058
    scope='advanced_policy_059'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy060AccessPolicy:
    name='advanced_policy_060'
    sequence=6059
    scope='advanced_policy_060'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy061AccessPolicy:
    name='advanced_policy_061'
    sequence=6060
    scope='advanced_policy_061'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy062AccessPolicy:
    name='advanced_policy_062'
    sequence=6061
    scope='advanced_policy_062'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy063AccessPolicy:
    name='advanced_policy_063'
    sequence=6062
    scope='advanced_policy_063'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy064AccessPolicy:
    name='advanced_policy_064'
    sequence=6063
    scope='advanced_policy_064'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy065AccessPolicy:
    name='advanced_policy_065'
    sequence=6064
    scope='advanced_policy_065'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy066AccessPolicy:
    name='advanced_policy_066'
    sequence=6065
    scope='advanced_policy_066'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy067AccessPolicy:
    name='advanced_policy_067'
    sequence=6066
    scope='advanced_policy_067'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy068AccessPolicy:
    name='advanced_policy_068'
    sequence=6067
    scope='advanced_policy_068'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy069AccessPolicy:
    name='advanced_policy_069'
    sequence=6068
    scope='advanced_policy_069'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy070AccessPolicy:
    name='advanced_policy_070'
    sequence=6069
    scope='advanced_policy_070'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy071AccessPolicy:
    name='advanced_policy_071'
    sequence=6070
    scope='advanced_policy_071'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy072AccessPolicy:
    name='advanced_policy_072'
    sequence=6071
    scope='advanced_policy_072'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy073AccessPolicy:
    name='advanced_policy_073'
    sequence=6072
    scope='advanced_policy_073'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy074AccessPolicy:
    name='advanced_policy_074'
    sequence=6073
    scope='advanced_policy_074'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy075AccessPolicy:
    name='advanced_policy_075'
    sequence=6074
    scope='advanced_policy_075'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy076AccessPolicy:
    name='advanced_policy_076'
    sequence=6075
    scope='advanced_policy_076'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy077AccessPolicy:
    name='advanced_policy_077'
    sequence=6076
    scope='advanced_policy_077'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy078AccessPolicy:
    name='advanced_policy_078'
    sequence=6077
    scope='advanced_policy_078'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy079AccessPolicy:
    name='advanced_policy_079'
    sequence=6078
    scope='advanced_policy_079'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy080AccessPolicy:
    name='advanced_policy_080'
    sequence=6079
    scope='advanced_policy_080'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy081AccessPolicy:
    name='advanced_policy_081'
    sequence=6080
    scope='advanced_policy_081'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy082AccessPolicy:
    name='advanced_policy_082'
    sequence=6081
    scope='advanced_policy_082'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy083AccessPolicy:
    name='advanced_policy_083'
    sequence=6082
    scope='advanced_policy_083'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy084AccessPolicy:
    name='advanced_policy_084'
    sequence=6083
    scope='advanced_policy_084'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy085AccessPolicy:
    name='advanced_policy_085'
    sequence=6084
    scope='advanced_policy_085'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy086AccessPolicy:
    name='advanced_policy_086'
    sequence=6085
    scope='advanced_policy_086'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy087AccessPolicy:
    name='advanced_policy_087'
    sequence=6086
    scope='advanced_policy_087'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy088AccessPolicy:
    name='advanced_policy_088'
    sequence=6087
    scope='advanced_policy_088'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy089AccessPolicy:
    name='advanced_policy_089'
    sequence=6088
    scope='advanced_policy_089'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy090AccessPolicy:
    name='advanced_policy_090'
    sequence=6089
    scope='advanced_policy_090'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy091AccessPolicy:
    name='advanced_policy_091'
    sequence=6090
    scope='advanced_policy_091'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy092AccessPolicy:
    name='advanced_policy_092'
    sequence=6091
    scope='advanced_policy_092'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy093AccessPolicy:
    name='advanced_policy_093'
    sequence=6092
    scope='advanced_policy_093'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy094AccessPolicy:
    name='advanced_policy_094'
    sequence=6093
    scope='advanced_policy_094'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy095AccessPolicy:
    name='advanced_policy_095'
    sequence=6094
    scope='advanced_policy_095'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy096AccessPolicy:
    name='advanced_policy_096'
    sequence=6095
    scope='advanced_policy_096'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy097AccessPolicy:
    name='advanced_policy_097'
    sequence=6096
    scope='advanced_policy_097'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy098AccessPolicy:
    name='advanced_policy_098'
    sequence=6097
    scope='advanced_policy_098'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy099AccessPolicy:
    name='advanced_policy_099'
    sequence=6098
    scope='advanced_policy_099'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy100AccessPolicy:
    name='advanced_policy_100'
    sequence=6099
    scope='advanced_policy_100'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy101AccessPolicy:
    name='advanced_policy_101'
    sequence=6100
    scope='advanced_policy_101'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy102AccessPolicy:
    name='advanced_policy_102'
    sequence=6101
    scope='advanced_policy_102'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy103AccessPolicy:
    name='advanced_policy_103'
    sequence=6102
    scope='advanced_policy_103'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy104AccessPolicy:
    name='advanced_policy_104'
    sequence=6103
    scope='advanced_policy_104'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy105AccessPolicy:
    name='advanced_policy_105'
    sequence=6104
    scope='advanced_policy_105'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy106AccessPolicy:
    name='advanced_policy_106'
    sequence=6105
    scope='advanced_policy_106'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy107AccessPolicy:
    name='advanced_policy_107'
    sequence=6106
    scope='advanced_policy_107'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy108AccessPolicy:
    name='advanced_policy_108'
    sequence=6107
    scope='advanced_policy_108'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy109AccessPolicy:
    name='advanced_policy_109'
    sequence=6108
    scope='advanced_policy_109'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy110AccessPolicy:
    name='advanced_policy_110'
    sequence=6109
    scope='advanced_policy_110'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy111AccessPolicy:
    name='advanced_policy_111'
    sequence=6110
    scope='advanced_policy_111'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy112AccessPolicy:
    name='advanced_policy_112'
    sequence=6111
    scope='advanced_policy_112'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy113AccessPolicy:
    name='advanced_policy_113'
    sequence=6112
    scope='advanced_policy_113'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy114AccessPolicy:
    name='advanced_policy_114'
    sequence=6113
    scope='advanced_policy_114'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy115AccessPolicy:
    name='advanced_policy_115'
    sequence=6114
    scope='advanced_policy_115'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy116AccessPolicy:
    name='advanced_policy_116'
    sequence=6115
    scope='advanced_policy_116'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy117AccessPolicy:
    name='advanced_policy_117'
    sequence=6116
    scope='advanced_policy_117'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy118AccessPolicy:
    name='advanced_policy_118'
    sequence=6117
    scope='advanced_policy_118'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy119AccessPolicy:
    name='advanced_policy_119'
    sequence=6118
    scope='advanced_policy_119'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy120AccessPolicy:
    name='advanced_policy_120'
    sequence=6119
    scope='advanced_policy_120'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy121AccessPolicy:
    name='advanced_policy_121'
    sequence=6120
    scope='advanced_policy_121'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy122AccessPolicy:
    name='advanced_policy_122'
    sequence=6121
    scope='advanced_policy_122'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy123AccessPolicy:
    name='advanced_policy_123'
    sequence=6122
    scope='advanced_policy_123'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy124AccessPolicy:
    name='advanced_policy_124'
    sequence=6123
    scope='advanced_policy_124'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy125AccessPolicy:
    name='advanced_policy_125'
    sequence=6124
    scope='advanced_policy_125'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy126AccessPolicy:
    name='advanced_policy_126'
    sequence=6125
    scope='advanced_policy_126'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy127AccessPolicy:
    name='advanced_policy_127'
    sequence=6126
    scope='advanced_policy_127'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy128AccessPolicy:
    name='advanced_policy_128'
    sequence=6127
    scope='advanced_policy_128'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy129AccessPolicy:
    name='advanced_policy_129'
    sequence=6128
    scope='advanced_policy_129'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy130AccessPolicy:
    name='advanced_policy_130'
    sequence=6129
    scope='advanced_policy_130'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy131AccessPolicy:
    name='advanced_policy_131'
    sequence=6130
    scope='advanced_policy_131'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy132AccessPolicy:
    name='advanced_policy_132'
    sequence=6131
    scope='advanced_policy_132'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy133AccessPolicy:
    name='advanced_policy_133'
    sequence=6132
    scope='advanced_policy_133'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy134AccessPolicy:
    name='advanced_policy_134'
    sequence=6133
    scope='advanced_policy_134'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy135AccessPolicy:
    name='advanced_policy_135'
    sequence=6134
    scope='advanced_policy_135'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy136AccessPolicy:
    name='advanced_policy_136'
    sequence=6135
    scope='advanced_policy_136'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy137AccessPolicy:
    name='advanced_policy_137'
    sequence=6136
    scope='advanced_policy_137'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy138AccessPolicy:
    name='advanced_policy_138'
    sequence=6137
    scope='advanced_policy_138'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy139AccessPolicy:
    name='advanced_policy_139'
    sequence=6138
    scope='advanced_policy_139'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy140AccessPolicy:
    name='advanced_policy_140'
    sequence=6139
    scope='advanced_policy_140'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy141AccessPolicy:
    name='advanced_policy_141'
    sequence=6140
    scope='advanced_policy_141'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy142AccessPolicy:
    name='advanced_policy_142'
    sequence=6141
    scope='advanced_policy_142'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy143AccessPolicy:
    name='advanced_policy_143'
    sequence=6142
    scope='advanced_policy_143'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy144AccessPolicy:
    name='advanced_policy_144'
    sequence=6143
    scope='advanced_policy_144'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy145AccessPolicy:
    name='advanced_policy_145'
    sequence=6144
    scope='advanced_policy_145'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy146AccessPolicy:
    name='advanced_policy_146'
    sequence=6145
    scope='advanced_policy_146'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy147AccessPolicy:
    name='advanced_policy_147'
    sequence=6146
    scope='advanced_policy_147'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy148AccessPolicy:
    name='advanced_policy_148'
    sequence=6147
    scope='advanced_policy_148'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy149AccessPolicy:
    name='advanced_policy_149'
    sequence=6148
    scope='advanced_policy_149'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy150AccessPolicy:
    name='advanced_policy_150'
    sequence=6149
    scope='advanced_policy_150'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy151AccessPolicy:
    name='advanced_policy_151'
    sequence=6150
    scope='advanced_policy_151'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy152AccessPolicy:
    name='advanced_policy_152'
    sequence=6151
    scope='advanced_policy_152'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy153AccessPolicy:
    name='advanced_policy_153'
    sequence=6152
    scope='advanced_policy_153'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy154AccessPolicy:
    name='advanced_policy_154'
    sequence=6153
    scope='advanced_policy_154'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy155AccessPolicy:
    name='advanced_policy_155'
    sequence=6154
    scope='advanced_policy_155'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy156AccessPolicy:
    name='advanced_policy_156'
    sequence=6155
    scope='advanced_policy_156'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy157AccessPolicy:
    name='advanced_policy_157'
    sequence=6156
    scope='advanced_policy_157'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy158AccessPolicy:
    name='advanced_policy_158'
    sequence=6157
    scope='advanced_policy_158'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy159AccessPolicy:
    name='advanced_policy_159'
    sequence=6158
    scope='advanced_policy_159'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy160AccessPolicy:
    name='advanced_policy_160'
    sequence=6159
    scope='advanced_policy_160'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy161AccessPolicy:
    name='advanced_policy_161'
    sequence=6160
    scope='advanced_policy_161'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy162AccessPolicy:
    name='advanced_policy_162'
    sequence=6161
    scope='advanced_policy_162'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy163AccessPolicy:
    name='advanced_policy_163'
    sequence=6162
    scope='advanced_policy_163'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy164AccessPolicy:
    name='advanced_policy_164'
    sequence=6163
    scope='advanced_policy_164'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy165AccessPolicy:
    name='advanced_policy_165'
    sequence=6164
    scope='advanced_policy_165'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy166AccessPolicy:
    name='advanced_policy_166'
    sequence=6165
    scope='advanced_policy_166'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy167AccessPolicy:
    name='advanced_policy_167'
    sequence=6166
    scope='advanced_policy_167'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy168AccessPolicy:
    name='advanced_policy_168'
    sequence=6167
    scope='advanced_policy_168'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy169AccessPolicy:
    name='advanced_policy_169'
    sequence=6168
    scope='advanced_policy_169'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy170AccessPolicy:
    name='advanced_policy_170'
    sequence=6169
    scope='advanced_policy_170'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy171AccessPolicy:
    name='advanced_policy_171'
    sequence=6170
    scope='advanced_policy_171'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy172AccessPolicy:
    name='advanced_policy_172'
    sequence=6171
    scope='advanced_policy_172'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy173AccessPolicy:
    name='advanced_policy_173'
    sequence=6172
    scope='advanced_policy_173'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy174AccessPolicy:
    name='advanced_policy_174'
    sequence=6173
    scope='advanced_policy_174'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy175AccessPolicy:
    name='advanced_policy_175'
    sequence=6174
    scope='advanced_policy_175'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy176AccessPolicy:
    name='advanced_policy_176'
    sequence=6175
    scope='advanced_policy_176'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy177AccessPolicy:
    name='advanced_policy_177'
    sequence=6176
    scope='advanced_policy_177'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy178AccessPolicy:
    name='advanced_policy_178'
    sequence=6177
    scope='advanced_policy_178'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}

class AdvancedPolicy179AccessPolicy:
    name='advanced_policy_179'
    sequence=6178
    scope='advanced_policy_179'
    def allows(self, principal: Principal, action: str) -> bool:
        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)
    def metadata(self) -> dict[str,Any]:
        return {"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}
