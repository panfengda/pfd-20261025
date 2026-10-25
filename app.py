import streamlit as st
from pfd.auth import require_login
from pfd.ui import apply_theme

st.set_page_config(page_title="PFD | 风电叶片雨蚀研究孪生", page_icon="🌬️", layout="wide")
apply_theme()
require_login()

st.markdown("""
<div class="hero">
  <div class="eyebrow">PFD · WIND ENERGY RESEARCH TWIN</div>
  <h1>风电叶片前缘雨蚀 · 环境驱动研究平台</h1>
  <p>历史气象回放、多场址比较、数据质量审计、可解释暴露指标与模型验证工作流</p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
c1.metric("研究对象", "叶片前缘雨蚀（LEE）")
c2.metric("气象输入", "历史再分析")
c3.metric("预测状态", "待数据验证")

st.warning(
    "研究边界：本项目目前不是经验证的剩余寿命预测器。天气数据来自历史再分析，不是风场现场实测；"
    "环境暴露指标仅用于筛查和场址比较，不能解释为真实涂层损失或剩余寿命。"
)
st.markdown("### 研究闭环")
st.markdown("""
1. **获取**：下载三个候选场址的历史风速、阵风、降雨、温度和湿度。
2. **审计**：保留原始文件、来源、抓取时间、单位、缺失与异常标记。
3. **分析**：计算透明的环境暴露代理指标，比较不同场址和时间段。
4. **验证**：与公开的叶片前缘侵蚀潜势图谱/论文结果进行外部合理性比较。
5. **升级**：只有获得材料雨蚀试验、叶片检查或现场损伤数据后，才拟合并验证损伤量或寿命模型。
""")
st.markdown("### 页面导航")
st.markdown("""
- **1 历史天气与场址**：查询 Open-Meteo 历史再分析 API，并下载 CSV。
- **2 雨蚀暴露分析**：查看风雨联合时序、暴露指标和不同场址排名。
- **3 数据质量与来源**：查看数据类型、质量标记、原始数据和数据字典。
- **4 验证与研究记录**：记录公开数据集、假设、验证限制和后续实验。
""")
st.caption("天气数据：Open-Meteo Historical Weather API / ERA5；研究参考：Pryor et al. (2024), An Atlas of Wind Turbine Blade Leading Edge Erosion for CONUS, Zenodo record 14247620.")
