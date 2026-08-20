import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_one_pager.py"
SPEC = importlib.util.spec_from_file_location("validate_one_pager", SCRIPT)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(validator)


FILLER = (
    "The diligence read separates public evidence from interpretation and keeps the immediate call objective in view. "
    "The available materials support a baseline product description, but they do not by themselves establish retention, "
    "gross margin, sales cycle quality, customer concentration, or repeatable distribution. MCA should treat the current "
    "public footprint as enough for call preparation and not as a substitute for private financial, legal, technical, or "
    "commercial diligence. The report should press for clear customer proof, current pipeline evidence, security posture, "
    "funding runway, and the operating assumptions behind the next 2 milestones. "
) * 2


def valid_report(no_news=False):
    last_30 = (
        "No material company specific news was located from July 22, 2026 through August 20, 2026 across the reviewed official and independent sources."
        if no_news
        else "\n".join(
            [
                "1. **August 10, 2026 | Product release.** ExampleCo published a new workflow that matters because it changes buyer onboarding. [Source](https://exampleco.com/news/product-release)",
                "2. **July 30, 2026 | Partnership update.** A named partner described a distribution integration that may widen reach. [Source](https://partner.example/news/exampleco)",
            ]
        )
    )
    return f"""# ExampleCo | Executive DD

**As of:** August 20, 2026, Asia/Manila
**News window:** July 22, 2026 to August 20, 2026
**Official:** https://exampleco.com | https://www.linkedin.com/company/exampleco

## Bottom Line

ExampleCo sells workflow software for mid-market finance teams that need faster vendor review and cleaner approval records. The central diligence tension is whether the product has repeatable commercial urgency beyond early design partners, because public evidence is clearer on positioning than on conversion, retention, and economics.

## Company Snapshot

| Field | Read |
|---|---|
| What it does | Automates vendor intake, review routing, and approval evidence for finance and operations teams. |
| Customer | Mid-market finance, procurement, and operations leaders with recurring vendor risk reviews. |
| Business model | Public materials point to subscription software, while pricing depth and expansion mechanics remain privately verifiable. |
| Stage and traction | Official materials and independent coverage show a live product and named ecosystem activity, but revenue scale is not public. |
| Leadership and base | The public company profile identifies the founding team and North American operating base. |
| Venture lens | PRIME is mixed: required and expensive manual work appear supported, while immediate budget urgency and market wedge depth need call testing. |

{FILLER}

## Last 30 Days

{last_30}

## DD Watchouts

1. **Medium | Unverified | Traction depth.** Public sources describe product capability and ecosystem activity, but they do not independently confirm recurring revenue, retention, or sales cycle quality. [Source](https://exampleco.com/customers)
2. **Low | Reported | Competitive crowding.** Independent category coverage shows several adjacent workflow vendors, so differentiation should be tested against budget-owning alternatives. [Source](https://industry.example/reports/vendor-risk-tools)
3. **Medium | Not found | Public information limitation.** No audited financials, detailed security disclosure, or customer retention metrics were located in reviewed public sources, so private diligence must close the evidence gap. [Source](https://exampleco.com/security)

## Call Priorities

1. Which buyer owns the budget, and what failed workaround makes the problem urgent this quarter?
2. What customer evidence proves retention, expansion, and deployment speed beyond early design partners?
3. What security, legal, and financial materials can MCA review to validate the core operating claims?

## Sources

1. ExampleCo Product Release, ExampleCo, August 10, 2026, https://exampleco.com/news/product-release
2. ExampleCo Customer Page, ExampleCo, August 1, 2026, https://exampleco.com/customers
3. Partner Update, Partner Example, July 30, 2026, https://partner.example/news/exampleco
4. Vendor Risk Tools Report, Industry Example, July 25, 2026, https://industry.example/reports/vendor-risk-tools
5. ExampleCo Security Page, ExampleCo, July 24, 2026, https://exampleco.com/security
"""


class ValidateOnePagerTests(unittest.TestCase):
    def assertValid(self, report):
        self.assertEqual([], validator.validate(report))

    def assertInvalidContains(self, report, expected):
        failures = validator.validate(report)
        self.assertTrue(
            any(expected in failure for failure in failures),
            f"Expected {expected!r} in failures: {failures}",
        )

    def test_valid_report_passes(self):
        self.assertValid(valid_report())

    def test_missing_heading_fails(self):
        self.assertInvalidContains(valid_report().replace("## Bottom Line", "## Summary"), "## Bottom Line")

    def test_invalid_date_range_fails(self):
        self.assertInvalidContains(
            valid_report().replace("**News window:** July 22, 2026 to August 20, 2026", "**News window:** last month"),
            "News window must contain exactly 2 absolute dates",
        )

    def test_report_below_450_words_fails(self):
        self.assertInvalidContains(valid_report().replace(FILLER, ""), "below 450 words")

    def test_report_above_650_words_fails(self):
        self.assertInvalidContains(valid_report().replace(FILLER, FILLER * 5), "above 650 words")

    def test_news_item_without_url_fails(self):
        self.assertInvalidContains(
            valid_report().replace("[Source](https://exampleco.com/news/product-release)", "Source missing"),
            "News item lacks an HTTP or HTTPS URL",
        )

    def test_watchout_without_severity_fails(self):
        self.assertInvalidContains(
            valid_report().replace("**Medium | Unverified | Traction depth.**", "**Unverified | Traction depth.**"),
            "Watchout lacks severity",
        )

    def test_watchout_without_evidence_status_fails(self):
        self.assertInvalidContains(
            valid_report().replace("**Medium | Unverified | Traction depth.**", "**Medium | Traction depth.**"),
            "Watchout lacks evidence status",
        )

    def test_fewer_than_3_call_priorities_fails(self):
        self.assertInvalidContains(
            valid_report().replace(
                "3. What security, legal, and financial materials can MCA review to validate the core operating claims?",
                "",
            ),
            "Call Priorities must contain exactly 3 numbered items",
        )

    def test_more_than_3_call_priorities_fails(self):
        self.assertInvalidContains(
            valid_report().replace(
                "3. What security, legal, and financial materials can MCA review to validate the core operating claims?",
                "3. What security, legal, and financial materials can MCA review to validate the core operating claims?\n4. What is the next hiring milestone?",
            ),
            "Call Priorities must contain exactly 3 numbered items",
        )

    def test_placeholder_text_fails(self):
        self.assertInvalidContains(valid_report().replace("ExampleCo | Executive DD", "[Company Name] | Executive DD"), "Placeholder text remains")

    def test_duplicate_source_urls_in_sources_fail(self):
        self.assertInvalidContains(
            valid_report().replace(
                "https://exampleco.com/security",
                "https://exampleco.com/customers",
            ),
            "Duplicate source URLs appear in Sources",
        )

    def test_no_recent_news_path_passes(self):
        self.assertValid(valid_report(no_news=True))


if __name__ == "__main__":
    unittest.main()
