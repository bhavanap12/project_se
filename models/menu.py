# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(B('Admission_Portal'), XML('&trade;&nbsp;'),
                  _class="navbar-brand", _href="http://www.web2py.com/",
                  _id="web2py-logo")
response.title = request.application.replace('_', ' ').title()
response.subtitle = ''

# ----------------------------------------------------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# ----------------------------------------------------------------------------------------------------------------------
response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

# ----------------------------------------------------------------------------------------------------------------------
# your http://google.com/analytics id
# ----------------------------------------------------------------------------------------------------------------------
response.google_analytics_id = None

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'index')),
    
    (T('Engineering'), False, URL('default', 'user'),[(T('Colleges'), False, URL('default', 'user')),(T('News_Stories'), False, URL('default', 'user')),(T('Announcements'), False, URL('default', 'user'))]),
    (T('Architecture'), False, URL('default', 'user'),[(T('Colleges'), False, URL('default', 'user')),(T('News_Stories'), False, URL('default', 'user')),(T('Announcements'), False, URL('default', 'user'))]),
    (T('Design'), False, URL('default', 'user'),[(T('Colleges'), False, URL('default', 'user')),(T('News_Stories'), False, URL('default', 'user')),(T('Announcements'), False, URL('default', 'user'))]),
]




# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. remove in production
# ----------------------------------------------------------------------------------------------------------------------



if "auth" in locals():
    auth.wikimenu()
