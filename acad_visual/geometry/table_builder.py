from dataclasses import dataclass
from typing import List, Optional, Tuple, Union
from acad_visual.core.primitives import Segment, MathLabel, StrokeStyle

@dataclass
class TableCell:
    content: Union[str, List[str]]
    rowspan: int = 1
    colspan: int = 1
    math_mode: bool = True
    font_size: float = 15.0
    font_weight: str = "normal"
    align: str = "center"

class TableLayoutEngine:
    """
    Universal Hybrid Table Layout Engine for academic, physics, and chemistry diagrams.
    Automatically handles:
    - Multi-line text wrapping (Bengali & Math/LaTeX)
    - Comma-separated list splitting
    - Proportional column width estimation
    - Rowspan and colspan merging
    - Clean grid segment drawing and centered multi-line text placement
    """
    def __init__(self, x_origin: float = 30.0, y_origin: float = 30.0, total_width: float = 500.0, base_row_height: float = 40.0):
        self.x_origin = x_origin
        self.y_origin = y_origin
        self.total_width = total_width
        self.base_row_height = base_row_height
        self.rows: List[List[TableCell]] = []
        self.col_widths: Optional[List[float]] = None
        self.footer_text: Optional[str] = None
        self.footer_height: float = 40.0

    @staticmethod
    def wrap_cell_content(text: str, max_chars: int = 12) -> List[str]:
        if not text:
            return [""]
        if "\n" in text:
            return [line.strip() for line in text.split("\n") if line.strip()]
        
        # If it's a comma-separated list (e.g. m = -3, -2, -1, 0, +1, +2, +3)
        if "," in text and len(text) > max_chars:
            parts = [p.strip() for p in text.split(",")]
            lines = []
            curr = ""
            for i, p in enumerate(parts):
                item = p + ("," if i < len(parts) - 1 else "")
                if not curr:
                    curr = item
                elif len(curr) + len(item) + 1 <= max_chars:
                    curr += " " + item
                else:
                    lines.append(curr)
                    curr = item
            if curr:
                lines.append(curr)
            return lines

        # If it's multi-word text (e.g. প্রধান কোয়ান্টাম সংখ্যা)
        words = text.split()
        if len(words) > 1 and (len(text) > max_chars or any(len(w) >= 5 for w in words)):
            lines = []
            curr = ""
            for w in words:
                if not curr:
                    curr = w
                elif len(curr) + len(w) + 1 <= max_chars:
                    curr += " " + w
                else:
                    lines.append(curr)
                    curr = w
            if curr:
                lines.append(curr)
            return lines

        return [text]

    def add_row(self, cells: List[Union[str, TableCell]]):
        row = []
        for c in cells:
            if isinstance(c, TableCell):
                row.append(c)
            else:
                row.append(TableCell(content=c))
        self.rows.append(row)

    def set_col_widths(self, widths: List[float]):
        self.col_widths = widths

    def set_footer(self, text: str, height: float = 40.0):
        self.footer_text = text
        self.footer_height = height

    def build(self) -> Tuple[List[Segment], List[MathLabel], float, float]:
        if not self.rows:
            return [], [], self.total_width, 100.0

        num_cols = max(sum(c.colspan for c in r) for r in self.rows)
        num_rows = len(self.rows)

        if not self.col_widths:
            w_each = self.total_width / num_cols
            col_widths = [w_each] * num_cols
        else:
            col_widths = self.col_widths

        x_coords = [self.x_origin]
        for w in col_widths:
            x_coords.append(x_coords[-1] + w)

        row_heights = []
        for r_idx, row in enumerate(self.rows):
            max_lines = 1
            for c in row:
                if isinstance(c.content, list):
                    lines_count = len(c.content)
                else:
                    lines_count = len(self.wrap_cell_content(c.content, max_chars=max(6, int(col_widths[0] / (c.font_size * 0.5)))))
                if c.rowspan == 1:
                    max_lines = max(max_lines, lines_count)
            rh = max(self.base_row_height, 20.0 + max_lines * 20.0)
            row_heights.append(rh)

        y_coords = [self.y_origin]
        for rh in row_heights:
            y_coords.append(y_coords[-1] + rh)

        segments: List[Segment] = []
        labels: List[MathLabel] = []
        occupied = [[False for _ in range(num_cols)] for _ in range(num_rows)]

        for r_idx, row in enumerate(self.rows):
            c_idx = 0
            for cell in row:
                while c_idx < num_cols and occupied[r_idx][c_idx]:
                    c_idx += 1
                if c_idx >= num_cols:
                    break

                for dr in range(cell.rowspan):
                    for dc in range(cell.colspan):
                        if r_idx + dr < num_rows and c_idx + dc < num_cols:
                            occupied[r_idx + dr][c_idx + dc] = True

                x0 = x_coords[c_idx]
                x1 = x_coords[c_idx + cell.colspan]
                y0 = y_coords[r_idx]
                y1 = y_coords[r_idx + cell.rowspan]

                if isinstance(cell.content, list):
                    lines = cell.content
                else:
                    col_w = x1 - x0
                    max_chars = max(6, int(col_w / (cell.font_size * 0.55)))
                    lines = self.wrap_cell_content(cell.content, max_chars=max_chars)

                num_lines = len(lines)
                line_spacing = cell.font_size * 1.35
                cell_mid_y = (y0 + y1) / 2.0
                total_text_h = (num_lines - 1) * line_spacing
                start_y = cell_mid_y - total_text_h / 2.0

                for l_idx, line in enumerate(lines):
                    line_y = start_y + l_idx * line_spacing
                    if cell.align == "center":
                        line_x = (x0 + x1) / 2.0
                        anchor = "middle"
                    elif cell.align == "left":
                        line_x = x0 + 10.0
                        anchor = "start"
                    else:
                        line_x = x1 - 10.0
                        anchor = "end"

                    labels.append(
                        MathLabel(
                            id=f"cell_{r_idx}_{c_idx}_{l_idx}",
                            text=line,
                            x=line_x,
                            y=line_y,
                            font_size=cell.font_size,
                            font_weight=cell.font_weight,
                            anchor=anchor,
                            math_mode=cell.math_mode
                        )
                    )
                c_idx += cell.colspan

        # Horizontal grid lines
        for r_idx in range(num_rows + 1):
            stroke_w = 2.2 if r_idx in [0, 1, num_rows] else 1.5
            curr_start = None
            for c_idx in range(num_cols):
                is_merged = False
                if 0 < r_idx < num_rows:
                    for test_r, r_obj in enumerate(self.rows):
                        test_c = 0
                        for cell_obj in r_obj:
                            if test_r <= r_idx - 1 < test_r + cell_obj.rowspan and test_r <= r_idx < test_r + cell_obj.rowspan:
                                if test_c <= c_idx < test_c + cell_obj.colspan:
                                    is_merged = True
                                    break
                            test_c += cell_obj.colspan
                        if is_merged:
                            break
                if not is_merged:
                    if curr_start is None:
                        curr_start = x_coords[c_idx]
                else:
                    if curr_start is not None:
                        segments.append(Segment(id=f"h_{r_idx}_{len(segments)}", start=(curr_start, y_coords[r_idx]), end=(x_coords[c_idx], y_coords[r_idx]), stroke_width=stroke_w, color="#111111"))
                        curr_start = None

            if curr_start is not None:
                segments.append(Segment(id=f"h_{r_idx}_{len(segments)}", start=(curr_start, y_coords[r_idx]), end=(x_coords[-1], y_coords[r_idx]), stroke_width=stroke_w, color="#111111"))

        # Vertical grid lines
        for c_idx in range(num_cols + 1):
            stroke_w = 2.2 if c_idx in [0, num_cols] else 1.5
            curr_start = None
            for r_idx in range(num_rows):
                is_merged = False
                if 0 < c_idx < num_cols:
                    for test_r, r_obj in enumerate(self.rows):
                        test_c = 0
                        for cell_obj in r_obj:
                            if test_c <= c_idx - 1 < test_c + cell_obj.colspan and test_c <= c_idx < test_c + cell_obj.colspan:
                                if test_r <= r_idx < test_r + cell_obj.rowspan:
                                    is_merged = True
                                    break
                            test_c += cell_obj.colspan
                        if is_merged:
                            break
                if not is_merged:
                    if curr_start is None:
                        curr_start = y_coords[r_idx]
                else:
                    if curr_start is not None:
                        segments.append(Segment(id=f"v_{c_idx}_{len(segments)}", start=(x_coords[c_idx], curr_start), end=(x_coords[c_idx], y_coords[r_idx]), stroke_width=stroke_w, color="#111111"))
                        curr_start = None

            if curr_start is not None:
                segments.append(Segment(id=f"v_{c_idx}_{len(segments)}", start=(x_coords[c_idx], curr_start), end=(x_coords[c_idx], y_coords[-1]), stroke_width=stroke_w, color="#111111"))

        total_h = y_coords[-1] + 20.0
        if self.footer_text:
            y_foot_top = y_coords[-1]
            y_foot_bot = y_foot_top + self.footer_height
            segments.append(Segment(id="foot_bot", start=(x_coords[0], y_foot_bot), end=(x_coords[-1], y_foot_bot), stroke_width=2.2, color="#111111"))
            segments.append(Segment(id="foot_left", start=(x_coords[0], y_foot_top), end=(x_coords[0], y_foot_bot), stroke_width=2.2, color="#111111"))
            segments.append(Segment(id="foot_right", start=(x_coords[-1], y_foot_top), end=(x_coords[-1], y_foot_bot), stroke_width=2.2, color="#111111"))
            labels.append(
                MathLabel(
                    id="lbl_footer",
                    text=self.footer_text,
                    x=(x_coords[0] + x_coords[-1]) / 2.0,
                    y=(y_foot_top + y_foot_bot) / 2.0,
                    font_size=16.0,
                    font_weight="bold",
                    math_mode=False
                )
            )
            total_h = y_foot_bot + 20.0

        return segments, labels, x_coords[-1] + self.x_origin, total_h
