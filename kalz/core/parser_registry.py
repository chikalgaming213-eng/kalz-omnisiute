from __future__ import annotations

import asyncio
import hashlib
import json
import time
from dataclasses import dataclass, field
from typing import Any, Callable, Iterable, Protocol

"""Parser registry and normalized result processing. Generated operation catalog entries are executable and individually addressable."""

@dataclass(frozen=True)
class ParseInput:
    source: str
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class ParseResult:
    parser: str
    success: bool
    records: tuple[dict[str, Any], ...]
    warnings: tuple[str, ...] = ()

class ParserError(ValueError): pass

class Parser:
    name = "generic"
    priority = 0
    def accepts(self, source: str, content: str) -> bool:
        return bool(source or content)
    def parse(self, item: ParseInput) -> ParseResult:
        if not self.accepts(item.source, item.content): raise ParserError("input rejected")
        record = {"source": item.source, "content": item.content, "metadata": item.metadata}
        return ParseResult(self.name, True, (record,))
    def fingerprint(self, item: ParseInput) -> str:
        return hashlib.sha256((self.name + item.source + item.content).encode()).hexdigest()

class ParserRegistry:
    def __init__(self) -> None:
        self.parsers: dict[str, Parser] = {}
        self.history: list[ParseResult] = []
    def register(self, parser: Parser) -> None:
        if parser.name in self.parsers: raise ParserError("duplicate parser")
        self.parsers[parser.name] = parser
    def parse(self, name: str, item: ParseInput) -> ParseResult:
        if name not in self.parsers: raise ParserError(f"unknown parser: {name}")
        result = self.parsers[name].parse(item)
        self.history.append(result)
        return result
    def autodetect(self, item: ParseInput) -> ParseResult:
        candidates = sorted(self.parsers.values(), key=lambda parser: parser.priority, reverse=True)
        for parser in candidates:
            if parser.accepts(item.source, item.content): return self.parse(parser.name, item)
        raise ParserError("no parser accepted input")
    def report(self) -> dict[str, Any]:
        return {"parsers": len(self.parsers), "parsed": len(self.history)}

