"""Design demo for We Buy Houses In West Georgia (Jimmy Harris), built on the RequityAI v2 system.

All copy, photos, reviews, phone, address and service areas come from the prospect's own site
(www.webuyhousesinwestgeorgia.com, read 2026-09-22) and his Google Business Profile (4.9 stars,
15 reviews, read 2026-09-22). SEO carry-over is deliberately NOT done yet: it happens after he
approves the design. Every page is noindex. Forms are demonstration only.
"""
from pathlib import Path
import re, html

ROOT = Path(__file__).resolve().parents[1]
BASE = '/westgeorgia-funnel/'
esc = html.escape
CSS_V = '20260922a'

COMPANY = 'We Buy Houses In West Georgia'
PHONE, TEL = '(404) 997-2197', 'tel:+14049972197'
EMAIL = 'Jimmy@WeBuyHousesInWestGeorgia.com'
ADDRESS = '283 Coppermine Rd<br>Buchanan, GA 30113'
GOOGLE_URL = 'https://www.google.com/maps/place/We+Buy+Houses+In+West+Georgia/data=!4m2!3m1!1s0x0:0x487ec71f87f9033d'
G_RATING, G_COUNT = '4.9', '15'
AREAS = ['Aragon', 'Bremen', 'Bowdon', 'Buchanan', 'Carrollton', 'Cedartown', 'Dallas', 'Douglasville', 'Hiram', 'Lithia Springs',
         'Marietta', 'Powder Springs', 'Rockmart', 'Temple', 'Villa Rica', 'Waco', 'Whitesburg', 'Winston']


def link(p=''):
    return BASE + p.lstrip('/')


QUIZ = link('get-a-cash-offer-today/')

ICONS = (Path('/Users/AndrewCherry/Documents/GitHub/homebuyerswi-funnel/site-source/build.py').read_text()
         .split("ICONS = '''", 1)[1].split("'''", 1)[0])
ICONS = ICONS.replace('<symbol id="i-book"', '<symbol id="i-shield" viewBox="0 0 24 24"><path d="M12 3 4.5 6v5.5c0 4.6 3.2 8.4 7.5 9.5 4.3-1.1 7.5-4.9 7.5-9.5V6Z"/><path d="m8.8 12.2 2.2 2.2 4.3-4.6"/></symbol><symbol id="i-book"')

SITUATIONS = [
    ('inherited', 'violet', 'I inherited a house', 'Estate', 'Inherited a house you don’t want', 'Probate, family decisions and a house full of belongings. Often from out of town.'),
    ('condition', 'gold', 'It needs a lot of work', 'Condition', 'Avoiding costly repairs', 'Smoke damage, flooding, a lived-in mess or a house nobody has touched in years.'),
    ('deadline', 'crimson', 'I want to avoid foreclosure', 'Time pressure', 'Want to avoid foreclosure', 'Behind on payments, a sale date on the calendar, or another reason time matters.'),
    ('rental', 'brand', 'I’m tired of being a landlord', 'Landlord', 'Tired of managing rental property', 'Tenants, repairs and a property you’re ready to let go of.'),
    ('moving', 'emerald', 'I’m relocating or starting over', 'Life change', 'Relocating, divorce or assisted living', 'Need to move quickly, separating, or helping a parent into assisted living.'),
    ('comparing', 'slate-l', 'I don’t want to list with an agent', 'Comparing', 'Don’t want to list with an agent', 'See a cash offer first, side by side with listing, before you commit to anything.'),
]

