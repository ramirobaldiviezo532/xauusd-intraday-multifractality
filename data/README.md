# Input data, provenance and usage boundaries

Three historical CSV inputs are used by the research notebook; none is distributed in this repository. The SHA-256 values below were **reported in archived result metadata** and have not been recalculated from the unavailable source files.

## XAUUSD: `OHLCV15MIN.csv`

- **Instrument and quote source:** XAUUSD CFD, Dukascopy. The quote history was managed/exported as closed 15-minute OHLCV candles in StrategyQuant Data Manager. `ICMarkets` denotes a software broker profile, not the documented original quote source.
- **Time convention:** the exported source label is the literal string `EST+07`. It is not independently established as an IANA/civil timezone, and is not converted to UTC by documentation convention.
- **Analytic interval:** 2003-05-05 through 2026-07-31, by source timestamps; records after the cutoff were excluded. Reported raw-read and post-cutoff row counts refer to different denominators.
- **Expected fields:** `Date`, `Time`, `Open`, `High`, `Low`, `Close` (with `Volume` optional); `Date` in `YYYYMMDD`, `Time` in `HH:MM:SS`. Retain rows in source order, original gaps and the export's numerical precision.
- **Return validation:** only successive closing observations exactly 15 minutes apart form valid 15-minute returns. Derived 30-minute OHLC bars use occupied, clock-aligned bins (`Open`: first; `High`: max; `Low`: min; `Close`: last). A bin need not contain both source 15-minute bars, while a validated 30-minute close-to-close return requires an exact 30-minute timestamp gap. Sensitivity to incomplete bins is not established by these files.
- **Historical SHA-256 reported for the CSV:** `8ecc6e7386d2ae1659759f849253cc18e4fec3eefae40dfb60db28777be71664`.

To obtain new inputs, use an official Dukascopy historical-data channel or an appropriately licensed StrategyQuant data-download workflow, record the feed/instrument, export settings, timestamp and cutoff, and follow the provider's applicable usage terms. Dukascopy provides an official [historical data export](https://www.dukascopy.com/swiss/english/marketwatch/historical/), while [StrategyQuant documents Dukascopy as an integrated source](https://www.strategyquant.com/doc/quantdatamanager/). A new export may differ in bar coverage, gaps, timestamp conventions, formatting, or upstream revisions. Its SHA-256 need not equal the historically reported one even if it covers the same nominal interval.

Dukascopy's [website terms of use](https://www.dukascopy.com/swiss/english/legal-pages/terms-of-use/) impose significant limitations on copying and redistributing website content. The effect of those terms, the actual acquisition contract, and any separate consent on particular raw exports and derived results requires rights-holder review. Free download or academic use does not itself establish public redistribution permission.

## Macroeconomic inputs from FRED

| Input CSV | Series | Frequency and attribution | Historically reported SHA-256 |
| --- | --- | --- | --- |
| `DTWEXBGS.csv` | [Nominal broad U.S. dollar index](https://fred.stlouisfed.org/series/DTWEXBGS) | Daily; Board of Governors of the Federal Reserve System (US) | `88db7d787e99129e671015fcc581f3507d0a2c527804c285ab555c2b83cd8054` |
| `VIXCLS.csv` | [Cboe VIX](https://fred.stlouisfed.org/series/VIXCLS) | Daily close; Cboe | `c054c5d293b251746c5c7414d49e519b085130b4a5c977a8672ebc84abf8be0a` |

FRED supports access to downloadable series, but recent downloads may have revised observations and may differ from the study snapshots. The [FRED API terms](https://fred.stlouisfed.org/docs/api/terms_of_use.html) explicitly note that individual series can be subject to third-party rights; FRED access does not override those rights. The VIXCLS series page marks Cboe data as copyrighted; it is not interchangeable with the public-domain characterization that may apply to some federal data. Check terms and attribution for each series independently.

## Inputs versus outputs

**Not redistributed here:** original XAUUSD candle/price sequences, the three source CSVs and input exports. **Included in `outputs/`:** aggregate findings, model parameters and other computed tables. Some included tables may encode portions of input-derived sequences, event dates, or individual observations rather than only non-reconstructive summaries. This distinction matters for rights clearance. The MIT code license does not apply to third-party quotes, Cboe data, or restricted derivatives. No blanket assessment of permission is made in this README.

The historical hashes are also transcribed in [`reproducibility/historical_input_sha256_reported.txt`](../reproducibility/historical_input_sha256_reported.txt). They can be independently checked **only if the identical original CSV bytes are available**; finding a data series with the same name is insufficient.

## Optional economic calendar

The notebook accepts `economic_calendar_publication_master.csv` as an optional input. It was not part of the archived inputs. Adding a calendar changes the configuration and must be logged separately, rather than presented as an exact reconstruction of the archived analysis.
