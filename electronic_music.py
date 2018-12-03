import os
import time
from tempfile import gettempdir

from selenium.common.exceptions import NoSuchElementException

from instapy import InstaPy

insta_username = 'Username'
insta_password = 'Password'

# set headless_browser=True if you want to run InstaPy on a server

# set these in instapy/settings.py if you're locating the
# library in the /usr/lib/pythonX.X/ directory:
#   Settings.database_location = '/path/to/instapy.db'
#   Settings.chromedriver_location = '/path/to/chromedriver'

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)

try:
    session.login()

    # settings
    session.set_relationship_bounds(enabled=True,
				 potency_ratio=-0.3,
				  delimit_by_numbers=True,
				   max_followers=200000,
				    max_following=10000,
				     min_followers=50,
				      min_following=0)
    session.set_do_comment(False, percentage=10)
    session.set_comments([':)', 'xoxo', 'nice'])
    session.set_do_follow(enabled=True, percentage=20, times=1)
    session.unfollow_users(amount=25, InstapyFollowed=(True, "all"), style="FIFO", unfollow_after=4*24*60*60, sleep_delay=501)
    session.set_dont_like([])

    # actions
    session.like_by_tags([
'musik',
'music',
'housemusic',
'dancemusic',
'edm', 
'electronicmusic',
'instamusic', 
'instalove', 
'nowplaying',
'katermukke',
'engtanz',
'festivallife',
'marteria',
'melodictechno',
'smsfestival',
'feelfestival',
'helenebeachfestival',
'airbeatone',
'lollapalooza',
'sputnikspringbreak',
'natureone',
'parookaville',
'fusionfestival',
'worldclubdome'
], amount= 20)

except Exception as exc:
    # if changes to IG layout, upload the file to help us locate the change
    if isinstance(exc, NoSuchElementException):
        file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
        with open(file_path, 'wb') as fp:
            fp.write(session.browser.page_source.encode('utf8'))
        print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
            '*' * 70, file_path))
    # full stacktrace when raising Github issue
    raise

finally:
    # end the bot session
    session.end()

