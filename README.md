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
- Education, teaching terms, and working-paper revision statuses come from the supplied `CV.tex`.
- Author names/order for papers listed on Linwei Xin’s live research page were checked on October 31, 2026: https://xin.engineering.cornell.edu/research/. Search-engine caches were stale; the live page includes Jingyuan Yang as fourth author on “A Bitter Lesson.” Its author order is Yi Sui, Chenjie Xiao, Linwei Xin, Jingyuan Yang, Donghai Huang, Lei Cao.
- The remanufacturing paper uses the CV’s updated title and the Cornell page’s Linwei Xin, Jingyuan Yang order; the link currently carries the earlier title, explicitly identified on the site.
- The technical note is published in Operations Research 74(2), 722–729 (2026), per the live Cornell page, superseding “forthcoming” in the CV.
- “Foundation Models for Newsvendor Decisions” is not listed on the Cornell research page. Its authors derive from the CV; Qichuan Yin is the formal name of Ethan Yin, verified at https://ethanqyin.github.io/. Its author order is provisional because the CV only lists coauthors. No public manuscript URL was supplied or verified, so the title has no invented link.
- Verified personal/faculty links are supplied for Linwei Xin, Qichuan Yin, Yuan Zhong, Chenyu Zhou, and Dongdong Ge. Other names remain plain text because a matching personal page was not verified.
- The sidebar uses the user-supplied portrait in its original rectangular proportions. Linwei Xin is identified as the advisor, as confirmed by the user.
- The CV's personal phone and street address are not included. The academic email is included. The CV source is not bundled in the public site.

## Private visitor analytics — not yet connected

The website does not display visitor counts, IP addresses, or statistics links. The previous hits.sh counter and ipify IP lookup have been removed entirely. No visitor analytics service is currently connected, so the website code does not collect a private visitor history or make analytics requests.

To enable private page-view reports by IP on GitHub Pages, use a separate authenticated analytics service. Statcounter is one option. The site owner must create a project for `https://angelaaa218.github.io/` and provide the website installation code. Keep the dashboard's public/guest access disabled, grant no other users access, and select an invisible counter. The invisible-counter option only controls the display; the account's access settings control who can read the reports. Verify that a signed-out visitor cannot open the reports before treating the setup as private. The provider processes the collected data; reports are private from website visitors.

Store no visitor logs, dashboard passwords, or analytics API credentials in this public website repository. A hidden page or a password checked in browser JavaScript would not protect analytics data on a static site. The provider's website installation identifiers are intended for embedding, and are different from account passwords or API credentials.

Statcounter documents IP lookup, IP masking, invisible counters, and user/public access in its [user manual](https://secure.statcounter.com/support/manual/). IP addresses may be shared or change, so they do not reliably identify individual people. Private analytics remain optional for publishing the academic website.
