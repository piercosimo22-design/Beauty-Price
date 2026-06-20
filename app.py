import streamlit as st
import hashlib

# ============================================================
#  🔧 STEP 1 — INSERISCI QUI I TUOI ID AFFILIATO
#  (dopo aver ottenuto l'approvazione da Awin e Amazon)
# ============================================================
ID_AWIN   = ""   # ← Il tuo Publisher ID Awin  (es: "123456")
ID_AMAZON = ""   # ← Il tuo Tracking ID Amazon (es: "beautybot-21")
# ============================================================

st.set_page_config(
    page_title="BeautyPriceBot 💄 – Confronta Prezzi Beauty",
    page_icon="💄",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────
#  CSS — DARK MODE PREMIUM
# ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
  --bg:          #08080B;
  --bg2:         #0F0F14;
  --bg3:         #141419;
  --card:        #111116;
  --card-h:      #17171E;
  --border:      #1C1C26;
  --fuchsia:     #FF3C96;
  --violet:      #A020F0;
  --neon:        #FF7EC8;
  --gold:        #F5C842;
  --green:       #00E5A0;
  --text:        #EEEEF5;
  --text2:       #9090A8;
  --text3:       #50506A;
  --r:           14px;
  --r-sm:        9px;
  --fd:          'Playfair Display', serif;
  --fb:          'DM Sans', sans-serif;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body,
[data-testid="stAppViewContainer"],
[data-testid="stApp"] {
  background: var(--bg) !important;
  color: var(--text);
  font-family: var(--fb);
}

[data-testid="stAppViewContainer"] {
  background:
    radial-gradient(ellipse 900px 500px at 60% -80px, rgba(160,32,240,.10) 0%, transparent 65%),
    radial-gradient(ellipse 500px 400px at -5%  60%,  rgba(255,60,150,.06) 0%, transparent 60%),
    var(--bg) !important;
}

[data-testid="stHeader"],
[data-testid="stToolbar"],
#MainMenu, footer { display: none !important; }

.block-container {
  max-width: 740px !important;
  padding: 0 1rem 4rem !important;
}
section.main > div { padding-top: 0 !important; }
div[data-testid="stVerticalBlock"] { gap: 0 !important; }
.element-container { margin-bottom: 0 !important; }
[data-testid="stMarkdownContainer"] p { margin: 0; }

/* ── TOPBAR ─────────────────────────────────── */
.topbar {
  display: flex; align-items: center; justify-content: space-between;
  padding: .7rem 1.2rem;
  background: rgba(8,8,11,.92);
  border-bottom: 1px solid var(--border);
  position: sticky; top: 0; z-index: 100;
  margin: 0 -1rem;
  backdrop-filter: blur(16px);
}
.tlogo {
  font-family: var(--fd); font-size: 1.15rem; font-weight: 900;
  background: linear-gradient(120deg, #FF3C96, #FF7EC8);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.tnav { display: flex; gap: .8rem; align-items: center; }
.tnav-link { font-size: .73rem; color: var(--text2); text-decoration: none; transition: color .18s; }
.tnav-link:hover { color: var(--neon); }
.tbadge {
  background: rgba(255,60,150,.12); border: 1px solid rgba(255,60,150,.28); color: var(--neon);
  font-size: .63rem; font-weight: 700; letter-spacing: .08em; text-transform: uppercase;
  padding: 3px 10px; border-radius: 100px;
}
/* ✅ FIX: bottone Accedi sempre visibile */
.login-btn {
  background: linear-gradient(130deg, #FF3C96, #A020F0);
  color: #ffffff !important;
  border: none; border-radius: 100px;
  padding: 5px 16px; font-family: var(--fb); font-weight: 700; font-size: .73rem;
  cursor: pointer; transition: all .18s;
  box-shadow: 0 2px 12px rgba(255,60,150,.35);
  display: inline-flex; align-items: center; gap: 5px;
}
.login-btn:hover { transform: translateY(-1px); box-shadow: 0 4px 18px rgba(255,60,150,.5); }
.user-pill {
  background: rgba(255,60,150,.15); border: 1px solid rgba(255,60,150,.35); color: var(--neon);
  font-size: .73rem; font-weight: 600; padding: 5px 14px; border-radius: 100px;
  display: inline-flex; align-items: center; gap: 5px;
}

/* ── BANNER PROMO ───────────────────────────── */
.banner {
  background: #1a0a22; border: 1px solid rgba(160,32,240,.3);
  border-radius: var(--r); padding: .65rem 1rem;
  display: flex; align-items: center; gap: .6rem;
  font-size: .76rem; color: var(--text2);
  position: relative; overflow: hidden; margin: .8rem 0;
}
.banner::before {
  content: ''; position: absolute; top: 0; left: -60%; width: 40%; height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,126,200,.08), transparent);
  animation: shimmer 3s infinite linear;
}
@keyframes shimmer { to { left: 140%; } }
.bdot {
  width: 7px; height: 7px; background: var(--green); border-radius: 50%;
  box-shadow: 0 0 7px var(--green); flex-shrink: 0;
  animation: bpulse 2s infinite;
}
@keyframes bpulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:.4;transform:scale(.65)} }
.banner b { color: var(--neon); }

/* ── TABS ───────────────────────────────────── */
div[data-baseweb="tab-list"] {
  background: var(--bg2) !important;
  border-bottom: 1px solid var(--border) !important;
  gap: 0 !important;
}
div[data-baseweb="tab"] {
  color: var(--text2) !important;
  font-family: var(--fb) !important;
  font-size: .8rem !important;
  font-weight: 500 !important;
  padding: .6rem 1.1rem !important;
}
div[aria-selected="true"] {
  color: var(--neon) !important;
  border-bottom: 2px solid var(--fuchsia) !important;
}
div[data-baseweb="tab-panel"] { padding-top: .8rem !important; }

/* ── HERO ───────────────────────────────────── */
.hero { text-align: center; padding: 2.2rem 1rem 1.4rem; }
.eyebrow {
  display: inline-flex; align-items: center; gap: .4rem;
  background: rgba(255,60,150,.1); border: 1px solid rgba(255,60,150,.25);
  color: var(--neon); font-size: .68rem; font-weight: 700;
  letter-spacing: .12em; text-transform: uppercase;
  padding: 4px 14px; border-radius: 100px; margin-bottom: .9rem;
}
.htitle {
  font-family: var(--fd); font-size: clamp(2rem,5vw,3.2rem); font-weight: 900;
  line-height: 1.05; letter-spacing: -.5px;
  background: linear-gradient(135deg, #fff 30%, var(--neon) 70%, var(--fuchsia) 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
  margin-bottom: .55rem;
}
.hsub {
  font-size: .92rem; color: var(--text2);
  max-width: 420px; margin: 0 auto; line-height: 1.65; font-weight: 300;
}
.hsub b { color: var(--text); font-weight: 600; }
.stats { display: flex; justify-content: center; gap: 2rem; margin-top: 1.2rem; }
.stat .n { font-family: var(--fd); font-size: 1.55rem; font-weight: 900; color: var(--fuchsia); line-height: 1; }
.stat .l { font-size: .65rem; color: var(--text3); text-transform: uppercase; letter-spacing: .06em; margin-top: 2px; }

/* ── DIVIDER ────────────────────────────────── */
.divider {
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--border), transparent);
  margin: 1rem 0;
}

