# Global Storage Census and Controlled Disposition Runbook V1

## 1. Admission

1. Load the startup bundle and activate `CLOUD_STORAGE_AND_INFORMATION_GOVERNANCE`.
2. Bind the run to an exact GitHub `main` SHA and governed work item.
3. Record adapters, allowlisted roots and excluded classes.
4. Start in `READ_ONLY_CENSUS`.

## 2. Census

Each source emits JSONL records conforming to `elementary.global-storage-inventory.entry.v1`.

Source states:

- `COMPLETE`: admitted roots and pagination exhausted;
- `PARTIAL`: some roots, pages or metadata unavailable;
- `BLOCKED`: access or provider capability unavailable;
- `NOT_ADMITTED`: intentionally outside the approved run.

Non-complete states are never represented as zero objects.

## 3. Classification

Classification is evidence-based. Exact duplicate status requires equal SHA-256 or equivalent provider-native immutable identity and size evidence. Exports, versions, backups and transfer copies remain separate classes.

## 4. Controlled disposition

Any move, quarantine or final removal requires an exact manifest batch, canonical-copy verification, retention and legal review, dependency review, independent verification, owner approval and recovery evidence. Final removal requires a separate approval after the review window.

## 5. Runtime protections

Protect current and previous verified releases, active backups, mutable runtime data, active worktrees and runner workspaces, Node identity, and files referenced by active services or scheduled execution.

## 6. Acceptance

A run is complete only when every scoped source is `COMPLETE` or has an exact blocker, every proposed action has evidence, and the final rescan reconciles object counts and identities.
