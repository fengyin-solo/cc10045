"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class ShipEntry(BaseModel):
    """船舶明细结构。"""

    field_0: str | None = None  # 船舶编号
    field_1: str | None = None  # 船名
    field_2: str | None = None  # 船型
    field_3: str | None = None  # 船级社
    field_4: str | None = None  # 总吨位
    field_5: str | None = None  # 主机功率
    field_6: str | None = None  # 船东单位
    field_7: str | None = None  # 船舶状态

class DockEntry(BaseModel):
    """船坞明细结构。"""

    field_0: str | None = None  # 坞位编号
    field_1: str | None = None  # 坞型
    field_2: str | None = None  # 坞长
    field_3: str | None = None  # 坞宽
    field_4: str | None = None  # 适用船型
    field_5: str | None = None  # 占用船舶
    field_6: str | None = None  # 进坞日期
    field_7: str | None = None  # 坞位状态

class BlockEntry(BaseModel):
    """分段明细结构。"""

    field_0: str | None = None  # 分段编号
    field_1: str | None = None  # 所属船舶
    field_2: str | None = None  # 分段类型
    field_3: str | None = None  # 分段重量
    field_4: str | None = None  # 建造区域
    field_5: str | None = None  # 开工日期
    field_6: str | None = None  # 完工日期
    field_7: str | None = None  # 分段状态

class WeldingEntry(BaseModel):
    """焊接记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 关联分段
    field_2: str | None = None  # 焊接方式
    field_3: str | None = None  # 焊缝长度
    field_4: str | None = None  # 焊工姓名
    field_5: str | None = None  # 探伤结论
    field_6: str | None = None  # 焊接日期
    field_7: str | None = None  # 焊接状态

class PipeEntry(BaseModel):
    """管系明细结构。"""

    field_0: str | None = None  # 管系编号
    field_1: str | None = None  # 所属船舶
    field_2: str | None = None  # 管系类别
    field_3: str | None = None  # 管径规格
    field_4: str | None = None  # 材质
    field_5: str | None = None  # 安装区域
    field_6: str | None = None  # 安装日期
    field_7: str | None = None  # 管系状态

class PaintEntry(BaseModel):
    """涂装单明细结构。"""

    field_0: str | None = None  # 涂装单号
    field_1: str | None = None  # 关联分段
    field_2: str | None = None  # 涂料类型
    field_3: str | None = None  # 涂装面积
    field_4: str | None = None  # 涂层道数
    field_5: str | None = None  # 施工班组
    field_6: str | None = None  # 完成日期
    field_7: str | None = None  # 涂装状态

class CableEntry(BaseModel):
    """电缆段明细结构。"""

    field_0: str | None = None  # 电缆编号
    field_1: str | None = None  # 所属船舶
    field_2: str | None = None  # 电缆型号
    field_3: str | None = None  # 敷设长度
    field_4: str | None = None  # 敷设区域
    field_5: str | None = None  # 接线状态
    field_6: str | None = None  # 敷设日期
    field_7: str | None = None  # 电缆状态

class OutfittingEntry(BaseModel):
    """舾装单明细结构。"""

    field_0: str | None = None  # 舾装单号
    field_1: str | None = None  # 所属船舶
    field_2: str | None = None  # 舾装类别
    field_3: str | None = None  # 舾装件数
    field_4: str | None = None  # 安装区域
    field_5: str | None = None  # 施工班组
    field_6: str | None = None  # 完成日期
    field_7: str | None = None  # 舾装状态

class InspectionEntry(BaseModel):
    """检验单明细结构。"""

    field_0: str | None = None  # 检验单号
    field_1: str | None = None  # 关联分段
    field_2: str | None = None  # 检验项目
    field_3: str | None = None  # 检验标准
    field_4: str | None = None  # 检验人员
    field_5: str | None = None  # 检验日期
    field_6: str | None = None  # 检验结论
    field_7: str | None = None  # 检验状态

class SeatrialEntry(BaseModel):
    """试航记录明细结构。"""

    field_0: str | None = None  # 试航编号
    field_1: str | None = None  # 所属船舶
    field_2: str | None = None  # 试航项目
    field_3: str | None = None  # 计划时段
    field_4: str | None = None  # 试航海域
    field_5: str | None = None  # 试航人员
    field_6: str | None = None  # 试航日期
    field_7: str | None = None  # 试航状态

class MaterialEntry(BaseModel):
    """领用单明细结构。"""

    field_0: str | None = None  # 领用单号
    field_1: str | None = None  # 材料名称
    field_2: str | None = None  # 材料规格
    field_3: str | None = None  # 领用数量
    field_4: str | None = None  # 领用人员
    field_5: str | None = None  # 领用日期
    field_6: str | None = None  # 所属区域
    field_7: str | None = None  # 领用状态

class EquipmentEntry(BaseModel):
    """维保记录明细结构。"""

    field_0: str | None = None  # 维保编号
    field_1: str | None = None  # 设备名称
    field_2: str | None = None  # 设备型号
    field_3: str | None = None  # 维保类型
    field_4: str | None = None  # 上次维保日
    field_5: str | None = None  # 下次维保日
    field_6: str | None = None  # 责任人
    field_7: str | None = None  # 维保状态

class SubcontractEntry(BaseModel):
    """分包单位明细结构。"""

    field_0: str | None = None  # 单位编码
    field_1: str | None = None  # 单位名称
    field_2: str | None = None  # 分包类别
    field_3: str | None = None  # 资质等级
    field_4: str | None = None  # 联系人
    field_5: str | None = None  # 联系电话
    field_6: str | None = None  # 现场负责人
    field_7: str | None = None  # 单位状态

class ProgressEntry(BaseModel):
    """进度记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 所属船舶
    field_2: str | None = None  # 工程节点
    field_3: str | None = None  # 计划进度
    field_4: str | None = None  # 实际进度
    field_5: str | None = None  # 偏差说明
    field_6: str | None = None  # 填报人员
    field_7: str | None = None  # 记录状态

class SafetyEntry(BaseModel):
    """监察记录明细结构。"""

    field_0: str | None = None  # 监察编号
    field_1: str | None = None  # 监察区域
    field_2: str | None = None  # 监察事项
    field_3: str | None = None  # 违规情形
    field_4: str | None = None  # 涉及单位
    field_5: str | None = None  # 监察人员
    field_6: str | None = None  # 监察日期
    field_7: str | None = None  # 监察状态

class TrialEntry(BaseModel):
    """系泊记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 所属船舶
    field_2: str | None = None  # 试验项目
    field_3: str | None = None  # 试验参数
    field_4: str | None = None  # 试验结论
    field_5: str | None = None  # 试验人员
    field_6: str | None = None  # 试验日期
    field_7: str | None = None  # 记录状态

class DeliveryEntry(BaseModel):
    """交船单明细结构。"""

    field_0: str | None = None  # 交船单号
    field_1: str | None = None  # 所属船舶
    field_2: str | None = None  # 交船项目
    field_3: str | None = None  # 验收标准
    field_4: str | None = None  # 船东代表
    field_5: str | None = None  # 交船日期
    field_6: str | None = None  # 验收结论
    field_7: str | None = None  # 交船状态

class SettlementEntry(BaseModel):
    """结算单明细结构。"""

    field_0: str | None = None  # 结算单号
    field_1: str | None = None  # 船东单位
    field_2: str | None = None  # 结算周期
    field_3: str | None = None  # 结算项数
    field_4: str | None = None  # 应付金额
    field_5: str | None = None  # 已付金额
    field_6: str | None = None  # 审核人员
    field_7: str | None = None  # 结算状态
