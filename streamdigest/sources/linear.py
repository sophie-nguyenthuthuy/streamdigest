"""Linear source stub.

Plan: Linear exposes a GraphQL API at https://api.linear.app/graphql.
Poll `notifications` with pagination cursor. Incremental on updatedAt.
Canonical row shape:
  {id, title=issue.title, body=issue.description,
   reason=notification.type (e.g. "issueAssignedToYou"),
   repo_full_name=team.key, subject_type="Issue", updated_at}

Requires LINEAR_API_KEY (personal API key).
"""

from __future__ import annotations


def linear_source(*_args, **_kwargs):
    raise NotImplementedError(
        "Linear source is a stub. See module docstring for the implementation plan."
    )
