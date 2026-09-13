from pathlib import Path

a=Path('kalz/automation/automation_engine.py')
a_names=['reconcile_services','reconcile_packages','reconcile_configs','reconcile_users','reconcile_groups','reconcile_mounts','reconcile_routes','reconcile_firewall','reconcile_desktop','reconcile_backups','reconcile_reports','reconcile_plugins','reconcile_scopes','reconcile_workflows','reconcile_schedules','reconcile_metrics','reconcile_logs','reconcile_alerts','reconcile_updates','reconcile_health','reconcile_inventory','reconcile_manifests','reconcile_permissions','reconcile_integrity','reconcile_release']
with a.open('a') as f:
    for i,n in enumerate(a_names,2000):
        c=''.join(x.title() for x in n.split('_'))+'CatalogOperation'
        f.write(f'''\nclass {c}(AutomationOperation):\n    category = "reconciliation"\n    name = {n!r}\n    reversible = True\n    requires_privilege = False\n    def validate(self, context: OperationContext) -> None:\n        super().validate(context)\n        if context.dry_run is False and context.mode == "safe":\n            raise AutomationError("reconciliation changes require standard mode")\n    def plan(self, context: OperationContext) -> dict[str, Any]:\n        result = super().plan(context)\n        result.update({{"sequence": {i}, "phase": "reconciliation", "review": True}})\n        return result\n''')
    f.write('\\nfor _catalog_operation in [\\n'+''.join('    '+''.join(x.title() for x in n.split('_'))+'CatalogOperation(),\\n' for n in a_names)+']:\\n    OPERATIONS[_catalog_operation.name] = _catalog_operation\\n')

s=Path('kalz/security/security_engine.py')
s_names=['credential_format','credential_scope','credential_owner','credential_usage','credential_backup','credential_restore','credential_export','credential_import','audit_owner','audit_scope','audit_format','audit_destination','audit_backup','audit_restore','audit_rotation','scope_format','scope_owner','scope_target','scope_service','scope_change','consent_actor','consent_reason','consent_ticket','consent_duration','consent_mode','panic_actor','panic_reason','panic_timestamp','panic_scope','panic_recovery','rate_actor','rate_operation','rate_resource','rate_priority','rate_retry','rate_backoff','quota_actor','quota_operation','quota_resource','quota_window','quota_reset']
with s.open('a') as f:
    for i,n in enumerate(s_names,2000):
        c=''.join(x.title() for x in n.split('_'))+'CatalogRule'
        f.write(f'''\nclass {c}(SecurityRule):\n    family = "catalog"\n    name = {n!r}\n    risk = "medium"\n    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:\n        base = super().evaluate(value, context)\n        if not base.allowed: return base\n        if not context.consent and context.mode in {{"safe", "standard"}}:\n            return SecurityDecision(self.name, False, "consent required", self.risk, {{"sequence": {i}}})\n        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {{"sequence": {i}, "value": repr(value)}})\n''')
    f.write('\\nfor _catalog_rule in [\\n'+''.join('    '+''.join(x.title() for x in n.split('_'))+'CatalogRule(),\\n' for n in s_names)+']:\\n    RULES[_catalog_rule.name] = _catalog_rule\\n')
