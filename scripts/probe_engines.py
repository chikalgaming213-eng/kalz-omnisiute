from kalz.automation.automation_engine import AutomationEngine, OperationContext
from kalz.security.security_engine import SecurityEngine, SecurityContext

automation = AutomationEngine()
security = SecurityEngine()
print('automation_operations', len(automation.operations))
print('security_rules', len(security.rules))
print('plan', automation.plan('detect_kernel', OperationContext('job-1')))
print('scope', security.evaluate('target', 'lab.local', SecurityContext('operator', targets=frozenset({'lab.local'}))))
