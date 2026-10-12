"""
API route controllers.
"""
from modules.db import get_user, list_users

# TODO: Add rate limiting middleware
# FIXME: Security vulnerability - sanitize user input in search

def get_users_route(request):
    """GET /api/v1/users"""
    query = request.args.get("q", "")
    return list_users(search=query)

def get_user_by_id(user_id: int):
    """GET /api/v1/users/{id}"""
    user = get_user(user_id)
    if not user:
        return {"error": "User not found"}, 404
    return user, 200

# TODO: Implement user creation POST /api/v1/users
