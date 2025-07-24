import browser_cookie3
from instaloader import Instaloader, Profile

def login_with_browser_cookies():
    # Try loading cookies from any available browser
    cookies = browser_cookie3.load(domain_name='instagram.com')
    L = Instaloader()
    L.context._session.cookies.update(cookies)
    L.save_session_to_file()
    return L

L = login_with_browser_cookies()
profile = Profile.from_username(L.context, 'manishaa__official')

for post in profile.get_posts():
    L.download_post(post, target='manishaa__official')