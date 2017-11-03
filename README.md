# SlackLinkChecker

Send regular updates about crawl status of our website and where there are broken links.

## Setup
1. Run install.sh
2. [Create a slack token for app authorization. ](https://get.slack.help/hc/en-us/articles/215770388-Create-and-regenerate-API-tokens)
3. Set the environmental variable for SLACK_API_TOKEN.  You can add this to ~/.profile with the line `export SLACK_API_TOKEN=YOURVARIABLEHERE`

Todo:
* [x] Add install for [wummel/linkchecker](https://github.com/wummel/linkchecker)
* [x] Add install for [slackapi/python-slackclient](https://github.com/slackapi/python-slackclient)
* [ ] Change course from python-slackclient to [slacker](https://github.com/os/slacker) so you can upload csv files?  Or do we want to make a URL with NGROK and a webpage of the results?
