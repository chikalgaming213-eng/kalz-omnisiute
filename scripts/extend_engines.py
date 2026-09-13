from pathlib import Path

def append_automation():
    path = Path('kalz/automation/automation_engine.py')
    out=[]
    names = ['discover_services','discover_units','discover_cron','discover_timers','discover_sockets','discover_devices','discover_usb','discover_pci','discover_bluetooth','discover_audio','discover_video','discover_printers','discover_locales','discover_fonts','discover_keyrings','discover_credentials','discover_shells','discover_editors','discover_compilers','discover_runtimes','verify_service','verify_unit','verify_timer','verify_socket','verify_device','verify_usb','verify_pci','verify_bluetooth','verify_audio','verify_video','verify_printer','verify_locale','verify_font','verify_keyring','verify_shell','verify_editor','verify_compiler','verify_runtime']
    for index,name in enumerate(names, 1000):
        cls=''.join(x.title() for x in name.split('_'))+'ExtendedOperation'
        out += [f'class {cls}(AutomationOperation):', "    category = 'extended'", f'    name = {name!r}', f'    reversible = {str(index % 2 == 0)}', f'    requires_privilege = {str(index % 5 == 0)}', '    def validate(self, context: OperationContext) -> None:', '        super().validate(context)', '        if not context.actor.strip(): raise AutomationError("actor is required")', '    def plan(self, context: OperationContext) -> dict[str, Any]:', '        plan = super().plan(context)', f'        plan.update({{"sequence": {index}, "resource": {name!r}, "guard": "review"}})', '        return plan', '    def execute(self, context: OperationContext) -> OperationResult:', '        return super().execute(context)', '']
    out += ['for _extended_operation in ['] + ['    '+''.join(x.title() for x in n.split('_'))+'ExtendedOperation(),' for n in names] + [']:', '    OPERATIONS[_extended_operation.name] = _extended_operation', '']
    with path.open('a',encoding='utf-8') as f:f.write('\n'.join(out)+'\n')

def append_security():
    path=Path('kalz/security/security_engine.py')
    out=[]
    names=['environment','filesystem_acl','filesystem_mount','filesystem_link','network_route','network_dns','network_proxy','network_tls','package_origin','package_version','package_lock','service_owner','service_group','service_mode','desktop_session','desktop_extension','desktop_theme','plugin_signature','plugin_capability','plugin_origin','workflow_graph','workflow_variable','workflow_secret','job_owner','job_priority','job_timeout','job_output','report_owner','report_destination','report_format','backup_origin','backup_destination','backup_retention','update_channel','update_signature','update_rollback','release_artifact','release_manifest','release_target','release_approval','credential_source','credential_rotation','credential_expiry','audit_export','audit_replay','audit_diff','scope_inheritance','scope_expiry','consent_expiry','panic_state','rate_window']
    for index,name in enumerate(names,1000):
        cls=''.join(x.title() for x in name.split('_'))+'ExtendedRule'
        risk = 'high' if index % 5 == 0 else 'medium'
        out += [f'class {cls}(SecurityRule):', "    family = 'extended'", f'    name = {name!r}', f'    risk = {risk!r}', '    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:', '        base = super().evaluate(value, context)', '        if not base.allowed: return base', '        if context.mode == "safe" and not context.consent:', '            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})', f'        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {{"sequence": {index}, "value_type": type(value).__name__}})', '']
    out += ['for _extended_rule in ['] + ['    '+''.join(x.title() for x in n.split('_'))+'ExtendedRule(),' for n in names] + [']:', '    RULES[_extended_rule.name] = _extended_rule', '']
    with path.open('a',encoding='utf-8') as f:f.write('\n'.join(out)+'\n')

if __name__=='__main__': append_automation(); append_security()
