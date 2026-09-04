from dataclasses import dataclass

@dataclass(frozen=True)
class Entry:
    key:str
    value:str
    line:int

def parse(text:str)->list[Entry]:
    out=[]
    for number,line in enumerate(text.splitlines(),1):
        raw=line.strip()
        if not raw or raw.startswith('#'): continue
        if '=' not in raw: continue
        key,value=raw.split('=',1); key=key.strip()
        if key: out.append(Entry(key,value.strip().strip('"\''),number))
    return out

def issues(entries:list[Entry])->list[str]:
    seen=set(); out=[]
    for item in entries:
        if item.key in seen: out.append(f"duplicate:{item.key}")
        seen.add(item.key)
        if not item.value: out.append(f"empty:{item.key}")
    return out
