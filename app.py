import streamlit as st
import pandas as pd
import urllib.parse

st.set_page_config(page_title="TourFinder India", page_icon="🌍", layout="wide", initial_sidebar_state="expanded")

# ── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@300;400;600&display=swap" rel="stylesheet">
<style>
:root{--spice:#c8502a;--gold:#e8a020;--teal:#1a7a6e;--deep:#1c2b2a;--muted:#6b7c7b;--card:#ffffffcc;--r:16px;--sh:0 6px 24px rgba(28,43,42,.1)}
html,body,[class*="css"]{font-family:'DM Sans',sans-serif!important;color:var(--deep)}
.stApp{background:linear-gradient(160deg,#f5ede0,#fdf8f2 60%,#e8f5f3);min-height:100vh}
section[data-testid="stSidebar"]{background:linear-gradient(180deg,#1c2b2a,#0f1d1c)!important;border-right:1px solid #2e4443}
section[data-testid="stSidebar"] *{color:#d4e8e6!important}
section[data-testid="stSidebar"] h2,section[data-testid="stSidebar"] h3{color:#e8a020!important;font-family:'Playfair Display',serif!important}
section[data-testid="stSidebar"] label{color:#9cbfbc!important;font-size:.75rem!important;text-transform:uppercase;letter-spacing:.06em}
section[data-testid="stSidebar"] .stMultiSelect [data-baseweb="tag"]{background:#c8502a!important}
.hero{background:linear-gradient(135deg,#1c2b2a,#2d4f4e,#1a7a6e);border-radius:22px;padding:3rem;margin-bottom:2rem;box-shadow:0 16px 48px rgba(28,43,42,.3);position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;inset:0;background:radial-gradient(circle at 80% 20%,#e8a02033,transparent 50%)}
.hero h1{font-family:'Playfair Display',serif;font-size:clamp(1.8rem,4vw,3rem);color:#fff;margin:0 0 .5rem;line-height:1.2}
.hero h1 span{color:#e8a020}
.hero p{color:#9cbfbccc;font-size:1rem;margin:0}
.badge-hero{display:inline-flex;align-items:center;gap:6px;background:#c8502a22;border:1px solid #c8502a66;color:#e8a020;font-size:.7rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:3px 12px;border-radius:100px;margin-bottom:1rem}
.mrow{display:flex;gap:14px;flex-wrap:wrap;margin-bottom:1.4rem}
.mc{background:var(--card);border:1px solid rgba(200,80,42,.15);border-radius:13px;padding:1rem 1.3rem;flex:1;min-width:130px;box-shadow:var(--sh);transition:transform .2s}
.mc:hover{transform:translateY(-3px)}
.ml{font-size:.68rem;font-weight:600;color:var(--muted);text-transform:uppercase;letter-spacing:.07em;margin-bottom:3px}
.mv{font-family:'Playfair Display',serif;font-size:1.5rem;font-weight:700;color:var(--spice)}
.sh{font-family:'Playfair Display',serif;font-size:1.4rem;font-weight:700;color:var(--deep);display:flex;align-items:center;gap:10px;margin:2rem 0 1rem;padding-bottom:.4rem;border-bottom:2px solid #e8a02033}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:18px}
.pc{background:var(--card);border:1px solid rgba(26,122,110,.15);border-radius:var(--r);padding:1.3rem;box-shadow:var(--sh);transition:transform .25s;position:relative;overflow:hidden}
.pc::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,var(--spice),var(--gold))}
.pc:hover{transform:translateY(-4px)}
.pc:hover .pn{background-size:100% 2px}
.pn{
  font-family:'Playfair Display',serif;
  font-size:1.15rem;font-weight:700;
  color:var(--deep);
  margin-bottom:6px;
  display:inline-block;
  background:linear-gradient(var(--gold),var(--gold)) no-repeat left bottom / 0% 2px;
  transition:background-size .35s ease;
  padding-bottom:2px;
  letter-spacing:.01em;
}
.pn-wrap{
  background:linear-gradient(135deg,rgba(232,160,32,.08),rgba(200,80,42,.05));
  border-left:3px solid var(--gold);
  border-radius:0 8px 8px 0;
  padding:.45rem .75rem .45rem .75rem;
  margin-bottom:8px;
}
.pl{font-size:.8rem;color:var(--muted);margin-bottom:9px}
.bwrap{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:10px}
.b{font-size:.67rem;font-weight:600;padding:2px 9px;border-radius:100px;letter-spacing:.04em}
.bt{background:#1a7a6e18;color:#1a7a6e;border:1px solid #1a7a6e33}
.br{background:#e8a02018;color:#b57a00;border:1px solid #e8a02033}
.bb{background:#c8502a15;color:#c8502a;border:1px solid #c8502a33}
.google-badge{display:inline-flex;align-items:center;gap:4px;background:#4285F408;border:1px solid #4285F433;color:#4285F4;font-size:.67rem;font-weight:700;padding:2px 9px;border-radius:100px;letter-spacing:.04em}
.mb{display:inline-flex;align-items:center;gap:5px;background:linear-gradient(135deg,#1c2b2a,#1a7a6e);color:#fff!important;text-decoration:none;font-size:.76rem;font-weight:600;padding:6px 14px;border-radius:100px;transition:opacity .2s}
.mb:hover{opacity:.85}
.mb2{background:linear-gradient(135deg,#c8502a,#e8a020)!important}
.cc{background:linear-gradient(135deg,#1c2b2a,#2d4f4e);border-radius:var(--r);padding:1.8rem;color:#fff;box-shadow:var(--sh);position:relative;overflow:hidden}
.cc::after{content:'₹';position:absolute;right:-8px;bottom:-28px;font-size:8rem;opacity:.05;font-family:'Playfair Display',serif}
.ct{font-family:'Playfair Display',serif;font-size:1.2rem;color:#e8a020;margin-bottom:.9rem}
.cr{display:flex;justify-content:space-between;padding:7px 0;border-bottom:1px solid rgba(255,255,255,.08)}
.ci{font-size:.85rem;color:#9cbfbc}.ca{font-family:'Playfair Display',serif;font-size:.95rem;color:#fff;font-weight:600}
.ac{background:var(--card);border:1px solid rgba(200,80,42,.2);border-radius:13px;padding:1.1rem 1.3rem;margin-bottom:10px;transition:transform .2s}
.ac:hover{transform:translateX(4px)}
.an{font-weight:600;font-size:.94rem;margin-bottom:3px}
.ai{font-size:.78rem;color:var(--muted)}
.stButton>button{background:linear-gradient(135deg,#c8502a,#e8a020)!important;color:#fff!important;border:none!important;border-radius:100px!important;font-weight:600!important;padding:.5rem 1.5rem!important;box-shadow:0 4px 14px rgba(200,80,42,.35)!important}
.stButton>button:hover{transform:translateY(-2px)!important;box-shadow:0 7px 20px rgba(200,80,42,.45)!important}
.map-wrap{border-radius:var(--r);overflow:hidden;box-shadow:var(--sh);border:1px solid rgba(26,122,110,.15)}
.map-wrap iframe{display:block;width:100%}
hr{border-color:rgba(26,122,110,.12)!important}
</style>""", unsafe_allow_html=True)

# ── AGENTS ────────────────────────────────────────────────────────────────────
AGENTS = {
    "Rajasthan":[{"name":"Rajasthan Travels Pvt. Ltd.","phone":"+91-141-2360000","email":"info@rajasthantravels.com","rating":4.7,"specialty":"Heritage & Desert"},{"name":"Royal Rajasthan Tours","phone":"+91-141-5120400","email":"bookings@royalraj.com","rating":4.5,"specialty":"Palace & Wildlife"},{"name":"Pink City Tour Co.","phone":"+91-141-4072000","email":"hello@pinkcitytours.in","rating":4.4,"specialty":"Cultural & Festival"}],
    "Kerala":[{"name":"Kerala Tourism Board","phone":"+91-471-2321132","email":"info@keralatourism.org","rating":4.8,"specialty":"Backwaters & Ayurveda"},{"name":"Green Kerala Travels","phone":"+91-484-2380000","email":"green@keralatravels.com","rating":4.6,"specialty":"Eco & Nature"},{"name":"Alleppey Cruises","phone":"+91-477-2232400","email":"cruise@alleppey.in","rating":4.5,"specialty":"Houseboat & Backwater"}],
    "Goa":[{"name":"Goa Travel Experts","phone":"+91-832-2420000","email":"goa@travelexperts.com","rating":4.6,"specialty":"Beach & Adventure"},{"name":"Coastal Goa Tours","phone":"+91-832-2650000","email":"info@coastalgoa.com","rating":4.4,"specialty":"Heritage & Beach"},{"name":"Panjim Tours","phone":"+91-832-2224000","email":"book@panjimtours.in","rating":4.3,"specialty":"City & Spice"}],
    "Tamil Nadu":[{"name":"TN Tourism Dev. Corp.","phone":"+91-44-25367776","email":"info@tntourism.in","rating":4.7,"specialty":"Temple & Cultural"},{"name":"Chennai Travel Circle","phone":"+91-44-42060000","email":"hello@chennaicircle.com","rating":4.4,"specialty":"City & Heritage"},{"name":"South India Pilgrim Tours","phone":"+91-44-24340000","email":"pilgrim@siptours.com","rating":4.5,"specialty":"Pilgrim & Religious"}],
    "Uttar Pradesh":[{"name":"UP Tourism Pvt. Ltd.","phone":"+91-522-2239516","email":"info@uptourism.gov.in","rating":4.6,"specialty":"Heritage & Pilgrimage"},{"name":"Agra Golden Triangle","phone":"+91-562-2227000","email":"agra@goldentriangle.in","rating":4.5,"specialty":"Taj Mahal & Mughal"},{"name":"Varanasi Spiritual Journeys","phone":"+91-542-2501000","email":"ganga@spiritualtours.in","rating":4.7,"specialty":"Spiritual & Ganga"}],
    "Maharashtra":[{"name":"MTDC Maharashtra","phone":"+91-22-22024482","email":"info@maharashtratourism.gov.in","rating":4.6,"specialty":"Adventure & Heritage"},{"name":"Mumbai City Explorers","phone":"+91-22-26500000","email":"explore@mumbaitours.com","rating":4.4,"specialty":"City & Bollywood"},{"name":"Pune Weekend Getaways","phone":"+91-20-27200000","email":"pune@weekendaway.in","rating":4.3,"specialty":"Forts & Nature"}],
    "Himachal Pradesh":[{"name":"HP Tourism Dev. Corp.","phone":"+91-177-2652561","email":"hptdc@hptravels.com","rating":4.7,"specialty":"Mountains & Trekking"},{"name":"Manali Adventure Trails","phone":"+91-1902-252000","email":"trek@manalitrails.com","rating":4.6,"specialty":"Snow & Adventure"},{"name":"Shimla Heritage Holidays","phone":"+91-177-2804000","email":"shimla@heritageholidays.in","rating":4.4,"specialty":"Colonial & Nature"}],
    "West Bengal":[{"name":"West Bengal Tourism","phone":"+91-33-22485917","email":"info@wbtourism.gov.in","rating":4.5,"specialty":"Cultural & Darjeeling"},{"name":"Kolkata Walks","phone":"+91-33-22150000","email":"walk@kolkatawalks.com","rating":4.6,"specialty":"Heritage City Walks"},{"name":"Darjeeling Tea Trails","phone":"+91-354-2254000","email":"tea@darjeeling.in","rating":4.7,"specialty":"Tea Gardens & Himalaya"}],
    "Karnataka":[{"name":"Karnataka Tourism Dept.","phone":"+91-80-22352828","email":"ktdc@karnataka.gov.in","rating":4.6,"specialty":"Heritage & Wildlife"},{"name":"Mysuru Palace Tours","phone":"+91-821-2421096","email":"palace@mysururoyaltours.com","rating":4.7,"specialty":"Royal & Cultural"},{"name":"Coorg Coffee Country","phone":"+91-8272-220000","email":"coorg@coffeecountry.in","rating":4.5,"specialty":"Plantation & Nature"}],
    "Gujarat":[{"name":"Gujarat Tourism Corp.","phone":"+91-79-23238665","email":"info@gujarattourism.com","rating":4.5,"specialty":"Heritage & Wildlife"},{"name":"Rann Utsav Packages","phone":"+91-2757-221000","email":"rann@whitesaltfest.in","rating":4.7,"specialty":"Rann of Kutch"},{"name":"Ahmedabad Heritage Walks","phone":"+91-79-25506000","email":"heritage@amdwalks.com","rating":4.4,"specialty":"UNESCO City Walks"}],
    "Andhra Pradesh":[{"name":"APTDC – AP Tourism","phone":"+91-40-23454600","email":"info@aptourism.gov.in","rating":4.5,"specialty":"Pilgrimage & Heritage"},{"name":"Tirupati Darshan Travels","phone":"+91-877-2230000","email":"book@tirupatitours.com","rating":4.7,"specialty":"Tirumala & Pilgrim"},{"name":"Vizag Beach Tours","phone":"+91-891-2750000","email":"vizag@beachtours.in","rating":4.4,"specialty":"Coastal & Nature"}],
    "Telangana":[{"name":"Telangana Tourism Corp.","phone":"+91-40-23454600","email":"info@telanganatourism.gov.in","rating":4.5,"specialty":"Heritage & Wildlife"},{"name":"Hyderabad City Tours","phone":"+91-40-27900000","email":"hyd@citytours.in","rating":4.4,"specialty":"Nizami & Food Tours"},{"name":"Nagarjunasagar Travels","phone":"+91-8642-241000","email":"book@nagarjunatours.com","rating":4.3,"specialty":"Buddhist & Dam Tours"}],
}
DEFAULT_AGENTS=[{"name":"India Tourism Dev. Corp.","phone":"+91-11-23320005","email":"info@itdc.co.in","rating":4.3,"specialty":"Pan-India Tours"},{"name":"Thomas Cook India","phone":"+91-22-67406720","email":"book@thomascook.in","rating":4.4,"specialty":"Customised Holidays"},{"name":"MakeMyTrip Holidays","phone":"+91-124-4628747","email":"care@makemytrip.com","rating":4.2,"specialty":"Online Packages"}]

# ── COST PRESETS ──────────────────────────────────────────────────────────────
COST_PRESETS = {
    "Budget 🎒":   {"stay":700,  "food":350, "local":250, "entry":60},
    "Mid-Range 🏨":{"stay":2000, "food":800, "local":500, "entry":120},
    "Luxury 🌟":   {"stay":5000, "food":1800,"local":1000,"entry":300},
}
INTERCITY = {"Bus 🚌":600,"Train 🚂":1200,"Flight ✈️":4000}

def estimate_cost(days, n_places, tier, intercity):
    p = COST_PRESETS[tier]
    stay    = p["stay"]  * days
    food    = p["food"]  * days
    local   = p["local"] * days
    entries = p["entry"] * min(n_places, days * 2)
    travel  = INTERCITY[intercity] * max(1, (days - 1) // 2)
    misc    = int((stay + food + local) * 0.06)
    total   = stay + food + local + entries + travel + misc
    return {"🏨 Accommodation":stay,"🍽️ Food & Drinks":food,"🚗 Local Transport":local,
            "🎫 Entry Fees":entries,"🚌 Inter-city Travel":travel,"💼 Misc (6%)":misc,"__TOTAL__":total}

# ── HELPERS ───────────────────────────────────────────────────────────────────
def gmap(q):  return f"https://www.google.com/maps/search/{urllib.parse.quote_plus(q)}"
def gembed(q):return f"https://maps.google.com/maps?q={urllib.parse.quote_plus(q)}&output=embed&z=12"

def stars_html(rating_val):
    """Convert numeric rating to filled/half/empty star HTML string."""
    try:
        r = float(rating_val)
        full  = int(r)
        half  = 1 if (r - full) >= 0.4 else 0
        empty = 5 - full - half
        return (
            '<span style="color:#fbbc04;font-size:.8rem">' +
            "★" * full +
            ("½" if half else "") +
            '<span style="color:#ccc">' + "★" * empty + '</span></span>'
        )
    except Exception:
        return ""

# ── LOAD DATA ─────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    path = r"C:\\Users\\Ramsai vakkapatla\\Downloads\\Top Indian Places to Visit.csv"
    try:
        df = pd.read_csv(path)
        df.columns = df.columns.str.strip()

        # ── Detect & normalise the Google review rating column ──────────────
        # The Kaggle dataset uses "Google review rating"; handle common variants
        GOOGLE_COL_CANDIDATES = [
            "Google review rating",
            "Google Review Rating",
            "google review rating",
            "Google Reviews",
            "google_review_rating",
            "GoogleReviewRating",
        ]
        google_col = None
        for candidate in GOOGLE_COL_CANDIDATES:
            if candidate in df.columns:
                google_col = candidate
                break

        if google_col and google_col != "Google review rating":
            df.rename(columns={google_col: "Google review rating"}, inplace=True)

        # Convert to numeric; coerce errors → NaN
        if "Google review rating" in df.columns:
            df["Google review rating"] = pd.to_numeric(
                df["Google review rating"], errors="coerce"
            )

        return df, None
    except FileNotFoundError:
        return None, f"File not found: `{path}`"

data, err = load_data()

# ── Determine the active rating column ───────────────────────────────────────
# Priority: "Google review rating" (from CSV) > "Rating" (fallback)
def get_rating_col(df):
    if df is None:
        return None
    if "Google review rating" in df.columns:
        return "Google review rating"
    if "Rating" in df.columns:
        return "Rating"
    return None

RATING_COL = get_rating_col(data)

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="badge-hero">🧭 India's Premier Travel Planner</div>
  <h1>Discover <span>Incredible India</span><br>One Place at a Time</h1>
  <p>Filter destinations · Estimate budget · Find agents · Open in Google Maps</p>
</div>""", unsafe_allow_html=True)

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
sb = st.sidebar
sb.markdown("## 🔎 Discover & Plan")

if err: st.error(f"⚠️ {err}"); st.stop()

# ── Starting Location ──
sb.markdown("### 📌 Your Starting Location")
start_loc = sb.text_input("Your current city", placeholder="e.g. Eluru, Vijayawada…")
sb.markdown("---")

# ── Cascading Destination Filters ──
sb.markdown("### 📍 Destination Filters")

all_states = sorted(data["State"].dropna().unique()) if "State" in data.columns else []
sel_state  = sb.selectbox("① Select State", ["— All States —"] + all_states)

df_s = data[data["State"] == sel_state] if sel_state != "— All States —" else data
all_cities = sorted(df_s["City"].dropna().unique()) if "City" in df_s.columns else []
sel_city   = sb.selectbox("② Select City", ["— All Cities —"] + all_cities)

df_sc = df_s[df_s["City"] == sel_city] if sel_city != "— All Cities —" else df_s
all_types = sorted(df_sc["Type"].dropna().unique()) if "Type" in df_sc.columns else []

if sel_state != "— All States —" or sel_city != "— All Cities —":
    scope = sel_city if sel_city != "— All Cities —" else sel_state
    sb.markdown(f'<div style="font-size:.72rem;color:#9cbfbc80;font-style:italic;padding-bottom:4px">✦ {len(all_types)} types in {scope}</div>', unsafe_allow_html=True)

sel_type = sb.selectbox("③ Select Place Type", ["— All Types —"] + all_types)

# ── Rating slider – uses Google review rating if available ──
if RATING_COL:
    col_min = float(data[RATING_COL].min()) if data[RATING_COL].notna().any() else 0.0
    col_max = float(data[RATING_COL].max()) if data[RATING_COL].notna().any() else 5.0
    slider_label = (
        "Minimum Google Review ⭐" if RATING_COL == "Google review rating"
        else "Minimum Rating ⭐"
    )
    min_rating = sb.slider(slider_label, col_min, col_max, max(col_min, 3.0), 0.1)
else:
    min_rating = 0.0

sb.markdown("---")

# ── Trip Details ──
sb.markdown("### 🗓️ Trip Details")
duration      = sb.number_input("Tour Duration (days)", 1, 60, 5, 1)
budget_tier   = sb.selectbox("Budget Tier", list(COST_PRESETS.keys()), index=1)
intercity_mode= sb.selectbox("Inter-city Transport", list(INTERCITY.keys()), index=1)
show_map      = sb.checkbox("📍 Show Map Preview", True)
show_agents   = sb.checkbox("🤝 Show Tourist Agents", True)
show_cost     = sb.checkbox("💰 Show Cost Estimate", True)
sb.markdown("---")
generate = sb.button("✨ Generate My Plan", use_container_width=True)
reset    = sb.button("🔄 Reset",            use_container_width=True)

# ── Session ───────────────────────────────────────────────────────────────────
if reset: st.session_state.clear(); st.rerun()
if generate:
    st.session_state["show"] = True
    st.session_state["loc"]  = start_loc.strip()

if not st.session_state.get("show"):
    st.markdown("""<div style="text-align:center;padding:4rem 0">
      <div style="font-size:4rem">🗺️</div>
      <div style="font-family:'Playfair Display',serif;font-size:1.5rem;color:#1c2b2a;margin:.4rem 0">Your Adventure Awaits</div>
      <div style="color:#6b7c7b;max-width:380px;margin:0 auto">Set your filters in the sidebar, then hit <strong>Generate My Plan</strong>.</div>
    </div>""", unsafe_allow_html=True)
    st.stop()

# ── Filter Data ───────────────────────────────────────────────────────────────
filt = data.copy()
if sel_state != "— All States —": filt = filt[filt["State"] == sel_state]
if sel_city  != "— All Cities —": filt = filt[filt["City"]  == sel_city]
if sel_type  != "— All Types —":  filt = filt[filt["Type"]  == sel_type]
if RATING_COL:
    filt = filt[pd.to_numeric(filt[RATING_COL], errors="coerce") >= min_rating]

n = len(filt)
if n == 0: st.error("❌ No places match. Try loosening your filters."); st.stop()

# ── Starting location banner ──────────────────────────────────────────────────
loc = st.session_state.get("loc", "")
if loc:
    st.markdown(f"""<div style="display:flex;align-items:center;gap:10px;background:linear-gradient(90deg,#1a7a6e18,transparent);border-left:3px solid #1a7a6e;border-radius:0 10px 10px 0;padding:.65rem 1.2rem;margin-bottom:1rem">
      <span style="font-size:1.1rem">📍</span>
      <div><div style="font-size:.68rem;color:#6b7c7b;text-transform:uppercase;letter-spacing:.07em;font-weight:600">Starting From</div>
      <div style="font-size:.92rem;color:#1c2b2a;font-weight:600">{loc}</div></div></div>""", unsafe_allow_html=True)

# ── Metrics ───────────────────────────────────────────────────────────────────
if RATING_COL:
    avg_r = pd.to_numeric(filt[RATING_COL], errors="coerce").mean()
    avg_r_str = f"{avg_r:.1f}"
else:
    avg_r_str = "—"

n_states= filt["State"].nunique() if "State" in filt.columns else "—"
costs   = estimate_cost(duration, n, budget_tier, intercity_mode)
total   = costs.pop("__TOTAL__")

rating_label = "Google ⭐" if RATING_COL == "Google review rating" else "⭐ Avg Rating"

st.markdown(f"""<div class="mrow">
  <div class="mc"><div class="ml">📍 Places</div><div class="mv">{n}</div></div>
  <div class="mc"><div class="ml">🗺️ States</div><div class="mv">{n_states}</div></div>
  <div class="mc"><div class="ml">{rating_label}</div><div class="mv">{avg_r_str}</div></div>
  <div class="mc"><div class="ml">🗓️ Days</div><div class="mv">{duration}</div></div>
  <div class="mc"><div class="ml">💰 Est. Budget</div><div class="mv">₹{total:,.0f}</div></div>
</div>""", unsafe_allow_html=True)

st.success(f"✅ **{n}** destinations found!")

# ── Place Cards ───────────────────────────────────────────────────────────────
st.markdown('<div class="sh">🏛️ Top Destinations</div>', unsafe_allow_html=True)
top = filt.head(12)

html = '<div class="pgrid">'
for _, r in top.iterrows():
    nm    = r.get("Name") or r.get("Place Name") or "—"
    city  = str(r.get("City",""))
    state = str(r.get("State",""))
    ptype = str(r.get("Type",""))
    best  = str(r.get("Best Time to Visit",""))
    loc_s = ", ".join(filter(None,[city,state]))
    murl  = gmap(f"{nm} {loc_s} India")

    # ── Google review rating (no API key – straight from CSV column) ──────
    raw_rating = r.get(RATING_COL, "") if RATING_COL else ""
    try:
        rat_val = float(raw_rating)
        rat_display = f"{rat_val:.1f}"
        rat_b = (
            f'<span class="google-badge">'
            f'<svg width="10" height="10" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg" style="vertical-align:middle">'
            f'<path d="M17.64 9.2c0-.637-.057-1.251-.164-1.84H9v3.481h4.844c-.209 1.125-.843 2.078-1.796 2.717v2.258h2.908c1.702-1.567 2.684-3.874 2.684-6.615z" fill="#4285F4"/>'
            f'<path d="M9 18c2.43 0 4.467-.806 5.956-2.18l-2.908-2.259c-.806.54-1.837.86-3.048.86-2.344 0-4.328-1.584-5.036-3.711H.957v2.332A8.997 8.997 0 009 18z" fill="#34A853"/>'
            f'<path d="M3.964 10.71A5.41 5.41 0 013.682 9c0-.593.102-1.17.282-1.71V4.958H.957A8.996 8.996 0 000 9c0 1.452.348 2.827.957 4.042l3.007-2.332z" fill="#FBBC05"/>'
            f'<path d="M9 3.58c1.321 0 2.508.454 3.44 1.345l2.582-2.58C13.463.891 11.426 0 9 0A8.997 8.997 0 00.957 4.958L3.964 7.29C4.672 5.163 6.656 3.58 9 3.58z" fill="#EA4335"/>'
            f'</svg>'
            f' {rat_display} ★</span>'
        )
    except (TypeError, ValueError):
        rat_b = ""   # no NaN shown – simply hide the badge

    dir_btn = ""
    if loc:
        durl = f"https://www.google.com/maps/dir/{urllib.parse.quote_plus(loc)}/{urllib.parse.quote_plus(nm+' '+loc_s+' India')}"
        dir_btn = f'<a href="{durl}" target="_blank" class="mb mb2" style="margin-left:6px">🧭 Directions</a>'

    type_b = f'<span class="b bt">{ptype}</span>' if ptype and ptype != "nan" else ""
    best_b = f'<span class="b bb">🌤 {best}</span>' if best and best != "nan" else ""

    html += (
        '<div class="pc">'
        '<div class="pn-wrap"><span class="pn">' + nm + '</span></div>'
        '<div class="pl">📍 ' + loc_s + '</div>'
        '<div class="bwrap">' + type_b + rat_b + best_b + '</div>'
        '<div style="display:flex;flex-wrap:wrap;gap:5px">'
        '<a href="' + murl + '" target="_blank" class="mb">🗺️ Open in Maps</a>' + dir_btn +
        '</div></div>'
    )
html += '</div>'
st.markdown(html, unsafe_allow_html=True)

# ── Show all places table (include Google review rating column) ───────────────
preferred_cols = ["Name","Place Name","City","State","Type",
                  "Google review rating","Rating","Best Time to Visit"]
dcols = [c for c in preferred_cols if c in filt.columns]

with st.expander(f"📋 View all {n} places"):
    display_df = filt[dcols].copy() if dcols else filt.copy()
    # Rename for clarity in the table header
    if "Google review rating" in display_df.columns:
        display_df.rename(columns={"Google review rating": "⭐ Google Review"}, inplace=True)
    st.dataframe(display_df, use_container_width=True)

# ── Map ───────────────────────────────────────────────────────────────────────
if show_map:
    st.markdown('<div class="sh">🗺️ Map Preview</div>', unsafe_allow_html=True)
    fr    = top.iloc[0] if len(top) else None
    mq    = f"{fr.get('Name') or fr.get('Place Name','')} {fr.get('State','')} India" if fr is not None else (f"{sel_state} India" if sel_state!="— All States —" else "India tourist places")
    c1,c2 = st.columns([2,1])
    with c1:
        st.markdown(f'<div class="map-wrap"><iframe src="{gembed(mq)}" height="380" style="border:0" allowfullscreen loading="lazy"></iframe></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<p style="font-family:\'Playfair Display\',serif;font-weight:600;margin:.5rem 0">📍 Quick Links</p>', unsafe_allow_html=True)
        for _, r in top.head(5).iterrows():
            nm = r.get("Name") or r.get("Place Name","Place")
            st.markdown(f'<a href="{gmap(f"{nm} {r.get(chr(67),"")} {r.get(chr(83),"")} India")}" target="_blank" class="mb" style="display:block;margin-bottom:7px">📍 {nm}</a>', unsafe_allow_html=True)

# ── Agents ────────────────────────────────────────────────────────────────────
if show_agents:
    st.markdown('<div class="sh">🤝 Recommended Tourist Agents</div>', unsafe_allow_html=True)
    raw = []
    if sel_state != "— All States —":
        raw = AGENTS.get(sel_state, DEFAULT_AGENTS)
    else:
        raw = DEFAULT_AGENTS
    seen, agents = set(), []
    for a in raw:
        if a["name"] not in seen: seen.add(a["name"]); agents.append(a)
    cols = st.columns(min(3, len(agents)))
    for i, a in enumerate(agents[:6]):
        with cols[i % len(cols)]:
            st.markdown(f"""<div class="ac">
              <div style="float:right;color:#e8a020;font-weight:700;font-size:.86rem">{a['rating']} ★</div>
              <div class="an">{a['name']}</div>
              <div class="ai"><span style="background:#1a7a6e18;color:#1a7a6e;padding:2px 7px;border-radius:100px;font-size:.68rem">{a['specialty']}</span></div>
              <div class="ai" style="margin-top:7px">📞 {a['phone']}<br>✉️ {a['email']}</div>
            </div>""", unsafe_allow_html=True)

# ── Cost ──────────────────────────────────────────────────────────────────────
if show_cost:
    st.markdown('<div class="sh">💰 Trip Cost Estimate</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        rows = "".join(f'<div class="cr"><span class="ci">{k}</span><span class="ca">₹{v:,.0f}</span></div>' for k,v in costs.items())
        st.markdown(f"""<div class="cc">
          <div class="ct">📊 {budget_tier} · {duration} Days</div>{rows}
          <div class="cr" style="margin-top:10px;border-top:1px solid rgba(255,255,255,.15);padding-top:10px;border-bottom:none">
            <span style="color:#e8a020;font-weight:700">💎 Total (per person)</span>
            <span style="font-family:'Playfair Display',serif;font-size:1.3rem;color:#e8a020;font-weight:700">₹{total:,.0f}</span>
          </div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div style="padding:1.3rem;background:rgba(255,255,255,.75);border-radius:16px;border:1px solid rgba(26,122,110,.15);box-shadow:var(--sh)">
          <p style="font-family:'Playfair Display',serif;font-size:1.1rem;font-weight:600;margin-bottom:.8rem">📝 Notes</p>
          <ul style="font-size:.83rem;color:#6b7c7b;line-height:2;padding-left:1.1rem;margin:0">
            <li>All costs are <strong>per person</strong> for <strong>{duration} days</strong>.</li>
            <li>Stay: {budget_tier.split()[0]}-tier hotels / guesthouses.</li>
            <li>Entry fees capped at 2 sights/day (realistic pace).</li>
            <li>Inter-city: <strong>{intercity_mode}</strong>.</li>
            <li style="color:#c8502a">Prices vary by season &amp; location.</li>
          </ul>
          <div style="margin-top:1rem;padding:9px 12px;background:#e8a02015;border-radius:9px;border-left:3px solid #e8a020;font-size:.8rem;color:#b57a00;font-weight:600">
            💡 Book via agents above for 15–25% package discounts.
          </div></div>""", unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""<div style="text-align:center;padding:2.5rem 0 1rem;margin-top:2.5rem;border-top:1px solid rgba(26,122,110,.12)">
  <span style="font-family:'Playfair Display',serif;color:#1c2b2a">🌍 TourFinder India</span>
  <span style="color:#9cbfbc;font-size:.8rem;margin-left:1rem">Empowering every Indian journey ✈️</span>
</div>""", unsafe_allow_html=True)