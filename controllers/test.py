# -*- coding: utf-8 -*-
# try something like
import unittest

from gluon.globals import Request

execfile("applications/project_se/controllers/default.py", globals())

db(db.subscribe.id>0).delete()  # Clear the database
db(db.notifications.id>0).delete()
db.commit()

class TestSubscriber(unittest.TestCase):
    def setUp(self):
        self.request = Request([])  # Use a clean Request object

    def testnews_and_articles(self):
        # Set variables for the test function
       
        request.post_vars={'id1':1,'branch':"Engineering",'specialization':"civil"}
        news_and_articles()
        
        
        self.assertEquals(200,response.status)
    def testProposal(self):
        # Set variables for the test function
        request.post_vars={'id1':1,'branch':"Engineering",'specialization':"civil"}
        proposals() 
        self.assertEquals(200,response.status)
    def testManage(self):
        # Set variables for the test function
        request.post_vars={'id1':1,'branch':"Engineering",'specialization':"civil"}
        manage_admin() 
        self.assertEquals(200,response.status)
    def testEngg_colleges(self):
        # Set variables for the test function
        request.post_vars={'id1':1,'branch':"Engineering",'specialization':"civil"}
        engg_colleges() 
        self.assertEquals(200,response.status)
    def testDesign_colleges(self):
        # Set variables for the test function
        request.post_vars={'id1':1,'branch':"Engineering",'specialization':"civil"}
        design_colleges() 
        self.assertEquals(200,response.status)
    def testArch_colleges(self):
        # Set variables for the test function
        request.post_vars={'id1':1,'branch':"Engineering",'specialization':"civil"}
        arch_colleges() 
        self.assertEquals(200,response.status)
    def testPut_subscriber(self):
        session.id1=1
        session.branchy="Engineering"
        session.specialization="Civil"
        put_subscriber()
        
        self.assertEquals(1,len(db(db.subscribe).select()))
    def testRemove_subscriber(self):
        session.id1=1
        session.branchy="Engineering"
        session.specialization="Civil"
        remove_subscriber()
        
        self.assertEquals(0,len(db(db.subscribe).select()))
    
    

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestSubscriber))
unittest.TextTestRunner(verbosity=2).run(suite)
