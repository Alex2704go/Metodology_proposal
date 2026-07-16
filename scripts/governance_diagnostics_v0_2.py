#!/usr/bin/env python3
"""Map governance v0.2 validation messages to stable diagnostic codes."""
RULES=[
 ('ADMITTED with non-PASS','GOV-STATE-002'),('illegal lifecycle','GOV-STATE-001'),('state mismatch','GOV-STATE-001'),
 ('missing provenance','GOV-PROV-001'),('provenance','GOV-PROV-001'),
 ('evidence strength mismatch','GOV-EVID-002'),('malformed','GOV-REF-001'),('unknown','GOV-REF-001'),
 ('direction/origin','GOV-DIR-001'),('maturity mismatch','GOV-MAT-001'),('latest outcome mismatch','GOV-MAT-001'),
 ('independence not demonstrated','GOV-IND-001'),('multi-world without independent','GOV-IND-001'),
 ('interpretation boundary contradiction','GOV-BOUND-001'),('document semantic contradiction','GOV-BOUND-001'),('missing mandatory prohibitions','GOV-BOUND-002'),
 ('epistemic upgrade','GOV-ASYM-001'),('counterexample search','GOV-COUNTER-001'),
 ('unregistered artifact','GOV-ART-001'),('claim-bearing artifact','GOV-ART-001'),
 ('claim cycle','GOV-GRAPH-001'),('unpinned antecedent','GOV-GRAPH-002'),('unknown antecedent','GOV-GRAPH-002'),
 ('digest mismatch','GOV-DIGEST-001'),('empty CEOS endpoint','GOV-ENDPOINT-001'),('empty classical endpoint','GOV-ENDPOINT-001')]
def code(message):
 for token,c in RULES:
  if token.lower() in message.lower():return c
 return 'GOV-GENERIC-001'
def diagnostics(errors):return [{'code':code(e),'severity':'ERROR','message':e} for e in errors]
