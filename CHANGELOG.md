# Changelog

## [v0.2.5] - 2025-12-23

### Added
- **跨域访问 (CORS)**:
  - 引入 `django-cors-headers` 并在 `INSTALLED_APPS` 与 `MIDDLEWARE` 中启用。
  - 允许域名 `https://apirouter.aibox.uno` 进行跨域访问，支持 `GET/POST/OPTIONS`。

## [v0.2.4] - 2025-12-23

### Changed
- **SoraGen API Logic**:
  - 调整 `submit` 接口逻辑：`style` 和 `productSeed` 参数变更为**可选**。
  - 若参数缺失或数据库中未找到对应记录，系统不再报错 (400/404)，而是将对应的 Prompt (Prompt A / Prompt B) 默认为空字符串。

## [v0.2.3] - 2025-12-23

### Added
- **项目工程化 (Project Engineering)**:
  - 新增 `.gitignore` 配置文件，规范化 Git 忽略规则（Python, Django, Environment, IDE）。
  - 更新 `README.md`，完善项目简介、快速开始指南及 SoraGen API 文档。

## [v0.2.2] - 2025-12-23

### Fixed
- **SoraGen API Submit**:
  - 修复了 `submit` 接口的上游请求方式。修正了 `requests.post` 使用 `json` 参数导致的 `Content-Type` 不一致问题，改为使用 `data` 参数以匹配 `application/x-www-form-urlencoded` 头信息。

## [v0.2.1] - 2025-12-23

### Changed
- **SoraGen 测试面板 (Test Panel)**:
  - 优化 API Key 自动填充逻辑，确保 Global Key 输入、粘贴或加载时能实时同步至所有子表单。

## [v0.2.0] - 2025-12-23

### Changed
- **SoraGen 测试面板 (Test Panel)**:
  - 将 `Style` 和 `Product Seed` 输入框升级为动态下拉菜单，数据实时从数据库加载。
  - 根据 API 规范设置了默认参数：`aspectRatio` (9:16), `duration` (10), `size` (small)。
  - 增加了 API Key 的本地缓存功能 (`localStorage`)，无需重复输入。

## [v0.1.1] - 2025-12-23

### Changed
- **路由重构 (Routes Refactoring)**:
  - 遵循 `BASE_URL/PROJECT_NAME/XXXXX` 规范，将 SoraGen 路由前缀统一为 `/soragen/`。
  - 新增 `test-panel` 页面用于 API 调试。

## [v0.1.0] - 2025-12-23

### Added
- **项目初始化 (Project Initialization)**:
  - 创建 Django 项目 `APIRouter`。
  - 创建 `soragen` 应用，定义 `SoraGenStyle` 和 `SoraGenProductSeed` 模型。
  - 配置数据库连接 (SQLite 兼容模式)。
  - 实现 `submit` (POST) 和 `detail` (GET) 接口逻辑。
  - 集成 Apple Design 风格的基础 UI 模板。

