"""Plugin contribution for the Rovo Dev community harness."""

from __future__ import annotations

from typing import Any

from omnigent.harness_install_spec import HarnessInstallSpec
from omnigent.harness_plugins import HarnessContribution

ROVO_HARNESS = "rovo-cli"
ROVO_ALIAS = "rovo"
ROVO_INSTALL_KEY = "rovo"
ROVO_MODEL_ENV = "HARNESS_ROVO_MODEL"


def build_rovo_spawn_env(
    spec: Any,
    *,
    cwd: object | None = None,
    workdir: object | None = None,
) -> dict[str, str]:
    """Build the Rovo harness spawn environment from an agent spec."""
    model = getattr(spec, "model", None)
    return {ROVO_MODEL_ENV: model} if model else {}


def get_contribution() -> HarnessContribution:
    """Return the Rovo Dev harness contribution."""
    return HarnessContribution(
        name="rovo",
        valid_harnesses=frozenset({ROVO_HARNESS}),
        harness_modules={
            ROVO_HARNESS: "omnigent.community.harnesses.rovo.inner.rovo_harness",
        },
        aliases={ROVO_ALIAS: ROVO_HARNESS},
        install_specs={
            ROVO_INSTALL_KEY: HarnessInstallSpec(
                display="Rovo Dev",
                binary="acli",
                package=None,
                login_args=("rovodev", "auth", "login"),
                install_hint="install Atlassian CLI (`acli`) from Atlassian",
                auth_hint="run `acli rovodev auth login`",
            ),
        },
        harness_install_keys={
            ROVO_HARNESS: ROVO_INSTALL_KEY,
            ROVO_ALIAS: ROVO_INSTALL_KEY,
        },
        model_env_keys={ROVO_HARNESS: ROVO_MODEL_ENV},
        spawn_env_builders={
            ROVO_HARNESS: "omnigent.community.harnesses.rovo.plugin:build_rovo_spawn_env",
        },
        harness_labels={ROVO_HARNESS: "Rovo Dev"},
    )
