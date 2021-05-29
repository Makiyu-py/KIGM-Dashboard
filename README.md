# KIGM Dashboard

Hi! This is the official bot dashboard of my (crap and dead) discord bot!

From the first line itself, I'm doing this for fun but also need some help! \
(fyi there's todo lists scattered around tysm)

## How to set-up

### 1. Make And Initialize Your Python venv

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Installing Required Packages

Python packages:

```
pip3 install -r requirements.txt
```

NPM packages:

```
npm install
```

### 3. Actually Running The Site

For Development:

```bash
npm run develop:css
python3 -m api -p { port number here }
```

For Production:

```bash
npm run build:css
```

(that'll make a purged CSS build for production)

```bash
python3 -m api --mode prod
```

(that'll remove the debug mode in Flask)

## Q&A

> Why is the production branch using Flask 1.1.4 while the development branch uses Flask 2.x?

The official python runtime in vercel isn't up-to-date with the new major updates from pallet projects' modules.
To be more specific, vercel's python runtime relies on Werkzeug 1.0.1 while Flask 2.0 relies on Werkzeug 2.x

When vercel's runtime updates to Workzeug 2.x, I'll change the production branch's version to be using Flask 2.0 ASAP.

## License

This project is under the MIT license.