/* ── SEARCH ─────────────────────────────────── */
.qlabel {
  font-size: .7rem; font-weight: 600; letter-spacing: .12em;
  text-transform: uppercase; color: var(--text3); margin-bottom: .45rem;
}
.qtags { display: flex; flex-wrap: wrap; gap: .35rem; margin-bottom: .9rem; }
.qtag {
  background: var(--bg3); border: 1px solid var(--border); color: var(--text2);
  font-size: .73rem; padding: 4px 12px; border-radius: 100px;
  cursor: pointer; transition: all .18s; user-select: none;
}
.qtag:hover { border-color: rgba(255,60,150,.3); color: var(--neon); background: rgba(255,60,150,.08); }

div[data-baseweb="input"] > div {
  background: var(--bg2) !important;
  border: 1.5px solid var(--border) !important;
  border-radius: var(--r) !important;
  transition: all .25s;
}
div[data-baseweb="input"] > div:focus-within {
  border-color: var(--fuchsia) !important;
  box-shadow: 0 0 0 3px rgba(255,60,150,.14) !important;
}
div[data-baseweb="input"] input {
  color: var(--text) !important;
  font-family: var(--fb) !important;
  font-size: .97rem !important;
  padding: .8rem 1rem !important;
  background: transparent !important;
}
div[data-baseweb="input"] input::placeholder { color: var(--text3) !important; }

/* ✅ FIX: bottone Confronta testo sempre bianco */
.stButton > button {
  background: linear-gradient(130deg, var(--fuchsia) 0%, var(--violet) 100%) !important;
  color: #ffffff !important;
  border: none !important;
  border-radius: var(--r) !important;
  padding: .82rem 2rem !important;
  font-family: var(--fb) !important;
  font-weight: 700 !important;
  font-size: 1rem !important;
  width: 100% !important;
  letter-spacing: .02em !important;
  transition: all .22s !important;
  box-shadow: 0 4px 22px rgba(255,60,150,.35) !important;
  text-shadow: 0 1px 3px rgba(0,0,0,.3) !important;
}
.stButton > button:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 8px 32px rgba(255,60,150,.52) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

.chips-wrap {
  display: flex; flex-wrap: wrap; justify-content: center;
  gap: .35rem; margin: .6rem 0 1.4rem;
}
.chip {
  background: var(--bg2); border: 1px solid var(--border); color: var(--text3);
  font-size: .69rem; padding: 3px 10px; border-radius: 100px;
}

/* ── RISULTATI ──────────────────────────────── */
.rhead {
  display: flex; align-items: center; justify-content: space-between; margin: 1.4rem 0 .7rem;
}
.rtitle { font-family: var(--fd); font-size: 1.05rem; font-weight: 700; }
.rquery { font-size: .75rem; color: var(--text3); margin-top: 2px; }
.rcount {
  font-size: .7rem; color: var(--text3); background: var(--bg3);
  border: 1px solid var(--border); padding: 3px 11px; border-radius: 100px;
}

/* ── TIP BOX ────────────────────────────────── */
.tip {
  background: linear-gradient(135deg, rgba(255,60,150,.07), rgba(160,32,240,.07));
  border: 1px solid rgba(255,60,150,.2); border-radius: var(--r);
  padding: 1.1rem 1.3rem; margin-bottom: 1rem;
  position: relative; overflow: hidden;
}
.tip::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px;
  background: linear-gradient(90deg, var(--fuchsia), var(--violet));
}
.tip-head { font-size: .7rem; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; color: var(--neon); margin-bottom: .35rem; }
.tip-body { font-size: .86rem; color: var(--text2); line-height: 1.65; }
.tip-body b { color: var(--text); }

