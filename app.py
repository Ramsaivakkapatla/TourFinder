import streamlit as st
import pandas as pd
import urllib.parse

st.set_page_config(page_title="TourFinder India", page_icon="🌍", layout="wide", initial_sidebar_state="expanded")

st.markdown("""<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@300;400;600&display=swap" rel="stylesheet">
<style>
:root{--spice:#c8502a;--gold:#e8a020;--teal:#1a7a6e;--deep:#1c2b2a;--muted:#6b7c7b;--card:#ffffffcc;--r:16px;--sh:0 6px 24px rgba(28,43,42,.1)}
html,body,[class*="css"]{font-family:'DM Sans',sans-serif!important;color:var(--deep)}
.stApp{background:linear-gradient(160deg,#f5ede0,#fdf8f2 60%,#e8f5f3);min-height:100vh}
section[data-testid="stSidebar"]{background:linear-gradient(180deg,#1c2b2a,#0f1d1c)!important}
section[data-testid="stSidebar"] *{color:#d4e8e6!important}
section[data-testid="stSidebar"] h2,section[data-testid="stSidebar"] h3{color:#e8a020!important;font-family:'Playfair Display',serif!important}
section[data-testid="stSidebar"] label{color:#9cbfbc!important;font-size:.75rem!important;text-transform:uppercase;letter-spacing:.06em}
.hero{background:linear-gradient(135deg,#1c2b2a,#2d4f4e,#1a7a6e);border-radius:22px;padding:3rem;margin-bottom:2rem;box-shadow:0 16px 48px rgba(28,43,42,.3)}
.hero h1{font-family:'Playfair Display',serif;font-size:clamp(1.8rem,4vw,3rem);color:#fff;margin:0 0 .5rem}
.hero h1 span{color:#e8a020}
.hero p{color:#9cbfbccc;font-size:1rem;margin:0}
.badge-hero{display:inline-flex;align-items:center;gap:6px;background:#c8502a22;border:1px solid #c8502a66;color:#e8a020;font-size:.7rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:3px 12px;border-radius:100px;margin-bottom:1rem}
.mrow{display:flex;gap:14px;flex-wrap:wrap;margin-bottom:1.4rem}
.mc{background:var(--card);border:1px solid rgba(200,80,42,.15);border-radius:13px;padding:1rem 1.3rem;flex:1;min-width:130px;box-shadow:var(--sh)}
.ml{font-size:.68rem;font-weight:600;color:var(--muted);text-transform:uppercase;letter-spacing:.07em;margin-bottom:3px}
.mv{font-family:'Playfair Display',serif;font-size:1.5rem;font-weight:700;color:var(--spice)}
.sh{font-family:'Playfair Display',serif;font-size:1.4rem;font-weight:700;color:var(--deep);display:flex;align-items:center;gap:10px;margin:2rem 0 1rem;padding-bottom:.4rem;border-bottom:2px solid #e8a02033}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:18px}
.pc{background:var(--card);border:1px solid rgba(26,122,110,.15);border-radius:var(--r);padding:1.3rem;box-shadow:var(--sh);position:relative;overflow:hidden;transition:transform .25s}
.pc::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,var(--spice),var(--gold))}
.pc:hover{transform:translateY(-4px)}
.pn{font-family:'Playfair Display',serif;font-size:1.15rem;font-weight:700;color:var(--deep)}
.pn-wrap{background:linear-gradient(135deg,rgba(232,160,32,.08),rgba(200,80,42,.05));border-left:3px solid var(--gold);border-radius:0 8px 8px 0;padding:.45rem .75rem;margin-bottom:8px}
.pl{font-size:.8rem;color:var(--muted);margin-bottom:9px}
.bwrap{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:10px}
.b{font-size:.67rem;font-weight:600;padding:2px 9px;border-radius:100px}
.bt{background:#1a7a6e18;color:#1a7a6e;border:1px solid #1a7a6e33}
.bb{background:#c8502a15;color:#c8502a;border:1px solid #c8502a33}
.gb{display:inline-flex;align-items:center;gap:4px;background:#4285F408;border:1px solid #4285F433;color:#4285F4;font-size:.67rem;font-weight:700;padding:2px 9px;border-radius:100px}
.mb{display:inline-flex;align-items:center;gap:5px;background:linear-gradient(135deg,#1c2b2a,#1a7a6e);color:#fff!important;text-decoration:none;font-size:.76rem;font-weight:600;padding:6px 14px;border-radius:100px}
.mb2{background:linear-gradient(135deg,#c8502a,#e8a020)!important}
.cc{background:linear-gradient(135deg,#1c2b2a,#2d4f4e);border-radius:var(--r);padding:1.8rem;color:#fff;box-shadow:var(--sh)}
.ct{font-family:'Playfair Display',serif;font-size:1.2rem;color:#e8a020;margin-bottom:.9rem}
.cr{display:flex;justify-content:space-between;padding:7px 0;border-bottom:1px solid rgba(255,255,255,.08)}
.ci{font-size:.84rem;color:#9cbfbc}
.ca{font-family:'Playfair Display',serif;font-size:.95rem;color:#fff;font-weight:600}
.ac{background:var(--card);border:1px solid rgba(200,80,42,.2);border-radius:13px;padding:1.1rem 1.3rem;margin-bottom:10px}
.an{font-weight:600;font-size:.94rem;margin-bottom:3px}
.ai{font-size:.78rem;color:var(--muted)}
.stButton>button{background:linear-gradient(135deg,#c8502a,#e8a020)!important;color:#fff!important;border:none!important;border-radius:100px!important;font-weight:600!important;padding:.5rem 1.5rem!important}
.map-wrap{border-radius:var(--r);overflow:hidden;box-shadow:var(--sh)}
.map-wrap iframe{display:block;width:100%}
.sbanner{display:flex;align-items:center;gap:12px;background:#1a7a6e12;border:1px solid #1a7a6e44;border-radius:12px;padding:.8rem 1.2rem;margin-bottom:1rem}
</style>""", unsafe_allow_html=True)