# Verbatim excerpts. Google texts read 2026-09-22 from the public listing; Nick and Wanda from the Google review
# images on his site; Cheralyn Pilgrim is an agent testimonial on his site. Individual star ratings are not shown.
REVIEWS = [
    ('Jimmy at We Buy Houses in West Georgia are the real deal!', 'Danny Johnson · Google review'),
    ('They made our home selling experience very simple and quick.', 'Heather Kirby · Google review'),
    ('I wish I could give Jimmy and the team more than 5 stars.', 'Kevin Richards · Google review'),
    ('Jimmy and his team really know their stuff and were a pleasure to work with.', 'Nick Castello · Google review'),
    ('We were VERY satisfied with our house selling experience with Jimmy.', 'Wanda Padgett · Google review'),
    ('I wish I had saved myself a lot of time and trouble and just contacted these guys first!', 'Danny Johnson · Google review'),
    ('The whole process was quick, efficient, and professional.', 'Kevin Richards · Google review'),
    ('They always closed on every home we got under contract!', 'Cheralyn Pilgrim · Agent, Cedartown, GA'),
]

FAQ = [
    ('Will you be listing my house or actually buying it?', 'We’re cash buyers, not agents. We can make an offer within 24 hours and close in as little as 7 days with a local attorney.'),
    ('Do you pay fair prices for properties?', 'We aim to offer the highest possible fair cash price, with no repairs, commissions, or closing costs for you.'),
    ('How do you determine the price to offer?', 'We consider the location, needed repairs, current condition, and recent comparable sales in your area.'),
    ('Are there any fees or commissions?', 'No. You won’t pay any fees or commissions when selling your home directly to us.'),
    ('How are you different from a real estate agent?', 'We buy houses directly for cash, providing faster closings without agent commissions or showings.'),
    ('Is there any obligation after I submit my info?', 'None at all. There’s no obligation. Review our offer and decide if it works for you.'),
]


def icon(name, cls=''):
    return f'<svg{" class=%s" % chr(34) + cls + chr(34) if cls else ""}><use href="#i-{name}"/></svg>'


def btn(label='Get my cash offer', href=QUIZ, cls='btn'):
    return f'<a class="{cls}" href="{href}">{label} {icon("arrow")}</a>'


def g_badge(cls=''):
    return (f'<a class="g-badge {cls}" href="{GOOGLE_URL}" target="_blank" rel="noopener"><span class="g-logo" aria-hidden="true">G</span><b>{G_RATING}</b>'
            f'<span class="stars" style="--rating:{G_RATING}" aria-hidden="true">★★★★★</span><small>{G_COUNT} Google reviews</small></a>')


def chips(cls='chips'):
    return f'<div class="{cls}">' + ''.join(
        f'<a class="chip" style="--c:var(--{c})" href="{QUIZ}?s={k}#quiz"><i>{icon(k)}</i><span>{label}</span>{icon("arrow", "go")}</a>'
        for k, c, label, *_ in SITUATIONS) + '</div>'


def review_ticker():
    items = ''.join(f'<li class="rt-item google"><span class="rt-q" aria-hidden="true">“</span><q>{esc(q)}</q><span class="rt-by">{esc(by)}</span></li>' for q, by in REVIEWS)
    return (f'<section class="review-ticker" aria-label="What sellers say about {COMPANY}">'
            f'<a class="rt-badge" href="{GOOGLE_URL}" target="_blank" rel="noopener"><span class="g-logo" aria-hidden="true">G</span><b>{G_RATING}</b>'
            f'<span class="stars" style="--rating:{G_RATING}" aria-hidden="true">★★★★★</span><small>{G_COUNT} Google reviews</small></a>'
            f'<div class="rt-viewport"><ul class="rt-track">{items}</ul><ul class="rt-track" aria-hidden="true">{items}</ul></div></section>')


def header(home=True):
    h = '' if home else link()
    nav = [('How it works', '#how'), ('Houses we’ve bought', '#bought'), ('Reviews', '#stories'), ('Areas', '#areas'), ('FAQs', '#faq')]
    return (f'<svg width="0" height="0" style="position:absolute" aria-hidden="true">{ICONS.split(">", 1)[1] if ICONS.lstrip().startswith("<svg") else ICONS}'
            f'<a class="skip" href="#main">Skip to content</a>'
            f'<div class="preview-bar">Design preview <span>Built for {COMPANY} · Forms are in demonstration mode</span></div>'
            f'<header class="site-header" data-header><div class="container nav">'
            f'<a class="logo" href="{link()}"><img src="{link("img/logo.png")}" alt="{COMPANY} home" width="430" height="321"></a>'
            f'<nav id="navigation" aria-label="Main navigation">' + ''.join(f'<a href="{h}{p}">{n}</a>' for n, p in nav) + '</nav>'
            f'<div class="nav-right"><a class="nav-phone" href="{TEL}">{icon("phone")}<span><small>Talk to Jimmy directly</small>{PHONE}</span></a>'
            f'<a class="btn btn-sm" href="{QUIZ}">Get my offer</a>'
            f'<button class="menu-toggle" aria-expanded="false" aria-controls="navigation"><span></span><span></span><span class="sr">Menu</span></button></div></div></header>')