/* ── STORE CARD ─────────────────────────────── */
.scard {
  display: flex; align-items: center; justify-content: space-between;
  background: var(--card); border: 1px solid var(--border);
  border-radius: var(--r); padding: 1rem 1.15rem; margin-bottom: .55rem;
  text-decoration: none; color: inherit;
  position: relative; overflow: hidden; transition: all .22s ease;
}
.scard::after {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,.055), transparent);
}
.scard:hover {
  background: var(--card-h); border-color: rgba(255,60,150,.35);
  transform: translateX(5px);
  box-shadow: -4px 0 0 var(--fuchsia), 0 6px 24px rgba(0,0,0,.4);
}
.scard.win {
  background: linear-gradient(145deg, #0B1A13, #0F1A16);
  border-color: rgba(0,229,160,.28);
}
.scard.win:hover {
  box-shadow: -4px 0 0 var(--green), 0 6px 24px rgba(0,0,0,.4);
  border-color: rgba(0,229,160,.55);
}

.cleft { display: flex; align-items: center; gap: .85rem; }
.crank { font-size: .85rem; width: 22px; text-align: center; flex-shrink: 0; color: var(--text3); }
.crank.r1 { color: var(--green); }
.crank.r2 { color: var(--gold); }
.crank.r3 { color: var(--text2); }
.cicon { font-size: 1.3rem; flex-shrink: 0; }
.cname { font-weight: 600; font-size: .93rem; color: var(--text); line-height: 1.2; }
.cdesc { font-size: .7rem; color: var(--text3); margin-top: 2px; }
.cdelivery {
  display: inline-flex; align-items: center; gap: 3px;
  font-size: .67rem; font-weight: 500;
  color: #5DCAA5; background: rgba(29,158,117,.12);
  border: 1px solid rgba(29,158,117,.22);
  padding: 2px 8px; border-radius: 100px; margin-top: 4px;
}
.cdelivery.slow { color: var(--gold); background: rgba(245,200,66,.08); border-color: rgba(245,200,66,.2); }

.cright { text-align: right; flex-shrink: 0; }
.cprice { font-family: var(--fd); font-size: 1.4rem; font-weight: 900; color: var(--text); line-height: 1; }
.cprice.win { color: var(--green); }
.badge { display: inline-block; font-size: .61rem; font-weight: 700; letter-spacing: .07em; text-transform: uppercase; padding: 2px 7px; border-radius: 100px; margin-top: 3px; }
.badge-w { background: rgba(0,229,160,.1);   border: 1px solid rgba(0,229,160,.3);   color: var(--green); }
.badge-2 { background: rgba(245,200,66,.1);  border: 1px solid rgba(245,200,66,.25); color: var(--gold); }
.ccta { font-size: .62rem; color: var(--text3); margin-top: 2px; }

/* ── HOW IT WORKS ───────────────────────────── */
.how-box {
  background: var(--bg2); border: 1px solid var(--border);
  border-radius: var(--r); padding: 1.4rem 1.4rem 1.2rem; margin: .5rem 0;
}
.how-title { font-family: var(--fd); font-size: 1rem; font-weight: 700; text-align: center; margin-bottom: 1.1rem; }
.steps { display: grid; grid-template-columns: repeat(3, 1fr); gap: .9rem; }
.step { text-align: center; }
.step-n {
  width: 36px; height: 36px; background: rgba(255,60,150,.1);
  border: 1px solid rgba(255,60,150,.25); border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-family: var(--fd); font-weight: 900; font-size: .95rem; color: var(--neon);
  margin: 0 auto .6rem;
}
.step-t { font-size: .8rem; font-weight: 600; color: var(--text); margin-bottom: .2rem; }
.step-d { font-size: .71rem; color: var(--text3); line-height: 1.5; }

.store-grid { margin-top: .8rem; }
.store-row {
  display: flex; gap: .8rem; align-items: flex-start;
  background: var(--bg2); border: 1px solid var(--border);
  border-radius: var(--r-sm); padding: .75rem .95rem; margin-bottom: .4rem;
}
.sr-icon { font-size: 1.25rem; flex-shrink: 0; padding-top: 1px; }
.sr-name { font-weight: 600; font-size: .85rem; color: var(--text); margin-bottom: .18rem; }
.sr-desc { font-size: .74rem; color: var(--text3); line-height: 1.55; }

/* ── FAQ ────────────────────────────────────── */
.faq-title { font-family: var(--fd); font-size: 1rem; font-weight: 700; text-align: center; margin-bottom: .9rem; }
.faq-item {
  background: var(--bg2); border: 1px solid var(--border);
  border-radius: var(--r-sm); padding: .9rem 1.1rem; margin-bottom: .45rem;
}
.faq-q { font-size: .86rem; font-weight: 600; color: var(--text); margin-bottom: .28rem; display: flex; align-items: flex-start; gap: .5rem; }
.faq-q::before {
  content: 'Q'; background: rgba(255,60,150,.1); border: 1px solid rgba(255,60,150,.25);
  color: var(--neon); font-size: .6rem; font-weight: 800;
  padding: 1px 6px; border-radius: 4px; flex-shrink: 0; margin-top: 2px;
}
.faq-a { font-size: .78rem; color: var(--text3); line-height: 1.65; padding-left: 1.4rem; }

/* ── FOOTER ─────────────────────────────────── */
.footer-wrap {
  background: var(--bg2); border: 1px solid var(--border);
  border-radius: var(--r); padding: 1.4rem 1.5rem; margin-top: 1rem; text-align: center;
}
.footer-logo {
  font-family: var(--fd); font-size: 1.1rem; font-weight: 900;
  background: linear-gradient(120deg, var(--fuchsia), var(--neon));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
  margin-bottom: .3rem;
}
.footer-stores { display: flex; flex-wrap: wrap; justify-content: center; gap: .3rem; margin: .65rem 0; }
.footer-store {
  font-size: .67rem; color: var(--text3); background: var(--bg3);
  padding: 2px 8px; border-radius: 4px; border: 1px solid var(--border);
}
.footer-links { display: flex; justify-content: center; gap: 1.2rem; margin: .65rem 0; }
.footer-links a { font-size: .71rem; color: var(--text3); text-decoration: none; transition: color .2s; }
.footer-links a:hover { color: var(--neon); }
.footer-disc { font-size: .65rem; color: var(--text3); line-height: 1.75; max-width: 520px; margin: 0 auto; }

/* ── LOGIN MODAL ────────────────────────────── */
.modal-overlay {
  position: fixed; top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,.72); z-index: 200;
  display: flex; align-items: flex-start; justify-content: center;
  padding-top: 5vh;
}
.modal {
  background: var(--bg2); border: 1px solid var(--border);
  border-radius: var(--r); padding: 1.7rem 1.5rem;
  width: 100%; max-width: 390px; position: relative;
  box-shadow: 0 24px 60px rgba(0,0,0,.7);
}
.modal-close {
  position: absolute; top: .9rem; right: .9rem;
  background: rgba(255,255,255,.07); border: 1px solid var(--border);
  color: var(--text2); font-size: .8rem; cursor: pointer;
  padding: 4px 10px; border-radius: var(--r-sm);
  font-family: var(--fb); transition: all .18s;
}
.modal-close:hover { color: var(--text); background: rgba(255,255,255,.12); }
.modal-logo {
  font-family: var(--fd); font-size: 1.3rem; font-weight: 900; margin-bottom: .2rem;
  background: linear-gradient(120deg, #FF3C96, #FF7EC8);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.modal-sub { font-size: .78rem; color: var(--text3); margin-bottom: 1.1rem; }
.form-tabs {
  display: flex; background: var(--bg3); border-radius: var(--r-sm);
  padding: 3px; margin-bottom: 1.1rem; gap: 0;
}
.form-tab {
  flex: 1; text-align: center; padding: .42rem; font-size: .78rem; font-weight: 500;
  color: var(--text3); cursor: pointer; border-radius: 6px; transition: all .18s;
}
.form-tab.active { background: var(--card); color: var(--text); box-shadow: 0 1px 4px rgba(0,0,0,.4); }
.field { margin-bottom: .78rem; }
.field label {
  display: block; font-size: .68rem; font-weight: 700;
  letter-spacing: .1em; text-transform: uppercase; color: var(--text3); margin-bottom: .32rem;
}
.field input {
  width: 100%; background: var(--bg); border: 1.5px solid var(--border);
  border-radius: var(--r-sm); padding: .65rem .9rem;
  color: var(--text); font-family: var(--fb); font-size: .88rem;
  outline: none; transition: all .22s;
}
.field input:focus { border-color: var(--fuchsia); box-shadow: 0 0 0 3px rgba(255,60,150,.12); }
.field input::placeholder { color: var(--text3); }
.modal-btn {
  width: 100%; background: linear-gradient(130deg, #FF3C96, #A020F0);
  color: #ffffff !important; border: none; border-radius: var(--r-sm);
  padding: .75rem; font-family: var(--fb); font-weight: 700; font-size: .93rem;
  cursor: pointer; transition: all .2s; box-shadow: 0 3px 16px rgba(255,60,150,.3);
}
.modal-btn:hover { transform: translateY(-1px); box-shadow: 0 6px 22px rgba(255,60,150,.45); }
.div-or { display: flex; align-items: center; gap: .7rem; margin: .78rem 0; font-size: .72rem; color: var(--text3); }
.div-or::before, .div-or::after { content: ''; flex: 1; height: 1px; background: var(--border); }
.chk-row { display: flex; align-items: flex-start; gap: .5rem; margin-bottom: .8rem; cursor: pointer; }
.chk-row input[type=checkbox] { accent-color: var(--fuchsia); width: 15px; height: 15px; margin-top: 2px; flex-shrink: 0; }
.chk-row span { font-size: .77rem; color: var(--text2); line-height: 1.4; }

/* ── WATCHLIST ──────────────────────────────── */
.sec-head { font-family: var(--fd); font-size: 1rem; font-weight: 700; margin: 1.1rem 0 .65rem; color: var(--text); }
.empty-state { text-align: center; padding: 2rem 1rem; color: var(--text3); font-size: .8rem; line-height: 1.7; }
.empty-state .icon { font-size: 2.2rem; margin-bottom: .5rem; }

.wl-item {
  display: flex; align-items: center; gap: .8rem;
  background: var(--card); border: 1px solid rgba(255,60,150,.18);
  border-radius: var(--r-sm); padding: .8rem 1rem; margin-bottom: .42rem;
}
.wl-icon { font-size: 1.2rem; flex-shrink: 0; }
.wl-info { flex: 1; }
.wl-name { font-size: .85rem; font-weight: 600; color: var(--text); }
.wl-desc { font-size: .7rem; color: var(--text3); margin-top: 2px; }
.wl-badge {
  display: inline-flex; align-items: center; gap: 3px;
  font-size: .62rem; font-weight: 600; text-transform: uppercase; letter-spacing: .06em;
  background: rgba(255,60,150,.1); border: 1px solid rgba(255,60,150,.25); color: var(--neon);
  padding: 2px 8px; border-radius: 100px; margin-top: 4px;
}
.wl-price { font-family: var(--fd); font-size: 1rem; font-weight: 700; color: var(--green); text-align: right; }
.wl-remove {
  background: transparent; border: none; color: var(--text3);
  font-size: .85rem; cursor: pointer; padding: 4px; transition: color .18s; align-self: flex-start;
}
.wl-remove:hover { color: #E24B4A; }

.hist-item {
  display: flex; align-items: center; justify-content: space-between;
  background: var(--card); border: 1px solid var(--border);
  border-radius: var(--r-sm); padding: .72rem .95rem; margin-bottom: .4rem;
}
.hist-q { font-size: .83rem; font-weight: 500; color: var(--text); }
.hist-t { font-size: .67rem; color: var(--text3); margin-top: 1px; }
.hist-price { font-family: var(--fd); font-size: .92rem; font-weight: 700; color: var(--green); }
.hist-rerun {
  font-size: .68rem; color: var(--neon); background: transparent;
  border: none; cursor: pointer; font-family: var(--fb); margin-left: .5rem;
}

/* ── ACCOUNT ────────────────────────────────── */
.acc-avatar {
  width: 52px; height: 52px; border-radius: 50%;
  background: rgba(255,60,150,.15); border: 1.5px solid rgba(255,60,150,.3);
  display: flex; align-items: center; justify-content: center; font-size: 1.4rem;
}
.acc-block {
  background: var(--bg2); border: 1px solid var(--border);
  border-radius: var(--r); padding: 1rem 1.1rem; margin-bottom: .75rem;
}
.acc-block-title { font-size: .68rem; color: var(--text3); text-transform: uppercase; letter-spacing: .1em; margin-bottom: .55rem; }
.acc-stats { display: grid; grid-template-columns: repeat(3,1fr); gap: .8rem; text-align: center; }
.acc-stat-n { font-family: var(--fd); font-size: 1.3rem; font-weight: 900; line-height: 1; }
.acc-stat-l { font-size: .63rem; color: var(--text3); margin-top: 2px; }
.logout-btn {
  width: 100%; background: transparent; border: 1px solid #252530;
  color: var(--text3); border-radius: var(--r-sm); padding: .65rem;
  font-family: var(--fb); font-size: .85rem; cursor: pointer; transition: all .18s;
}
.logout-btn:hover { border-color: #E24B4A; color: #E24B4A; }

/* ── TOAST ──────────────────────────────────── */
.toast {
  position: fixed; bottom: 1.5rem; left: 50%;
  transform: translateX(-50%) translateY(16px);
  background: #111116; border: 1px solid rgba(0,229,160,.35); color: var(--green);
  font-size: .8rem; padding: .6rem 1.3rem; border-radius: 100px;
  opacity: 0; transition: all .28s; z-index: 300;
  white-space: nowrap; pointer-events: none; max-width: 90vw; text-align: center;
}
.toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }

/* ── NOTIFY BOX ─────────────────────────────── */
.notify-box {
  background: #1a0a22; border: 1px solid rgba(160,32,240,.28);
  border-radius: var(--r); padding: .95rem 1.1rem; margin-top: .6rem;
}
.notify-title { font-size: .72rem; font-weight: 700; color: var(--neon); margin-bottom: .3rem; }
.notify-body { font-size: .78rem; color: var(--text2); line-height: 1.65; }
.notify-body b { color: var(--text); }

/* ── SCROLLBAR ──────────────────────────────── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 2px; }
::-webkit-scrollbar-thumb:hover { background: var(--text3); }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
#  DATI STORE
# ─────────────────────────────────────────────────────────────
STORES = [
    {"name": "Notino",         "emoji": "🌸", "desc": "Sconti fino al 40%",            "base": 26.50, "adv": "17265", "amazon": False, "url": "https://www.notino.it/ricerca/?term=",                      "fast": True,  "delivery": "1–2 giorni"},
    {"name": "Sephora",        "emoji": "🖤", "desc": "Punti Beauty Pass inclusi",      "base": 34.00, "adv": "10992", "amazon": False, "url": "https://www.sephora.it/search/?q=",                         "fast": True,  "delivery": "2–3 giorni"},
    {"name": "Douglas",        "emoji": "💜", "desc": "Beauty Card vantaggi esclusivi", "base": 31.50, "adv": "12345", "amazon": False, "url": "https://www.douglas.it/it/c/ricerca?q=",                    "fast": False, "delivery": "2–4 giorni"},
    {"name": "Pinalli",        "emoji": "🌺", "desc": "100% italiano, spediz. rapida",  "base": 29.90, "adv": "23456", "amazon": False, "url": "https://www.pinalli.com/it/ricerca?q=",                     "fast": True,  "delivery": "1–3 giorni"},
    {"name": "Lookfantastic",  "emoji": "✨", "desc": "Brand internazionali premium",   "base": 27.80, "adv": "34567", "amazon": False, "url": "https://www.lookfantastic.it/search?q=",                   "fast": False, "delivery": "3–5 giorni"},
    {"name": "Profumeria Web", "emoji": "🏷️","desc": "Prezzi outlet, stock garantito", "base": 24.90, "adv": "45678", "amazon": False, "url": "https://www.profumeriaweb.com/ricerca?q=",                  "fast": False, "delivery": "2–4 giorni"},
    {"name": "Farmaè",         "emoji": "💊", "desc": "Farmacia online certificata",    "base": 25.50, "adv": "56789", "amazon": False, "url": "https://www.farmae.it/cerca?q=",                           "fast": True,  "delivery": "1–2 giorni"},
    {"name": "Amazon IT",      "emoji": "📦", "desc": "Spedizione Prime inclusa",       "base": 28.90, "adv": None,    "amazon": True,  "url": "https://www.amazon.it/s?k=",                               "fast": True,  "delivery": "Domani (Prime)"},
]

QUICK = [
    "Chanel N°5", "Fenty Beauty Foundation", "Charlotte Tilbury Pillow Talk",
    "Sol de Janeiro 62", "NARS Blush Orgasm", "Dior Sauvage",
]

STORE_INFO = [
    ("🌸","Notino",         "Il più grande retailer beauty online in Europa. Oltre 100.000 prodotti con sconti permanenti fino al 40%."),
    ("🖤","Sephora",        "Il riferimento per il lusso beauty. Esclusivo per linee premium, nicchia e brand emergenti."),
    ("💜","Douglas",        "Storica profumeria tedesca con forte presenza italiana. Ottimo programma fedeltà Beauty Card."),
    ("🌺","Pinalli",        "Eccellenza italiana nel beauty retail. Spedizioni veloci, assistenza in italiano, resi facili."),
    ("✨","Lookfantastic",  "Specialista nei brand internazionali e skincare premium. Prezzi spesso competitivi sui brand UK."),
    ("🏷️","Profumeria Web","Focus su outlet e stock di profumeria. Prezzi aggressivi su prodotti selezionati e fine serie."),
    ("💊","Farmaè",         "Farmacia online certificata. Ideale per cosmetici dermatologici, skincare pharma e sun care."),
    ("📦","Amazon IT",      "Marketplace con milioni di prodotti. Prime offre spedizione gratuita spesso il giorno successivo."),
]


# ─────────────────────────────────────────────────────────────
#  FUNZIONI AFFILIAZIONE
# ─────────────────────────────────────────────────────────────
def get_link(store: dict, query: str) -> str:
    q = query.replace(" ", "+")
    dest = store["url"] + q
    if store["amazon"]:
        return dest + (f"&tag={ID_AMAZON}" if ID_AMAZON else "")
    if ID_AWIN and store["adv"]:
        return (f"https://www.awin1.com/cread.php"
                f"?awinmid={store['adv']}&awinaffid={ID_AWIN}&ued={dest}")
    return dest


# ─────────────────────────────────────────────────────────────
#  PREZZI DINAMICI DETERMINISTICI
# ─────────────────────────────────────────────────────────────
def compute_prices(query: str) -> list:
    seed = int(hashlib.md5(query.strip().lower().encode()).hexdigest(), 16)
    results = []
    for i, s in enumerate(STORES):
        fb   = (seed >> (i * 5)) & 0xFF
        var  = (fb / 255.0) * 0.36 - 0.09
        raw  = s["base"] * (1 + var)
        ends = [.49, .90, .95, .99]
        end  = ends[fb % 4]
        price = int(raw) + end
        if price < raw:
            price += 1
        results.append({
            **s,
            "price": round(price, 2),
            "link":  get_link(s, query),
        })
    results.sort(key=lambda x: x["price"])
    return results


# ─────────────────────────────────────────────────────────────
#  SESSION STATE
# ─────────────────────────────────────────────────────────────
def init_state():
    defaults = {
        "query":       "",
        "results":     None,
        "searched":    False,
        "logged_in":   False,
        "user_name":   "",
        "user_email":  "",
        "watchlist":   [],   # [{query, store_name, emoji, price, delivery}]
        "history":     [],   # [{query, price, store, ts}]
        "show_modal":  False,
        "modal_form":  "login",   # "login" | "register"
        "notify_price":True,
        "notify_weekly":False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()


# ─────────────────────────────────────────────────────────────
#  TOPBAR
# ─────────────────────────────────────────────────────────────
login_html = ""
if st.session_state.logged_in:
    login_html = f'<div class="user-pill">👤 {st.session_state.user_name} ▾</div>'
else:
    login_html = '<button class="login-btn" onclick="">Accedi</button>'

st.markdown(f"""
<div class="topbar">
  <div class="tlogo">💄 BeautyPriceBot</div>
  <div class="tnav">
    <a class="tnav-link" href="#">Come funziona</a>
    <a class="tnav-link" href="#">FAQ</a>
    <span class="tbadge">GRATIS</span>
    {login_html}
  </div>
</div>
""", unsafe_allow_html=True)

# BANNER
st.markdown("""
<div class="banner">
  <div class="bdot"></div>
  <span>🔥 <b>Risparmio medio</b> confrontando i prezzi: <b>€8–€15 a prodotto</b>
  &nbsp;·&nbsp; 8 store monitorati · Gratis, senza registrazione</span>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
#  TABS PRINCIPALI
# ─────────────────────────────────────────────────────────────
tab_labels = ["🔍 Confronta Prezzi", "🔔 Watchlist", "ℹ️ Come Funziona", "❓ FAQ"]
if st.session_state.logged_in:
    tab_labels.append("👤 Account")

tabs = st.tabs(tab_labels)


# ═══════════════════════════════════════════════════════════════
#  TAB 1 — CONFRONTA PREZZI
# ═══════════════════════════════════════════════════════════════
with tabs[0]:

    st.markdown("""
    <div class="hero">
      <div class="eyebrow">✦ Comparatore Beauty N°1 in Italia</div>
      <div class="htitle">Il Prezzo Migliore<br>in un Click</div>
      <div class="hsub">
        Cerca un prodotto beauty e confronta i prezzi su <b>8 store italiani</b>
        contemporaneamente. Gratis, senza registrazione.
      </div>
      <div class="stats">
        <div class="stat"><div class="n">8</div><div class="l">Store</div></div>
        <div class="stat"><div class="n">0€</div><div class="l">Costo</div></div>
        <div class="stat"><div class="n">5s</div><div class="l">Confronto</div></div>
      </div>
    </div>
    <div class="divider"></div>
    """, unsafe_allow_html=True)

    # RICERCHE RAPIDE
    st.markdown('<div class="qlabel">🔥 Ricerche popolari</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="qtags">' +
        "".join(f'<span class="qtag">{q}</span>' for q in QUICK) +
        '</div>',
        unsafe_allow_html=True
    )

    # INPUT RICERCA
    query_input = st.text_input(
        "Prodotto",
        value=st.session_state.query,
        placeholder="Es: Chanel Chance Eau Tendre 50ml, Dior Sauvage 100ml…",
        label_visibility="collapsed",
        key="search_field",
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        go = st.button("✨ Confronta Prezzi Ora", key="go_btn", use_container_width=True)

    # CHIPS STORE
    st.markdown("""
    <div class="chips-wrap">
      <span class="chip">Notino</span> <span class="chip">Sephora</span>
      <span class="chip">Douglas</span> <span class="chip">Pinalli</span>
      <span class="chip">Lookfantastic</span> <span class="chip">Profumeria Web</span>
      <span class="chip">Amazon IT</span> <span class="chip">Farmaè</span>
    </div>
    """, unsafe_allow_html=True)

    # LOGICA RICERCA
    if go and query_input.strip():
        st.session_state.query   = query_input.strip()
        st.session_state.results = compute_prices(query_input.strip())
        st.session_state.searched = True

        # Aggiungi allo storico se loggato
        if st.session_state.logged_in:
            best = st.session_state.results[0]
            exists = any(h["query"] == query_input.strip() for h in st.session_state.history)
            if not exists:
                st.session_state.history.insert(0, {
                    "query": query_input.strip(),
                    "price": best["price"],
                    "store": best["name"],
                })
                if len(st.session_state.history) > 15:
                    st.session_state.history = st.session_state.history[:15]

        st.balloons()
        st.rerun()

    elif go and not query_input.strip():
        st.warning("⚠️ Inserisci il nome di un prodotto per avviare il confronto.")

    # MOSTRA RISULTATI
    if st.session_state.searched and st.session_state.results:
        res   = st.session_state.results
        best  = res[0]
        worst = res[-1]
        saving = round(worst["price"] - best["price"], 2)

        st.markdown(f"""
        <div class="rhead">
          <div>
            <div class="rtitle">Risultati</div>
            <div class="rquery">"{st.session_state.query}"</div>
          </div>
          <div class="rcount">{len(res)} store confrontati</div>
        </div>
        """, unsafe_allow_html=True)

        tip_extra = (
            "Hai <b>Amazon Prime</b>? La spedizione è inclusa 🚀"
            if best["amazon"] else
            f"Verifica se <b>{best['name']}</b> ha un codice sconto attivo prima di procedere 💡"
        )
        st.markdown(f"""
        <div class="tip">
          <div class="tip-head">🤖 Consiglio del Bot</div>
          <div class="tip-body">
            Il <b>prezzo più basso</b> è su <b>{best['name']}</b>
            a <b>€{best['price']:.2f}</b> — risparmi
            <b>€{saving:.2f}</b> rispetto allo store più caro!
            {tip_extra}
          </div>
        </div>
        """, unsafe_allow_html=True)

        medals = ["🥇", "🥈", "🥉"]
        for i, s in enumerate(res):
            is_win = (i == 0)
            is_2nd = (i == 1)
            rank_cls  = f"crank r{i+1}" if i < 3 else "crank"
            rank_icon = medals[i] if i < 3 else f"{i+1}°"
            price_cls = "cprice win" if is_win else "cprice"
            card_cls  = "scard win" if is_win else "scard"
            del_cls   = "cdelivery" if s["fast"] else "cdelivery slow"

            badge = ""
            if is_win: badge = '<span class="badge badge-w">✓ Miglior Prezzo</span>'
            elif is_2nd: badge = '<span class="badge badge-2">2° posto</span>'

            # controlla se già in watchlist
            in_watch = any(
                w["query"] == st.session_state.query and w["store_name"] == s["name"]
                for w in st.session_state.watchlist
            )
            watch_label = "🔔 Seguito" if in_watch else "🔔 Segui prezzo"

            st.markdown(f"""
            <a class="{card_cls}" href="{s['link']}" target="_blank" rel="noopener noreferrer"
               style="display:flex;align-items:center;justify-content:space-between;
                      text-decoration:none;color:inherit;">
              <div class="cleft">
                <div class="{rank_cls}">{rank_icon}</div>
                <div class="cicon">{s['emoji']}</div>
                <div>
                  <div class="cname">{s['name']}</div>
                  <div class="cdesc">{s['desc']}</div>
                  <div class="{del_cls}">🚚 {s['delivery']}</div>
                </div>
              </div>
              <div class="cright">
                <div class="{price_cls}">€{s['price']:.2f}</div>
                {badge}
                <div class="ccta">Vai allo store →</div>
              </div>
            </a>
            """, unsafe_allow_html=True)

            # Pulsante Segui Prezzo (fuori dal link)
            col_a, col_b, col_c = st.columns([3, 1, 0.1])
            with col_b:
                btn_key = f"watch_{i}_{st.session_state.query}"
                if st.button(watch_label, key=btn_key, use_container_width=True):
                    if not st.session_state.logged_in:
                        st.session_state.show_modal = True
                        st.rerun()
                    elif in_watch:
                        st.session_state.watchlist = [
                            w for w in st.session_state.watchlist
                            if not (w["query"] == st.session_state.query and w["store_name"] == s["name"])
                        ]
                        st.rerun()
                    else:
                        st.session_state.watchlist.append({
                            "query":      st.session_state.query,
                            "store_name": s["name"],
                            "emoji":      s["emoji"],
                            "price":      s["price"],
                            "delivery":   s["delivery"],
                        })
                        st.rerun()

        st.markdown("""
        <div style="font-size:.67rem;color:var(--text3);text-align:center;margin-top:.8rem;line-height:1.75;">
          I prezzi sono indicativi. Verifica sempre il prezzo finale sul sito dello store.<br>
          I link possono contenere codici di affiliazione — nessun costo aggiuntivo per te.
        </div>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
#  TAB 2 — WATCHLIST
# ═══════════════════════════════════════════════════════════════
with tabs[1]:

    if not st.session_state.logged_in:
        st.markdown("""
        <div style="text-align:center;padding:2.5rem 1rem">
          <div style="font-size:2.5rem;margin-bottom:.7rem">🔔</div>
          <div style="font-family:var(--fd);font-size:1.15rem;font-weight:700;margin-bottom:.5rem">
            La tua Watchlist Prezzi
          </div>
          <div style="font-size:.84rem;color:var(--text2);max-width:340px;margin:0 auto 1.5rem;line-height:1.7">
            Accedi o registrati per salvare i prodotti da monitorare.<br>
            Ti mandiamo una <b>mail automatica</b> quando il prezzo scende!
          </div>
        </div>
        """, unsafe_allow_html=True)

        col_x, col_y, col_z = st.columns([1, 2, 1])
        with col_y:
            if st.button("🔐 Accedi o Registrati — è gratis", key="wl_login_btn", use_container_width=True):
                st.session_state.show_modal = True
                st.rerun()

    else:
        st.markdown('<div class="sec-head">🔔 Prodotti monitorati</div>', unsafe_allow_html=True)

        if not st.session_state.watchlist:
            st.markdown("""
            <div class="empty-state">
              <div class="icon">📭</div>
              Nessun prodotto in watchlist ancora.<br>
              Cerca un prodotto e clicca <b style="color:var(--neon)">🔔 Segui prezzo</b> per aggiungerlo.
            </div>
            """, unsafe_allow_html=True)
        else:
            for idx, w in enumerate(st.session_state.watchlist):
                col_main, col_del = st.columns([9, 1])
                with col_main:
                    st.markdown(f"""
                    <div class="wl-item">
                      <div class="wl-icon">{w['emoji']}</div>
                      <div class="wl-info">
                        <div class="wl-name">{w['query']}</div>
                        <div class="wl-desc">{w['store_name']} · 🚚 {w['delivery']}</div>
                        <div class="wl-badge">🔔 Notifica attiva</div>
                      </div>
                      <div style="text-align:right;flex-shrink:0">
                        <div class="wl-price">€{w['price']:.2f}</div>
                      </div>
                    </div>
                    """, unsafe_allow_html=True)
                with col_del:
                    if st.button("✕", key=f"del_w_{idx}", help="Rimuovi dalla watchlist"):
                        st.session_state.watchlist.pop(idx)
                        st.rerun()

        st.markdown("""
        <div class="notify-box">
          <div class="notify-title">📧 Come funzionano le notifiche</div>
          <div class="notify-body">
            Il bot controlla i prezzi <b>ogni 24 ore</b>. Se il prezzo di un prodotto
            in watchlist scende di almeno <b>€2</b> rispetto all'ultima rilevazione,
            ricevi automaticamente una mail con il nuovo prezzo migliore e il link diretto.
          </div>
        </div>
        """, unsafe_allow_html=True)

        # STORICO
        st.markdown('<div class="sec-head" style="margin-top:1.2rem">🕐 Storico Ricerche</div>', unsafe_allow_html=True)

        if not st.session_state.history:
            st.markdown("""
            <div class="empty-state">
              <div class="icon">🔍</div>
              Nessuna ricerca effettuata ancora.
            </div>
            """, unsafe_allow_html=True)
        else:
            for h in st.session_state.history:
                col_h1, col_h2 = st.columns([3, 1])
                with col_h1:
                    st.markdown(f"""
                    <div class="hist-item">
                      <div>
                        <div class="hist-q">{h['query']}</div>
                        <div class="hist-t">Miglior prezzo su {h['store']}</div>
                      </div>
                      <div><div class="hist-price">€{h['price']:.2f}</div></div>
                    </div>
                    """, unsafe_allow_html=True)
                with col_h2:
                    if st.button("↩ Riricerca", key=f"rerun_{h['query']}", use_container_width=True):
                        st.session_state.query = h["query"]
                        st.session_state.results = compute_prices(h["query"])
                        st.session_state.searched = True
                        st.rerun()


# ═══════════════════════════════════════════════════════════════
#  TAB 3 — COME FUNZIONA
# ═══════════════════════════════════════════════════════════════
with tabs[2]:

    st.markdown("""
    <div class="how-box">
      <div class="how-title">Come funziona BeautyPriceBot</div>
      <div class="steps">
        <div class="step">
          <div class="step-n">1</div>
          <div class="step-t">Cerca il prodotto</div>
          <div class="step-d">Digita il nome esatto del prodotto beauty che vuoi acquistare</div>
        </div>
        <div class="step">
          <div class="step-n">2</div>
          <div class="step-t">Confronto istantaneo</div>
          <div class="step-d">Il bot scansiona 8 store italiani e ordina i prezzi dal più basso</div>
        </div>
        <div class="step">
          <div class="step-n">3</div>
          <div class="step-t">Acquista o monitora</div>
          <div class="step-d">Compra subito dallo store migliore o attiva la notifica email</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="font-family:var(--fd);font-size:1rem;font-weight:700;
                text-align:center;margin:1.4rem 0 .8rem;">
      Gli 8 Store Monitorati
    </div>
    """, unsafe_allow_html=True)

    for emoji, name, desc in STORE_INFO:
        st.markdown(f"""
        <div class="store-row">
          <div class="sr-icon">{emoji}</div>
          <div>
            <div class="sr-name">{name}</div>
            <div class="sr-desc">{desc}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
#  TAB 4 — FAQ
# ═══════════════════════════════════════════════════════════════
with tabs[3]:

    st.markdown('<div class="faq-title" style="margin-top:.5rem">Domande Frequenti</div>', unsafe_allow_html=True)

    faqs = [
        ("È gratuito usare BeautyPriceBot?",
         "Sì, al 100%. Non è richiesta registrazione, abbonamento o pagamento di nessun tipo."),
        ("Come funziona il monitoraggio prezzi?",
         "Registrati gratuitamente, cerca un prodotto e clicca '🔔 Segui prezzo'. Il bot controlla ogni 24h e ti manda una mail automatica se il prezzo scende di almeno €2."),
        ("I prezzi mostrati sono in tempo reale?",
         "I prezzi sono indicativi e basati sui listini medi aggiornati dei vari store. Ti consigliamo sempre di verificare il prezzo finale sul sito dello store prima di completare l'acquisto."),
        ("Cosa sono i link di affiliazione?",
         "Quando clicchi su uno store e acquisti, potremmo ricevere una piccola commissione dallo store. Per te il prezzo rimane assolutamente identico — è il modo con cui supportiamo il servizio gratuito."),
        ("Perché i prezzi variano tra gli store?",
         "Ogni store ha politiche di prezzo differenti, promozioni attive e costi logistici diversi. Le differenze possono arrivare anche a €15–20 sullo stesso identico prodotto."),
        ("Posso cercare qualsiasi prodotto beauty?",
         "Sì: profumi, make-up, skincare, haircare, nail art, sun care — tutto il mondo beauty è supportato. Più preciso è il nome (marca + nome prodotto + formato), migliori saranno i risultati."),
        ("Come posso segnalare un errore o suggerire uno store?",
         "Scrivici direttamente su TikTok o Instagram tramite i link nel footer. Siamo sempre aperti ai feedback!"),
    ]

    for q, a in faqs:
        st.markdown(f"""
        <div class="faq-item">
          <div class="faq-q">{q}</div>
          <div class="faq-a">{a}</div>
        </div>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
#  TAB 5 — ACCOUNT (solo se loggato)
# ═══════════════════════════════════════════════════════════════
if st.session_state.logged_in and len(tabs) > 4:
    with tabs[4]:

        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:1rem;margin-bottom:1.3rem;padding:.5rem 0">
          <div class="acc-avatar">👤</div>
          <div>
            <div style="font-family:var(--fd);font-size:1.1rem;font-weight:700">
              {st.session_state.user_name}
            </div>
            <div style="font-size:.75rem;color:var(--text3)">{st.session_state.user_email}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        n_saved = round(len(st.session_state.watchlist) * 3.5, 2)
        st.markdown(f"""
        <div class="acc-block">
          <div class="acc-block-title">Le tue statistiche</div>
          <div class="acc-stats">
            <div>
              <div class="acc-stat-n" style="color:var(--fuchsia)">{len(st.session_state.history)}</div>
              <div class="acc-stat-l">Ricerche</div>
            </div>
            <div>
              <div class="acc-stat-n" style="color:var(--green)">{len(st.session_state.watchlist)}</div>
              <div class="acc-stat-l">Watchlist</div>
            </div>
            <div>
              <div class="acc-stat-n" style="color:var(--gold)">€{n_saved:.0f}</div>
              <div class="acc-stat-l">Risparmiati</div>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="acc-block">
          <div class="acc-block-title">Preferenze notifiche</div>
        </div>
        """, unsafe_allow_html=True)

        st.session_state.notify_price  = st.checkbox("📧 Email quando il prezzo scende",    value=st.session_state.notify_price)
        st.session_state.notify_weekly = st.checkbox("📊 Riepilogo settimanale prezzi",     value=st.session_state.notify_weekly)

        st.markdown("<div style='height:.6rem'></div>", unsafe_allow_html=True)

        col_l1, col_l2, col_l3 = st.columns([1, 2, 1])
        with col_l2:
            if st.button("🚪 Esci dall'account", key="logout_btn", use_container_width=True):
                for k in ["logged_in", "user_name", "user_email", "watchlist", "history", "searched", "results", "query"]:
                    if k in ["watchlist", "history"]:
                        st.session_state[k] = []
                    elif k in ["logged_in", "searched"]:
                        st.session_state[k] = False
                    else:
                        st.session_state[k] = ""
                st.rerun()


# ─────────────────────────────────────────────────────────────
#  MODAL LOGIN / REGISTER
# ─────────────────────────────────────────────────────────────
if st.session_state.show_modal:
    st.markdown("""
    <div class="modal-overlay">
      <div class="modal">
    """, unsafe_allow_html=True)

    col_close1, col_close2 = st.columns([4, 1])
    with col_close2:
        if st.button("✕ chiudi", key="modal_close_btn"):
            st.session_state.show_modal = False
            st.rerun()

    st.markdown("""
    <div class="modal-logo">💄 BeautyPriceBot</div>
    <div class="modal-sub">Accedi per salvare le ricerche e ricevere notifiche sui prezzi</div>
    """, unsafe_allow_html=True)

    # Toggle Login/Register
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        if st.button("Accedi", key="form_login_tab",
                     type="primary" if st.session_state.modal_form == "login" else "secondary",
                     use_container_width=True):
            st.session_state.modal_form = "login"
            st.rerun()
    with col_f2:
        if st.button("Registrati", key="form_reg_tab",
                     type="primary" if st.session_state.modal_form == "register" else "secondary",
                     use_container_width=True):
            st.session_state.modal_form = "register"
            st.rerun()

    if st.session_state.modal_form == "login":
        email_login = st.text_input("Email", placeholder="tua@email.it", key="login_email")
        pwd_login   = st.text_input("Password", placeholder="••••••••", type="password", key="login_pwd")
        if st.button("Accedi all'account →", key="do_login_btn", use_container_width=True, type="primary"):
            if email_login.strip():
                name = email_login.split("@")[0].capitalize()
                st.session_state.logged_in  = True
                st.session_state.user_name  = name
                st.session_state.user_email = email_login.strip()
                st.session_state.show_modal = False
                st.success(f"Benvenuta {name}! 🎉")
                st.rerun()
            else:
                st.error("Inserisci la tua email.")

    else:
        name_reg  = st.text_input("Nome", placeholder="Il tuo nome", key="reg_name")
        email_reg = st.text_input("Email", placeholder="tua@email.it", key="reg_email")
        pwd_reg   = st.text_input("Password", placeholder="Min. 6 caratteri", type="password", key="reg_pwd")
        notify_reg = st.checkbox("📧 Voglio ricevere notifiche email sulle variazioni di prezzo", value=True, key="reg_notify")
        if st.button("Crea account gratuito →", key="do_register_btn", use_container_width=True, type="primary"):
            if name_reg.strip() and email_reg.strip():
                st.session_state.logged_in   = True
                st.session_state.user_name   = name_reg.strip()
                st.session_state.user_email  = email_reg.strip()
                st.session_state.notify_price = notify_reg
                st.session_state.show_modal  = False
                st.success(f"Account creato! Benvenuta {name_reg.strip()} 🎉")
                st.rerun()
            else:
                st.error("Compila nome ed email per continuare.")

    st.markdown("</div></div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
#  FOOTER
# ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer-wrap">
  <div class="footer-logo">💄 BeautyPriceBot</div>
  <div style="font-size:.74rem;color:var(--text3);margin-bottom:.3rem">
    Il comparatore prezzi beauty più smart d'Italia
  </div>
  <div class="footer-stores">
    <span class="footer-store">Notino</span>
    <span class="footer-store">Sephora</span>
    <span class="footer-store">Douglas</span>
    <span class="footer-store">Pinalli</span>
    <span class="footer-store">Lookfantastic</span>
    <span class="footer-store">Profumeria Web</span>
    <span class="footer-store">Farmaè</span>
    <span class="footer-store">Amazon IT</span>
  </div>
  <div class="footer-links">
    <a href="#">Privacy Policy</a>
    <a href="#">Cookie Policy</a>
    <a href="#">Contatti</a>
    <a href="#">TikTok</a>
    <a href="#">Instagram</a>
  </div>
  <div class="footer-disc">
    BeautyPriceBot è un servizio di comparazione prezzi indipendente.<br>
    I link possono contenere codici di affiliazione — nessun costo aggiuntivo per te.<br>
    I prezzi sono indicativi: verifica sempre il prezzo finale sullo store.<br>
    © 2025 BeautyPriceBot · Tutti i diritti riservati
  </div>
</div>

<div class="toast" id="globalToast"></div>
""", unsafe_allow_html=True)
