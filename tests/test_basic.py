import components.auth as auth


def test_login_ui_import():
    assert callable(auth.login_ui)
