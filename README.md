# APIRouter

**APIRouter** 是一个基于 Django 开发的多项目 API 中转处理站。它旨在为不同的 AI 服务和内部工具提供统一的 API 路由、请求预处理（如 Prompt 拼接）和数据管理功能。

## 📦 项目模块

### 1. SoraGen API (`/soragen/`)
用于处理 Sora 视频生成服务的请求中转。
- **核心功能**:
  - **Prompt 拼接**: 根据数据库配置的 `Style` (Prompt A) 和 `Product Seed` (Prompt B)，自动组合用户的 Prompt。
  - **API 转发**: 将处理后的请求转发至上游服务。
  - **测试面板**: 提供 Apple Design 风格的 Web 界面进行 API 调试。

## 🚀 快速开始

### 环境要求
- Python 3.11+
- SQLite (默认) 或 MySQL

### 安装步骤

1. **克隆项目并进入目录**
   ```bash
   cd apirouter
   ```

2. **创建并激活虚拟环境**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

4. **数据库迁移**
   初始化数据库表结构：
   ```bash
   python manage.py migrate
   ```

5. **启动服务**
   ```bash
   python manage.py runserver
   ```
   服务将运行在 `http://127.0.0.1:8000/`

## 📚 API 文档

### SoraGen

#### 1. 提交任务 (Submit)
- **URL**: `/api/sora2/submit` (中转) 或 `/soragen/api/sora2/submit` (本地)
- **Method**: `POST`
- **Params**:
  - `key`: API Key (Query Param)
  - `style`: 风格标识 (Body)
  - `productSeed`: 产品种子标识 (Body)
  - `prompt`: 用户提示词 (Body)
  - `aspectRatio`: 宽高比 (Body, 默认 9:16)
  - `duration`: 时长 (Body, 默认 10)

#### 2. 查询详情 (Detail)
- **URL**: `/api/sora2/detail` (中转) 或 `/soragen/api/sora2/detail` (本地)
- **Method**: `GET`
- **Params**:
  - `key`: API Key
  - `id`: 任务 ID

## 🛠 开发指南

### 路由规范
所有新项目路由应遵循 `BASE_URL/PROJECT_NAME/XXXXX` 格式。

### 变更日志
本项目遵循“只增不删”原则记录变更日志，详情请查阅 [CHANGELOG.md](CHANGELOG.md)。
