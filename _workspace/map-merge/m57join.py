s = open('login.html').read()
head = s[:s.index('</style>') + len('</style>')]
head = head.replace('<title>Piano Butler — Teacher sign in</title>', '<title>Piano Butler — Join</title>')
url = s[s.index('const SUPABASE_URL  = "') + len('const SUPABASE_URL  = "'):]; url = url[:url.index('"')]
anon = s[s.index('const SUPABASE_ANON = "') + len('const SUPABASE_ANON = "'):]; anon = anon[:anon.index('"')]
body = '''
  <style>
    .choice { display:block; width:100%; text-align:left; padding:14px 16px; margin-bottom:10px; border-radius:14px; border:1.5px solid var(--navy-line); background:#fff; cursor:pointer; font-family:inherit; color:var(--navy); }
    .choice b { display:block; font-size:16px; }
    .choice span { display:block; font-size:13px; color:var(--muted); margin-top:3px; line-height:1.4; }
    .choice.on { border-color:var(--navy); box-shadow:0 0 0 2px var(--navy) inset; }
    .gift { font-size:13px; color:var(--muted); line-height:1.5; margin:0 0 16px; }
    .gift b { color:var(--good); }
  </style>
</head>
<body>
  <div class="card">
    <div class="header">
      <svg width="56" height="34" viewBox="0 0 32 32" aria-hidden="true"><path d="M3 6 L16 16 L3 26 Z" fill="none" stroke="#26296b" stroke-width="2.4" stroke-linejoin="round"/><path d="M29 6 L16 16 L29 26 Z" fill="none" stroke="#26296b" stroke-width="2.4" stroke-linejoin="round"/><circle cx="16" cy="16" r="2.6" fill="#e4572e"/></svg>
      <h1>Piano Butler</h1>
      <p>Join for free</p>
    </div>
    <div class="staff"></div>
    <div class="body">
      <div id="step1">
        <button class="choice" id="c-teacher" type="button"><b>I have a piano teacher</b><span>Your teacher sends you your own link. Open it and everything is ready.</span></button>
        <button class="choice" id="c-own" type="button"><b>I'm learning on my own</b><span>Your butler plans each week, keeps your practice record and shows you what comes next.</span></button>
        <div id="teacher-note" class="ok-box" style="display:none">Ask your teacher for your student link. Nothing else to do here.</div>
      </div>
      <form id="own" style="display:none" autocomplete="on">
        <p class="gift">Free with an account: <b>Level 0 and Level ½, every room</b>, your practice record and your cards.</p>
        <label for="name">Your first name</label>
        <input id="name" name="given-name" autocomplete="given-name" placeholder="e.g. Clara" required>
        <label for="email">Email</label>
        <input id="email" type="email" name="email" autocomplete="email" placeholder="you@example.com" required>
        <div id="err" class="error-box" style="display:none"></div>
        <div id="ok" class="ok-box" style="display:none"></div>
        <button class="submit-btn" id="go" type="submit">Email me a sign-in link</button>
        <p class="footer-note">No password. The link signs you in on this device.</p>
      </form>
      <div id="already" class="ok-box" style="display:none"></div>
    </div>
  </div>
  <script>
    const SUPABASE_URL  = "''' + url + '''";
    const SUPABASE_ANON = "''' + anon + '''";
    const _supabase = supabase.createClient(SUPABASE_URL, SUPABASE_ANON);
    const $ = (id) => document.getElementById(id);
    const drills = window.location.origin + window.location.pathname.replace(/[^/]*$/, "") + "drills.html?teacher=0&view=today";
    _supabase.auth.getSession().then(({ data }) => {
      const u = data && data.session && data.session.user;
      if (u && u.user_metadata && u.user_metadata.role === "learner") { $("already").style.display = "block"; $("already").innerHTML = 'You are signed in. <a href="' + drills + '">Go to your practice ›</a>'; $("step1").style.display = "none"; }
    });
    $("c-teacher").onclick = () => { $("c-teacher").classList.add("on"); $("c-own").classList.remove("on"); $("teacher-note").style.display = "block"; $("own").style.display = "none"; };
    $("c-own").onclick = () => { $("c-own").classList.add("on"); $("c-teacher").classList.remove("on"); $("teacher-note").style.display = "none"; $("own").style.display = "block"; $("name").focus(); };
    $("own").onsubmit = async (e) => {
      e.preventDefault(); $("err").style.display = "none"; $("ok").style.display = "none";
      const email = $("email").value.trim(), name = $("name").value.trim().slice(0, 40);
      if (!email || !name) return;
      $("go").disabled = true; $("go").textContent = "Sending…";
      const { error } = await _supabase.auth.signInWithOtp({ email, options: { shouldCreateUser: true, data: { role: "learner", name }, emailRedirectTo: drills } });
      $("go").disabled = false; $("go").textContent = "Email me a sign-in link";
      if (error) { $("err").textContent = "Couldn't send the link: " + error.message; $("err").style.display = "block"; return; }
      $("ok").textContent = "Check your email for the link, then open it on this device."; $("ok").style.display = "block";
    };
  </script>
</body>
</html>
'''
open('join.html', 'w').write(head + body)
# the dashboard is for teachers: a learner's session goes to their practice instead
a = open('auth.js').read()
if 'role === "learner"' not in a:
    a = a.replace('''  if (!session) {
    window.location.href = "login.html";
    return null;
  }
  return session;''', '''  if (!session) {
    window.location.href = "login.html";
    return null;
  }
  // m57: a learner (signed up on join.html) has no dashboard: their practice is in the drills
  if (session.user && session.user.user_metadata && session.user.user_metadata.role === "learner") {
    window.location.href = "drills.html?teacher=0&view=today";
    return null;
  }
  return session;''')
    open('auth.js', 'w').write(a)
print('ok')
