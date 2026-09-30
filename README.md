# 船舶修造工程管理平台

面向船舶档案、船坞调度、分段建造、管系安装、涂装作业与试航验收的一体化船厂工程管理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 船舶档案 | `ship` | 船舶 | 船舶编号、船名、船型 |
| 船坞调度 | `dock` | 船坞 | 坞位编号、坞型、坞长 |
| 分段建造 | `block` | 分段 | 分段编号、所属船舶、分段类型 |
| 焊接作业 | `welding` | 焊接记录 | 记录编号、关联分段、焊接方式 |
| 管系安装 | `pipe` | 管系 | 管系编号、所属船舶、管系类别 |
| 涂装作业 | `paint` | 涂装单 | 涂装单号、关联分段、涂料类型 |
| 电缆敷设 | `cable` | 电缆段 | 电缆编号、所属船舶、电缆型号 |
| 舾装作业 | `outfitting` | 舾装单 | 舾装单号、所属船舶、舾装类别 |
| 质量检验 | `inspection` | 检验单 | 检验单号、关联分段、检验项目 |
| 试航试验 | `seatrial` | 试航记录 | 试航编号、所属船舶、试航项目 |
| 材料领用 | `material` | 领用单 | 领用单号、材料名称、材料规格 |
| 设备维保 | `equipment` | 维保记录 | 维保编号、设备名称、设备型号 |
| 分包管理 | `subcontract` | 分包单位 | 单位编码、单位名称、分包类别 |
| 工程进度 | `progress` | 进度记录 | 记录编号、所属船舶、工程节点 |
| 安全监察 | `safety` | 监察记录 | 监察编号、监察区域、监察事项 |
| 系泊试验 | `trial` | 系泊记录 | 记录编号、所属船舶、试验项目 |
| 交船验收 | `delivery` | 交船单 | 交船单号、所属船舶、交船项目 |
| 工程结算 | `settlement` | 结算单 | 结算单号、船东单位、结算周期 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