# ── DATA ──────────────────────────────────────────────────────────────────────
AGENTS = {
    "Rajasthan":[{"name":"Rajasthan Travels Pvt. Ltd.","phone":"+91-141-2360000","email":"info@rajasthantravels.com","rating":4.7,"specialty":"Heritage & Desert"},{"name":"Royal Rajasthan Tours","phone":"+91-141-5120400","email":"bookings@royalraj.com","rating":4.5,"specialty":"Palace & Wildlife"}],
    "Kerala":[{"name":"Kerala Tourism Board","phone":"+91-471-2321132","email":"info@keralatourism.org","rating":4.8,"specialty":"Backwaters & Ayurveda"},{"name":"Green Kerala Travels","phone":"+91-484-2380000","email":"green@keralatravels.com","rating":4.6,"specialty":"Eco & Nature"}],
    "Goa":[{"name":"Goa Travel Experts","phone":"+91-832-2420000","email":"goa@travelexperts.com","rating":4.6,"specialty":"Beach & Adventure"},{"name":"Coastal Goa Tours","phone":"+91-832-2650000","email":"info@coastalgoa.com","rating":4.4,"specialty":"Heritage & Beach"}],
    "Tamil Nadu":[{"name":"TN Tourism Dev. Corp.","phone":"+91-44-25367776","email":"info@tntourism.in","rating":4.7,"specialty":"Temple & Cultural"},{"name":"South India Pilgrim Tours","phone":"+91-44-24340000","email":"pilgrim@siptours.com","rating":4.5,"specialty":"Pilgrim & Religious"}],
    "Uttar Pradesh":[{"name":"UP Tourism Pvt. Ltd.","phone":"+91-522-2239516","email":"info@uptourism.gov.in","rating":4.6,"specialty":"Heritage & Pilgrimage"},{"name":"Varanasi Spiritual Journeys","phone":"+91-542-2501000","email":"ganga@spiritualtours.in","rating":4.7,"specialty":"Spiritual & Ganga"}],
    "Maharashtra":[{"name":"MTDC Maharashtra","phone":"+91-22-22024482","email":"info@maharashtratourism.gov.in","rating":4.6,"specialty":"Adventure & Heritage"},{"name":"Mumbai City Explorers","phone":"+91-22-26500000","email":"explore@mumbaitours.com","rating":4.4,"specialty":"City & Bollywood"}],
    "Himachal Pradesh":[{"name":"HP Tourism Dev. Corp.","phone":"+91-177-2652561","email":"hptdc@hptravels.com","rating":4.7,"specialty":"Mountains & Trekking"},{"name":"Manali Adventure Trails","phone":"+91-1902-252000","email":"trek@manalitrails.com","rating":4.6,"specialty":"Snow & Adventure"}],
    "West Bengal":[{"name":"West Bengal Tourism","phone":"+91-33-22485917","email":"info@wbtourism.gov.in","rating":4.5,"specialty":"Cultural & Darjeeling"},{"name":"Darjeeling Tea Trails","phone":"+91-354-2254000","email":"tea@darjeeling.in","rating":4.7,"specialty":"Tea Gardens & Himalaya"}],
    "Karnataka":[{"name":"Karnataka Tourism Dept.","phone":"+91-80-22352828","email":"ktdc@karnataka.gov.in","rating":4.6,"specialty":"Heritage & Wildlife"},{"name":"Mysuru Palace Tours","phone":"+91-821-2421096","email":"palace@mysururoyaltours.com","rating":4.7,"specialty":"Royal & Cultural"}],
    "Gujarat":[{"name":"Gujarat Tourism Corp.","phone":"+91-79-23238665","email":"info@gujarattourism.com","rating":4.5,"specialty":"Heritage & Wildlife"},{"name":"Rann Utsav Packages","phone":"+91-2757-221000","email":"rann@whitesaltfest.in","rating":4.7,"specialty":"Rann of Kutch"}],
    "Andhra Pradesh":[{"name":"APTDC - AP Tourism","phone":"+91-40-23454600","email":"info@aptourism.gov.in","rating":4.5,"specialty":"Pilgrimage & Heritage"},{"name":"Vizag Beach Tours","phone":"+91-891-2750000","email":"vizag@beachtours.in","rating":4.4,"specialty":"Coastal & Nature"}],
    "Telangana":[{"name":"Telangana Tourism Corp.","phone":"+91-40-23454600","email":"info@telanganatourism.gov.in","rating":4.5,"specialty":"Heritage & Wildlife"},{"name":"Hyderabad City Tours","phone":"+91-40-27900000","email":"hyd@citytours.in","rating":4.4,"specialty":"Nizami & Food Tours"}],
}
DEFAULT_AGENTS = [{"name":"India Tourism Dev. Corp.","phone":"+91-11-23320005","email":"info@itdc.co.in","rating":4.3,"specialty":"Pan-India Tours"},{"name":"Thomas Cook India","phone":"+91-22-67406720","email":"book@thomascook.in","rating":4.4,"specialty":"Customised Holidays"},{"name":"MakeMyTrip Holidays","phone":"+91-124-4628747","email":"care@makemytrip.com","rating":4.2,"specialty":"Online Packages"}]

