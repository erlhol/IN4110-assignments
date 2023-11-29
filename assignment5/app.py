"""
strompris fastapi app entrypoint
"""
import datetime
import os
from typing import List, Optional

import altair as alt
from fastapi import FastAPI, Query, Request
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from strompris import (
    ACTIVITIES,
    LOCATION_CODES,
    fetch_day_prices,
    fetch_prices,
    plot_activity_prices,
    plot_daily_prices,
    plot_prices,
)

app = FastAPI()
templates_directory = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "templates"
)
templates = Jinja2Templates(directory=templates_directory)


# `GET /` should render the `strompris.html` template
# with inputs:
# - request
# - location_codes: location code dict
# - today: current date


@app.get("/")
def strompris(request: Request):
    return templates.TemplateResponse(
        "strompris.html",
        {
            "request": request,
            "locations": LOCATION_CODES.items(),
            "today": datetime.datetime.now().strftime("%Y-%m-%d"),
        },
    )


# GET /plot_prices.json should take inputs:
# - locations (list from Query)
# - end (date)
# - days (int, default=7)
# all inputs should be optional
# return should be a vega-lite JSON chart (alt.Chart.to_dict())
# produced by `plot_prices`
# (task 5.6: return chart stacked with plot_daily_prices)


@app.get("/plot_prices.json")
def get_plot_prices(
    end: datetime.date, days: int, locations: Optional[List[str]] = Query(default=None)
):
    df = fetch_prices(locations=locations, end_date=end, days=days)
    return plot_prices(df).to_dict()


# Task 5.6 (bonus):
# `GET /activity` should render the `activity.html` template
# activity.html template must be adapted from `strompris.html`
# with inputs:
# - request
# - location_codes: location code dict
# - activities: activity energy dict
# - today: current date


...

# Task 5.6:
# `GET /plot_activity.json` should return vega-lite chart JSON (alt.Chart.to_dict())
# from `plot_activity_prices`
# with inputs:
# - location (single, default=NO1)
# - activity (str, default=shower)
# - minutes (int, default=10)


...


# mount your docs directory as static files at `/help`

...


def main():
    """Launches the application on port 5000 with uvicorn"""
    # use uvicorn to launch your application on port 5000
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=5000)


if __name__ == "__main__":
    main()