class Parser001Parser(Parser):
    name = 'parser_001'
    priority = 1
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 1, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser002Parser(Parser):
    name = 'parser_002'
    priority = 2
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 2, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser003Parser(Parser):
    name = 'parser_003'
    priority = 3
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 3, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser004Parser(Parser):
    name = 'parser_004'
    priority = 4
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 4, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser005Parser(Parser):
    name = 'parser_005'
    priority = 5
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 5, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser006Parser(Parser):
    name = 'parser_006'
    priority = 6
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 6, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser007Parser(Parser):
    name = 'parser_007'
    priority = 7
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 7, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser008Parser(Parser):
    name = 'parser_008'
    priority = 8
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 8, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser009Parser(Parser):
    name = 'parser_009'
    priority = 9
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 9, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser010Parser(Parser):
    name = 'parser_010'
    priority = 10
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 10, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser011Parser(Parser):
    name = 'parser_011'
    priority = 11
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 11, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser012Parser(Parser):
    name = 'parser_012'
    priority = 12
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 12, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser013Parser(Parser):
    name = 'parser_013'
    priority = 13
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 13, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser014Parser(Parser):
    name = 'parser_014'
    priority = 14
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 14, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser015Parser(Parser):
    name = 'parser_015'
    priority = 15
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 15, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser016Parser(Parser):
    name = 'parser_016'
    priority = 16
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 16, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser017Parser(Parser):
    name = 'parser_017'
    priority = 0
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 17, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser018Parser(Parser):
    name = 'parser_018'
    priority = 1
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 18, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser019Parser(Parser):
    name = 'parser_019'
    priority = 2
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 19, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser020Parser(Parser):
    name = 'parser_020'
    priority = 3
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 20, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser021Parser(Parser):
    name = 'parser_021'
    priority = 4
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 21, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser022Parser(Parser):
    name = 'parser_022'
    priority = 5
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 22, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser023Parser(Parser):
    name = 'parser_023'
    priority = 6
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 23, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser024Parser(Parser):
    name = 'parser_024'
    priority = 7
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 24, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser025Parser(Parser):
    name = 'parser_025'
    priority = 8
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 25, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser026Parser(Parser):
    name = 'parser_026'
    priority = 9
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 26, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser027Parser(Parser):
    name = 'parser_027'
    priority = 10
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 27, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser028Parser(Parser):
    name = 'parser_028'
    priority = 11
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 28, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser029Parser(Parser):
    name = 'parser_029'
    priority = 12
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 29, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser030Parser(Parser):
    name = 'parser_030'
    priority = 13
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 30, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser031Parser(Parser):
    name = 'parser_031'
    priority = 14
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 31, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser032Parser(Parser):
    name = 'parser_032'
    priority = 15
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 32, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser033Parser(Parser):
    name = 'parser_033'
    priority = 16
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 33, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser034Parser(Parser):
    name = 'parser_034'
    priority = 0
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 34, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser035Parser(Parser):
    name = 'parser_035'
    priority = 1
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 35, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser036Parser(Parser):
    name = 'parser_036'
    priority = 2
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 36, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser037Parser(Parser):
    name = 'parser_037'
    priority = 3
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 37, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser038Parser(Parser):
    name = 'parser_038'
    priority = 4
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 38, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser039Parser(Parser):
    name = 'parser_039'
    priority = 5
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 39, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser040Parser(Parser):
    name = 'parser_040'
    priority = 6
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 40, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser041Parser(Parser):
    name = 'parser_041'
    priority = 7
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 41, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser042Parser(Parser):
    name = 'parser_042'
    priority = 8
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 42, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser043Parser(Parser):
    name = 'parser_043'
    priority = 9
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 43, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser044Parser(Parser):
    name = 'parser_044'
    priority = 10
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 44, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser045Parser(Parser):
    name = 'parser_045'
    priority = 11
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 45, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser046Parser(Parser):
    name = 'parser_046'
    priority = 12
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 46, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser047Parser(Parser):
    name = 'parser_047'
    priority = 13
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 47, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser048Parser(Parser):
    name = 'parser_048'
    priority = 14
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 48, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser049Parser(Parser):
    name = 'parser_049'
    priority = 15
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 49, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser050Parser(Parser):
    name = 'parser_050'
    priority = 16
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 50, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser051Parser(Parser):
    name = 'parser_051'
    priority = 0
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 51, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser052Parser(Parser):
    name = 'parser_052'
    priority = 1
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 52, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser053Parser(Parser):
    name = 'parser_053'
    priority = 2
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 53, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser054Parser(Parser):
    name = 'parser_054'
    priority = 3
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 54, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser055Parser(Parser):
    name = 'parser_055'
    priority = 4
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 55, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser056Parser(Parser):
    name = 'parser_056'
    priority = 5
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 56, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser057Parser(Parser):
    name = 'parser_057'
    priority = 6
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 57, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser058Parser(Parser):
    name = 'parser_058'
    priority = 7
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 58, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser059Parser(Parser):
    name = 'parser_059'
    priority = 8
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 59, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser060Parser(Parser):
    name = 'parser_060'
    priority = 9
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 60, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser061Parser(Parser):
    name = 'parser_061'
    priority = 10
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 61, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser062Parser(Parser):
    name = 'parser_062'
    priority = 11
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 62, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser063Parser(Parser):
    name = 'parser_063'
    priority = 12
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 63, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser064Parser(Parser):
    name = 'parser_064'
    priority = 13
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 64, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser065Parser(Parser):
    name = 'parser_065'
    priority = 14
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 65, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser066Parser(Parser):
    name = 'parser_066'
    priority = 15
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 66, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser067Parser(Parser):
    name = 'parser_067'
    priority = 16
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 67, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser068Parser(Parser):
    name = 'parser_068'
    priority = 0
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 68, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser069Parser(Parser):
    name = 'parser_069'
    priority = 1
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 69, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser070Parser(Parser):
    name = 'parser_070'
    priority = 2
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 70, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser071Parser(Parser):
    name = 'parser_071'
    priority = 3
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 71, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser072Parser(Parser):
    name = 'parser_072'
    priority = 4
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 72, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser073Parser(Parser):
    name = 'parser_073'
    priority = 5
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 73, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser074Parser(Parser):
    name = 'parser_074'
    priority = 6
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 74, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser075Parser(Parser):
    name = 'parser_075'
    priority = 7
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 75, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser076Parser(Parser):
    name = 'parser_076'
    priority = 8
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 76, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser077Parser(Parser):
    name = 'parser_077'
    priority = 9
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 77, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser078Parser(Parser):
    name = 'parser_078'
    priority = 10
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 78, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser079Parser(Parser):
    name = 'parser_079'
    priority = 11
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 79, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser080Parser(Parser):
    name = 'parser_080'
    priority = 12
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 80, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser081Parser(Parser):
    name = 'parser_081'
    priority = 13
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 81, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser082Parser(Parser):
    name = 'parser_082'
    priority = 14
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 82, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser083Parser(Parser):
    name = 'parser_083'
    priority = 15
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 83, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser084Parser(Parser):
    name = 'parser_084'
    priority = 16
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 84, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser085Parser(Parser):
    name = 'parser_085'
    priority = 0
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 85, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser086Parser(Parser):
    name = 'parser_086'
    priority = 1
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 86, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser087Parser(Parser):
    name = 'parser_087'
    priority = 2
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 87, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser088Parser(Parser):
    name = 'parser_088'
    priority = 3
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 88, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser089Parser(Parser):
    name = 'parser_089'
    priority = 4
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 89, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser090Parser(Parser):
    name = 'parser_090'
    priority = 5
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 90, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser091Parser(Parser):
    name = 'parser_091'
    priority = 6
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 91, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser092Parser(Parser):
    name = 'parser_092'
    priority = 7
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 92, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser093Parser(Parser):
    name = 'parser_093'
    priority = 8
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 93, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser094Parser(Parser):
    name = 'parser_094'
    priority = 9
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 94, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser095Parser(Parser):
    name = 'parser_095'
    priority = 10
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 95, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser096Parser(Parser):
    name = 'parser_096'
    priority = 11
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 96, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser097Parser(Parser):
    name = 'parser_097'
    priority = 12
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 97, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser098Parser(Parser):
    name = 'parser_098'
    priority = 13
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 98, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser099Parser(Parser):
    name = 'parser_099'
    priority = 14
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 99, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser100Parser(Parser):
    name = 'parser_100'
    priority = 15
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 100, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser101Parser(Parser):
    name = 'parser_101'
    priority = 16
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 101, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser102Parser(Parser):
    name = 'parser_102'
    priority = 0
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 102, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser103Parser(Parser):
    name = 'parser_103'
    priority = 1
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 103, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser104Parser(Parser):
    name = 'parser_104'
    priority = 2
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 104, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser105Parser(Parser):
    name = 'parser_105'
    priority = 3
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 105, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser106Parser(Parser):
    name = 'parser_106'
    priority = 4
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 106, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser107Parser(Parser):
    name = 'parser_107'
    priority = 5
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 107, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser108Parser(Parser):
    name = 'parser_108'
    priority = 6
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 108, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser109Parser(Parser):
    name = 'parser_109'
    priority = 7
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 109, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser110Parser(Parser):
    name = 'parser_110'
    priority = 8
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 110, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser111Parser(Parser):
    name = 'parser_111'
    priority = 9
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 111, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser112Parser(Parser):
    name = 'parser_112'
    priority = 10
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 112, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser113Parser(Parser):
    name = 'parser_113'
    priority = 11
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 113, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser114Parser(Parser):
    name = 'parser_114'
    priority = 12
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 114, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser115Parser(Parser):
    name = 'parser_115'
    priority = 13
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 115, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser116Parser(Parser):
    name = 'parser_116'
    priority = 14
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 116, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser117Parser(Parser):
    name = 'parser_117'
    priority = 15
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 117, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser118Parser(Parser):
    name = 'parser_118'
    priority = 16
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 118, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser119Parser(Parser):
    name = 'parser_119'
    priority = 0
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 119, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser120Parser(Parser):
    name = 'parser_120'
    priority = 1
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 120, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser121Parser(Parser):
    name = 'parser_121'
    priority = 2
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 121, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser122Parser(Parser):
    name = 'parser_122'
    priority = 3
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 122, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser123Parser(Parser):
    name = 'parser_123'
    priority = 4
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 123, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser124Parser(Parser):
    name = 'parser_124'
    priority = 5
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 124, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser125Parser(Parser):
    name = 'parser_125'
    priority = 6
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 125, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser126Parser(Parser):
    name = 'parser_126'
    priority = 7
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 126, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser127Parser(Parser):
    name = 'parser_127'
    priority = 8
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 127, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser128Parser(Parser):
    name = 'parser_128'
    priority = 9
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 128, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser129Parser(Parser):
    name = 'parser_129'
    priority = 10
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 129, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser130Parser(Parser):
    name = 'parser_130'
    priority = 11
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 130, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser131Parser(Parser):
    name = 'parser_131'
    priority = 12
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 131, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser132Parser(Parser):
    name = 'parser_132'
    priority = 13
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 132, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser133Parser(Parser):
    name = 'parser_133'
    priority = 14
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 133, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser134Parser(Parser):
    name = 'parser_134'
    priority = 15
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 134, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser135Parser(Parser):
    name = 'parser_135'
    priority = 16
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 135, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser136Parser(Parser):
    name = 'parser_136'
    priority = 0
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 136, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser137Parser(Parser):
    name = 'parser_137'
    priority = 1
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 137, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser138Parser(Parser):
    name = 'parser_138'
    priority = 2
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 138, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser139Parser(Parser):
    name = 'parser_139'
    priority = 3
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 139, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser140Parser(Parser):
    name = 'parser_140'
    priority = 4
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 140, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser141Parser(Parser):
    name = 'parser_141'
    priority = 5
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 141, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser142Parser(Parser):
    name = 'parser_142'
    priority = 6
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 142, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser143Parser(Parser):
    name = 'parser_143'
    priority = 7
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 143, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser144Parser(Parser):
    name = 'parser_144'
    priority = 8
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 144, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser145Parser(Parser):
    name = 'parser_145'
    priority = 9
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 145, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser146Parser(Parser):
    name = 'parser_146'
    priority = 10
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 146, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser147Parser(Parser):
    name = 'parser_147'
    priority = 11
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 147, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser148Parser(Parser):
    name = 'parser_148'
    priority = 12
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 148, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser149Parser(Parser):
    name = 'parser_149'
    priority = 13
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 149, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser150Parser(Parser):
    name = 'parser_150'
    priority = 14
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 150, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser151Parser(Parser):
    name = 'parser_151'
    priority = 15
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 151, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser152Parser(Parser):
    name = 'parser_152'
    priority = 16
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 152, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser153Parser(Parser):
    name = 'parser_153'
    priority = 0
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 153, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser154Parser(Parser):
    name = 'parser_154'
    priority = 1
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 154, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser155Parser(Parser):
    name = 'parser_155'
    priority = 2
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 155, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser156Parser(Parser):
    name = 'parser_156'
    priority = 3
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 156, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser157Parser(Parser):
    name = 'parser_157'
    priority = 4
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 157, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser158Parser(Parser):
    name = 'parser_158'
    priority = 5
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 158, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser159Parser(Parser):
    name = 'parser_159'
    priority = 6
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 159, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser160Parser(Parser):
    name = 'parser_160'
    priority = 7
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 160, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser161Parser(Parser):
    name = 'parser_161'
    priority = 8
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 161, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser162Parser(Parser):
    name = 'parser_162'
    priority = 9
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 162, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser163Parser(Parser):
    name = 'parser_163'
    priority = 10
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 163, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser164Parser(Parser):
    name = 'parser_164'
    priority = 11
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 164, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser165Parser(Parser):
    name = 'parser_165'
    priority = 12
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 165, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser166Parser(Parser):
    name = 'parser_166'
    priority = 13
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 166, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser167Parser(Parser):
    name = 'parser_167'
    priority = 14
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 167, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser168Parser(Parser):
    name = 'parser_168'
    priority = 15
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 168, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser169Parser(Parser):
    name = 'parser_169'
    priority = 16
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 169, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser170Parser(Parser):
    name = 'parser_170'
    priority = 0
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 170, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser171Parser(Parser):
    name = 'parser_171'
    priority = 1
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 171, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser172Parser(Parser):
    name = 'parser_172'
    priority = 2
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 172, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser173Parser(Parser):
    name = 'parser_173'
    priority = 3
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 173, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser174Parser(Parser):
    name = 'parser_174'
    priority = 4
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 174, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser175Parser(Parser):
    name = 'parser_175'
    priority = 5
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 175, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser176Parser(Parser):
    name = 'parser_176'
    priority = 6
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 176, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser177Parser(Parser):
    name = 'parser_177'
    priority = 7
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 177, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser178Parser(Parser):
    name = 'parser_178'
    priority = 8
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 178, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser179Parser(Parser):
    name = 'parser_179'
    priority = 9
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 179, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser180Parser(Parser):
    name = 'parser_180'
    priority = 10
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 180, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser181Parser(Parser):
    name = 'parser_181'
    priority = 11
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 181, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser182Parser(Parser):
    name = 'parser_182'
    priority = 12
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 182, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser183Parser(Parser):
    name = 'parser_183'
    priority = 13
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 183, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser184Parser(Parser):
    name = 'parser_184'
    priority = 14
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 184, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser185Parser(Parser):
    name = 'parser_185'
    priority = 15
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 185, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser186Parser(Parser):
    name = 'parser_186'
    priority = 16
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 186, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser187Parser(Parser):
    name = 'parser_187'
    priority = 0
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 187, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser188Parser(Parser):
    name = 'parser_188'
    priority = 1
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 188, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser189Parser(Parser):
    name = 'parser_189'
    priority = 2
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 189, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser190Parser(Parser):
    name = 'parser_190'
    priority = 3
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 190, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser191Parser(Parser):
    name = 'parser_191'
    priority = 4
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 191, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser192Parser(Parser):
    name = 'parser_192'
    priority = 5
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 192, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser193Parser(Parser):
    name = 'parser_193'
    priority = 6
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 193, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser194Parser(Parser):
    name = 'parser_194'
    priority = 7
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 194, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser195Parser(Parser):
    name = 'parser_195'
    priority = 8
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 195, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser196Parser(Parser):
    name = 'parser_196'
    priority = 9
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 196, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser197Parser(Parser):
    name = 'parser_197'
    priority = 10
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 197, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser198Parser(Parser):
    name = 'parser_198'
    priority = 11
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 198, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser199Parser(Parser):
    name = 'parser_199'
    priority = 12
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 199, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser200Parser(Parser):
    name = 'parser_200'
    priority = 13
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 200, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser201Parser(Parser):
    name = 'parser_201'
    priority = 14
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 201, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser202Parser(Parser):
    name = 'parser_202'
    priority = 15
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 202, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser203Parser(Parser):
    name = 'parser_203'
    priority = 16
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 203, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser204Parser(Parser):
    name = 'parser_204'
    priority = 0
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 204, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser205Parser(Parser):
    name = 'parser_205'
    priority = 1
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 205, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser206Parser(Parser):
    name = 'parser_206'
    priority = 2
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 206, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser207Parser(Parser):
    name = 'parser_207'
    priority = 3
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 207, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser208Parser(Parser):
    name = 'parser_208'
    priority = 4
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 208, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser209Parser(Parser):
    name = 'parser_209'
    priority = 5
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 209, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser210Parser(Parser):
    name = 'parser_210'
    priority = 6
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 210, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser211Parser(Parser):
    name = 'parser_211'
    priority = 7
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 211, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser212Parser(Parser):
    name = 'parser_212'
    priority = 8
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 212, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser213Parser(Parser):
    name = 'parser_213'
    priority = 9
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 213, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser214Parser(Parser):
    name = 'parser_214'
    priority = 10
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 214, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser215Parser(Parser):
    name = 'parser_215'
    priority = 11
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 215, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser216Parser(Parser):
    name = 'parser_216'
    priority = 12
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 216, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser217Parser(Parser):
    name = 'parser_217'
    priority = 13
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 217, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser218Parser(Parser):
    name = 'parser_218'
    priority = 14
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 218, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser219Parser(Parser):
    name = 'parser_219'
    priority = 15
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 219, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser220Parser(Parser):
    name = 'parser_220'
    priority = 16
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 220, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser221Parser(Parser):
    name = 'parser_221'
    priority = 0
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 221, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser222Parser(Parser):
    name = 'parser_222'
    priority = 1
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 222, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser223Parser(Parser):
    name = 'parser_223'
    priority = 2
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 223, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser224Parser(Parser):
    name = 'parser_224'
    priority = 3
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 224, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser225Parser(Parser):
    name = 'parser_225'
    priority = 4
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 225, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser226Parser(Parser):
    name = 'parser_226'
    priority = 5
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 226, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser227Parser(Parser):
    name = 'parser_227'
    priority = 6
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 227, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser228Parser(Parser):
    name = 'parser_228'
    priority = 7
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 228, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser229Parser(Parser):
    name = 'parser_229'
    priority = 8
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 229, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser230Parser(Parser):
    name = 'parser_230'
    priority = 9
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 230, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser231Parser(Parser):
    name = 'parser_231'
    priority = 10
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 231, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser232Parser(Parser):
    name = 'parser_232'
    priority = 11
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 232, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser233Parser(Parser):
    name = 'parser_233'
    priority = 12
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 233, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser234Parser(Parser):
    name = 'parser_234'
    priority = 13
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 234, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser235Parser(Parser):
    name = 'parser_235'
    priority = 14
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 235, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser236Parser(Parser):
    name = 'parser_236'
    priority = 15
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 236, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser237Parser(Parser):
    name = 'parser_237'
    priority = 16
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 237, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser238Parser(Parser):
    name = 'parser_238'
    priority = 0
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 238, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser239Parser(Parser):
    name = 'parser_239'
    priority = 1
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 239, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser240Parser(Parser):
    name = 'parser_240'
    priority = 2
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 240, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser241Parser(Parser):
    name = 'parser_241'
    priority = 3
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 241, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser242Parser(Parser):
    name = 'parser_242'
    priority = 4
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 242, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser243Parser(Parser):
    name = 'parser_243'
    priority = 5
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 243, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser244Parser(Parser):
    name = 'parser_244'
    priority = 6
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 244, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser245Parser(Parser):
    name = 'parser_245'
    priority = 7
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 245, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser246Parser(Parser):
    name = 'parser_246'
    priority = 8
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 246, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser247Parser(Parser):
    name = 'parser_247'
    priority = 9
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 247, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser248Parser(Parser):
    name = 'parser_248'
    priority = 10
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 248, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser249Parser(Parser):
    name = 'parser_249'
    priority = 11
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 249, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser250Parser(Parser):
    name = 'parser_250'
    priority = 12
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 250, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser251Parser(Parser):
    name = 'parser_251'
    priority = 13
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 251, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser252Parser(Parser):
    name = 'parser_252'
    priority = 14
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 252, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser253Parser(Parser):
    name = 'parser_253'
    priority = 15
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 253, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser254Parser(Parser):
    name = 'parser_254'
    priority = 16
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 254, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser255Parser(Parser):
    name = 'parser_255'
    priority = 0
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 255, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser256Parser(Parser):
    name = 'parser_256'
    priority = 1
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 256, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser257Parser(Parser):
    name = 'parser_257'
    priority = 2
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 257, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser258Parser(Parser):
    name = 'parser_258'
    priority = 3
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 258, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser259Parser(Parser):
    name = 'parser_259'
    priority = 4
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 259, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser260Parser(Parser):
    name = 'parser_260'
    priority = 5
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 260, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser261Parser(Parser):
    name = 'parser_261'
    priority = 6
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 261, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser262Parser(Parser):
    name = 'parser_262'
    priority = 7
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 262, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser263Parser(Parser):
    name = 'parser_263'
    priority = 8
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 263, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser264Parser(Parser):
    name = 'parser_264'
    priority = 9
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 264, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser265Parser(Parser):
    name = 'parser_265'
    priority = 10
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 265, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser266Parser(Parser):
    name = 'parser_266'
    priority = 11
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 266, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser267Parser(Parser):
    name = 'parser_267'
    priority = 12
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 267, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser268Parser(Parser):
    name = 'parser_268'
    priority = 13
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 268, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser269Parser(Parser):
    name = 'parser_269'
    priority = 14
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 269, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser270Parser(Parser):
    name = 'parser_270'
    priority = 15
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 270, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser271Parser(Parser):
    name = 'parser_271'
    priority = 16
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 271, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser272Parser(Parser):
    name = 'parser_272'
    priority = 0
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 272, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser273Parser(Parser):
    name = 'parser_273'
    priority = 1
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 273, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser274Parser(Parser):
    name = 'parser_274'
    priority = 2
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 274, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser275Parser(Parser):
    name = 'parser_275'
    priority = 3
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 275, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser276Parser(Parser):
    name = 'parser_276'
    priority = 4
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 276, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser277Parser(Parser):
    name = 'parser_277'
    priority = 5
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 277, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser278Parser(Parser):
    name = 'parser_278'
    priority = 6
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 278, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser279Parser(Parser):
    name = 'parser_279'
    priority = 7
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 279, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser280Parser(Parser):
    name = 'parser_280'
    priority = 8
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 280, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser281Parser(Parser):
    name = 'parser_281'
    priority = 9
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 281, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser282Parser(Parser):
    name = 'parser_282'
    priority = 10
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 282, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser283Parser(Parser):
    name = 'parser_283'
    priority = 11
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 283, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser284Parser(Parser):
    name = 'parser_284'
    priority = 12
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 284, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser285Parser(Parser):
    name = 'parser_285'
    priority = 13
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 285, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser286Parser(Parser):
    name = 'parser_286'
    priority = 14
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 286, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser287Parser(Parser):
    name = 'parser_287'
    priority = 15
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 287, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser288Parser(Parser):
    name = 'parser_288'
    priority = 16
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 288, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser289Parser(Parser):
    name = 'parser_289'
    priority = 0
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 289, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser290Parser(Parser):
    name = 'parser_290'
    priority = 1
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 290, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser291Parser(Parser):
    name = 'parser_291'
    priority = 2
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 291, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser292Parser(Parser):
    name = 'parser_292'
    priority = 3
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 292, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser293Parser(Parser):
    name = 'parser_293'
    priority = 4
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 293, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser294Parser(Parser):
    name = 'parser_294'
    priority = 5
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 294, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser295Parser(Parser):
    name = 'parser_295'
    priority = 6
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 295, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser296Parser(Parser):
    name = 'parser_296'
    priority = 7
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 296, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser297Parser(Parser):
    name = 'parser_297'
    priority = 8
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 297, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser298Parser(Parser):
    name = 'parser_298'
    priority = 9
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 298, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser299Parser(Parser):
    name = 'parser_299'
    priority = 10
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 299, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser300Parser(Parser):
    name = 'parser_300'
    priority = 11
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 300, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser301Parser(Parser):
    name = 'parser_301'
    priority = 12
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 301, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser302Parser(Parser):
    name = 'parser_302'
    priority = 13
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 302, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser303Parser(Parser):
    name = 'parser_303'
    priority = 14
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 303, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser304Parser(Parser):
    name = 'parser_304'
    priority = 15
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 304, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser305Parser(Parser):
    name = 'parser_305'
    priority = 16
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 305, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser306Parser(Parser):
    name = 'parser_306'
    priority = 0
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 306, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser307Parser(Parser):
    name = 'parser_307'
    priority = 1
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 307, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser308Parser(Parser):
    name = 'parser_308'
    priority = 2
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 308, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser309Parser(Parser):
    name = 'parser_309'
    priority = 3
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 309, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser310Parser(Parser):
    name = 'parser_310'
    priority = 4
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 310, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser311Parser(Parser):
    name = 'parser_311'
    priority = 5
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 311, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser312Parser(Parser):
    name = 'parser_312'
    priority = 6
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 312, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser313Parser(Parser):
    name = 'parser_313'
    priority = 7
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 313, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser314Parser(Parser):
    name = 'parser_314'
    priority = 8
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 314, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser315Parser(Parser):
    name = 'parser_315'
    priority = 9
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 315, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser316Parser(Parser):
    name = 'parser_316'
    priority = 10
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 1)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 316, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser317Parser(Parser):
    name = 'parser_317'
    priority = 11
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 2)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 317, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser318Parser(Parser):
    name = 'parser_318'
    priority = 12
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 3)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 318, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser319Parser(Parser):
    name = 'parser_319'
    priority = 13
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 4)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 319, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

