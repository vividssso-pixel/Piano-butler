/**
 * Piano Butler — Auth Utility
 * ============================
 * auth.js  (no React required — pure JS utility)
 *
 * Provides:
 *   1. _supabase  — Supabase client (global)
 *   2. requireAuth()  — call on any protected page; redirects to login.html if no session
 *   3. signOut()      — signs out and redirects to login.html
 *
 * Usage in any protected HTML page:
 *   1. Load Supabase CDN script BEFORE this file
 *   2. Load this file
 *   3. In your page script, call: requireAuth();
 */

const SUPABASE_URL  = "https://icefqxaccclwasnfzgnp.supabase.co";
const SUPABASE_ANON = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImljZWZxeGFjY2Nsd2FzbmZ6Z25wIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcwNjgzMTgsImV4cCI6MjA5MjY0NDMxOH0.lZ8BO_L8iOtET8RtUuk9trkf9bQbLqR8K6rKEfPtmtQ";

const _supabase = supabase.createClient(SUPABASE_URL, SUPABASE_ANON);

/**
 * requireAuth()
 * Call at the top of any protected page script.
 * If no active session → redirects to login.html immediately.
 * Returns the session object if authenticated.
 */
async function requireAuth() {
  const { data: { session } } = await _supabase.auth.getSession();
  if (!session) {
    window.location.href = "login.html";
    return null;
  }
  return session;
}

/**
 * signOut()
 * Signs out the current user and redirects to login.html.
 */
async function signOut() {
  await _supabase.auth.signOut();
  window.location.href = "login.html";
}
