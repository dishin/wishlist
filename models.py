# -*- coding: utf-8 -*-
from mongoengine import *

from flask.ext.mongoengine.wtf import model_form
from datetime import datetime

# our demo model from week 5 in class
class Log(Document):
	text = StringField()
	timestamp = DateTimeField(default=datetime.now())

class Comment(EmbeddedDocument):
	name = StringField()
	comment = StringField()
	timestamp = DateTimeField(default=datetime.now())

class Idea(Document):

	creator = StringField(max_length=120, required=True, verbose_name="Your Name", help_text="Please enter your first name")
	title = StringField(max_length=120, required=True, verbose_name="Item Title")
	#title = StringField(max_length=120, required=True)
	slug = StringField()
	idea = StringField(required=True, verbose_name="Description")
	#image = StringField(required=True, verbose_name="item image")
	#idea = StringField(required=True, verbose_name="Description?")

	# Category is a list of Strings
	categories = ListField(StringField(max_length=30))

	# Images
	#images = ListField(StringField)

	# Comments is a list of Document type 'Comments' defined above
	comments = ListField( EmbeddedDocumentField(Comment) )

	# Timestamp will record the date and time idea was created.
	timestamp = DateTimeField(default=datetime.now())

IdeaForm = model_form(Idea)