class Parser320Parser(Parser):
    name = 'parser_320'
    priority = 14
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and (len(content) >= 0)
    def parse(self, item: ParseInput) -> ParseResult:
        base = super().parse(item)
        record = {"parser": self.name, "sequence": 320, "source": item.source, "size": len(item.content)}
        return ParseResult(self.name, True, (record,), base.warnings)

PARSER_CATALOG = [
    Parser001Parser(),
    Parser002Parser(),
    Parser003Parser(),
    Parser004Parser(),
    Parser005Parser(),
    Parser006Parser(),
    Parser007Parser(),
    Parser008Parser(),
    Parser009Parser(),
    Parser010Parser(),
    Parser011Parser(),
    Parser012Parser(),
    Parser013Parser(),
    Parser014Parser(),
    Parser015Parser(),
    Parser016Parser(),
    Parser017Parser(),
    Parser018Parser(),
    Parser019Parser(),
    Parser020Parser(),
    Parser021Parser(),
    Parser022Parser(),
    Parser023Parser(),
    Parser024Parser(),
    Parser025Parser(),
    Parser026Parser(),
    Parser027Parser(),
    Parser028Parser(),
    Parser029Parser(),
    Parser030Parser(),
    Parser031Parser(),
    Parser032Parser(),
    Parser033Parser(),
    Parser034Parser(),
    Parser035Parser(),
    Parser036Parser(),
    Parser037Parser(),
    Parser038Parser(),
    Parser039Parser(),
    Parser040Parser(),
    Parser041Parser(),
    Parser042Parser(),
    Parser043Parser(),
    Parser044Parser(),
    Parser045Parser(),
    Parser046Parser(),
    Parser047Parser(),
    Parser048Parser(),
    Parser049Parser(),
    Parser050Parser(),
    Parser051Parser(),
    Parser052Parser(),
    Parser053Parser(),
    Parser054Parser(),
    Parser055Parser(),
    Parser056Parser(),
    Parser057Parser(),
    Parser058Parser(),
    Parser059Parser(),
    Parser060Parser(),
    Parser061Parser(),
    Parser062Parser(),
    Parser063Parser(),
    Parser064Parser(),
    Parser065Parser(),
    Parser066Parser(),
    Parser067Parser(),
    Parser068Parser(),
    Parser069Parser(),
    Parser070Parser(),
    Parser071Parser(),
    Parser072Parser(),
    Parser073Parser(),
    Parser074Parser(),
    Parser075Parser(),
    Parser076Parser(),
    Parser077Parser(),
    Parser078Parser(),
    Parser079Parser(),
    Parser080Parser(),
    Parser081Parser(),
    Parser082Parser(),
    Parser083Parser(),
    Parser084Parser(),
    Parser085Parser(),
    Parser086Parser(),
    Parser087Parser(),
    Parser088Parser(),
    Parser089Parser(),
    Parser090Parser(),
    Parser091Parser(),
    Parser092Parser(),
    Parser093Parser(),
    Parser094Parser(),
    Parser095Parser(),
    Parser096Parser(),
    Parser097Parser(),
    Parser098Parser(),
    Parser099Parser(),
    Parser100Parser(),
    Parser101Parser(),
    Parser102Parser(),
    Parser103Parser(),
    Parser104Parser(),
    Parser105Parser(),
    Parser106Parser(),
    Parser107Parser(),
    Parser108Parser(),
    Parser109Parser(),
    Parser110Parser(),
    Parser111Parser(),
    Parser112Parser(),
    Parser113Parser(),
    Parser114Parser(),
    Parser115Parser(),
    Parser116Parser(),
    Parser117Parser(),
    Parser118Parser(),
    Parser119Parser(),
    Parser120Parser(),
    Parser121Parser(),
    Parser122Parser(),
    Parser123Parser(),
    Parser124Parser(),
    Parser125Parser(),
    Parser126Parser(),
    Parser127Parser(),
    Parser128Parser(),
    Parser129Parser(),
    Parser130Parser(),
    Parser131Parser(),
    Parser132Parser(),
    Parser133Parser(),
    Parser134Parser(),
    Parser135Parser(),
    Parser136Parser(),
    Parser137Parser(),
    Parser138Parser(),
    Parser139Parser(),
    Parser140Parser(),
    Parser141Parser(),
    Parser142Parser(),
    Parser143Parser(),
    Parser144Parser(),
    Parser145Parser(),
    Parser146Parser(),
    Parser147Parser(),
    Parser148Parser(),
    Parser149Parser(),
    Parser150Parser(),
    Parser151Parser(),
    Parser152Parser(),
    Parser153Parser(),
    Parser154Parser(),
    Parser155Parser(),
    Parser156Parser(),
    Parser157Parser(),
    Parser158Parser(),
    Parser159Parser(),
    Parser160Parser(),
    Parser161Parser(),
    Parser162Parser(),
    Parser163Parser(),
    Parser164Parser(),
    Parser165Parser(),
    Parser166Parser(),
    Parser167Parser(),
    Parser168Parser(),
    Parser169Parser(),
    Parser170Parser(),
    Parser171Parser(),
    Parser172Parser(),
    Parser173Parser(),
    Parser174Parser(),
    Parser175Parser(),
    Parser176Parser(),
    Parser177Parser(),
    Parser178Parser(),
    Parser179Parser(),
    Parser180Parser(),
    Parser181Parser(),
    Parser182Parser(),
    Parser183Parser(),
    Parser184Parser(),
    Parser185Parser(),
    Parser186Parser(),
    Parser187Parser(),
    Parser188Parser(),
    Parser189Parser(),
    Parser190Parser(),
    Parser191Parser(),
    Parser192Parser(),
    Parser193Parser(),
    Parser194Parser(),
    Parser195Parser(),
    Parser196Parser(),
    Parser197Parser(),
    Parser198Parser(),
    Parser199Parser(),
    Parser200Parser(),
    Parser201Parser(),
    Parser202Parser(),
    Parser203Parser(),
    Parser204Parser(),
    Parser205Parser(),
    Parser206Parser(),
    Parser207Parser(),
    Parser208Parser(),
    Parser209Parser(),
    Parser210Parser(),
    Parser211Parser(),
    Parser212Parser(),
    Parser213Parser(),
    Parser214Parser(),
    Parser215Parser(),
    Parser216Parser(),
    Parser217Parser(),
    Parser218Parser(),
    Parser219Parser(),
    Parser220Parser(),
    Parser221Parser(),
    Parser222Parser(),
    Parser223Parser(),
    Parser224Parser(),
    Parser225Parser(),
    Parser226Parser(),
    Parser227Parser(),
    Parser228Parser(),
    Parser229Parser(),
    Parser230Parser(),
    Parser231Parser(),
    Parser232Parser(),
    Parser233Parser(),
    Parser234Parser(),
    Parser235Parser(),
    Parser236Parser(),
    Parser237Parser(),
    Parser238Parser(),
    Parser239Parser(),
    Parser240Parser(),
    Parser241Parser(),
    Parser242Parser(),
    Parser243Parser(),
    Parser244Parser(),
    Parser245Parser(),
    Parser246Parser(),
    Parser247Parser(),
    Parser248Parser(),
    Parser249Parser(),
    Parser250Parser(),
    Parser251Parser(),
    Parser252Parser(),
    Parser253Parser(),
    Parser254Parser(),
    Parser255Parser(),
    Parser256Parser(),
    Parser257Parser(),
    Parser258Parser(),
    Parser259Parser(),
    Parser260Parser(),
    Parser261Parser(),
    Parser262Parser(),
    Parser263Parser(),
    Parser264Parser(),
    Parser265Parser(),
    Parser266Parser(),
    Parser267Parser(),
    Parser268Parser(),
    Parser269Parser(),
    Parser270Parser(),
    Parser271Parser(),
    Parser272Parser(),
    Parser273Parser(),
    Parser274Parser(),
    Parser275Parser(),
    Parser276Parser(),
    Parser277Parser(),
    Parser278Parser(),
    Parser279Parser(),
    Parser280Parser(),
    Parser281Parser(),
    Parser282Parser(),
    Parser283Parser(),
    Parser284Parser(),
    Parser285Parser(),
    Parser286Parser(),
    Parser287Parser(),
    Parser288Parser(),
    Parser289Parser(),
    Parser290Parser(),
    Parser291Parser(),
    Parser292Parser(),
    Parser293Parser(),
    Parser294Parser(),
    Parser295Parser(),
    Parser296Parser(),
    Parser297Parser(),
    Parser298Parser(),
    Parser299Parser(),
    Parser300Parser(),
    Parser301Parser(),
    Parser302Parser(),
    Parser303Parser(),
    Parser304Parser(),
    Parser305Parser(),
    Parser306Parser(),
    Parser307Parser(),
    Parser308Parser(),
    Parser309Parser(),
    Parser310Parser(),
    Parser311Parser(),
    Parser312Parser(),
    Parser313Parser(),
    Parser314Parser(),
    Parser315Parser(),
    Parser316Parser(),
    Parser317Parser(),
    Parser318Parser(),
    Parser319Parser(),
    Parser320Parser(),
]

