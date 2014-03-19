# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
## http://www.utf8-chartable.de/
#########################################################################

import base64

def index():
    return dict(message="Hello from MyApp")

def songform():
    if request.vars.title:
		# session.title = maketitledata(request.vars.title, request.vars.author)
        # redirect(URL('songfile'))
        response.headers['Content-Type'] = 'text/xml'
        attachment = 'attachment;filename=' + request.vars.title + '.pro5'
        response.headers['Content-Disposition'] = attachment
        content = maketitledata(request.vars.title, request.vars.author)
        raise HTTP(200,str(content),
                   **{'Content-Type':'text/xml',
                      'Content-Disposition':attachment + ';'})
        redirect(URL('songfile'))
    return dict()
	
def songfile():
	return dict(message="Hello from MyApp")

def maketitledata( title, author):
    return base64.b64encode(formattitle(title,author))
	
def formattitle( title, author ):
    return ("{\\rtf1\\ansi\\ansicpg1252\\cocoartf1265\n" +
			"\\cocoascreenfonts1{\\fonttbl\\f0\\fswiss\\fcharset0 Helvetica;}\n" +
			"{\\colortbl;\\red255\\green255\\blue255;}\n" +
			"\\pard\\tx560\\tx1120\\tx1680\\tx2240\\tx2800\\tx3360\\tx3920\\tx4480\\tx5040\\tx5600\\tx6160\\tx6720\\pardirnatural\\qr\n"+
			"\n"
			"\\f0\\fs100 \\cf1 " + formatunicode(title) + "\\\n"
			"\\pard\\tx560\\tx1120\\tx1680\\tx2240\\tx2800\\tx3360\\tx3920\\tx4480\\tx5040\\tx5600\\tx6160\\tx6720\\pardirnatural\\qr\n"+
			"\r\n"
			"\\fs60 \\cf1 " + formatunicode(author) + "}")
	

