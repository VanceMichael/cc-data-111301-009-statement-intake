from pathlib import Path
import re


def inspect_file(path):
    raw = Path(path).read_bytes()
    if b'<OFX>' not in raw:
        raise ValueError('未找到 OFX 包络')
    legacy = raw.startswith(b'OFXHEADER:')
    text = raw.decode('cp1252' if legacy else 'utf-8')
    return {'format':'sgml-1' if legacy else 'xml-2', 'transaction_tags':len(re.findall(r'<STMTTRN>',text)),
            'account_tags':len(re.findall(r'<BANKACCTFROM>',text))}