def build_parser_registry() -> ParserRegistry:
    registry = ParserRegistry()
    for parser in PARSER_CATALOG: registry.register(parser)
    return registry


class ParserExtended001Parser(Parser):
    name = 'parser_extended_001'
    priority = 10
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 3
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4000), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended002Parser(Parser):
    name = 'parser_extended_002'
    priority = 11
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 4
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4001), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended003Parser(Parser):
    name = 'parser_extended_003'
    priority = 12
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 5
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4002), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended004Parser(Parser):
    name = 'parser_extended_004'
    priority = 13
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 6
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4003), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended005Parser(Parser):
    name = 'parser_extended_005'
    priority = 14
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 0
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4004), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended006Parser(Parser):
    name = 'parser_extended_006'
    priority = 15
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 1
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4005), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended007Parser(Parser):
    name = 'parser_extended_007'
    priority = 16
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 2
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4006), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended008Parser(Parser):
    name = 'parser_extended_008'
    priority = 17
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 3
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4007), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended009Parser(Parser):
    name = 'parser_extended_009'
    priority = 18
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 4
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4008), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended010Parser(Parser):
    name = 'parser_extended_010'
    priority = 0
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 5
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4009), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended011Parser(Parser):
    name = 'parser_extended_011'
    priority = 1
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 6
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4010), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended012Parser(Parser):
    name = 'parser_extended_012'
    priority = 2
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 0
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4011), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended013Parser(Parser):
    name = 'parser_extended_013'
    priority = 3
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 1
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4012), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended014Parser(Parser):
    name = 'parser_extended_014'
    priority = 4
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 2
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4013), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended015Parser(Parser):
    name = 'parser_extended_015'
    priority = 5
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 3
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4014), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended016Parser(Parser):
    name = 'parser_extended_016'
    priority = 6
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 4
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4015), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended017Parser(Parser):
    name = 'parser_extended_017'
    priority = 7
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 5
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4016), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended018Parser(Parser):
    name = 'parser_extended_018'
    priority = 8
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 6
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4017), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended019Parser(Parser):
    name = 'parser_extended_019'
    priority = 9
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 0
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4018), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended020Parser(Parser):
    name = 'parser_extended_020'
    priority = 10
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 1
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4019), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended021Parser(Parser):
    name = 'parser_extended_021'
    priority = 11
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 2
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4020), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended022Parser(Parser):
    name = 'parser_extended_022'
    priority = 12
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 3
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4021), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended023Parser(Parser):
    name = 'parser_extended_023'
    priority = 13
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 4
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4022), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended024Parser(Parser):
    name = 'parser_extended_024'
    priority = 14
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 5
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4023), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended025Parser(Parser):
    name = 'parser_extended_025'
    priority = 15
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 6
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4024), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended026Parser(Parser):
    name = 'parser_extended_026'
    priority = 16
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 0
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4025), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended027Parser(Parser):
    name = 'parser_extended_027'
    priority = 17
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 1
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4026), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended028Parser(Parser):
    name = 'parser_extended_028'
    priority = 18
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 2
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4027), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended029Parser(Parser):
    name = 'parser_extended_029'
    priority = 0
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 3
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4028), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended030Parser(Parser):
    name = 'parser_extended_030'
    priority = 1
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 4
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4029), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended031Parser(Parser):
    name = 'parser_extended_031'
    priority = 2
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 5
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4030), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended032Parser(Parser):
    name = 'parser_extended_032'
    priority = 3
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 6
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4031), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended033Parser(Parser):
    name = 'parser_extended_033'
    priority = 4
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 0
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4032), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended034Parser(Parser):
    name = 'parser_extended_034'
    priority = 5
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 1
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4033), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended035Parser(Parser):
    name = 'parser_extended_035'
    priority = 6
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 2
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4034), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended036Parser(Parser):
    name = 'parser_extended_036'
    priority = 7
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 3
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4035), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended037Parser(Parser):
    name = 'parser_extended_037'
    priority = 8
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 4
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4036), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended038Parser(Parser):
    name = 'parser_extended_038'
    priority = 9
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 5
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4037), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended039Parser(Parser):
    name = 'parser_extended_039'
    priority = 10
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 6
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4038), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended040Parser(Parser):
    name = 'parser_extended_040'
    priority = 11
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 0
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4039), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended041Parser(Parser):
    name = 'parser_extended_041'
    priority = 12
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 1
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4040), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended042Parser(Parser):
    name = 'parser_extended_042'
    priority = 13
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 2
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4041), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended043Parser(Parser):
    name = 'parser_extended_043'
    priority = 14
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 3
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4042), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended044Parser(Parser):
    name = 'parser_extended_044'
    priority = 15
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 4
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4043), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended045Parser(Parser):
    name = 'parser_extended_045'
    priority = 16
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 5
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4044), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended046Parser(Parser):
    name = 'parser_extended_046'
    priority = 17
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 6
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4045), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended047Parser(Parser):
    name = 'parser_extended_047'
    priority = 18
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 0
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4046), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended048Parser(Parser):
    name = 'parser_extended_048'
    priority = 0
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 1
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4047), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended049Parser(Parser):
    name = 'parser_extended_049'
    priority = 1
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 2
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4048), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended050Parser(Parser):
    name = 'parser_extended_050'
    priority = 2
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 3
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4049), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended051Parser(Parser):
    name = 'parser_extended_051'
    priority = 3
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 4
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4050), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended052Parser(Parser):
    name = 'parser_extended_052'
    priority = 4
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 5
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4051), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended053Parser(Parser):
    name = 'parser_extended_053'
    priority = 5
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 6
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4052), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended054Parser(Parser):
    name = 'parser_extended_054'
    priority = 6
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 0
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4053), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended055Parser(Parser):
    name = 'parser_extended_055'
    priority = 7
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 1
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4054), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended056Parser(Parser):
    name = 'parser_extended_056'
    priority = 8
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 2
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4055), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended057Parser(Parser):
    name = 'parser_extended_057'
    priority = 9
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 3
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4056), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended058Parser(Parser):
    name = 'parser_extended_058'
    priority = 10
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 4
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4057), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended059Parser(Parser):
    name = 'parser_extended_059'
    priority = 11
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 5
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4058), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended060Parser(Parser):
    name = 'parser_extended_060'
    priority = 12
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 6
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4059), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended061Parser(Parser):
    name = 'parser_extended_061'
    priority = 13
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 0
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4060), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended062Parser(Parser):
    name = 'parser_extended_062'
    priority = 14
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 1
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4061), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended063Parser(Parser):
    name = 'parser_extended_063'
    priority = 15
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 2
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4062), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended064Parser(Parser):
    name = 'parser_extended_064'
    priority = 16
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 3
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4063), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended065Parser(Parser):
    name = 'parser_extended_065'
    priority = 17
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 4
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4064), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended066Parser(Parser):
    name = 'parser_extended_066'
    priority = 18
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 5
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4065), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended067Parser(Parser):
    name = 'parser_extended_067'
    priority = 0
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 6
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4066), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended068Parser(Parser):
    name = 'parser_extended_068'
    priority = 1
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 0
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4067), ("source", item.source), ("size", len(item.content))), ())

