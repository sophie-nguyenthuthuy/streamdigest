"""Slack source stub.

Plan: use slack_sdk WebClient.conversations_history / conversations_replies.
Incremental on `ts` per channel. Canonical output shape matches GitHub:
  {id=ts, title=first-line-of-text, body=full text (+ threaded replies joined),
   reason="mention"|"channel_post"|"dm", repo_full_name=channel_name,
   subject_type="SlackMessage", updated_at}

Requires SLACK_BOT_TOKEN with channels:history, groups:history, im:history, mpim:history.
"""

from __future__ import annotations


def slack_source(*_args, **_kwargs):
    raise NotImplementedError(
        "Slack source is a stub. See module docstring for the implementation plan."
    )
