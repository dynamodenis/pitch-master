from app.models import User,Comment
from app import db
import unittest

class TestComment(unittest.TestCase):
    #SET UP USER AND COMMENT
    def setUp(self):
        self.user=User(username='denis',email='dm@gmail.com',password='banana',bio='programmer' ,pitch='live life alone')
        self.comment=Comment(comment='i like it',pitch='live life alone',posted='12/12/2020',user=self.user)

    def tearDown(self):
        self.comment.query.delete()
        self.user.query.delete()

    def test_comment_instance(self):
        self.assertEquals(self.comment.comment,'i like it')
        self.assertEquals(self.comment.pitch,'live life alone')
        self.assertEquals(self.comment.posted,'12/12/2020')
        self.assertEquals(self.comment.user,self.user)

    def test_save(self):
        self.comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment(self):
        self.comment.save_comment()
        get=Comment.get_comments('live life alone')
        self.assertTrue(len(get)==1)
