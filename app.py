#!/usr/bin/env python3
import argparse
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class ChecklistItem:
    category: str
    description: str
    priority: str  # low, medium, high


@dataclass
class Track:
    key: str
    name: str
    summary: str
    items: List[ChecklistItem]


def make_tracks() -> Dict[str, Track]:
    return {
        "aztec": Track(
            key="aztec",
            name="Aztec-style zk L2",
            summary=(
                "Checklist for a privacy-preserving zkRollup inspired by projects like Aztec. "
                "Focuses on encrypted state, proving systems, and secure integration with L1."
            ),
            items=[
                ChecklistItem("Protocol design", "Define which parts of state are encrypted vs public.", "high"),
                ChecklistItem("ZK system", "Select a proving system and circuit language for L2 logic.", "high"),
                ChecklistItem("Bridging", "Specify how L1 and L2 balances are synchronized and verified.", "high"),
                ChecklistItem("Privacy UX", "Design flows for managing viewing keys and private balances.", "medium"),
                ChecklistItem("Gas and costs", "Estimate proof generation cost and impact on fees.", "medium"),
                ChecklistItem("Audits", "Plan audits for circuits, contracts, and trusted setup, if any.", "high"),
            ],
        ),
        "zama": Track(
            key="zama",
            name="Zama-style FHE application",
            summary=(
                "Checklist for a Web3 or crypto system using fully homomorphic encryption, "
                "inspired by ecosystems like Zama."
            ),
            items=[
                ChecklistItem("Data model", "Define which fields must remain encrypted end-to-end.", "high"),
                ChecklistItem("FHE scheme", "Choose the FHE scheme and libraries suited for your workloads.", "high"),
                ChecklistItem("Performance", "Benchmark ciphertext sizes and computation latency.", "high"),
                ChecklistItem("Key management", "Design key generation, rotation, and recovery procedures.", "high"),
                ChecklistItem("Interoperability", "Specify how FHE outputs interact with on-chain logic.", "medium"),
                ChecklistItem("Security review", "Document threat model for ciphertext leakage and misuse.", "high"),
            ],
        ),
        "soundness": Track(
            key="soundness",
            name="Soundness-focused research lab",
            summary=(
                "Checklist for a team that prioritizes formal soundness, proofs, and rigorous verification "
                "of cryptographic protocols."
            ),
            items=[
                ChecklistItem("Specifications", "Maintain executable, unambiguous protocol specifications.", "high"),
                ChecklistItem("Proof strategy", "Select proof techniques and tools for main security properties.", "high"),
                ChecklistItem("Modeling", "Model protocols in a formal framework or proof assistant.", "high"),
                ChecklistItem("Review process", "Define a process for proof and spec reviews before implementation.", "medium"),
                ChecklistItem("Implementation alignment", "Continuously check that code matches the specification.", "high"),
                ChecklistItem("Knowledge sharing", "Document assumptions, invariants, and common pitfalls.", "medium"),
            ],
        ),
    }


def format_checklist(track: Track, compact: bool = False) -> str:
    lines: List[str] = []
    lines.append(f"Track: {track.name}")
    lines.append("")
    lines.append("Summary:")
    lines.append(f"  {track.summary}")
    lines.append("")
    lines.append("Checklist:")

    for i, item in enumerate(track.items, start=1):
        if compact:
            lines.append(f"{i}. [{item.priority}] {item.category} - {item.description}")
        else:
            lines.append(f"{i}. Category: {item.category}")
            lines.append(f"   Priority: {item.priority}")
            lines.append(f"   Task: {item.description}")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def list_tracks(tracks: Dict[str, Track]) -> str:
    lines = []
    lines.append("Available tracks related to Web3 privacy and soundness:")
    for key, track in tracks.items():
        lines.append(f"- {key}: {track.name}")
    lines.append("")
    lines.append("Use --track with one of the keys above to print a detailed checklist.")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="web3_privacy_roadmap",
        description=(
            "Generate a design checklist for different Web3 privacy and soundness tracks "
            "inspired by ecosystems like Aztec, Zama, and research labs focused on protocol soundness."
        ),
    )
    parser.add_argument(
        "--track",
        type=str,
        help="Which track to print (aztec, zama, soundness).",
    )
    parser.add_argument(
        "--compact",
        action="store_true",
        help="Print checklist in a compact one-line-per-item format.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all available tracks.",
    )
    args = parser.parse_args()

    tracks = make_tracks()

    if args.list:
        print(list_tracks(tracks))
        return

    if not args.track:
        print("web3_privacy_roadmap - design checklist generator")
        print("")
        print(list_tracks(tracks))
        print("Examples:")
        print("  python app.py --track aztec")
        print("  python app.py --track zama --compact")
        return

    key = args.track.lower()
    if key not in tracks:
        print("Unknown track key.")
        print("")
        print(list_tracks(tracks))
        return

    track = tracks[key]
    print(format_checklist(track, compact=args.compact))


if __name__ == "__main__":
    main()