TIERS = {
    "Budget 🎒":    {"stay":600,  "food":250, "local":150, "entry":40},
    "Mid-Range 🏨": {"stay":1500, "food":600, "local":300, "entry":100},
    "Luxury 🌟":    {"stay":5000, "food":1500,"local":800, "entry":280},
}
OW = {"Bus 🚌":350, "Train 🚂":800, "Flight ✈️":3500}

# ── HELPERS ───────────────────────────────────────────────────────────────────
def gmap(q):   return f"https://www.google.com/maps/search/{urllib.parse.quote_plus(q)}"
def gembed(q): return f"https://maps.google.com/maps?q={urllib.parse.quote_plus(q)}&output=embed&z=12"

def same_city_check(start, city, state):
    if not start: return False
    def n(s):
        s = s.lower().strip()
        for x in [" district"," city"," town"," mandal"," tehsil"," taluk"]:
            s = s.replace(x,"")
        return s.strip()
    sn = n(start)
    if city and city not in ("— All Cities —",""):
        cn = n(city)
        if sn == cn or cn in sn or sn in cn: return True
    if state and state not in ("— All States —",""):
        if sn == n(state): return True
    return False

def calc_cost(days, n_places, tier, intercity, local_trip):
    p = TIERS[tier]
    stay    = 0 if local_trip else p["stay"] * days
    food    = p["food"] * days
    local   = int(p["local"] * 0.55) * days if local_trip else p["local"] * days
    entries = p["entry"] * min(n_places, max(1, int(days * 1.5)))
    travel  = 0 if local_trip else OW[intercity] * 2
    misc    = int((stay + food + local) * 0.05)
    total   = stay + food + local + entries + travel + misc
    return {"🏨 Accommodation":stay,"🍽️ Food & Drinks":food,"🚗 Local Transport":local,
            "🎫 Entry Fees":entries,"🚌 Inter-city Travel":travel,"💼 Misc (5%)":misc}, total

