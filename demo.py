import logging
from datetime import datetime

from grafanimate.model import AnimationScenario, AnimationSequence, SequencingMode

logger = logging.getLogger(__name__)


def playdemo():
    """
    Run demo on `play.grafana.org`.

    Synopsis::

        grafanimate --scenario=playdemo --output=./animations
    """
    logger.info("Running scenario playdemo")

    return AnimationScenario(
        grafana_url="https://monitor.nowum.fh-aachen.de/",
        dashboard_uid="FEg9kde7z",
        sequences=[
            AnimationSequence(
                start=datetime(2021, 11, 14, 2, 0, 0),
                stop=datetime(2021, 12, 1, 2, 0, 0),
                every="1d",
                mode=SequencingMode.CUMULATIVE,
            ),
        ],
    )


def assume():
    """
    Run demo on `localhost`.

    Synopsis::

        grafanimate --scenario=playdemo --output=./animations
    """
    logger.info("Running scenario playdemo")

    return AnimationScenario(
        grafana_url="http://assume:assume@localhost:3000/",
        dashboard_uid="mQ3Lvkr4k",
        # panel_id="panel-11",
        sequences=[
            AnimationSequence(
                start=datetime(2019, 1, 14, 2, 0, 0),
                stop=datetime(2019, 2, 1, 2, 0, 0),
                every="1d",
                mode=SequencingMode.CUMULATIVE,
            ),
        ],
    )

def assume_grid():
    """
    Run demo on `localhost`.

    Synopsis::

        grafanimate --scenario=playdemo --output=./animations
    """
    logger.info("Running scenario playdemo")

    return AnimationScenario(
        grafana_url="http://assume:assume@localhost:3000/",
        dashboard_uid="nodalview",
        # panel_id="panel-11",
        sequences=[
            AnimationSequence(
                start=datetime(2019, 1, 2, 2, 0, 0),
                stop=datetime(2019, 1, 7, 0, 0, 0),
                every="1h",
                mode=SequencingMode.CUMULATIVE,
            ),
        ],
    )



def monitor_entsoe():
    """
    Run demo on `localhost`.

    Synopsis::

        grafanimate --scenario=demo.py:monitor_entsoe --output=./animations --panel-id="panel-2" --exposure-time=0.7
        grafanimate --scenario=demo.py:monitor_entsoe --output=./animations --dashboard-view="d-solo" --panel-id="panel-26" --exposure-time=0.7
    """
    logger.info("Running scenario playdemo")

    return AnimationScenario(
        grafana_url="https://monitor.nowum.fh-aachen.de/",
        dashboard_uid="FEg9kde7z",
        # panel_id="panel-11",
        sequences=[
            AnimationSequence(
                start=datetime(2019, 1, 1),
                stop=datetime(2024, 11, 1, 2, 0, 0),
                every="14d",
                mode=SequencingMode.CUMULATIVE,
            ),
        ],
    )


def monitor_weather():
    """
    Run demo on `localhost`.

    Synopsis::

        grafanimate --scenario=demo.py:monitor_weather --output=./animations --dashboard-view="d-solo" --panel-id="panel-3" --exposure-time=0.7
    """
    logger.info("Running scenario playdemo")

    return AnimationScenario(
        grafana_url="https://monitor.nowum.fh-aachen.de/",
        dashboard_uid="a6ade184-244d-437f-8cad-ff820ce8b380",
        # panel_id="panel-3",
        sequences=[
            AnimationSequence(
                start=datetime(2019, 1, 1),
                stop=datetime(2019, 11, 1, 2, 0, 0),
                every="14d",
                mode=SequencingMode.CUMULATIVE,
            ),
        ],
    )


def monitor_market():
    """
    Run demo on `localhost`.

    Synopsis::

        grafanimate --scenario=demo.py:monitor_market --output=./animations --exposure-time=0.7
    """
    logger.info("Running scenario playdemo")

    return AnimationScenario(
        grafana_url="https://monitor.nowum.fh-aachen.de/",
        dashboard_uid="QFWaoTOIz",
        # panel_id="panel-3",
        sequences=[
            AnimationSequence(
                start=datetime(2019, 1, 1),
                stop=datetime(2019, 1, 8, 2, 0, 0),
                every="4d",
                mode=SequencingMode.WINDOW,
            ),
        ],
    )


def price_map():
    """
    Run demo on `localhost`.

    Synopsis::

        grafanimate --scenario=demo.py:price_map --output=./animations --exposure-time=3 --dashboard-view="d-solo" --panel-id=panel-27
    """
    logger.info("Running scenario playdemo")

    return AnimationScenario(
        grafana_url="https://grafana.nowum.fh-aachen.de/",
        dashboard_uid="FEg9kde7z",
        # panel_id="panel-3",
        sequences=[
            AnimationSequence(
                start=datetime(2024, 11, 1),
                stop=datetime(2024, 11, 7),
                every="1h",
                mode=SequencingMode.WINDOW,
            ),
        ],
    )
