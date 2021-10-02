import re

import pytest

from scrapli_community.cisco.asa.cisco_asa import DEFAULT_PRIVILEGE_LEVELS


# TODO
@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("exec", "ACME-FIREWALL>"),
        ("exec", "ACME_FIREWALL> "),
        ("exec", "ACME_FIREWALL/act/pri>"),
        ("privilege_exec", "ACME-FIREWALL#"),
        ("configuration", "ACME-FIREWALL(config)#"),
        ("configuration", "ACME-FIREWALL(config-if)#"),
        ("privilege_exec", "ACME_FIREWALL# "),
        ("configuration", "ACME_FIREWALL(config)# "),
    ],
    ids=[
        "base_prompt_exec",
        "base_prompt_underscore_exec",
        "base_prompt_underscore_exec_fw_status",
        "base_prompt_privilege_exec",
        "base_prompt_configuration",
        "interface_configuration",
        "base_prompt_underscore_privilege_exec",
        "base_prompt_underscore_configuration",
    ],
)
def test_default_prompt_patterns(priv_pattern):
    priv_level_name = priv_pattern[0]
    prompt = priv_pattern[1]
    prompt_pattern = DEFAULT_PRIVILEGE_LEVELS.get(priv_level_name).pattern
    match = re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)
    assert match
