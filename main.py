import argparse
from instagram_private_api import __version__, Client


def get_following():
    user_following = []
    next_max_id = ""
    while next_max_id is not None:
        results = api.user_following(
            user_id=api.authenticated_user_id,
            rank_token=api.generate_uuid(),
            max_id=next_max_id
        )
        user_following = user_following + [u['username'] for u in results['users']]
        next_max_id = results.get("next_max_id")
    return user_following


def get_followers():
    user_followers = []
    next_max_id = ""
    while next_max_id is not None:
        results = api.user_followers(
            user_id=api.authenticated_user_id,
            rank_token=api.generate_uuid(),
            max_id=next_max_id
        )
        user_followers = user_followers + [u['username'] for u in results['users']]
        next_max_id = results.get("next_max_id")
    return user_followers


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Unfollow your unfollowers')
    parser.add_argument('-u', '--username', dest='username', type=str, required=True)
    parser.add_argument('-p', '--password', dest='password', type=str, required=True)

    args = parser.parse_args()

    print('Client version: {0!s}'.format(__version__))
    api = Client(args.username, args.password)

    i = 0
    for username in [value for value in get_following() if value not in get_followers()]:
        i += 1
        print("{}) https://www.instagram.com/{}/".format(i, username))