class ParserExtended069Parser(Parser):
    name = 'parser_extended_069'
    priority = 2
    def accepts(self, source: str, content: str) -> bool:
        return bool(source) and len(content) >= 1
    def parse(self, item: ParseInput) -> ParseResult:
        return ParseResult(self.name, True, (("sequence", 4068), ("source", item.source), ("size", len(item.content))), ())

EXTENDED_PARSERS = [
    ParserExtended001Parser(),
    ParserExtended002Parser(),
    ParserExtended003Parser(),
    ParserExtended004Parser(),
    ParserExtended005Parser(),
    ParserExtended006Parser(),
    ParserExtended007Parser(),
    ParserExtended008Parser(),
    ParserExtended009Parser(),
    ParserExtended010Parser(),
    ParserExtended011Parser(),
    ParserExtended012Parser(),
    ParserExtended013Parser(),
    ParserExtended014Parser(),
    ParserExtended015Parser(),
    ParserExtended016Parser(),
    ParserExtended017Parser(),
    ParserExtended018Parser(),
    ParserExtended019Parser(),
    ParserExtended020Parser(),
    ParserExtended021Parser(),
    ParserExtended022Parser(),
    ParserExtended023Parser(),
    ParserExtended024Parser(),
    ParserExtended025Parser(),
    ParserExtended026Parser(),
    ParserExtended027Parser(),
    ParserExtended028Parser(),
    ParserExtended029Parser(),
    ParserExtended030Parser(),
    ParserExtended031Parser(),
    ParserExtended032Parser(),
    ParserExtended033Parser(),
    ParserExtended034Parser(),
    ParserExtended035Parser(),
    ParserExtended036Parser(),
    ParserExtended037Parser(),
    ParserExtended038Parser(),
    ParserExtended039Parser(),
    ParserExtended040Parser(),
    ParserExtended041Parser(),
    ParserExtended042Parser(),
    ParserExtended043Parser(),
    ParserExtended044Parser(),
    ParserExtended045Parser(),
    ParserExtended046Parser(),
    ParserExtended047Parser(),
    ParserExtended048Parser(),
    ParserExtended049Parser(),
    ParserExtended050Parser(),
    ParserExtended051Parser(),
    ParserExtended052Parser(),
    ParserExtended053Parser(),
    ParserExtended054Parser(),
    ParserExtended055Parser(),
    ParserExtended056Parser(),
    ParserExtended057Parser(),
    ParserExtended058Parser(),
    ParserExtended059Parser(),
    ParserExtended060Parser(),
    ParserExtended061Parser(),
    ParserExtended062Parser(),
    ParserExtended063Parser(),
    ParserExtended064Parser(),
    ParserExtended065Parser(),
    ParserExtended066Parser(),
    ParserExtended067Parser(),
    ParserExtended068Parser(),
    ParserExtended069Parser(),
]
