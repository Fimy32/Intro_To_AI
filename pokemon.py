import requests
import time
import json
from typing import Dict, Any, List, Optional

BASE = "https://pokeapi.co/api/v2"

def get_json(url: str) -> Optional[Dict[str, Any]]:
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.json()
        else:
            print("Warning: non-200 status", resp.status_code, url)
            return None
    except Exception as e:
        print("Exception in get_json:", e, url)
        return None

def fetch_pokemon_list(limit: int = 2000) -> List[Dict[str, Any]]:
    url = f"{BASE}/pokemon?limit={limit}"
    j = get_json(url)
    if not j:
        return []
    return j.get("results", [])

def simplify_species_data(species_json: Dict[str, Any]) -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    c = species_json.get("color")
    out["color"] = c.get("name") if c else None
    sh = species_json.get("shape")
    out["shape"] = sh.get("name") if sh else None
    gen = species_json.get("generation")
    out["generation"] = gen.get("name") if gen else None
    out["is_legendary"] = species_json.get("is_legendary", False)
    out["is_mythical"] = species_json.get("is_mythical", False)
    return out

def fetch_pokemon_data(poke_entry: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    name = poke_entry.get("name")
    url = poke_entry.get("url")
    if not url or not name:
        return None
    pj = get_json(url)
    if pj is None:
        return None

    species_url = pj.get("species", {}).get("url")
    species_json = get_json(species_url) if species_url else None

    rec: Dict[str, Any] = {}
    rec["name"] = name
    types = []
    for t in pj.get("types", []):
        tname = t.get("type", {}).get("name")
        if tname:
            types.append(tname)
    rec["types"] = types

    rec["height"] = pj.get("height")
    rec["weight"] = pj.get("weight")

    stats = {}
    for st in pj.get("stats", []):
        stat_name = st.get("stat", {}).get("name")
        base = st.get("base_stat")
        if stat_name:
            stats[stat_name] = base
    rec["base_stats"] = stats

    if species_json:
        sp = simplify_species_data(species_json)
        rec.update(sp)
    else:
        rec["color"] = None
        rec["shape"] = None
        rec["generation"] = None
        rec["is_legendary"] = False
        rec["is_mythical"] = False

    return rec

def build_full_pokemon_json(out_path: str = "pokemon_full.json"):
    pokes = fetch_pokemon_list(limit=2000)
    print(f"Fetched list of Pokémon, total count: {len(pokes)}")
    results = []
    count = 0
    for p in pokes:
        rec = fetch_pokemon_data(p)
        if rec:
            results.append(rec)
            print(json.dumps(rec, indent=2))  # Print each Pokémon data to console
        count += 1
        if count % 50 == 0:
            print(f"Fetched {count} entries so far...")
        time.sleep(0.2)  # Be polite with API requests
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(results)} Pokémon entries to {out_path}")

if __name__ == "__main__":
    build_full_pokemon_json()