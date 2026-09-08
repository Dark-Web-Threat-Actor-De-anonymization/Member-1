from app.database import get_connection
from psycopg2.extras import RealDictCursor
from typing import Optional, Any, List, Dict

def fetch_all(query: str, params: Optional[tuple]=None) -> List[Dict[str, Any]]:
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, params)
            rows = cur.fetchall()
            return [dict(r) for r in rows]
    finally:
        conn.close()

def fetch_one(query: str, params: Optional[tuple]=None) -> Optional[Dict[str, Any]]:
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, params)
            row = cur.fetchone()
            return dict(row) if row else None
    finally:
        conn.close()

def execute_query(query: str, params: Optional[tuple]=None) -> None:
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
        conn.commit()
    finally:
        conn.close()

def fetch_all_with_values(query: str, params: Optional[tuple]=None) -> List[Dict[str, Any]]:
    """
    Executes a query that RETURNS rows (e.g. INSERT ... RETURNING *) and returns them.
    Commits transaction on success.
    """
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, params)
            try:
                rows = cur.fetchall()
                conn.commit()
                return [dict(r) for r in rows]
            except Exception:
                # Query returned no rows
                conn.commit()
                return []
    finally:
        conn.close()
