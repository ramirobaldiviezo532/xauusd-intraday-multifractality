# Input data: reconstruction and distribution limits

The three original raw CSV input files are intentionally **not included**.

## XAUUSD market quotes (`OHLCV15MIN.csv`)

- Recorded quote source: **Dukascopy**; instrument: **XAUUSD**, CFD.
- Download/export management: **StrategyQuant Data Manager**, underlying tick history exported as **closed 15-minute OHLCV** candles.
- `ICMarkets` is the associated **broker profile**, not the documented origin of the quote history.
- Recorded timezone label: literal **`EST+07`** from the platform. It has not been equated with UTC or with a standard civil timezone.
- Scientific study covers **2003-05-05 through 2026-07-31** according to source timestamps; data after the study cutoff were not analyzed.
- Required columns: `Date`, `Time`, `Open`, `High`, `Low`, `Close` (optional `Volume`). The original notebook expects `YYYYMMDD` dates and `HH:MM:SS` times.
- Keep the original timestamps, bar order, and unfilled gaps. For intraday returns, only adjacent closed bars separated by exactly 15 minutes generate valid 15-min returns.
- The notebook derives 30-min OHLC candles by clock-aligned resampling and retains exact 30-min close-to-close intervals. It does not require two source candles per resampling bin.
- **SHA-256 recorded for the original input:** `8ecc6e7386d2ae1659759f849253cc18e4fec3eefae40dfb60db28777be71664`.

A correctly documented fresh export can still differ byte-for-byte from the historical source file. An identical source hash requires the exact original CSV, including formatting and row order. Do not publish the raw price series without confirming the contractual redistribution rights applicable to its acquisition; the public website terms alone are not sufficient to establish your particular rights.

## External FRED variables

- `DTWEXBGS`: U.S. nominal broad trade-weighted dollar index — https://fred.stlouisfed.org/series/DTWEXBGS
- `VIXCLS`: Cboe VIX index daily closing series — https://fred.stlouisfed.org/series/VIXCLS
- Recorded input SHA-256: `DTWEXBGS.csv` = `88db7d787e99129e671015fcc581f3507d0a2c527804c285ab555c2b83cd8054`; `VIXCLS.csv` = `c054c5d293b251746c5c7414d49e519b085130b4a5c977a8672ebc84abf8be0a`.

These series may be revised or formatted differently in subsequent downloads. Third-party licenses apply (particularly to Cboe's VIX data); public access on FRED does not automatically confer redistribution permission.

## Optional calendar

`economic_calendar_publication_master.csv` is an optional input to the notebook. It was not supplied with these uploads. Preserve its provenance if it was used in the original run; otherwise the notebook continues without it.
