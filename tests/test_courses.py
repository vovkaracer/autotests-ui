from playwright.sync_api import expect, Page
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    no_result_list_courses_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(no_result_list_courses_title).to_be_visible()
    expect(no_result_list_courses_title).to_have_text('There is no results')

    empty_list_courses_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_list_courses_icon).to_be_visible()

    empty_list_courses_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_list_courses_description).to_be_visible()
    expect(empty_list_courses_description).to_have_text(
        'Results from the load test pipeline will be displayed here')