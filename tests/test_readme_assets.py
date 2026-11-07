import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = (ROOT / "README.md").read_text(encoding="utf-8")
LOCAL_IMAGES = [s for s in re.findall(r'<img[^>]+src="([^"]+)"', README) if not s.startswith("http")]


class ReadmeAssets(unittest.TestCase):
    def test_local_images_exist(self):
        self.assertTrue(LOCAL_IMAGES)
        for src in LOCAL_IMAGES:
            self.assertTrue((ROOT / src).is_file(), src)

    def test_svgs_animate_with_css_only_and_honor_reduced_motion(self):
        # SMIL ignores prefers-reduced-motion and is blocked by Firefox under GitHub's CSP.
        for src in LOCAL_IMAGES:
            svg = (ROOT / src).read_text(encoding="utf-8")
            self.assertNotRegex(svg, r"<(animate|animateMotion|animateTransform|set)\b", src)
            if "@keyframes" in svg:
                self.assertIn("prefers-reduced-motion: reduce", svg, src)

    def test_svgs_load_nothing_external(self):
        # GitHub serves SVG images with default-src 'none': external fonts or images never load.
        for src in LOCAL_IMAGES:
            svg = (ROOT / src).read_text(encoding="utf-8")
            self.assertNotRegex(svg, r"@import|(href|src)=\"https?:", src)


if __name__ == "__main__":
    unittest.main()
