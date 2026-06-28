# Mom's 60th Birthday Invitation 🎉

A single-page, interactive, animated invitation website. Share the link and guests
get a festive invite with the event details, a live countdown, and fun buttons.

**Event**
- 📅 Sunday, 12 July 2026
- 🕧 12:30 PM onwards
- 📍 St Thomas Community Hall, Mission Compound, Shimoga

## Features
- Animated gradient background, floating sparkles, and **tap-to-pop balloons** 🎈
- Confetti cannons on load and on the **"Count me in!"** button
- Live **countdown** to the celebration
- **Add to Calendar** (downloads an `.ics` file)
- **View Venue** (opens Google Maps)
- **Share Invite** (native share / copies the link)

## View it
Just open `index.html` in any browser — everything is self-contained (no build, no server).

## Personalize
Open `index.html` and edit the `EVENT` config block near the bottom `<script>`:
```js
var EVENT = {
  honoree: "Our Beloved Mom",  // <- put your mom's name here
  ...
};
```

## Publish a shareable link (GitHub Pages)
1. Push this repo to GitHub.
2. Repo **Settings → Pages → Build and deployment → Source: Deploy from a branch**.
3. Choose branch `main` and folder `/ (root)`, then **Save**.
4. Your invite goes live at `https://<username>.github.io/<repo>/`.
