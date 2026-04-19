"""Gmail source stub.

Plan: IMAP via `imap-tools` or dlt's verified `inbox` source. Reason for
leaving as a stub here: the primary source (GitHub) is sufficient to prove
the pipeline end-to-end and has simpler auth (PAT vs. OAuth/app-password).

To implement:
  1. pip install imap-tools
  2. Use IDLE or since-UID incremental cursor keyed on Message-ID
  3. Yield rows with a canonical shape: {id, title, body, reason, repo_full_name=None,
     subject_type="Email", updated_at}
  4. Add GMAIL_* env vars to config.Settings and wire into the Prefect flow
     behind a `--source gmail` CLI flag.
"""

from __future__ import annotations


def gmail_source(*_args, **_kwargs):
    raise NotImplementedError(
        "Gmail source is a stub. See module docstring for the implementation plan."
    )
