"""Tests for publication experiments estimator selection."""

from tsml_eval.publications.y2023.tsc_bakeoff import (
    _set_bakeoff_classifier,
    bakeoff_classifiers,
)
from tsml_eval.utils.test_utils import _check_set_method, _check_set_method_results


def test_set_bakeoff_classifiers():
    """Test set_bakeoff_classifier method."""
    classifier_dict = {}
    all_classifier_names = []

    _check_set_method(
        _set_bakeoff_classifier,
        bakeoff_classifiers,
        classifier_dict,
        all_classifier_names,
    )

    _check_set_method_results(
        classifier_dict,
        estimator_name="Classifiers",
        method_name="_set_bakeoff_classifier",
    )
