from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.charts.chart_view_component import ChartViewComponent

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.dashboard_toolbar_view = DashboardToolbarViewComponent(page)
        self.scores_chart = ChartViewComponent(page, 'scores', 'scatter')
        self.courses_chart = ChartViewComponent(page, 'courses', 'pie')
        self.students_chart = ChartViewComponent(page, 'students', 'bar')
        self.activities_chart = ChartViewComponent(page, 'activities', 'line')

    def check_visible_students_chart(self):
        self.students_chart.check_visible('Students')

    def check_visible_activities_chart(self):
        self.activities_chart.check_visible('Activities')

    def check_visible_scores_chart(self):
        self.scores_chart.check_visible('Scores')

    def check_visible_courses_chart(self):
        self.courses_chart.check_visible('Courses')