@st.cache_data
def load_data():
    path = r"Top Indian Places to Visit.csv"
    try:
        df = pd.read_csv(path); df.columns = df.columns.str.strip()
        candidates = ["Google review rating","Google Review Rating","google review rating","Google Reviews","google_review_rating"]
        gc = next((c for c in candidates if c in df.columns), None)
        if gc and gc != "Google review rating": df.rename(columns={gc:"Google review rating"}, inplace=True)
        if "Google review rating" in df.columns:
            df["Google review rating"] = pd.to_numeric(df["Google review rating"], errors="coerce")
        return df, None
    except FileNotFoundError:
        return None, f"File not found: `{path}`"

data, err = load_data()
RCOL = "Google review rating" if data is not None and "Google review rating" in data.columns else ("Rating" if data is not None and "Rating" in data.columns else None)

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""<div class="hero"><div class="badge-hero">🧭 India's Premier Travel Planner</div>
<h1>Discover <span>Incredible India</span><br>One Place at a Time</h1>
<p>Filter destinations · Estimate budget · Find agents · Open in Google Maps</p></div>""", unsafe_allow_html=True)

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
sb = st.sidebar
sb.markdown("## 🔎 Discover & Plan")
if err: st.error(f"⚠️ {err}"); st.stop()

sb.markdown("### 📌 Starting Location")
start_loc = sb.text_input("Your current city", placeholder="e.g. Vijayawada, Mumbai…")
sb.markdown("---")
sb.markdown("### 📍 Destination Filters")

all_states = sorted(data["State"].dropna().unique()) if "State" in data.columns else []
sel_state  = sb.selectbox("① State", ["— All States —"] + all_states)
df_s       = data[data["State"]==sel_state] if sel_state != "— All States —" else data

all_cities = sorted(df_s["City"].dropna().unique()) if "City" in df_s.columns else []
sel_city   = sb.selectbox("② City", ["— All Cities —"] + all_cities)
df_sc      = df_s[df_s["City"]==sel_city] if sel_city != "— All Cities —" else df_s

all_types  = sorted(df_sc["Type"].dropna().unique()) if "Type" in df_sc.columns else []
sel_type   = sb.selectbox("③ Place Type", ["— All Types —"] + all_types)

if RCOL:
    rmin = float(data[RCOL].min()) if data[RCOL].notna().any() else 0.0
    rmax = float(data[RCOL].max()) if data[RCOL].notna().any() else 5.0
    min_rating = sb.slider("Min Google Review ⭐" if RCOL=="Google review rating" else "Min Rating ⭐", rmin, rmax, max(rmin,3.0), 0.1)
else:
    min_rating = 0.0

sb.markdown("---")
sb.markdown("### 🗓️ Trip Details")
duration  = sb.number_input("Duration (days)", 1, 60, 5, 1)
tier      = sb.selectbox("Budget Tier", list(TIERS.keys()), index=1)
intercity = sb.selectbox("Inter-city Transport", list(OW.keys()), index=1)
show_map  = sb.checkbox("📍 Show Map", True)
show_ag   = sb.checkbox("🤝 Show Agents", True)
show_cost = sb.checkbox("💰 Show Cost", True)
sb.markdown("---")
generate  = sb.button("✨ Generate My Plan", use_container_width=True)
reset     = sb.button("🔄 Reset", use_container_width=True)

if reset: st.session_state.clear(); st.rerun()
if generate: st.session_state.update(show=True, loc=start_loc.strip())

if not st.session_state.get("show"):
    st.markdown("""<div style="text-align:center;padding:4rem 0">
      <div style="font-size:4rem">🗺️</div>
      <div style="font-family:'Playfair Display',serif;font-size:1.5rem;color:#1c2b2a;margin:.4rem 0">Your Adventure Awaits</div>
      <div style="color:#6b7c7b">Set filters in the sidebar, then hit <strong>Generate My Plan</strong>.</div>
    </div>""", unsafe_allow_html=True); st.stop()

# ── FILTER ────────────────────────────────────────────────────────────────────
filt = data.copy()
if sel_state != "— All States —": filt = filt[filt["State"]==sel_state]
if sel_city  != "— All Cities —": filt = filt[filt["City"]==sel_city]
if sel_type  != "— All Types —":  filt = filt[filt["Type"]==sel_type]
if RCOL: filt = filt[pd.to_numeric(filt[RCOL], errors="coerce") >= min_rating]

n = len(filt)
if n == 0: st.error("❌ No places match. Try loosening your filters."); st.stop()

loc       = st.session_state.get("loc","")
dcity     = sel_city  if sel_city  != "— All Cities —"  else ""
dstate    = sel_state if sel_state != "— All States —"  else ""
local_trip = same_city_check(loc, dcity, dstate)

# ── BANNERS ───────────────────────────────────────────────────────────────────
if loc:
    tag = (' <span style="background:#1a7a6e22;color:#1a7a6e;font-size:.67rem;font-weight:700;padding:2px 9px;border-radius:100px">🏠 Local</span>' if local_trip
           else ' <span style="background:#c8502a18;color:#c8502a;font-size:.67rem;font-weight:700;padding:2px 9px;border-radius:100px">🚀 Outstation</span>')
    st.markdown(f'<div style="display:flex;align-items:center;gap:10px;background:linear-gradient(90deg,#1a7a6e18,transparent);border-left:3px solid #1a7a6e;border-radius:0 10px 10px 0;padding:.65rem 1.2rem;margin-bottom:.6rem"><span style="font-size:1.1rem">📍</span><div><div style="font-size:.68rem;color:#6b7c7b;text-transform:uppercase;letter-spacing:.07em;font-weight:600">Starting From</div><div style="font-size:.92rem;color:#1c2b2a;font-weight:600">{loc}{tag}</div></div></div>', unsafe_allow_html=True)

if local_trip and loc:
    saved = TIERS[tier]["stay"]*int(duration) + OW[intercity]*2
    st.markdown(f'<div class="sbanner"><span style="font-size:1.6rem">🎉</span><div><div style="font-size:.83rem;color:#1a7a6e;font-weight:600">You\'re already in <strong>{dcity or dstate}</strong>! Stay & travel costs removed.</div><div style="font-family:\'Playfair Display\',serif;font-size:1rem;color:#1a7a6e;font-weight:700">You save ≈ ₹{saved:,.0f}</div></div></div>', unsafe_allow_html=True)

# ── METRICS ───────────────────────────────────────────────────────────────────
costs, total = calc_cost(int(duration), n, tier, intercity, local_trip)
avg_r  = f"{pd.to_numeric(filt[RCOL], errors='coerce').mean():.1f}" if RCOL else "—"
rlabel = "Google ⭐" if RCOL=="Google review rating" else "⭐ Avg Rating"
ns     = filt["State"].nunique() if "State" in filt.columns else "—"

st.markdown(f"""<div class="mrow">
  <div class="mc"><div class="ml">📍 Places</div><div class="mv">{n}</div></div>
  <div class="mc"><div class="ml">🗺️ States</div><div class="mv">{ns}</div></div>
  <div class="mc"><div class="ml">{rlabel}</div><div class="mv">{avg_r}</div></div>
  <div class="mc"><div class="ml">🗓️ Days</div><div class="mv">{duration}</div></div>
  <div class="mc"><div class="ml">💰 Budget</div><div class="mv">₹{total:,.0f}</div></div>
