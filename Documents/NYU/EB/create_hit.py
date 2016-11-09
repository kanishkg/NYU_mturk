import boto.mturk.connection
sandbox_host = 'mechanicalturk.sandbox.amazonaws.com'
real_host = 'mechanicalturk.amazonaws.com'
url = "https://django-env.hgryvtimgy.us-west-2.elasticbeanstalk.com/"
title = "Video Similarity"
description = "Rate if the two videos are similar"
keywords = ["video","similarity","survey"]
frame_height = 600
amount = .8
num_tasks = 100
questionform = boto.mturk.question.ExternalQuestion( url, frame_height )
mturk = boto.mturk.connection.MTurkConnection(
		aws_access_key_id = 'AKIAJ7EDZM5JP4XWF7EQ',
		aws_secret_access_key = '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',
		host = sandbox_host,
		debug = 1 # debug = 2 prints out all requests.
		)
  
create_hit_result = mturk.create_hit(
	title = 'vidsim3', max_assignments = 10,
	description = description,
	keywords = keywords,
	question = questionform,
	reward = boto.mturk.price.Price( amount = amount),
	response_groups = ( 'Minimal', 'HITDetail' ), # I don't know what response groups are
	)

