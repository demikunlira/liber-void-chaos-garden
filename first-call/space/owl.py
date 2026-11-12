"""Mother Owl announce — envelope only, never contents. House law for every cloud crossing."""
def announce(kind: str, provider: str, size_bytes: int = 0) -> str:
    return f"🦉 Owl: a crossing. {kind} → {provider} ({size_bytes} bytes). Contents not logged."
