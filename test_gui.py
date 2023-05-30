"""GUI tests for the web app"""
from playwright.sync_api import Page, expect


def test_homepage_has_fast_api_project_in_title(page: Page):
    """checks if starting page has correct title"""
    page.goto("http://16.170.222.98/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title("Fast Api Project")


def test_homepage_has_users_button(page: Page):
    """checks if button "użytkownicy" is clickable"""
    page.goto("http://16.170.222.98/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title("Fast Api Project")

    page.get_by_role("button", name="użytkownicy").click()


def test_homepage_has_mainpage_button(page: Page):
    """checks if button "mainpage" is clickable"""
    page.goto("http://16.170.222.98/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title("Fast Api Project")

    page.get_by_role("button", name="mainpage").click()


def test_homepage_has_posts_button(page: Page):
    """checks if button "posty" is clickable"""
    page.goto("http://16.170.222.98/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title("Fast Api Project")

    page.get_by_role("button", name="posty").click()


def test_posts_has_title(page: Page):
    """checks if page "posts" has correct title"""
    page.goto("http://16.170.222.98/posts")

    expect(page).to_have_title("Fast Api Project")


def test_users_has_title(page: Page):
    """checks if page "users" has correct titles"""
    page.goto("http://16.170.222.98/users")

    expect(page).to_have_title("Fast Api Project")


def test_post1_has_title(page: Page):
    """checks if post 1 has correct title"""
    page.goto("http://16.170.222.98/mainpage/post/1")

    expect(page).to_have_title("Fast Api Project")
