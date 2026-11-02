# Jingyuan (Angela) Yang — academic homepage

Three static pages for `https://angelaaa218.github.io/`, inspired by the restrained academic layout at https://yuhangdu-edu.github.io/. No dependencies or build service required. The design and implementation are original; no reference-site photos or source code are copied.

## Edit and preview

Edit text and paper metadata in `build.py`; edit the shared layout styles in `docs/assets/style.css`. Run `python build.py` after content changes. Serve locally with `python -m http.server 8000 --directory docs`, then visit http://localhost:8000.

## GitHub Pages

Planned repository: https://github.com/Angelaaa218/angelaaa218.github.io

Planned publishing source: **main** branch, **/docs** folder. Once enabled, GitHub Pages will publish updates after changes are pushed to this branch. The intended public URL is https://angelaaa218.github.io/. Publication is awaiting approval; no repository has been created or website files uploaded yet.

To update the site, edit `build.py` or the assets, run `python3 build.py`, and commit and push both the source and generated `docs` files. No additional build service or dependencies are required. All site navigation and assets use relative paths so previews also work under a project subpath. Canonical URLs target the personal homepage.

## Content and verification notes

- The research statement was supplied directly by Jingyuan Yang on November 1, 2026. It emphasizes AI for supply chains, foundation models for inventory decisions, classical inventory theory, and stochastic modeling, optimization, and deep learning.
- Education, Booth teaching terms, and working-paper revision statuses come from the supplied `CV.tex`. The High-dimensional Data Analysis teaching assistant role at Shanghai University of Finance and Economics (September 2020–January 2021) was supplied directly by the site owner.
- Author names/order for papers listed on Linwei Xin’s live research page were checked on October 31, 2026: https://xin.engineering.cornell.edu/research/. Search-engine caches were stale; the live page includes Jingyuan Yang as fourth author on “A Bitter Lesson.” Its author order is Yi Sui, Chenjie Xiao, Linwei Xin, Jingyuan Yang, Donghai Huang, Lei Cao.
- The remanufacturing paper uses the CV’s updated title and the Cornell page’s Linwei Xin, Jingyuan Yang order; the link currently carries the earlier title, explicitly identified on the site.
- The technical note is published in Operations Research 74(2), 722–729 (2026), per the live Cornell page, superseding “forthcoming” in the CV.
- “Foundation Models for Newsvendor Decisions” is not listed on the Cornell research page. Its authors derive from the CV; Qichuan Yin is the formal name of Ethan Yin, verified at https://ethanqyin.github.io/. Its author order is provisional because the CV only lists coauthors. No public manuscript URL was supplied or verified, so the title has no invented link.
- Research coauthors are shown as plain text, with Jingyuan Yang's name in bold. Paper title links are retained. The homepage introduction retains the advisor's personal link and uses the owner-specified Booth Ph.D. program link.
- The sidebar uses the user-supplied portrait in its original rectangular proportions. Linwei Xin is identified as the advisor, as confirmed by the user.
- The portrait is enlarged and centered within the desktop sidebar. The Chinese name uses installed 楷体 fonts where available, with a self-hosted three-character subset of [LXGW WenKai](https://github.com/lxgw/LxgwWenKai) as a fallback. The renamed web-font subset and its SIL Open Font License are in `docs/assets/fonts/`; no third-party font request is needed.
- The CV's personal phone and street address are not included. The academic email is included. The CV source is not bundled in the public site.

## Private visitor analytics — configured, awaiting publication

The website does not display visitor counts, IP addresses, or statistics links. The previous hits.sh counter and ipify IP lookup have been removed entirely. Statcounter project `13364396` is configured using the installation code provided by the site owner. The invisible tracker is included on all three pages and will begin recording eligible visits once the website is published.

To connect your account, copy `sc_project` and `sc_security` from the project's website installation code into `statcounter_project_id` and `statcounter_security_code` in `analytics.json`. These are public installation identifiers, not your account password or API key. Run `python3 build.py` to include the invisible tracker on all three pages. The tracker loads only on the HTTPS production domain, not localhost, file previews, or other domains. JavaScript-disabled visits and blocked tracking requests are not counted.

Open the [Statcounter project dashboard](https://statcounter.com/p13364396/) while signed into the owner's account to review reports. Keep the dashboard's public/guest access disabled and grant no other users access. The invisible-counter option only controls the display; the account's access settings control who can read the reports. The provider processes the collected data. Owner-only membership and the account's IP-reporting preferences must be checked inside the owner's account.

Signed-out checks on November 1, 2026 returned **Login Required** for the project summary, visitor activity, and visitor paths. These checks confirm that those reports were not publicly readable; they do not inspect membership inside the owner's account.

Store no visitor logs, dashboard passwords, or analytics API credentials in this public website repository. A hidden page or a password checked in browser JavaScript would not protect analytics data on a static site. The provider's website installation identifiers are intended for embedding, and are different from account passwords or API credentials.

Statcounter documents IP lookup, IP masking, invisible counters, and user/public access in its [user manual](https://secure.statcounter.com/support/manual/). IP addresses may be shared or change, so they do not reliably identify individual people. Live collection begins after publication; it has not yet been verified with a real visit to the published website.
