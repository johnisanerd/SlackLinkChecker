# SlackLinkChecker

Send regular updates about crawl status of our website and where there are broken links.

## Setup
1. Run install.sh
2. [Create a slack token for app authorization. ](https://get.slack.help/hc/en-us/articles/215770388-Create-and-regenerate-API-tokens)
3. Set the environmental variable for SLACK_API_TOKEN.  You can add this to ~/.profile with the line `export SLACK_API_TOKEN=YOURVARIABLEHERE`

Todo:
* [x] Add install for [wummel/linkchecker](https://github.com/wummel/linkchecker)
* [x] Add instalcurl -F file=@test.csv -F ti/api/files.uploadontent="Hello" -F channels=#website-broken-links -F token=$SLACK_API_TOKEN https://slack.com/
l for [slackapi/python-slackclient](https://github.com/slackapi/python-slackclient)
* [ ] For Upload use the command `curl -F file=@test.csv -F title="Hello!" -F content="Hello" -F channels=#website-broken-links -F token=$SLACK_API_TOKEN https://slack.com/api/files.upload `  [Source](https://api.slack.com/methods/files.upload)
