from app.models import User,Comment,Pitch
from app import db
import unittest

class TestComment(unittest.TestCase):
    #SET UP USER AND COMMENT
    def setUp(self):
        self.pitch=Pitch(pitch='we only live once', pitch_category='sales pitch')
        self.comment=Comment(comment='i like it',pitch=self.pitch)

    def tearDown(self):
        self.comment.query.delete()
        self.pitch.query.delete()

    def test_comment_instance(self):
        self.assertEquals(self.comment.comment,'i like it')
        self.assertEquals(self.comment.pitch,self.pitch)

    def test_save(self):
        self.comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment(self):
        self.comment.save_comment()
        get=Comment.get_comments(self.pitch.id)
        self.assertTrue(len(get)==1)