</div>""", unsafe_allow_html=True)
st.success(f"✅ **{n}** destinations found!")

# ── PLACE CARDS ───────────────────────────────────────────────────────────────
st.markdown('<div class="sh">🏛️ Top Destinations</div>', unsafe_allow_html=True)
top  = filt.head(12)
G_SVG = '<svg width="10" height="10" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg" style="vertical-align:middle"><path d="M17.64 9.2c0-.637-.057-1.251-.164-1.84H9v3.481h4.844c-.209 1.125-.843 2.078-1.796 2.717v2.258h2.908c1.702-1.567 2.684-3.874 2.684-6.615z" fill="#4285F4"/><path d="M9 18c2.43 0 4.467-.806 5.956-2.18l-2.908-2.259c-.806.54-1.837.86-3.048.86-2.344 0-4.328-1.584-5.036-3.711H.957v2.332A8.997 8.997 0 009 18z" fill="#34A853"/><path d="M3.964 10.71A5.41 5.41 0 013.682 9c0-.593.102-1.17.282-1.71V4.958H.957A8.996 8.996 0 000 9c0 1.452.348 2.827.957 4.042l3.007-2.332z" fill="#FBBC05"/><path d="M9 3.58c1.321 0 2.508.454 3.44 1.345l2.582-2.58C13.463.891 11.426 0 9 0A8.997 8.997 0 00.957 4.958L3.964 7.29C4.672 5.163 6.656 3.58 9 3.58z" fill="#EA4335"/></svg>'

html = '<div class="pgrid">'
for _, r in top.iterrows():
    nm    = r.get("Name") or r.get("Place Name") or "—"
    city  = str(r.get("City",""));  state = str(r.get("State",""))
    ptype = str(r.get("Type",""));  best  = str(r.get("Best Time to Visit",""))
    ls    = ", ".join(filter(None,[city,state]))
    try:
        rv   = float(r.get(RCOL,"") if RCOL else "")
        ratb = f'<span class="gb">{G_SVG} {rv:.1f} ★</span>'
    except: ratb = ""
    tb   = f'<span class="b bt">{ptype}</span>' if ptype and ptype!="nan" else ""
    bb   = f'<span class="b bb">🌤 {best}</span>' if best and best!="nan" else ""
    dirb = (f'<a href="https://www.google.com/maps/dir/{urllib.parse.quote_plus(loc)}/{urllib.parse.quote_plus(nm+" "+ls+" India")}" target="_blank" class="mb mb2" style="margin-left:6px">🧭 Directions</a>' if loc else "")
    html += (f'<div class="pc"><div class="pn-wrap"><span class="pn">{nm}</span></div>'
             f'<div class="pl">📍 {ls}</div><div class="bwrap">{tb}{ratb}{bb}</div>'
             f'<div style="display:flex;flex-wrap:wrap;gap:5px"><a href="{gmap(nm+" "+ls+" India")}" target="_blank" class="mb">🗺️ Maps</a>{dirb}</div></div>')
html += '</div>'
st.markdown(html, unsafe_allow_html=True)

dcols = [c for c in ["Name","Place Name","City","State","Type","Google review rating","Rating","Best Time to Visit"] if c in filt.columns]
with st.expander(f"📋 View all {n} places"):
    df_show = filt[dcols].copy()
    if "Google review rating" in df_show.columns: df_show.rename(columns={"Google review rating":"⭐ Google Review"}, inplace=True)
    st.dataframe(df_show, use_container_width=True)

# ── MAP ───────────────────────────────────────────────────────────────────────
if show_map:
    st.markdown('<div class="sh">🗺️ Map Preview</div>', unsafe_allow_html=True)
    fr = top.iloc[0] if len(top) else None
    mq = (f"{fr.get('Name') or fr.get('Place Name','')} {fr.get('State','')} India" if fr is not None
          else f"{sel_state} India" if sel_state!="— All States —" else "India tourist places")
    c1, c2 = st.columns([2,1])
    with c1:
        st.markdown(f'<div class="map-wrap"><iframe src="{gembed(mq)}" height="380" style="border:0" allowfullscreen loading="lazy"></iframe></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<p style="font-family:\'Playfair Display\',serif;font-weight:600;margin:.5rem 0">📍 Quick Links</p>', unsafe_allow_html=True)
        for _, r in top.head(5).iterrows():
            nm = r.get("Name") or r.get("Place Name","Place")
            st.markdown(f'<a href="{gmap(nm+" "+str(r.get("City",""))+" "+str(r.get("State",""))+" India")}" target="_blank" class="mb" style="display:block;margin-bottom:7px">📍 {nm}</a>', unsafe_allow_html=True)

# ── AGENTS ────────────────────────────────────────────────────────────────────
if show_ag:
    st.markdown('<div class="sh">🤝 Recommended Agents</div>', unsafe_allow_html=True)
    agents = list({a["name"]:a for a in AGENTS.get(sel_state, DEFAULT_AGENTS)}.values())
    cols   = st.columns(min(3, len(agents)))
    for i, a in enumerate(agents[:6]):
        with cols[i % len(cols)]:
            r_val      = float(a["rating"])
            star_color = "#f5c518" if r_val >= 4.5 else "#e8a020" if r_val >= 4.0 else "#9cbfbc"
            card = (
                '<div style="background:#ffffff;border:1.5px solid #e2dbd0;border-radius:16px;'
                'overflow:hidden;box-shadow:0 4px 18px rgba(28,43,42,.10);margin-bottom:4px">'
                # accent bar
                '<div style="height:4px;background:linear-gradient(90deg,#c8502a,#e8a020)"></div>'
                '<div style="padding:14px 15px 13px">'
                # rating badge float right
                f'<div style="float:right;display:inline-flex;align-items:center;gap:4px;'
                f'background:linear-gradient(135deg,#1c2b2a,#2d4f4e);'
                f'color:{star_color};font-weight:800;font-size:.84rem;'
                f'padding:3px 11px;border-radius:100px;margin-left:8px;white-space:nowrap">'
                f'{a["rating"]} ★</div>'
                # agency name — bold, dark, Playfair
                f'<div style="font-family:Playfair Display,serif;font-size:1.05rem;'
                f'font-weight:700;color:#1c2b2a;line-height:1.35;'
                f'margin-bottom:9px;overflow:hidden">{a["name"]}</div>'
                # specialty pill
                f'<div style="margin-bottom:10px">'
                f'<span style="display:inline-block;background:#1a7a6e15;'
                f'color:#1a7a6e;border:1px solid #1a7a6e44;'
                f'padding:3px 11px;border-radius:100px;font-size:.71rem;'
                f'font-weight:700;letter-spacing:.05em;text-transform:uppercase">'
                f'{a["specialty"]}</span></div>'
                # divider
                '<div style="border-top:1px solid #f0ebe3;margin-bottom:9px"></div>'
                # contacts
                '<div style="display:flex;flex-direction:column;gap:5px">'
                f'<div style="display:flex;align-items:center;gap:7px;'
                f'font-size:.8rem;font-weight:600;color:#2d4040">'
                f'<span>📞</span>{a["phone"]}</div>'
                f'<div style="display:flex;align-items:center;gap:7px;'
                f'font-size:.8rem;font-weight:600;color:#2d4040">'
                f'<span>✉️</span>{a["email"]}</div>'
                '</div>'
                '</div></div>'
            )
            st.markdown(card, unsafe_allow_html=True)

# ── COST ──────────────────────────────────────────────────────────────────────
if show_cost:
    st.markdown('<div class="sh">💰 Cost Estimate</div>', unsafe_allow_html=True)
    c1, c2 = st.columns([3,2])
    WAIVED = {"🏨 Accommodation":"sleeping at home","🚌 Inter-city Travel":"no ticket needed"}
    with c1:
        rows = ""
        for k, v in costs.items():
            wn  = f' <span style="font-size:.62rem;color:#1a7a6e">(waived – {WAIVED[k]})</span>' if local_trip and k in WAIVED else ""
            rows += f'<div class="cr"><span class="ci">{k}{wn}</span><span class="ca">₹{v:,.0f}</span></div>'
        st.markdown(f'<div class="cc"><div class="ct">📊 {"🏠 Local" if local_trip else "🚀 Outstation"} · {tier} · {duration} days</div>{rows}<div class="cr" style="margin-top:10px;border-top:2px solid rgba(255,255,255,.15);padding-top:10px;border-bottom:none"><span style="color:#e8a020;font-weight:700">💎 Total (per person)</span><span style="font-family:\'Playfair Display\',serif;font-size:1.3rem;color:#e8a020;font-weight:700">₹{total:,.0f}</span></div></div>', unsafe_allow_html=True)
    with c2:
        p = TIERS[tier]; sn = min(n, max(1, int(int(duration)*1.5)))
        calc_rows = [
            ("🏨", "Stay",   "₹0 — sleeping at home" if local_trip else f"₹{p['stay']:,}/night × {duration} nights"),
            ("🍽️", "Food",  f"₹{p['food']:,}/day × {duration} days"),
            ("🚗", "Local",  f"₹{int(p['local']*.55):,}/day (city autos)" if local_trip else f"₹{p['local']:,}/day"),
            ("🎫", "Entry",  f"₹{p['entry']:,} × {sn} sights"),
            ("🚌", "Travel", "₹0 — no ticket needed" if local_trip else f"₹{OW[intercity]:,} × 2 (round trip)"),
            ("💼", "Misc",   "5% of daily costs"),
        ]

        def make_row(icon, label, value, is_zero):
            bg     = "#f0faf7" if is_zero else "#f9f6f1"
            border = "#1a7a6e55" if is_zero else "#e0d8cc"
            lcolor = "#0a5c4a" if is_zero else "#2d3a3a"
            vcolor = "#0a5c4a" if is_zero else "#1c2b2a"
            return (
                f'<div style="display:flex;justify-content:space-between;align-items:center;'
                f'padding:9px 12px;margin-bottom:6px;border-radius:10px;'
                f'background:{bg};border:1px solid {border}">'
                f'<div style="display:flex;align-items:center;gap:8px">'
                f'<span style="font-size:.9rem">{icon}</span>'
                f'<span style="font-size:.79rem;font-weight:800;color:{lcolor};'
                f'text-transform:uppercase;letter-spacing:.05em">{label}</span>'
                f'</div>'
                f'<span style="font-size:.79rem;font-weight:700;color:{vcolor};'
                f'text-align:right;padding-left:8px">{value}</span>'
                f'</div>'
            )

        row_cards = "".join(
            make_row(icon, label, value, local_trip and label in ("Stay", "Travel"))
            for icon, label, value in calc_rows
        )

        tip1 = ('<div style="display:flex;align-items:flex-start;gap:8px;padding:9px 11px;'
                'background:#fffbee;border-radius:9px;border:1px solid #e8a02066;border-left:4px solid #e8a020;margin-bottom:6px">'
                '<span style="font-size:.85rem;flex-shrink:0">💡</span>'
                '<span style="font-size:.79rem;font-weight:700;color:#7a5500;line-height:1.5">'
                'Book via agents above for <u>15-25% off</u>.</span></div>')
        tip2 = ('<div style="display:flex;align-items:flex-start;gap:8px;padding:9px 11px;'
                'background:#eef8f5;border-radius:9px;border:1px solid #1a7a6e55;border-left:4px solid #1a7a6e">'
                '<span style="font-size:.85rem;flex-shrink:0">&#9888;&#65039;</span>'
                '<span style="font-size:.79rem;font-weight:700;color:#0d4f3c;line-height:1.5">'
                'Prices vary by season, booking time &amp; city tier.</span></div>')

        header = ('<div style="background:linear-gradient(135deg,#1c2b2a,#2d4f4e);'
                  'padding:13px 16px;display:flex;align-items:center;gap:9px">'
                  '<span style="font-size:1rem">📋</span>'
                  '<span style="font-family:Playfair Display,serif;font-size:1rem;'
                  'font-weight:700;color:#e8a020">How We Calculated</span></div>')

        html_card = (
            '<div style="border-radius:16px;overflow:hidden;border:2px solid #d6cfc5;'
            'box-shadow:0 6px 24px rgba(28,43,42,.13)">'
            + header
            + '<div style="background:#ffffff;padding:12px 12px 6px">' + row_cards + '</div>'
            + '<div style="background:#ffffff;padding:4px 12px 12px">' + tip1 + tip2 + '</div>'
            + '</div>'
        )
        st.markdown(html_card, unsafe_allow_html=True)

st.markdown('<div style="text-align:center;padding:2rem 0 1rem;margin-top:2rem;border-top:1px solid rgba(26,122,110,.12)"><span style="font-family:\'Playfair Display\',serif;color:#1c2b2a">🌍 TourFinder India</span> <span style="color:#9cbfbc;font-size:.8rem">Empowering every Indian journey ✈️</span></div>', unsafe_allow_html=True)
