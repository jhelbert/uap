import urllib2
import json
import time




since = 300
all_users = {}
max_repos = 0
while since < 10000:
	response = urllib2.urlopen(' https://api.github.com/repositories?since=%s&access_token=4c2dff998dc5fd9bb79c113542646c885228b819' % since) #&access_token=4c2dff998dc5fd9bb79c113542646c885228b819

	repos = json.loads(response.read())


	for repo in repos:

		repo_url = repo['url']
		succeeded = False
		while not succeeded:
			try:
				#TODO: fix repo that keeps erring out
				contrib_response = urllib2.urlopen(repo_url + "/contributors?access_token=4c2dff998dc5fd9bb79c113542646c885228b819") #&access_token=4c2dff998dc5fd9bb79c113542646c885228b819
				succeeded = True
			except:
				time.sleep(15)
				print "rate limit..."

		contributors = json.loads(contrib_response.read())
		contributor_names = [contributor['login'] for contributor in contributors]
		print "%s\t\t%s\t\tusers:%s" % (repos.index(repo), repo['full_name'], len(contributor_names))
		if len(contributor_names) < 100:
			for i1 in range(len(contributor_names)):
				c1 = contributor_names[i1]
				for i2 in range(i1 + 1,len(contributor_names)):
					c2 = contributor_names[i2]

					if not all_users.get(c1):
						all_users[c1] = {}
					if not all_users.get(c2):
						all_users[c2] = {}

					if not all_users[c1].get(c2):
						all_users[c1][c2] = 0
					if not all_users[c2].get(c1):
						all_users[c2][c1] = 0

					all_users[c1][c2] += 1

					all_users[c2][c1] += 1

					if all_users[c1][c2] > max_repos:
						max_repos = all_users[c1][c2]
						print "new max repos:%s" % max_repos




	open('github_data.txt', 'w').close()
	f = open('github_data.txt','w')
	since += 100
	f.write("since:%s\n\n" % since)
	f.write(json.dumps(all_users))


	print "num_users:%s" % len(all_users)








