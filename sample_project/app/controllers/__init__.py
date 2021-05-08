from .teacher_resource import TeacherResource, TeacherListResource
from .course_resource import CourseResource, CourseListResource
from .topic_resource import TopicResource, TopicListResource
from .synopsis_resource import SynopsisPdfResource, SynopsisPptxResource


def add_resources(api):
    api.add_resource(TeacherResource, '/teacher/<int:teacher_id>')
    api.add_resource(TeacherListResource, '/teachers')
    api.add_resource(CourseResource, '/course/<int:course_id>')
    api.add_resource(CourseListResource, '/courses')
    api.add_resource(TopicResource, '/topic/<int:topic_id>')
    api.add_resource(TopicListResource, '/course/<int:course_id>/topics')
    api.add_resource(SynopsisPdfResource, '/topic/<int:topic_id>/synopsis_pdf')
    api.add_resource(SynopsisPptxResource, '/topic/<int:topic_id>/synopsis_pptx')
