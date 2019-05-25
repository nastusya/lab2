from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import UserModel
from .course import CourseModel
from .course_status import CourseStatusModel
from .course_review import CourseReviewModel
from .week_task import WeekTaskModel
from .course_week import CourseWeekModel
from .user_course import UserCourseModel
