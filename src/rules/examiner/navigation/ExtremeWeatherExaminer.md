# ExtremeWeatherExaminer

## Synopsis

Estimates the probability that a vessel capsizes, given the sea she is in and the hull she is, using a small Bayesian network. Scores a violation when that probability crosses a configured alarm threshold.

## Operation

This is an inference rather than a threshold test, because the four inputs do not act independently: a severe sea is survivable in a large vessel in ballast and lethal in a small overladen one, and poor visibility contributes nothing on its own but compounds a sea that would otherwise be handled. The network in `CapsizeModel` states those interactions once — payload and size determine `stability`, and stability, wave height and visibility determine `capsize` — instead of spreading them through nested conditionals. Three of the four inputs have no Legata resolver term, so the examiner gathers them directly: sea state by sampling the `SEA_WAVE` force field at the vessel's position and taking the vector magnitude, payload as the ratio of the vessel's weight to its declared capacity, and size from `OwnShip.Length`; only visibility comes from a term. Each value is mapped to a network state using the boundaries in `config/risk/capsize.model.yaml`, evidence is set, and the marginal on `capsize` is read back. The figure is always published on `/Faculty/Concern/Weather`, and is additionally penalised as `weather.capsize_risk` when it reaches `alarm_threshold`.

## Features

- Reuses the same toolchain as the ASV risk model, so the capsize CPTs are numpy matrices with declared parent orders and are edited the same way.
- Inference captures the interaction between loading, hull size, sea and visibility that a chain of thresholds cannot.
- State boundaries are configuration, so the model can be recalibrated without rebuilding the network.
- Degrades gracefully: any input that cannot be gathered is simply omitted from the evidence and that node keeps its prior.
- Reports the probability continuously and penalises only above threshold, so a consumer can watch risk build before anything is scored.
- Publishes the evidence alongside the probability, making every assessment reconstructable.

## Known limitations

- **Every conditional probability in the network is a placeholder.** The tables are monotone and sign-correct, so the model propagates sensibly, but none is calibrated against casualty data and no number should be cited.
- Publishes a message every tick even below threshold, which is heavy at simulation scale.
- `band()` silently returns the default when a configured `states`/`edges` pair is inconsistent, so a mis-edited config fails soft rather than loudly.
- Takes the strongest wave field across all fields rather than the one actually covering the vessel.
