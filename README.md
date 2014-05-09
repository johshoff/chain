Don't break the chain
---------------------

A productivity tip by Jerry Seinfeld: Don't break the chain. Mark off your calendar
every day you do something like writing a sitcom or programming, and you might end
up getting stuff done.

This is the calendar.

To get data from a hg repository:

	hg log --user <username> --template '{date}\n'

And from a git repository:

	git log --author=<username> --pretty=format:%at

Then manually magnle it into json.
