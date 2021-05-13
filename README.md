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
python3 -m app -p { port number here }
```

For Production:

```bash
npm run build:css
```

(that'll make a purged CSS build for production)

```bash
python3 -m app --mode prod
```

(that'll remove the debug mode in Flask)

## License

This project is under the MIT license.
