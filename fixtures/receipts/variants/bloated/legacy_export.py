"""legacy_export.py: the pre-CLI export pipeline, superseded by the
current summary output but kept around for the finance team's old
automation until they migrate off it."""

from __future__ import annotations

import xml.etree.ElementTree as ET


class LegacyFormatterV1:
    """Formats records for the discontinued export target #1."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v1')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV2:
    """Formats records for the discontinued export target #2."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v2')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV3:
    """Formats records for the discontinued export target #3."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v3')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV4:
    """Formats records for the discontinued export target #4."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v4')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV5:
    """Formats records for the discontinued export target #5."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v5')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV6:
    """Formats records for the discontinued export target #6."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v6')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV7:
    """Formats records for the discontinued export target #7."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v7')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV8:
    """Formats records for the discontinued export target #8."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v8')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV9:
    """Formats records for the discontinued export target #9."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v9')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV10:
    """Formats records for the discontinued export target #10."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v10')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV11:
    """Formats records for the discontinued export target #11."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v11')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV12:
    """Formats records for the discontinued export target #12."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v12')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV13:
    """Formats records for the discontinued export target #13."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v13')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV14:
    """Formats records for the discontinued export target #14."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v14')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV15:
    """Formats records for the discontinued export target #15."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v15')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV16:
    """Formats records for the discontinued export target #16."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v16')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV17:
    """Formats records for the discontinued export target #17."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v17')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV18:
    """Formats records for the discontinued export target #18."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v18')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV19:
    """Formats records for the discontinued export target #19."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v19')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV20:
    """Formats records for the discontinued export target #20."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v20')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV21:
    """Formats records for the discontinued export target #21."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v21')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV22:
    """Formats records for the discontinued export target #22."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v22')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV23:
    """Formats records for the discontinued export target #23."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v23')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV24:
    """Formats records for the discontinued export target #24."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v24')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV25:
    """Formats records for the discontinued export target #25."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v25')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV26:
    """Formats records for the discontinued export target #26."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v26')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV27:
    """Formats records for the discontinued export target #27."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v27')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV28:
    """Formats records for the discontinued export target #28."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v28')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV29:
    """Formats records for the discontinued export target #29."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v29')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV30:
    """Formats records for the discontinued export target #30."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v30')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV31:
    """Formats records for the discontinued export target #31."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v31')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV32:
    """Formats records for the discontinued export target #32."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v32')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV33:
    """Formats records for the discontinued export target #33."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v33')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV34:
    """Formats records for the discontinued export target #34."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v34')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV35:
    """Formats records for the discontinued export target #35."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v35')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV36:
    """Formats records for the discontinued export target #36."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v36')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV37:
    """Formats records for the discontinued export target #37."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v37')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV38:
    """Formats records for the discontinued export target #38."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v38')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV39:
    """Formats records for the discontinued export target #39."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v39')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV40:
    """Formats records for the discontinued export target #40."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v40')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV41:
    """Formats records for the discontinued export target #41."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v41')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV42:
    """Formats records for the discontinued export target #42."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v42')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV43:
    """Formats records for the discontinued export target #43."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v43')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV44:
    """Formats records for the discontinued export target #44."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v44')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV45:
    """Formats records for the discontinued export target #45."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v45')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV46:
    """Formats records for the discontinued export target #46."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v46')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV47:
    """Formats records for the discontinued export target #47."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v47')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV48:
    """Formats records for the discontinued export target #48."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v48')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV49:
    """Formats records for the discontinued export target #49."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v49')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV50:
    """Formats records for the discontinued export target #50."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v50')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV51:
    """Formats records for the discontinued export target #51."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v51')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV52:
    """Formats records for the discontinued export target #52."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v52')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV53:
    """Formats records for the discontinued export target #53."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v53')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV54:
    """Formats records for the discontinued export target #54."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v54')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV55:
    """Formats records for the discontinued export target #55."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v55')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV56:
    """Formats records for the discontinued export target #56."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v56')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV57:
    """Formats records for the discontinued export target #57."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v57')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV58:
    """Formats records for the discontinued export target #58."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v58')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV59:
    """Formats records for the discontinued export target #59."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v59')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV60:
    """Formats records for the discontinued export target #60."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v60')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV61:
    """Formats records for the discontinued export target #61."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v61')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV62:
    """Formats records for the discontinued export target #62."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v62')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV63:
    """Formats records for the discontinued export target #63."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v63')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV64:
    """Formats records for the discontinued export target #64."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v64')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV65:
    """Formats records for the discontinued export target #65."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v65')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV66:
    """Formats records for the discontinued export target #66."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v66')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV67:
    """Formats records for the discontinued export target #67."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v67')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV68:
    """Formats records for the discontinued export target #68."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v68')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV69:
    """Formats records for the discontinued export target #69."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v69')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV70:
    """Formats records for the discontinued export target #70."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v70')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV71:
    """Formats records for the discontinued export target #71."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v71')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV72:
    """Formats records for the discontinued export target #72."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v72')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV73:
    """Formats records for the discontinued export target #73."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v73')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV74:
    """Formats records for the discontinued export target #74."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v74')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV75:
    """Formats records for the discontinued export target #75."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v75')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV76:
    """Formats records for the discontinued export target #76."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v76')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV77:
    """Formats records for the discontinued export target #77."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v77')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV78:
    """Formats records for the discontinued export target #78."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v78')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV79:
    """Formats records for the discontinued export target #79."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v79')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV80:
    """Formats records for the discontinued export target #80."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v80')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV81:
    """Formats records for the discontinued export target #81."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v81')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV82:
    """Formats records for the discontinued export target #82."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v82')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV83:
    """Formats records for the discontinued export target #83."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v83')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV84:
    """Formats records for the discontinued export target #84."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v84')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV85:
    """Formats records for the discontinued export target #85."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v85')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV86:
    """Formats records for the discontinued export target #86."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v86')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV87:
    """Formats records for the discontinued export target #87."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v87')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV88:
    """Formats records for the discontinued export target #88."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v88')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV89:
    """Formats records for the discontinued export target #89."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v89')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV90:
    """Formats records for the discontinued export target #90."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v90')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV91:
    """Formats records for the discontinued export target #91."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v91')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV92:
    """Formats records for the discontinued export target #92."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v92')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV93:
    """Formats records for the discontinued export target #93."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v93')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV94:
    """Formats records for the discontinued export target #94."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v94')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV95:
    """Formats records for the discontinued export target #95."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v95')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV96:
    """Formats records for the discontinued export target #96."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v96')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV97:
    """Formats records for the discontinued export target #97."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v97')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV98:
    """Formats records for the discontinued export target #98."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v98')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV99:
    """Formats records for the discontinued export target #99."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v99')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV100:
    """Formats records for the discontinued export target #100."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v100')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV101:
    """Formats records for the discontinued export target #101."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v101')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV102:
    """Formats records for the discontinued export target #102."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v102')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV103:
    """Formats records for the discontinued export target #103."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v103')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV104:
    """Formats records for the discontinued export target #104."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v104')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV105:
    """Formats records for the discontinued export target #105."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v105')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV106:
    """Formats records for the discontinued export target #106."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v106')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV107:
    """Formats records for the discontinued export target #107."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v107')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV108:
    """Formats records for the discontinued export target #108."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v108')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV109:
    """Formats records for the discontinued export target #109."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v109')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV110:
    """Formats records for the discontinued export target #110."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v110')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV111:
    """Formats records for the discontinued export target #111."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v111')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV112:
    """Formats records for the discontinued export target #112."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v112')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV113:
    """Formats records for the discontinued export target #113."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v113')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV114:
    """Formats records for the discontinued export target #114."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v114')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV115:
    """Formats records for the discontinued export target #115."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v115')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV116:
    """Formats records for the discontinued export target #116."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v116')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV117:
    """Formats records for the discontinued export target #117."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v117')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV118:
    """Formats records for the discontinued export target #118."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v118')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV119:
    """Formats records for the discontinued export target #119."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v119')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV120:
    """Formats records for the discontinued export target #120."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v120')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV121:
    """Formats records for the discontinued export target #121."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v121')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV122:
    """Formats records for the discontinued export target #122."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v122')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV123:
    """Formats records for the discontinued export target #123."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v123')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV124:
    """Formats records for the discontinued export target #124."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v124')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV125:
    """Formats records for the discontinued export target #125."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v125')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV126:
    """Formats records for the discontinued export target #126."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v126')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV127:
    """Formats records for the discontinued export target #127."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v127')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV128:
    """Formats records for the discontinued export target #128."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v128')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV129:
    """Formats records for the discontinued export target #129."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v129')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV130:
    """Formats records for the discontinued export target #130."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v130')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV131:
    """Formats records for the discontinued export target #131."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v131')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV132:
    """Formats records for the discontinued export target #132."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v132')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV133:
    """Formats records for the discontinued export target #133."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v133')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV134:
    """Formats records for the discontinued export target #134."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v134')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV135:
    """Formats records for the discontinued export target #135."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v135')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV136:
    """Formats records for the discontinued export target #136."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v136')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV137:
    """Formats records for the discontinued export target #137."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v137')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV138:
    """Formats records for the discontinued export target #138."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v138')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV139:
    """Formats records for the discontinued export target #139."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v139')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV140:
    """Formats records for the discontinued export target #140."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v140')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV141:
    """Formats records for the discontinued export target #141."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v141')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV142:
    """Formats records for the discontinued export target #142."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v142')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV143:
    """Formats records for the discontinued export target #143."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v143')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV144:
    """Formats records for the discontinued export target #144."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v144')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV145:
    """Formats records for the discontinued export target #145."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v145')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV146:
    """Formats records for the discontinued export target #146."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v146')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV147:
    """Formats records for the discontinued export target #147."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v147')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV148:
    """Formats records for the discontinued export target #148."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v148')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV149:
    """Formats records for the discontinued export target #149."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v149')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV150:
    """Formats records for the discontinued export target #150."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v150')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV151:
    """Formats records for the discontinued export target #151."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v151')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV152:
    """Formats records for the discontinued export target #152."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v152')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV153:
    """Formats records for the discontinued export target #153."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v153')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV154:
    """Formats records for the discontinued export target #154."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v154')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV155:
    """Formats records for the discontinued export target #155."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v155')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV156:
    """Formats records for the discontinued export target #156."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v156')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV157:
    """Formats records for the discontinued export target #157."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v157')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV158:
    """Formats records for the discontinued export target #158."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v158')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV159:
    """Formats records for the discontinued export target #159."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v159')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV160:
    """Formats records for the discontinued export target #160."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v160')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV161:
    """Formats records for the discontinued export target #161."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v161')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV162:
    """Formats records for the discontinued export target #162."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v162')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV163:
    """Formats records for the discontinued export target #163."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v163')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV164:
    """Formats records for the discontinued export target #164."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v164')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV165:
    """Formats records for the discontinued export target #165."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v165')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV166:
    """Formats records for the discontinued export target #166."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v166')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV167:
    """Formats records for the discontinued export target #167."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v167')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV168:
    """Formats records for the discontinued export target #168."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v168')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV169:
    """Formats records for the discontinued export target #169."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v169')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV170:
    """Formats records for the discontinued export target #170."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v170')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV171:
    """Formats records for the discontinued export target #171."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v171')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV172:
    """Formats records for the discontinued export target #172."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v172')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV173:
    """Formats records for the discontinued export target #173."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v173')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV174:
    """Formats records for the discontinued export target #174."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v174')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV175:
    """Formats records for the discontinued export target #175."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v175')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV176:
    """Formats records for the discontinued export target #176."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v176')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV177:
    """Formats records for the discontinued export target #177."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v177')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV178:
    """Formats records for the discontinued export target #178."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v178')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV179:
    """Formats records for the discontinued export target #179."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v179')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV180:
    """Formats records for the discontinued export target #180."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v180')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV181:
    """Formats records for the discontinued export target #181."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v181')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV182:
    """Formats records for the discontinued export target #182."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v182')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV183:
    """Formats records for the discontinued export target #183."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v183')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV184:
    """Formats records for the discontinued export target #184."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v184')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV185:
    """Formats records for the discontinued export target #185."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v185')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV186:
    """Formats records for the discontinued export target #186."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v186')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV187:
    """Formats records for the discontinued export target #187."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v187')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV188:
    """Formats records for the discontinued export target #188."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v188')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV189:
    """Formats records for the discontinued export target #189."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v189')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV190:
    """Formats records for the discontinued export target #190."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v190')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV191:
    """Formats records for the discontinued export target #191."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v191')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV192:
    """Formats records for the discontinued export target #192."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v192')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV193:
    """Formats records for the discontinued export target #193."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v193')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV194:
    """Formats records for the discontinued export target #194."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v194')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV195:
    """Formats records for the discontinued export target #195."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v195')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV196:
    """Formats records for the discontinued export target #196."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v196')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV197:
    """Formats records for the discontinued export target #197."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v197')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV198:
    """Formats records for the discontinued export target #198."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v198')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV199:
    """Formats records for the discontinued export target #199."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v199')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV200:
    """Formats records for the discontinued export target #200."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v200')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV201:
    """Formats records for the discontinued export target #201."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v201')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV202:
    """Formats records for the discontinued export target #202."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v202')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV203:
    """Formats records for the discontinued export target #203."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v203')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV204:
    """Formats records for the discontinued export target #204."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v204')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV205:
    """Formats records for the discontinued export target #205."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v205')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV206:
    """Formats records for the discontinued export target #206."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v206')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV207:
    """Formats records for the discontinued export target #207."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v207')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV208:
    """Formats records for the discontinued export target #208."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v208')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV209:
    """Formats records for the discontinued export target #209."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v209')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV210:
    """Formats records for the discontinued export target #210."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v210')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV211:
    """Formats records for the discontinued export target #211."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v211')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV212:
    """Formats records for the discontinued export target #212."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v212')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV213:
    """Formats records for the discontinued export target #213."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v213')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV214:
    """Formats records for the discontinued export target #214."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v214')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV215:
    """Formats records for the discontinued export target #215."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v215')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV216:
    """Formats records for the discontinued export target #216."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v216')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV217:
    """Formats records for the discontinued export target #217."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v217')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV218:
    """Formats records for the discontinued export target #218."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v218')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)


class LegacyFormatterV219:
    """Formats records for the discontinued export target #219."""

    def __init__(self, options=None):
        self.options = options or {}

    def format(self, records):
        root = ET.Element('legacy_export_v219')
        for record in records:
            item = ET.SubElement(root, 'item')
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)
        return ET.tostring(root)

