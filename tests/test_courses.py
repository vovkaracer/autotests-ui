from playwright.sync_api import expect, Page
from pages.create_course_page import CreateCoursePage
from pages.courses_page import CoursesListPage
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

@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form(
        title='',
        description='',
        estimated_time='',
        min_score='0',
        max_score='0'
    )

    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()

    create_course_page.upload_preview_image(file='./test_data/files/image.png')
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)
    create_course_page.fill_create_course_form(
        title='Playwright',
        estimated_time='2 weeks',
        description='Playwright',
        max_score='100',
        min_score='10'
    )
    create_course_page.click_create_course_button()

    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(
        index=0,
        text='Playwright',
        max_score='100',
        min_score='10',
        estimated_time='2 weeks'
    )