def closing():
    return (f'<section class="closing"><div class="closing-rings"><span></span><span></span><span></span></div>'
            f'<div class="container closing-inner reveal"><p class="eyebrow light">Sell your house fast in West Georgia</p>'
            f'<h2>Tell us what’s going on. Jimmy will take it from there.</h2><p>A few questions, a real conversation, and no obligation to accept.</p>'
            f'<div class="closing-actions">{btn("Get my cash offer", cls="btn btn-lg")}<a class="btn-ghost" href="{TEL}">{icon("phone")}{PHONE}</a></div>'
            f'<ul class="closing-checks"><li>{icon("check")}No realtor</li><li>{icon("check")}No fees</li><li>{icon("check")}No repairs</li><li>{icon("check")}No cleaning</li></ul></div></section>')


def footer(sticky=True, home=True):
    h = '' if home else link()
    s = f'<div class="sticky-cta" data-sticky><a class="call" href="{TEL}" aria-label="Call {PHONE}">{icon("phone")}</a>{btn()}</div>' if sticky else ''
    return (f'<footer class="site-footer"><div class="container footer-grid">'
            f'<div class="footer-brand"><span class="logo-chip"><img src="{link("img/logo.png")}" alt="{COMPANY}" width="430" height="321"></span>'
            f'<p>Cash home buyers in Carrollton<br>and across West Georgia.</p>{g_badge("dark")}</div>'
            f'<div><b>Selling</b><a href="{QUIZ}">Get a cash offer</a><a href="{h}#how">How it works</a><a href="{h}#bought">Houses we’ve bought</a><a href="{h}#faq">Questions</a></div>'
            f'<div><b>Situations</b>' + ''.join(f'<a href="{QUIZ}?s={k}#quiz">{t}</a>' for k, _, _, _, t, _ in SITUATIONS[:5]) + '</div>'
            f'<div><b>Where we buy</b>' + ''.join(f'<span class="f-area">{a}</span>' for a in AREAS[:8]) + f'<a href="{h}#areas">All {len(AREAS)} areas</a></div>'
            f'<div><b>Talk to Jimmy</b><a class="footer-phone" href="{TEL}">{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a><p>{COMPANY}<br>{ADDRESS}</p>'
            f'<img class="bbb" src="{link("assets/bbb.png")}" alt="BBB Accredited Business" width="150" height="57"></div>'
            f'</div><div class="container footer-bottom">© 2026 {COMPANY} <span>Design preview by RequityAI · No inquiries are sent from this preview.</span></div></footer>'
            f'{s}<script src="{link("assets/site.js?v=" + CSS_V)}" defer></script>')


def page(title, body, description, extra='', body_cls='', sticky=True, home=True):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{esc(title)}</title><meta name="description" content="{esc(description)}"><meta name="robots" content="noindex,nofollow">'
            f'<meta name="theme-color" content="#0D1A2D"><link rel="icon" href="{link("img/favicon.png")}"><link rel="apple-touch-icon" href="{link("img/favicon.png")}">'
            f'<link rel="preload" href="{link("assets/source-sans.woff2")}" as="font" type="font/woff2" crossorigin>'
            f'<link rel="stylesheet" href="{link("assets/site.css?v=" + CSS_V)}"><script>document.documentElement.classList.add("js")</script>{extra}</head>'
            f'<body class="{body_cls}">{header(home)}{review_ticker()}<main id="main">{body}</main>{closing()}{footer(sticky, home)}</body></html>')


