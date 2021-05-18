# https://devcenter.heroku.com/articles/ssl-endpoint
#
# As long as the notebook lives in the herokuapp.com domain,
# we have SSL certificates enabled for encryption purposes.
c.NotebookApp.ip = "*"
c.NotebookApp.open_browser = False
c.NotebookApp.password = 'argon2:$argon2id$v=19$m=10240,t=10,p=8$PFNzH66Tby2B0yCc84qvLA$rSHvdej3iRnL1x/WurT0cQ'
