# 地图、港口与人口

> 何时读：改人口、拆州、查港口与海路、开地图编辑器之前。不必读：只改脚本逻辑。

| 工具 | 位置 | 用途与运行 |
|---|---|---|
| `pop_rewrite.py` | `tools/map-pops/` | 按 JSON 计划改 `history/pops`：替换某文化人数、追加人口，逐州断言总量。人口重配、拆州后补人口：`python tools/map-pops/pop_rewrite.py <plan.json>`（只预览）；确认后加 `--write` |
| 地图审计与提案 | `WORK/tools/map_design_audit.py`、`map_design_options.py` | 州人口、产业、面积、邻接、locator 证据 |
| 交通与港口门禁 | `WORK/tools/map_transport_preflight.py`、`inspect_splnet.py`、`spline_candidate.py` | 只读检查海路网 `gfx/map/spline_network/spline_network.splnet`（二进制，用 `inspect_splnet.py` 读，不要说“读不了”）；见 [map-transport.md](../../references/map-transport.md) |
| 地图编辑器工程 | `WORK/editor/`（`province_move.py`、`harbor_routes.py`、`map_editor_runtime.py`） | 拆州的守恒计算、显式新港口、隔离启动编辑器 |

先读 `lookup/map-data.md`（州、港口、海路、编辑器实测）与 `references/map-transport.md`，再用工具。
