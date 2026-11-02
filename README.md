# Jingyuan (Angela) Yang — academic homepage

Three static pages for `https://angelaaa218.github.io/`, inspired by the restrained academic layout at https://yuhangdu-edu.github.io/. No dependencies or build service required. The design and implementation are original; no reference-site photos or source code are copied.

## Edit and preview

Edit text and paper metadata in `build.py`; edit the shared layout styles in `docs/assets/style.css`. Run `python build.py` after content changes. Serve locally with `python -m http.server 8000 --directory docs`, then visit http://localhost:8000.

## GitHub Pages

Repository: https://github.com/Angelaaa218/angelaaa218.github.io

Publishing source: **main** branch, **/docs** folder. GitHub Pages publishes updates after changes are pushed to this branch. The public URL is https://angelaaa218.github.io/.

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

## Public visitor statistics

The footer shares one total page-view badge across Homepage, Research, and Teaching using https://hits.sh/angelaaa218.github.io/. It counts badge requests, not unique people: caching, bots, blockers, and service availability may affect totals. The production badge only loads on angelaaa218.github.io so local reviews do not inflate it. No API key or account is required. A `?visitor-preview=1` URL enables a separately labelled preview counter for testing.

Each browser calls https://api64.ipify.org?format=json to display its own public IPv4/IPv6 address. The page does not save IPs, send them to the counter as data, or expose other visitors' addresses. Both providers receive ordinary network requests from visitors. With JavaScript disabled the IP label says “Requires JavaScript”; unavailable services show an explicit fallback.

Provider documentation: https://github.com/silentsoft/hits and https://www.ipify.org/.
