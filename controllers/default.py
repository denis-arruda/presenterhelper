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

start_document = ("<RVPresentationDocument height=\"768\" width=\"1024\" versionNumber=\"500\" docType=\"0\" creatorCode=\"1349676880\" lastDateUsed=\"2012-04-05T00:16:34\" usedCount=\"0\" category=\"M\xc3\xbasica\" resourcesDirectory=\"\" backgroundColor=\"1 0.5 0 1\" drawingBackgroundColor=\"0\" notes=\"\" artist=\"\" author=\"\" album=\"\" CCLIDisplay=\"0\" CCLIArtistCredits=\"\" CCLISongTitle=\"\" CCLIPublisher=\"\" CCLICopyrightInfo=\"\" CCLILicenseNumber=\"\" chordChartPath=\"\">"
	"<timeline timeOffSet=\"0\" selectedMediaTrackIndex=\"0\" unitOfMeasure=\"60\" duration=\"0\" loop=\"0\">"
		"<timeCues containerClass=\"NSMutableArray\"></timeCues>"
		"<mediaTracks containerClass=\"NSMutableArray\"></mediaTracks>"
	"</timeline>"
	"<bibleReference containerClass=\"NSMutableDictionary\"></bibleReference>"
	"<_-RVProTransitionObject-_transitionObject transitionType=\"-1\" transitionDuration=\"1\" motionEnabled=\"0\" motionDuration=\"20\" motionSpeed=\"100\"></_-RVProTransitionObject-_transitionObject>"
		"<groups containerClass=\"NSMutableArray\">"
			"<RVSlideGrouping name=\"Verse 1\" uuid=\"3986CF53-D65A-433F-9B39-4115DD9DCB66\" color=\"0 0 1 1\" serialization-array-index=\"0\">"
				"<slides containerClass=\"NSMutableArray\">")

start_slide_part1 = ("<RVDisplaySlide backgroundColor=\"0 0 0 0\" enabled=\"1\" highlightColor=\"\" hotKey=\"\" label=\"\" notes=\"\" slideType=\"1\" sort_index=\"")

start_slide_part2 = ("\" UUID=\"7EBF6747-5CF5-44EC-9A47-EF4F06F20559\" drawingBackgroundColor=\"0\" chordChartPath=\"\" serialization-array-index=\"")

start_slide_part3 = ("\"><cues containerClass=\"NSMutableArray\"></cues>"
					"<displayElements containerClass=\"NSMutableArray\">")

title_part1 = ("<RVTextElement displayDelay=\"0\" displayName=\"\" locked=\"0\" persistent=\"0\" typeID=\"0\" fromTemplate=\"0\" bezelRadius=\"0\" drawingFill=\"0\" drawingShadow=\"1\" drawingStroke=\"0\" fillColor=\"0 0 0 1\" rotation=\"0\" source=\"\" adjustsHeightToFit=\"0\" verticalAlignment=\"1\" RTFData=\"")

title_part2 = ("\" revealType=\"0\" serialization-array-index=\"0\">"
    "<_-RVRect3D-_position x=\"40\" y=\"40\" z=\"1\" width=\"1200\" height=\"160\"></_-RVRect3D-_position>"
    "<_-D-_serializedShadow containerClass=\"NSMutableDictionary\">"
	"<NSMutableString serialization-native-value=\"{4.3301301, -2.5}\" serialization-dictionary-key=\"shadowOffset\"></NSMutableString>"
	"<NSNumber serialization-native-value=\"5\" serialization-dictionary-key=\"shadowBlurRadius\"></NSNumber>"
	"<NSColor serialization-native-value=\"0 0 0 0.75\" serialization-dictionary-key=\"shadowColor\"></NSColor>"
	"</_-D-_serializedShadow>"
	"<stroke containerClass=\"NSMutableDictionary\">"
	"<NSColor serialization-native-value=\"0 0 0 1\" serialization-dictionary-key=\"RVShapeElementStrokeColorKey\"></NSColor>"
	"<NSNumber serialization-native-value=\"1\" serialization-dictionary-key=\"RVShapeElementStrokeWidthKey\"></NSNumber>"
	"</stroke>"
    "</RVTextElement>")

line_part1 = ("<RVTextElement displayDelay=\"0\" displayName=\"\" locked=\"0\" persistent=\"0\" typeID=\"0\" fromTemplate=\"0\" bezelRadius=\"0\" drawingFill=\"0\" drawingShadow=\"1\" drawingStroke=\"0\" fillColor=\"0 0 0 0.300000011920929\" rotation=\"0\" source=\"\" adjustsHeightToFit=\"0\" verticalAlignment=\"0\" RTFData=\"")

