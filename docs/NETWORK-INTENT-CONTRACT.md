# Network intent contract — public Godot clients

This document defines the public client-side intent boundary shared by the Godot Classic and Godot VR starters.

## Proof scope

`net/intent_contract.gd` is **transport-independent client validation only**.

It does not:
- open a socket;
- encode the private canonical Zig wire protocol;
- prove authentication, shard handoff or reconnect;
- prove server-side authorization;
- prove compatibility with any `zig-server-v2` revision.

Current proof status remains `NOT_PROVEN` for live Zig interoperability.

## Allowed base intent families

- `session`: `hello`, `authenticate`, `resume` envelope only;
- `move`: normalized client movement intent only;
- `interact`: bounded target identifier;
- `talk`: bounded text plus optional target identifier.

The server remains authoritative over resulting movement, interaction outcome, dialogue/gameplay effects and session validity.

## Forbidden client authority

The public client contract rejects authority-like fields including damage/healing, currency/gold, inventory/item grants, permissions/roles, teleport, server position and quest rewards.

This list is defense-in-depth, not a substitute for Zig validation. The server must independently reject unauthorized fields/actions.

## Promotion rule

A future transport adapter may consume the sanitized intent returned by this contract. It must remain a separate layer. No transport implementation may change `zig_compatibility` or proof level to true until the exact private server baseline and real E2E evidence are recorded.

## Licensing boundary

This public contract is MIT with the starter. Private Zig framing, auth internals, gameplay implementation and production configuration remain proprietary/commercial, all rights reserved unless explicitly licensed otherwise.
