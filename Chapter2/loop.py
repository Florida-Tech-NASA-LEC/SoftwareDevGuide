subteams = ["excavation", "software", "structures"]

for team in subteams:
	if "software" in team:
		print team + " is VERY cool!"
	elif "excavation" in team:
		print team + " is SUPER cool!"
	else:
		print team + " is UBER cool!"
