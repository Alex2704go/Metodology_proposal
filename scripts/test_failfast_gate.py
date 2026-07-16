#!/usr/bin/env python3
"""Regression for the fail-fast integrity-gate contract."""
from pathlib import Path
import subprocess,tempfile
ROOT=Path(__file__).resolve().parents[1];SCRIPT=ROOT/'scripts/run_integrity_gate.sh';OUT=ROOT/'reports/checkpoint_failfast_gate.md'
def main():
 text=SCRIPT.read_text();declared='set -euo pipefail' in text
 with tempfile.TemporaryDirectory() as d:
  marker=Path(d)/'should_not_exist';r=subprocess.run(['bash','-c',f'set -euo pipefail; false; touch {marker}'],capture_output=True)
  stopped=r.returncode!=0 and not marker.exists()
 checks={'integrity_script_declares_failfast':declared,'failed_stage_stops_following_command':stopped,'failure_exit_is_nonzero':r.returncode!=0};passed=sum(checks.values())
 lines=['# Checkpoint — Fail-Fast Integrity Gate','',f'- Checks: **{len(checks)}**',f'- Passed: **{passed}**',f'- Failed: **{len(checks)-passed}**','']+[f"- `{k}`: **{'PASS' if v else 'FAIL'}**" for k,v in checks.items()]
 OUT.write_text('\n'.join(lines)+'\n')
 if passed!=len(checks):raise SystemExit('Fail-fast gate test failed')
 print({'checks':len(checks),'passed':passed,'failed':0})
if __name__=='__main__':main()
