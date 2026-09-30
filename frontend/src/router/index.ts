import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Ship = () => import('@/views/ship/index.vue')
const Dock = () => import('@/views/dock/index.vue')
const Block = () => import('@/views/block/index.vue')
const Welding = () => import('@/views/welding/index.vue')
const Pipe = () => import('@/views/pipe/index.vue')
const Paint = () => import('@/views/paint/index.vue')
const Cable = () => import('@/views/cable/index.vue')
const Outfitting = () => import('@/views/outfitting/index.vue')
const Inspection = () => import('@/views/inspection/index.vue')
const Seatrial = () => import('@/views/seatrial/index.vue')
const Material = () => import('@/views/material/index.vue')
const Equipment = () => import('@/views/equipment/index.vue')
const Subcontract = () => import('@/views/subcontract/index.vue')
const Progress = () => import('@/views/progress/index.vue')
const Safety = () => import('@/views/safety/index.vue')
const Trial = () => import('@/views/trial/index.vue')
const Delivery = () => import('@/views/delivery/index.vue')
const Settlement = () => import('@/views/settlement/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/ship', name: 'ship', component: Ship },
    { path: '/dock', name: 'dock', component: Dock },
    { path: '/block', name: 'block', component: Block },
    { path: '/welding', name: 'welding', component: Welding },
    { path: '/pipe', name: 'pipe', component: Pipe },
    { path: '/paint', name: 'paint', component: Paint },
    { path: '/cable', name: 'cable', component: Cable },
    { path: '/outfitting', name: 'outfitting', component: Outfitting },
    { path: '/inspection', name: 'inspection', component: Inspection },
    { path: '/seatrial', name: 'seatrial', component: Seatrial },
    { path: '/material', name: 'material', component: Material },
    { path: '/equipment', name: 'equipment', component: Equipment },
    { path: '/subcontract', name: 'subcontract', component: Subcontract },
    { path: '/progress', name: 'progress', component: Progress },
    { path: '/safety', name: 'safety', component: Safety },
    { path: '/trial', name: 'trial', component: Trial },
    { path: '/delivery', name: 'delivery', component: Delivery },
    { path: '/settlement', name: 'settlement', component: Settlement },
  ],
})

export default router