def write(path, content):
    p = ROOT / (path.strip('/') + '/index.html' if path.strip('/') else 'index.html')
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)


def img(name, alt, cls='', lazy=True):
    return f'<img{" class=%s" % chr(34) + cls + chr(34) if cls else ""} src="{link("assets/" + name)}" alt="{esc(alt)}"{" loading=" + chr(34) + "lazy" + chr(34) if lazy else ""} decoding="async">'


bought = [('bought-1.jpg', 'A ranch-style house with white siding, brown trim, and large tree in the front yard, bought by We Buy Houses in West Georgia'),
          ('bought-2.jpg', 'A ranch-style house with blue siding and brown brick, bought by We Buy Houses in West Georgia'),
          ('bought-3.jpg', 'A ranch-style red brick house with a closed carport, bought by We Buy Houses in West Georgia'),
          ('bought-4.jpg', 'A ranch-style house with white siding, black trim, and a carport, bought by We Buy Houses in West Georgia'),
          ('bought-5.jpg', 'A ranch-style house with white siding, gray trim, and several front windows, bought by We Buy Houses in West Georgia'),
          ('bought-6.jpg', 'A ranch house with beige siding and wooden shutters bought by We Buy Houses in West Georgia')]

home = f'''
<section class="hero">
  <div class="hero-glow g1"></div><div class="hero-glow g2"></div><div class="hero-dots"></div>
  <div class="container hero-grid">
    <div class="hero-copy">
      <p class="pill"><span class="pulse"></span>Carrollton &amp; West Georgia · Local cash house buyers</p>
      <h1><span class="h1-top">Sell your house fast</span> <span class="h1-bottom">in <span class="mark">Carrollton, GA<svg viewBox="0 0 300 24" preserveAspectRatio="none" aria-hidden="true"><path d="M3 17C60 7 180 3 297 12"/></svg></span></span></h1>
      <ul class="hero-points"><li>{icon("check")}No realtor</li><li>{icon("check")}No fees</li><li>{icon("check")}No repairs</li><li>{icon("check")}No cleaning</li></ul>
      <p class="lede">We are cash house buyers, and we buy houses as-is. When you call, you get our founder, Jimmy, directly on the phone.</p>
      <div class="picker"><p class="picker-title">What’s going on with the house? <span>Pick one to start</span></p>{chips()}
        <p class="picker-foot">A few quick questions so Jimmy calls you already knowing your situation. <a href="{TEL}">Or call {PHONE}</a></p></div>
    </div>
    <div class="hero-visual">
      <div class="arch-ring"></div>
      <figure class="arch">{img("jimmy-shayna.jpg", "Jimmy and Shayna from We Buy Houses in West Georgia", lazy=False)}</figure>
      <div class="float-card hello"><span class="avatar-dot"></span><div><small>Your local buyers</small><b>Hi, we’re Jimmy &amp; Shayna.</b></div></div>
      <blockquote class="float-card quote"><p>“Jimmy at We Buy Houses in West Georgia are the real deal!”</p><footer>Danny Johnson · Google review</footer></blockquote>
      {g_badge("float-card rating")}
    </div>
  </div>
</section>

<section class="benefits"><div class="container"><ul class="benefit-card">
  <li style="--c:var(--emerald)"><i>{icon("cash")}</i><div><b>No fees or closing costs</b><span>We handle all closing costs</span></div></li>
  <li style="--c:var(--brand)"><i>{icon("calendar")}</i><div><b>Cash offer in 24 hours</b><span>Close in as little as 7 days</span></div></li>
  <li style="--c:var(--gold)"><i>{icon("hammer")}</i><div><b>No repairs, no cleaning</b><span>Take what you want, leave the rest</span></div></li>
  <li style="--c:var(--violet)"><i>{icon("shield")}</i><div><b>BBB accredited</b><span>Closings with a local attorney</span></div></li>
</ul></div></section>

<section class="section situations">
  <div class="container">
    <div class="head reveal"><p class="eyebrow">We buy houses in ANY situation</p><h2>Every situation gets <br class="d">its own path.</h2>
      <p>Inherited a house you don’t want? Facing a divorce? Trying to avoid foreclosure? We have seen it all. Choose what brought you here and we’ll ask only what matters for your situation.</p></div>
    <div class="bento">''' + ''.join(
    f'<a class="tile{" wide" if k in ("inherited", "comparing") else ""}{" dark" if k == "comparing" else ""} reveal" style="--c:var(--{"brand-d" if c == "brand" else c});--s:var(--{"brand" if c == "brand" else c.replace("-l", "")}-soft)" href="{QUIZ}?s={k}#quiz"><span class="tag">{tag}</span><i>{icon(k)}</i><h3>{t}</h3><p>{d}</p><span class="start">{"See my cash offer first" if k == "comparing" else "Start here"} {icon("arrow")}</span></a>'
    for k, c, _, tag, t, d in SITUATIONS) + f'''</div>
  </div>
</section>

<section class="section intro">
  <div class="container intro-grid">
    <div class="intro-copy reveal">
      <p class="eyebrow">Get cash for your Carrollton house</p>
      <h2>We Buy Houses in West Georgia</h2>
      <p class="big">We are professional house buyers in Carrollton, GA and we buy houses as-is for cash. We have over 20 years of experience in helping people offload properties in the Carrollton area without the hassle of the traditional selling method.</p>
      <p>When you call us, you get our founder, Jimmy, directly on the phone to answer any questions and find the best real estate solution for you.</p>
      <p>We can make you a cash offer within 24 hours and close in as little as 7 days, without worrying about things like paying fees, making repairs, or waiting for offers.</p>
      <div class="callout" style="--c:var(--act)"><h3>Qualified in two minutes, not two weeks</h3><p>Answer a few questions about the house and your timeline. Jimmy reads them before he calls, so the first conversation is about your options, not paperwork.</p></div>
    </div>
    <div class="intro-visual reveal">
      <figure class="tilt">{img("bought-7.jpg", "A white two-story house purchased in cash by We Buy Houses in West Georgia")}</figure>
      <div class="intro-badge">{icon("shield")}<span><b>20+ years</b> buying houses in West Georgia</span></div>
    </div>
  </div>
</section>

<section class="section mke" id="bought">
  <div class="mke-glow"></div>
  <div class="container">
    <div class="sold-head reveal">
      <div><p class="eyebrow light">Proof, not promises</p><h2>Houses we’ve bought <em>across West Georgia.</em></h2></div>
      <p>We bought all of these properties as-is from local homeowners in and around Carrollton, GA. It doesn’t matter if your property is a house, duplex, or mobile home. It doesn’t matter what kind of condition the property is in.</p>
    </div>
    <div class="sold-grid reveal">''' + ''.join(f'<figure class="s{k}">{img(f, a)}</figure>' for k, (f, a) in enumerate(bought)) + f'''</div>
    <div class="stats sold-stats reveal">
      <div style="--c:var(--amber)"><b>20+</b><span>years helping West Georgia homeowners</span></div>
      <div style="--c:#4DA3FF"><b>24 hrs</b><span>to a cash offer, then close in as little as 7 days</span></div>
      <div style="--c:#7BDCB5"><b>{G_RATING}★</b><span>from {G_COUNT} Google reviews</span></div>
    </div>
  </div>
</section>

<section class="section condition">
  <div class="container">
    <div class="head center reveal"><p class="eyebrow">No repairs, no decluttering, no cleaning</p><h2>We buy houses in <span class="grad">ANY condition.</span></h2>
      <p>From smoke damage to flooding to lived-in messes, we have bought it before. When you sell to us, you can simply take what you want, and leave the rest.</p></div>
    <div class="cond-grid reveal">
      <figure style="--c:var(--gold)">{img("cond-bath.jpg", "A bathroom of a purchased property in need of repairs")}<figcaption><b>Needs repairs</b>Bought as-is</figcaption></figure>
      <figure style="--c:var(--crimson)">{img("cond-fire.jpg", "A purchased property with fire damage")}<figcaption><b>Fire damage</b>Bought as-is</figcaption></figure>
      <figure style="--c:var(--violet)">{img("cond-kitchen.jpg", "The kitchen of a house bought without cleaning")}<figcaption><b>Never cleaned</b>Bought as-is</figcaption></figure>
    </div>
    <p class="cond-foot reveal">“We are flippers, and the more work there is for our team, the more excited we are!”</p>
  </div>
</section>

<section class="section process" id="how">
  <div class="container">
    <div class="head center reveal"><p class="eyebrow">How can I sell my house fast?</p><h2>Three steps. <span class="grad">That’s it.</span></h2><p>A cash offer within 24 hours. Close in as little as 7 days, or on your schedule.</p></div>
    <ol class="timeline reveal">
      <li style="--c:var(--brand)"><span class="num">1</span><h3>Send us some info</h3><p>Answer a few quick and easy questions about your property and your situation. Takes about two minutes.</p></li>
      <li style="--c:var(--violet)"><span class="num">2</span><h3>We will contact you</h3><p>Jimmy calls to answer questions, see the house and make your cash offer within 24 hours.</p></li>
      <li style="--c:var(--act)"><span class="num">3</span><h3>Get paid!</h3><p>If you accept, we close with a local attorney in as little as 7 days, and you get cash for your house.</p></li>
    </ol>
  </div>
</section>

<section class="section compare">
  <div class="container">
    <div class="head reveal"><p class="eyebrow">Before you list with an agent</p><h2>Sell without an agent. <br class="d">Sell without the uncertainty.</h2></div>
    <div class="compare-grid">
      <div class="compare-card cash reveal"><span class="ribbon">No commissions</span><i>{icon("cash")}</i><h3>No commissions and no fees!</h3><p class="sub">Sell your house without an agent</p><p>Why not see about our cash offer on your house before you commit to listing with an agent? You don’t have to deal with the hassle of listing your home, and you don’t have to pay thousands of dollars in realtor commissions.</p><ul class="checks"><li>No open houses or showings</li><li>No inspections or contingencies delaying the closing</li><li>No extra fees, no haggling, and no surprises</li></ul></div>
      <div class="compare-card trad reveal"><i>{icon("calendar")}</i><h3>No waiting, no hassle, no worries!</h3><p class="sub">Sell your house without uncertainties</p><p>Selling your house can be a long and difficult process. From getting the property market-ready to waiting for an offer, you can run into several delays that can prevent you from closing on your house and moving on.</p><ul class="checks" style="--c:var(--brand)"><li>No inspection contingencies</li><li>No failed deals</li><li>No waiting on bank financing</li></ul></div>
    </div>
  </div>
</section>

<section class="section stories" id="stories">
  <div class="container">
    <div class="head stories-head reveal"><div><p class="eyebrow">Reviews</p><h2>West Georgia sellers <br class="d">in their own words.</h2><p>From Google and from agents who have worked with Jimmy.</p></div>{g_badge("big")}</div>
    <div class="story-grid">
      <figure class="story feature reveal" style="--c:var(--violet)"><span class="tag">Google review</span>
        <blockquote>“I wish I could give Jimmy and the team more than 5 stars. The whole process was quick, efficient, and professional. <mark>Everything was completed faster than I thought possible</mark>, and everything was done based on what was best for me.”</blockquote>
        <figcaption><span class="initial" data-i="K" aria-hidden="true"></span><b>Kevin Richards</b><small>Google review</small></figcaption></figure>
      <figure class="story reveal" style="--c:var(--emerald)"><span class="tag">Google review</span>
        <blockquote>“Jimmy and his team are top notch. <mark>They made our home selling experience very simple and quick.</mark> Any questions we had throughout the process were answered in a timely manner.”</blockquote>
        <figcaption><span class="initial" data-i="H" aria-hidden="true"></span><b>Heather Kirby</b></figcaption></figure>
      <figure class="story reveal" style="--c:var(--gold)"><span class="tag">Google review</span>
        <blockquote>“So many people told me they would offer a good price and then could not close. <mark>I wish I had saved myself a lot of time and trouble and just contacted these guys first!</mark>”</blockquote>
        <figcaption><span class="initial" data-i="D" aria-hidden="true"></span><b>Danny Johnson</b><small>Local Guide</small></figcaption></figure>
      <figure class="story reveal" style="--c:var(--brand)"><span class="tag">Agent testimonial</span>
        <blockquote>“As an agent I brought them many deals, <mark>they always closed on every home we got under contract!</mark> You can rest assured that any dealings with Jimmy &amp; Rob will be top notch and handled with utmost honesty and respect for all parties involved.”</blockquote>
        <figcaption><span class="initial" data-i="C" aria-hidden="true"></span><b>Cheralyn Pilgrim</b><small>Cedartown, GA</small></figcaption></figure>
    </div>
  </div>
</section>

<section class="section riz" id="areas">
  <div class="container riz-grid">
    <div class="riz-visual reveal"><div class="blob"></div>
      <figure class="lake">{img("bought-3.jpg", "A ranch-style red brick house with a closed carport, bought by We Buy Houses in West Georgia")}</figure>
      <div class="riz-badge">{img("jimmy-shayna.jpg", "Jimmy and Shayna")}<div><b>Jimmy &amp; Shayna</b><span>{COMPANY}</span></div></div></div>
    <div class="riz-copy reveal">
      <p class="eyebrow">Areas we buy houses</p>
      <h2>Carrollton, and <em>all of West Georgia.</em></h2>
      <p>We buy houses in any Carrollton neighborhood and in any of the surrounding cities. Our mission is to help homeowners offload burdensome properties.</p>
      <p class="areas-title">{icon("pin")}We buy houses in</p>
      <div class="areas">''' + ''.join(f'<span class="area">{a}</span>' for a in AREAS) + f'''</div>
      <a class="text-link" href="{QUIZ}">Check if we buy in your town {icon("arrow")}</a>
    </div>
  </div>
</section>

<section class="section faqs" id="faq">
  <div class="container faq-grid">
    <div class="head reveal"><p class="eyebrow">Good questions. Straight answers.</p><h2>Before you take the next step.</h2><a class="text-link" href="{TEL}">Or ask Jimmy: {PHONE} {icon("arrow")}</a></div>
    <div class="faq-list reveal">''' + ''.join(
    f'<details style="--c:var(--{c})"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for (q, a), c in zip(FAQ, ['gold', 'violet', 'emerald', 'brand', 'crimson', 'slate'])) + '''</div>
  </div>
</section>'''
write('', page('We Buy Houses in West Georgia | Sell Your House Fast for Cash', home,
               'Sell your house fast in Carrollton, Georgia. We buy houses as-is for cash: no repairs, no cleaning, no commissions necessary.', body_cls='home'))

# ---------------- Assessment (iframe) and its page ----------------
original = (ROOT / 'site-source/funnel-original.html').read_text()
style = re.search(r'<style>(.*?)</style>', original, re.S).group(1)
quiz = original[original.index('<section id="quiz">'):]
quiz = quiz[:quiz.index('</section>') + 10]
scripts = '\n'.join(re.findall(r'<script>(.*?)</script>', original, re.S))
scripts = scripts.replace('var ASSISTANT_ON = true', 'var ASSISTANT_ON = false').replace('const ASSISTANT_ON = true', 'const ASSISTANT_ON = false')
scripts = re.sub(r'function doneHtml\(\)\{.*?\n\}', '''function doneHtml(){return '<div class="fade done"><div class="tick">✓</div><h3>You’ve reached the end of the preview.</h3><p>Your answers stayed in this browser. No inquiry was sent and no callback has been requested.</p><p>On the live site, this step confirms that Jimmy has your details and is reading your answers before he calls.</p><a class="btn btn-line" href="../" target="_top">Back to the homepage</a></div>';}''', scripts, flags=re.S)
scripts = scripts.replace('label="Sent"', 'label="Preview complete"')
scripts = scripts.replace('if(consent&&!consent.checked) problems.push("the tick box so we are allowed to contact you");', '')
scripts = scripts.replace('consent:{given:true,', 'consent:{given:!!(consent && consent.checked),')
scripts = scripts.replace('I agree to receive text messages', '(Optional) I agree to receive text messages')
scripts = scripts.replace('if(window.console) console.info("[lead payload]", lead);', '/* Preview only: no transmission, PII logging or conversion event. */')
scripts = re.sub(r'function getGuide\(e\)\{[^\n]+\}', 'function getGuide(e){ e.preventDefault(); top.location.href="../"; return false; }', scripts)
scripts = scripts.replace('"Send Me The Guide":"Send This And Call Me Back"', '"Finish Preview":"Finish Preview"')
scripts = scripts.replace('No obligation. Not a listing agreement. Not a commitment to sell.', 'Preview only. Please use made-up contact details. No information is sent.')
quiz = quiz.replace('Most people are in more than one situation at once.', 'What’s happening with your house?')
quiz = re.sub(r'<p class="sec-p">.*?</p>', '<p class="sec-p">Choose everything that applies. We’ll ask a few relevant questions so Jimmy’s first call starts in the right place.</p><p class="preview-note">This is a demonstration. Please use made-up details. No inquiry will be sent.</p>', quiz, count=1, flags=re.S)
quiz_v2 = (ROOT / 'site-source/quiz-v2.css').read_text()
funnel_doc = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">'
              f'<title>Get your cash offer | {COMPANY}</title>'
              f'<style>@font-face{{font-family:"Source Sans 3";src:url("{link("assets/source-sans.woff2")}") format("woff2");font-weight:200 900;font-display:swap}}'
              + style + '\n' + quiz_v2 + '</style></head><body>' + quiz + '<script>' + scripts + '</script>'
              '<script>new ResizeObserver(()=>{parent.postMessage({type:"wg-height",height:document.body.scrollHeight},location.origin)}).observe(document.body);</script></body></html>')
write('assessment/', funnel_doc)

quiz_hero = (f'<section class="page-hero quiz-hero"><div class="hero-glow g1"></div><div class="hero-dots"></div><div class="container">'
             f'<nav class="crumbs" aria-label="Breadcrumb"><a href="{link()}">Home</a><span>/</span><span>Get a cash offer</span></nav>'
             f'<h1>Sell your house fast. Your situation comes first.</h1>'
             f'<div class="quiz-trust"><span>{icon("check")}About two minutes</span><span>{icon("check")}Offer in 24 hours</span><span>{icon("check")}Close in 7 days</span><a href="{TEL}">{icon("phone")}{PHONE}</a>{g_badge("dark")}</div></div></section>')
quiz_frame = f'<section class="quiz-wrap" id="quiz"><div class="container"><div class="quiz-card"><iframe id="assessment-frame" title="Property situation assessment" src="{link("assessment/")}" loading="eager"></iframe></div></div></section>'
frame_js = '<script>addEventListener("DOMContentLoaded",()=>{const f=document.getElementById("assessment-frame");f.src+="?"+new URLSearchParams(location.search).toString();addEventListener("message",e=>{if(e.origin===location.origin&&e.source===f.contentWindow&&e.data?.type==="wg-height"&&Number.isFinite(e.data.height))f.style.height=Math.max(520,e.data.height+10)+"px";});});</script>'
write('get-a-cash-offer-today/', page(f'Get A Cash Offer | {COMPANY}', quiz_hero + quiz_frame, 'Tell us about your house and your situation. No obligation.',
                                      extra=frame_js, body_cls='inner quiz-page', sticky=False, home=False))
(ROOT / '.nojekyll').touch()
(ROOT / 'robots.txt').write_text('User-agent: *\nDisallow: /\n')
print('Built homepage, quiz page and assessment')
