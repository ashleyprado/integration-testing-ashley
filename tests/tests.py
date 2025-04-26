"""
Tests for ../app.py

Run from the project directory (not the tests directory) with the invocation `pytest tests/tests.py`
"""
import streamlit as st
from streamlit.testing.v1 import AppTest

def test_button_increments_counter():
    """Test that the counter increments when the button is clicked."""
    at = AppTest.from_file("app.py").run()

    # Initialize the session state
    at.session_state.count = 1

    # Click the button
    at.button(key="increment").click().run()

    # Assert that the counter has been incremented
    assert at.session_state.count == 2

def test_button_decrements_counter():
    """Test that the counter decrements when the button is clicked, but does not go below 0."""
    at = AppTest.from_file("app.py").run()

    # Initialize the session state
    at.session_state.count = 1

    # Click the decrement button
    at.button(key="decrement").click().run()

    # Assert that the counter has been decremented
    assert at.session_state.count == 0

    # Try to decrement again (should not go below 0)
    at.button(key="decrement").click().run()

    # Assert that the counter is still 0
    assert at.session_state.count == 0

def test_button_increments_counter_ten_x():
    """Test that the increment button works correctly in 10x mode."""
    at = AppTest.from_file("app.py").run()

    # Initialize the session state
    at.session_state.count = 0
    at.session_state.ten_x = True

    # Click the increment button
    at.button(key="increment").click().run()

    # Assert that the counter has increased by 10
    assert at.session_state.count == 10

def test_button_decrements_counter_ten_x():
    """Test that the decrement button works correctly in 10x mode and does not go below 0."""
    at = AppTest.from_file("app.py").run()

    # Initialize the session state
    at.session_state.count = 15
    at.session_state.ten_x = True

    # Click the decrement button
    at.button(key="decrement").click().run()

    # Assert that the counter has decreased by 10
    assert at.session_state.count == 5

    # Click the decrement button again (should drop to 0, not negative)
    at.button(key="decrement").click().run()
    assert at.session_state.count == 0

def test_output_text_correct():
    """Test that the text shows the correct value."""
    at = AppTest.from_file("app.py").run()

    # Initialize session state
    at.session_state.count = 0
    at.session_state.ten_x = False

    # Increment once at 1x
    at.button(key="increment").click().run()

    # Turn on 10x mode
    at.checkbox(key="ten_x").check().run()

    # Increment once at 10x
    at.button(key="increment").click().run()

    # Check displayed text value
    assert at.markdown[0].value == "Total count is 11"
