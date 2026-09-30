<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">船舶修造工程管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向船舶档案、船坞调度、分段建造、管系安装、涂装作业与试航验收的一体化船厂工程管理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "船舶档案", path: "/ship" }, { label: "船坞调度", path: "/dock" }, { label: "分段建造", path: "/block" }, { label: "焊接作业", path: "/welding" }, { label: "管系安装", path: "/pipe" }, { label: "涂装作业", path: "/paint" }, { label: "电缆敷设", path: "/cable" }, { label: "舾装作业", path: "/outfitting" }, { label: "质量检验", path: "/inspection" }, { label: "试航试验", path: "/seatrial" }, { label: "材料领用", path: "/material" }, { label: "设备维保", path: "/equipment" }, { label: "分包管理", path: "/subcontract" }, { label: "工程进度", path: "/progress" }, { label: "安全监察", path: "/safety" }, { label: "系泊试验", path: "/trial" }, { label: "交船验收", path: "/delivery" }, { label: "工程结算", path: "/settlement" }]
</script>