## http://www.utf8-chartable.de/	
## str = text.replace("\xc3\xb3","\\\'f3")
def formatunicode( text ):
	str = text.replace("\x5c","\\\'5c")
	str = str.replace("\x27","\\\'27")
	str = str.replace("\xc2\xa1","\\\'a1")
	str = str.replace("\xc2\xa2","\\\'a2")
	str = str.replace("\xc2\xa3","\\\'a3")
	str = str.replace("\xc2\xa4","\\\'a4")
	str = str.replace("\xc2\xa5","\\\'a5")
	str = str.replace("\xc2\xa6","\\\'a6")
	str = str.replace("\xc2\xa7","\\\'a7")
	str = str.replace("\xc2\xa8","\\\'a8")
	str = str.replace("\xc2\xa9","\\\'a9")
	str = str.replace("\xc2\xaa","\\\'aa")
	str = str.replace("\xc2\xab","\\\'ab")
	str = str.replace("\xc2\xac","\\\'ac")
	str = str.replace("\xc2\xae","\\\'ae")
	str = str.replace("\xc2\xaf","\\\'af")
	str = str.replace("\xc2\xb0","\\\'b0")
	str = str.replace("\xc2\xb1","\\\'b1")
	str = str.replace("\xc2\xb2","\\\'b2")
	str = str.replace("\xc2\xb3","\\\'b3")
	str = str.replace("\xc2\xb4","\\\'b4")
	str = str.replace("\xc2\xb5","\\\'b5")
	str = str.replace("\xc2\xb6","\\\'b6")
	str = str.replace("\xc2\xb7","\\\'b7")
	str = str.replace("\xc2\xb8","\\\'b8")
	str = str.replace("\xc2\xb9","\\\'b9")
	str = str.replace("\xc2\xba","\\\'ba")
	str = str.replace("\xc2\xbb","\\\'bb")
	str = str.replace("\xc2\xbc","\\\'bc")
	str = str.replace("\xc2\xbd","\\\'bd")
	str = str.replace("\xc2\xbe","\\\'be")
	str = str.replace("\xc2\xbf","\\\'bf")
	str = str.replace("\xc3\x80","\\\'c0")
	str = str.replace("\xc3\x81","\\\'c1")
	str = str.replace("\xc3\x82","\\\'c2")
	str = str.replace("\xc3\x83","\\\'c3")
	str = str.replace("\xc3\x84","\\\'c4")
	str = str.replace("\xc3\x85","\\\'c5")
	str = str.replace("\xc3\x86","\\\'c6")
	str = str.replace("\xc3\x87","\\\'c7")
	str = str.replace("\xc3\x88","\\\'c8")
	str = str.replace("\xc3\x89","\\\'c9")
	str = str.replace("\xc3\x8a","\\\'ca")
	str = str.replace("\xc3\x8b","\\\'cb")
	str = str.replace("\xc3\x8c","\\\'cc")
	str = str.replace("\xc3\x8d","\\\'cd")
	str = str.replace("\xc3\x8e","\\\'ce")
	str = str.replace("\xc3\x8f","\\\'cf")
	str = str.replace("\xc3\x90","\\\'d0")
	str = str.replace("\xc3\x91","\\\'d1")
	str = str.replace("\xc3\x92","\\\'d2")
	str = str.replace("\xc3\x93","\\\'d3")
	str = str.replace("\xc3\x94","\\\'d4")
	str = str.replace("\xc3\x95","\\\'d5")
	str = str.replace("\xc3\x96","\\\'d6")
	str = str.replace("\xc3\x97","\\\'d7")
	str = str.replace("\xc3\x98","\\\'d8")
	str = str.replace("\xc3\x99","\\\'d9")
	str = str.replace("\xc3\x9a","\\\'da")
	str = str.replace("\xc3\x9b","\\\'db")
	str = str.replace("\xc3\x9c","\\\'dc")
	str = str.replace("\xc3\x9d","\\\'dd")
	str = str.replace("\xc3\x9e","\\\'de")
	str = str.replace("\xc3\x9f","\\\'df")
	str = str.replace("\xc3\xa0","\\\'e0")
	str = str.replace("\xc3\xa1","\\\'e1")
	str = str.replace("\xc3\xa2","\\\'e2")
	str = str.replace("\xc3\xa3","\\\'e3")
	str = str.replace("\xc3\xa4","\\\'e4")
	str = str.replace("\xc3\xa5","\\\'e5")
	str = str.replace("\xc3\xa6","\\\'e6")
	str = str.replace("\xc3\xa7","\\\'e7")
	str = str.replace("\xc3\xa8","\\\'e8")
	str = str.replace("\xc3\xa9","\\\'e9")
	str = str.replace("\xc3\xaa","\\\'ea")
	str = str.replace("\xc3\xab","\\\'eb")
	str = str.replace("\xc3\xac","\\\'ec")
	str = str.replace("\xc3\xad","\\\'ed")
	str = str.replace("\xc3\xae","\\\'ee")
	str = str.replace("\xc3\xaf","\\\'ef")
	str = str.replace("\xc3\xb0","\\\'f0")
	str = str.replace("\xc3\xb1","\\\'f1")
	str = str.replace("\xc3\xb2","\\\'f2")
	str = str.replace("\xc3\xb3","\\\'f3")
	str = str.replace("\xc3\xb4","\\\'f4")
	str = str.replace("\xc3\xb5","\\\'f5")
	str = str.replace("\xc3\xb6","\\\'f6")
	str = str.replace("\xc3\xb7","\\\'f7")
	str = str.replace("\xc3\xb8","\\\'f8")
	str = str.replace("\xc3\xb9","\\\'f9")
	str = str.replace("\xc3\xba","\\\'fa")
	str = str.replace("\xc3\xbb","\\\'fb")
	str = str.replace("\xc3\xbc","\\\'fc")
	str = str.replace("\xc3\xbd","\\\'fd")
	str = str.replace("\xc3\xbe","\\\'fe")
	str = str.replace("\xc3\xbf","\\\'ff")
	str = str.replace("\x21","\\\'21")
	str = str.replace("\x22","\\\'22")
	str = str.replace("\x23","\\\'23")
	str = str.replace("\x24","\\\'24")
	str = str.replace("\x25","\\\'25")
	str = str.replace("\x26","\\\'26")
	str = str.replace("\x28","\\\'28")
	str = str.replace("\x29","\\\'29")
	str = str.replace("\x2a","\\\'2a")
	str = str.replace("\x2b","\\\'2b")
	str = str.replace("\x2c","\\\'2c")
	str = str.replace("\x2d","\\\'2d")
	str = str.replace("\x2e","\\\'2e")
	str = str.replace("\x2f","\\\'2f")
	str = str.replace("\x3a","\\\'3a")
	str = str.replace("\x3b","\\\'3b")
	str = str.replace("\x3c","\\\'3c")
	str = str.replace("\x3d","\\\'3d")
	str = str.replace("\x3e","\\\'3e")
	str = str.replace("\x3f","\\\'3f")
	str = str.replace("\x40","\\\'40")
	str = str.replace("\x5b","\\\'5b")
	str = str.replace("\x5d","\\\'5d")
	str = str.replace("\x5e","\\\'5e")
	str = str.replace("\x5f","\\\'5f")
	str = str.replace("\x60","\\\'60")
	str = str.replace("\x7b","\\\'7b")
	str = str.replace("\x7c","\\\'7c")
	str = str.replace("\x7d","\\\'7d")
	str = str.replace("\x7e","\\\'7e")
	return str
	
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
