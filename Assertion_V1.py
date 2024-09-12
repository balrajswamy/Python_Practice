def test_user_status(status):
    response_status = status # This could be set by some logic
    status_message = "User is active" if response_status == "active" else "User is inactive"

    # Assert that the status message is as expected
    assert status_message == "User is active", f"Expected 'User is active', but got {status_message}"
    return status_message


print(test_user_status("active"))
