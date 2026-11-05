# LoL Win Predictor

Predicting the winner of a League of Legends ranked match from the first 10 minutes of the game, using data from the Riot Games API (MATCH-V5 + match timeline).

> 🚧 Early stage: data exploration and feature engineering. No trained models yet.

## Why this project

Final match stats (kills, gold at the end) almost dictate the outcome, so predicting from them is trivial and uninteresting. This project asks a harder question: **how much of the result is already decided by minute 10?** The goal is a well-evaluated model, not a flashy accuracy number: proper baselines, leakage-free validation, calibrated probabilities and an explanation of which early-game signals matter.

## Approach

- **Target:** whether the blue side wins.
- **Granularity:** one row per match (not one per team), so the same match never lands in both the train and the test set.
- **Features** (all as blue minus red, at the 10:00 mark):
  - total gold, XP, level and CS difference
  - kills difference and first blood
  - objectives taken (dragons, towers) if any
- **Scope:** a single queue (ranked solo/duo) to keep the data comparable.

## Planned pipeline

1. **Data collection:** crawl matches from many different players (match participants seed the next requests), store raw match + timeline JSON locally and derived features in a table.
2. **Analysis and baselines:** class balance, distributions, missing data. Baselines: "always blue" and logistic regression on gold difference only.
3. **Classical models:** logistic regression, kNN, XGBoost (scikit-learn). Time-based split (older matches for training, newer for testing) to avoid patch and player leakage.
4. **Neural network:** a small MLP in PyTorch on the same features and split, compared honestly with the tree-based model.
5. **Evaluation:** ROC-AUC, log loss, accuracy, calibration curve; SHAP for explainability.
6. **Serving:** FastAPI `/predict` endpoint (Pydantic schema, saved model, Docker), tests with pytest, CI in GitHub Actions.

## Results

_To be filled in once the models are trained._

| Model | ROC-AUC | Log loss | Accuracy |
|---|---|---|---|
| Always blue (baseline) | - | - | - |
| Logistic regression (gold diff only) | - | - | - |
| Logistic regression (all features) | - | - | - |
| XGBoost | - | - | - |
| MLP (PyTorch) | - | - | - |

## Project structure

```
lol-win-predictor/
├── src/
│   ├── riot_client.py     # Riot API client with rate-limit handling
│   └── features.py        # Feature extraction from match + timeline
├── fetch_sample.py        # Download one sample match + timeline
├── explore.py             # Inspect the raw data
├── data/                  # Raw data (git-ignored)
├── requirements.txt
└── README.md
```

## Getting started

1. Clone the repo and create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Create a `.env` file with your Riot API key (from the [Riot Developer Portal](https://developer.riotgames.com/)):
   ```
   RIOT_API_KEY=your-key-here
   ```
3. Create the `data/` folder, set a match ID in `fetch_sample.py` and download a sample:
   ```bash
   mkdir data
   python fetch_sample.py
   python explore.py
   ```

## Known limitations and pitfalls

- Riot's development API key expires every 24 hours and has a low rate limit, so collecting thousands of matches takes several sessions.
- Game patches change balance, so older matches may not be comparable with newer ones. Collected data is split by time and the patch is recorded.
- A prediction from minute 10 is inherently noisy; the interesting result is how much signal there is, not near-perfect accuracy.
- Raw data (including other players' identifiers) is not committed to the repository.

## Project status

- [x] Riot API client (match + timeline)
- [x] Data exploration
- [ ] Feature extraction
- [ ] Data collection (multi-player crawl)
- [ ] Baselines and classical models
- [ ] PyTorch MLP
- [ ] Evaluation, calibration, SHAP
- [ ] FastAPI `/predict` + Docker
- [ ] Tests and CI

## Disclaimer

This project is not endorsed by Riot Games and does not reflect the views of Riot Games or anyone officially involved in producing or managing League of Legends.

## License

MIT
