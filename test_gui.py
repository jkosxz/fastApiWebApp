import re
from playwright.sync_api import Page, expect


def test_homepage_has_Fast_Api_Project_in_title(page: Page):
    page.goto("http://16.170.222.98/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title("Fast Api Project")

def test_homepage_has_users_button(page: Page):
    page.goto("http://16.170.222.98/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title("Fast Api Project")

    page.get_by_role("button", name="użytkownicy").click()

def test_homepage_has_mainpage_button(page: Page):
    page.goto("http://16.170.222.98/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title("Fast Api Project")

    page.get_by_role("button", name="mainpage").click()

def test_homepage_has_posts_button(page: Page):
    page.goto("http://16.170.222.98/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title("Fast Api Project")

    page.get_by_role("button", name="posty").click()