line_part2 = ("\" revealType=\"0\" serialization-array-index=\"1\">"
				"<_-RVRect3D-_position x=\"0\" y=\"505\" z=\"0\" width=\"1024\" height=\"240\"></_-RVRect3D-_position>"
					"<_-D-_serializedShadow containerClass=\"NSMutableDictionary\">"
						"<NSMutableString serialization-native-value=\"{4.3301301, -2.5}\" serialization-dictionary-key=\"shadowOffset\"></NSMutableString>"
							"<NSNumber serialization-native-value=\"5\" serialization-dictionary-key=\"shadowBlurRadius\"></NSNumber>"
								"<NSColor serialization-native-value=\"0 0 0 0.75\" serialization-dictionary-key=\"shadowColor\"></NSColor>"
								"</_-D-_serializedShadow>"
								"<stroke containerClass=\"NSMutableDictionary\">"
									"<NSColor serialization-native-value=\"0 0 0 1\" serialization-dictionary-key=\"RVShapeElementStrokeColorKey\"></NSColor>"
									"<NSNumber serialization-native-value=\"1\" serialization-dictionary-key=\"RVShapeElementStrokeWidthKey\"></NSNumber>"
								"</stroke>"
							"</RVTextElement>"
							"<RVShapeElement displayDelay=\"0\" displayName=\"\" locked=\"0\" persistent=\"0\" typeID=\"0\" fromTemplate=\"0\" bezelRadius=\"0\" drawingFill=\"1\" drawingShadow=\"0\" drawingStroke=\"0\" fillColor=\"0 0 0 0.2000000029802322\" rotation=\"0\" source=\"\" serialization-array-index=\"2\">"
								"<_-RVRect3D-_position x=\"0\" y=\"500\" z=\"0\" width=\"1024\" height=\"250\"></_-RVRect3D-_position>"
								"<_-D-_serializedShadow containerClass=\"NSMutableDictionary\">"
									"<NSMutableString serialization-native-value=\"{5, -5}\" serialization-dictionary-key=\"shadowOffset\"></NSMutableString>"
									"<NSNumber serialization-native-value=\"0\" serialization-dictionary-key=\"shadowBlurRadius\"></NSNumber>"
									"<NSColor serialization-native-value=\"0 0 0 0.3333333432674408\" serialization-dictionary-key=\"shadowColor\"></NSColor>"
								"</_-D-_serializedShadow>"
								"<stroke containerClass=\"NSMutableDictionary\">"
									"<NSColor serialization-native-value=\"0 0 0 1\" serialization-dictionary-key=\"RVShapeElementStrokeColorKey\"></NSColor>"
									"<NSNumber serialization-native-value=\"1\" serialization-dictionary-key=\"RVShapeElementStrokeWidthKey\"></NSNumber>"
								"</stroke>"
							"</RVShapeElement>")

end_slide = ("</displayElements>"
				"<_-RVProTransitionObject-_transitionObject transitionType=\"-1\" transitionDuration=\"1\" motionEnabled=\"0\" motionDuration=\"20\" motionSpeed=\"100\"></_-RVProTransitionObject-_transitionObject>"
					"</RVDisplaySlide>")
  
end_document = (	"</slides>"
				"</RVSlideGrouping>"
			"</groups>"
		"<arrangements containerClass=\"NSMutableArray\"></arrangements>"
	"</RVPresentationDocument>")

rtflinestart = ("{\\rtf1\\ansi\\ansicpg1252\\cocoartf1265"
    "\\cocoascreenfonts1{\\fonttbl\\f0\\fswiss\\fcharset0 Helvetica;}"
    "{\\colortbl;\\red255\\green255\\blue255;}"
    "\\pard\\tx560\\tx1120\\tx1680\\tx2240\\tx2800\\tx3360\\tx3920\\tx4480\\tx5040\\tx5600\\tx6160\\tx6720\\pardirnatural\\qc"
    "\\f0\\fs104\\cf1")

def index():
    return dict(message="Hello from MyApp")

def songform():
    if request.vars.title:
        session.title = request.vars.title
        session.author = request.vars.author
        session.lyrics = request.vars.lyrics
        redirect(URL('songfile'))
    return dict()
	
def songfile():
	return dict(message="O arquivo est� sendo gerado...")
	
def generate():
    response.headers['Content-Type'] = 'text/xml'
    attachment = 'attachment;filename=' + session.title.strip() + '.pro5'
    response.headers['Content-Disposition'] = attachment
    lines = formatlyrics(maketitledata(session.title, session.author), session.lyrics)
    content = start_document + lines + end_document
    raise HTTP(200,str(content),
               **{'Content-Type':'text/xml',
                  'Content-Disposition':attachment + ';'})

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

def formatlyrics( title, text ):
    lines = text.splitlines()
    str_lines = filter(None,lines)
    count = 0
    sort_index = 0
    result = ""
    while (count < (len(str_lines) - 1)):
        result = result + start_slide_part1 + str(sort_index) + start_slide_part2 + str(sort_index) + start_slide_part3
        sort_index = sort_index + 1
        if (count == 0): 
            result = result + title_part1 + title + title_part2 + line_part1 + formatlines(str_lines[count], str_lines[count+1]) + line_part2
        else:
            result = result + line_part1 + formatlines(str_lines[count], str_lines[count+1]) + line_part2
        result = result + end_slide
        count = count + 2
    if ((len(str_lines) % 2) == 1):
        result = result + start_slide_part1 + str(sort_index) + start_slide_part2 + str(sort_index) + start_slide_part3
        count = len(str_lines) - 1
        result = result + line_part1 + formatline(str_lines[count]) + line_part2
        result = result + end_slide
    return result

def formatlines( line1, line2 ):
    return base64.b64encode(rtflinestart + formatunicode(line1) + "\\\r\n" + formatunicode(line2) + "}")

def formatline ( line1 ):
    return base64.b64encode(rtflinestart + formatunicode(line1) + "}")

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
