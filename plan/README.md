# plan — the published route plan (v3.4.5-geo)

The operational output of the engine, as issued to the Regional Transport Office.

| File | What |
|---|---|
| `Rationalised_Routes_Kashmir_v3.csv` | All 644 engine rows (614 permits + 30 e-bus routes): 186 active (32 trunk, 154 feeder) and 458 merged, with headway, cycle time, fleet and vehicle mix per route. |
| `Rationalised_Routes_Kashmir_v3.geojson` | The 186 active route geometries. |
| `Master_Transit_Map_Kashmir_v3.html` | Interactive network map (open in a browser). |
| `Kashmir_Route_Frequency_Plan_v3.4.5_RTO_Pretty.xlsx` | The two-sheet bus schedule for the RTO (summary + route plan with route codes). |
| `Kashmir_Route_Frequency_Plan_v3.4.5_RTO.xlsx` | The full nine-sheet RTO master workbook. |
| `Kashmir_Timetables_v1.xlsx` | Departure-board timetables, one sheet per district. |
| `Kashmir_Route_Verification_Appendix_v3.4.5_RTO.xlsx` | Route-by-route verification against web-sourced road distances. |
| `Kashmir_Stops_Master_v4.csv` | 143 canonical stops with district, tehsil and code. |
| `Rationalisation_Log_Kashmir_v3.csv` | Per-route reasoning for every decision. |
| `Passenger_Impact_Kashmir_v3.csv` | Public-facing per-route summary. |

**Read with the analysis.** The published fleet (1,011) is what the engine specifies. At observed GPS
pace the fleet is 1,130–1,266 ([`docs/03_results.md`](../docs/03_results.md)); population-served columns
in the CSV use straight-line catchments, which overstate the walking catchment by a median 37.4 %.
