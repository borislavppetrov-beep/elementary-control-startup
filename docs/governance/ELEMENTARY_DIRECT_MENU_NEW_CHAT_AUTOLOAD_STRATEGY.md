# ELEMENTARY Direct Menu New Chat Autoload Strategy

## Problem

A user can start a new ChatGPT conversation directly from the application menu. That route may bypass an ELEMENTARY controlled chat launcher, transfer package, rollover package or browser-dispatched work item.

The repository can define mandatory startup context, but repository files alone cannot force an arbitrary platform-created new chat to read those files unless one of the enforcement layers below is active.

## Required outcome

Every new ELEMENTARY chat must load the startup bundle before capability claims, runtime-version claims, repeated-problem diagnoses or execution decisions:

```text
contracts/governance/chat-startup-context-bundle-v1.json
```

## Enforcement layers

### Layer 1 — Platform / Project / Custom GPT instructions

This is the only durable zero-click enforcement path for a direct menu-created chat.

The ChatGPT Project, Custom GPT / Gizmo or workspace-level instruction must include a startup rule equivalent to:

```text
At the start of every ELEMENTARY chat, first read contracts/governance/chat-startup-context-bundle-v1.json from borislavppetrov-beep/elementary-construction-os, then read all files in its read_order. Confirm the required startup attestation fields before making capability claims, runtime-version claims, repeated-problem diagnoses or execution decisions. If repository access is unavailable, state that startup context cannot be verified and ask for the transfer package or repository access.
```

Limit: the repository cannot edit ChatGPT platform instructions by itself. This layer must be installed through the platform/project configuration surface if available.

### Layer 2 — Browser auto-bootstrap watcher

For browser sessions controlled by ELEMENTARY, the Windows browser adapter can detect a newly opened ChatGPT conversation and inject a startup message automatically.

Target behavior:

```text
new ChatGPT composer detected
conversation has no user messages
ELEMENTARY project/chat context detected or forced by launcher
inject startup prompt
wait for attestation
continue work only after startup context is loaded
```

Safety boundary:

```text
no credential extraction
no cookie reads
no browser profile dump
no hidden arbitrary prompt mutation outside ELEMENTARY scope
no execution if user is composing unrelated personal chat
```

This layer can reduce manual mistakes, but it depends on the controlled browser adapter being active and authorized. It is not a universal platform-level guarantee.

### Layer 3 — Governed controlled-chat launcher

All ELEMENTARY-created chats should be opened through the controlled launcher instead of the generic menu when operational continuity matters.

The launcher must create the chat and submit the startup bootstrap message as the first message. This is the most reliable governed route for agent work, specialist work and rollover packages.

### Layer 4 — Transfer package hard gate

Every transfer/rollover/resume package must include the startup instruction for the next chat.

A package is invalid if it omits:

```text
Before continuing work, read contracts/governance/chat-startup-context-bundle-v1.json and then read all files in its read_order. Confirm the required startup attestation fields before capability claims, runtime-version claims, repeated-problem diagnoses or execution.
```

This does not catch direct menu-created chats with no package, so it is a gate, not a full direct-menu solution.

## Decision

Use all layers:

1. Install Layer 1 text into Project/Gizmo/workspace startup instructions where platform access allows.
2. Implement Layer 2 as a bounded browser adapter capability for ChatGPT web sessions.
3. Keep Layer 3 as the required route for governed agent work.
4. Keep Layer 4 as mandatory for every transfer/resume package.

## Canonical limitation

A direct menu-created chat cannot be guaranteed to read repository files automatically unless a platform instruction, browser watcher or controlled launcher is active before the chat starts.

Future agents must not claim that the repository alone enforces direct-menu autoload. They must identify which layer is active and provide evidence.
