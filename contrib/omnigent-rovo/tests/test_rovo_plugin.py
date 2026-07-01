"""Tests for the Rovo community harness contribution."""

from __future__ import annotations

from types import SimpleNamespace

from omnigent.community.harnesses.rovo.plugin import (
    ROVO_HARNESS,
    ROVO_MODEL_ENV,
    build_rovo_spawn_env,
    get_contribution,
)


def test_contribution_registers_rovo_harness() -> None:
    contribution = get_contribution()

    assert contribution.name == "rovo"
    assert contribution.valid_harnesses == frozenset({ROVO_HARNESS})
    assert contribution.aliases == {"rovo": ROVO_HARNESS}
    assert contribution.harness_modules == {
        ROVO_HARNESS: "omnigent.community.harnesses.rovo.inner.rovo_harness"
    }
    assert contribution.model_env_keys == {ROVO_HARNESS: ROVO_MODEL_ENV}
    assert contribution.spawn_env_builders == {
        ROVO_HARNESS: "omnigent.community.harnesses.rovo.plugin:build_rovo_spawn_env"
    }
    assert contribution.harness_labels == {ROVO_HARNESS: "Rovo Dev"}


def test_contribution_registers_acli_install_metadata() -> None:
    contribution = get_contribution()

    spec = contribution.install_specs["rovo"]
    assert spec.display == "Rovo Dev"
    assert spec.binary == "acli"
    assert spec.package is None
    assert spec.login_args == ("rovodev", "auth", "login")
    assert contribution.harness_install_keys == {
        ROVO_HARNESS: "rovo",
        "rovo": "rovo",
    }


def test_build_rovo_spawn_env_uses_spec_model() -> None:
    assert build_rovo_spawn_env(SimpleNamespace(model="Claude Sonnet 4.6")) == {
        ROVO_MODEL_ENV: "Claude Sonnet 4.6"
    }
    assert build_rovo_spawn_env(SimpleNamespace(model=None)) == {}
