"""
This module stores fixtures for performing tests.
"""
import os
import pytest
from vault import VaultClient
from telegram.telegram import TelegramBot


@pytest.fixture(name="url", scope='session')
def fixture_url():
    """Returns the vault url"""
    if os.getenv("CI"):
        return "http://localhost:8200"
    return "http://0.0.0.0:8200"


@pytest.fixture(name="name", scope='session')
def fixture_name():
    """Returns the project name"""
    return "testapp-1"


@pytest.fixture(name="policy_path", scope='session')
def fixture_policy_path():
    """Returns the policy path"""
    return "tests/vault/policy.hcl"


@pytest.fixture(name="vault", scope='session')
def fixture_vault(url, name, policy_path):
    """Prepare a storage instance for py tests and return the client"""
    configurator = VaultClient(
                url=url,
                name=name,
                new=True
    )
    namespace = configurator.create_namespace(
            name=name
    )
    policy = configurator.create_policy(
            name=name,
            path=policy_path
        )
    approle = configurator.create_approle(
        name=name,
        path=namespace,
        policy=policy
    )
    return VaultClient(
            url=url,
            name=name,
            approle=approle
    )


@pytest.fixture(name="telegram_client", scope='session')
def fixture_telegram_client(vault):
    """Returns telegram client with vault"""
    response = vault.write_secret(
        path='configuration/telegram',
        key='token',
        value='qwerty123'
    )
    print(f"Prepared test data status: {response}")
    return TelegramBot(
        name='testapp-1',
        vault=vault,
        messages_config='tests/configs/messages.json'
    )
