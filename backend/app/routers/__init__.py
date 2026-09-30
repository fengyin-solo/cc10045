"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import ship as router_ship
from app.routers import dock as router_dock
from app.routers import block as router_block
from app.routers import welding as router_welding
from app.routers import pipe as router_pipe
from app.routers import paint as router_paint
from app.routers import cable as router_cable
from app.routers import outfitting as router_outfitting
from app.routers import inspection as router_inspection
from app.routers import seatrial as router_seatrial
from app.routers import material as router_material
from app.routers import equipment as router_equipment
from app.routers import subcontract as router_subcontract
from app.routers import progress as router_progress
from app.routers import safety as router_safety
from app.routers import trial as router_trial
from app.routers import delivery as router_delivery
from app.routers import settlement as router_settlement

ROUTERS = [router_ship, router_dock, router_block, router_welding, router_pipe, router_paint, router_cable, router_outfitting, router_inspection, router_seatrial, router_material, router_equipment, router_subcontract, router_progress, router_safety, router_trial, router_delivery, router_settlement]
