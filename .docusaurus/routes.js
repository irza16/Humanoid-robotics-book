import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/Humanoid-robotics-book/docs',
    component: ComponentCreator('/Humanoid-robotics-book/docs', '940'),
    routes: [
      {
        path: '/Humanoid-robotics-book/docs',
        component: ComponentCreator('/Humanoid-robotics-book/docs', '140'),
        routes: [
          {
            path: '/Humanoid-robotics-book/docs',
            component: ComponentCreator('/Humanoid-robotics-book/docs', '7df'),
            routes: [
              {
                path: '/Humanoid-robotics-book/docs/appendix/glossary',
                component: ComponentCreator('/Humanoid-robotics-book/docs/appendix/glossary', '214'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/appendix/installation-guides',
                component: ComponentCreator('/Humanoid-robotics-book/docs/appendix/installation-guides', '40a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/appendix/resources',
                component: ComponentCreator('/Humanoid-robotics-book/docs/appendix/resources', 'd3a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/appendix/troubleshooting',
                component: ComponentCreator('/Humanoid-robotics-book/docs/appendix/troubleshooting', '91a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/foundations/core-subsystems',
                component: ComponentCreator('/Humanoid-robotics-book/docs/foundations/core-subsystems', '62d'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/foundations/future-trajectory',
                component: ComponentCreator('/Humanoid-robotics-book/docs/foundations/future-trajectory', '653'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/foundations/modern-examples',
                component: ComponentCreator('/Humanoid-robotics-book/docs/foundations/modern-examples', 'ad6'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/foundations/overview',
                component: ComponentCreator('/Humanoid-robotics-book/docs/foundations/overview', '2aa'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/foundations/what-is-humanoid-robotics',
                component: ComponentCreator('/Humanoid-robotics-book/docs/foundations/what-is-humanoid-robotics', 'a90'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/hardware-guide/cloud-vs-onpremise',
                component: ComponentCreator('/Humanoid-robotics-book/docs/hardware-guide/cloud-vs-onpremise', '089'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/hardware-guide/edge-kits',
                component: ComponentCreator('/Humanoid-robotics-book/docs/hardware-guide/edge-kits', '5c3'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/hardware-guide/robot-options',
                component: ComponentCreator('/Humanoid-robotics-book/docs/hardware-guide/robot-options', 'e35'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/hardware-guide/workstation-specs',
                component: ComponentCreator('/Humanoid-robotics-book/docs/hardware-guide/workstation-specs', 'ebd'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/intro',
                component: ComponentCreator('/Humanoid-robotics-book/docs/intro', 'aa7'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/module-1-ros2/assignments',
                component: ComponentCreator('/Humanoid-robotics-book/docs/module-1-ros2/assignments', 'e4b'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/module-1-ros2/capstone-nervous-system',
                component: ComponentCreator('/Humanoid-robotics-book/docs/module-1-ros2/capstone-nervous-system', '1bf'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/module-1-ros2/overview',
                component: ComponentCreator('/Humanoid-robotics-book/docs/module-1-ros2/overview', '45f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/module-1-ros2/week-3-foundations',
                component: ComponentCreator('/Humanoid-robotics-book/docs/module-1-ros2/week-3-foundations', 'b01'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/module-1-ros2/week-4-sensors-tf',
                component: ComponentCreator('/Humanoid-robotics-book/docs/module-1-ros2/week-4-sensors-tf', '342'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/module-1-ros2/week-5-control-ai',
                component: ComponentCreator('/Humanoid-robotics-book/docs/module-1-ros2/week-5-control-ai', '97e'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/module-2-simulation/assignments',
                component: ComponentCreator('/Humanoid-robotics-book/docs/module-2-simulation/assignments', '8d9'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/module-2-simulation/gazebo-setup',
                component: ComponentCreator('/Humanoid-robotics-book/docs/module-2-simulation/gazebo-setup', 'cb5'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/module-2-simulation/overview',
                component: ComponentCreator('/Humanoid-robotics-book/docs/module-2-simulation/overview', 'bc3'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/module-2-simulation/sensor-simulation',
                component: ComponentCreator('/Humanoid-robotics-book/docs/module-2-simulation/sensor-simulation', 'fce'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/module-2-simulation/unity-integration',
                component: ComponentCreator('/Humanoid-robotics-book/docs/module-2-simulation/unity-integration', '135'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/module-3-isaac/assignments',
                component: ComponentCreator('/Humanoid-robotics-book/docs/module-3-isaac/assignments', '438'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/module-3-isaac/capstone-perception-pipeline',
                component: ComponentCreator('/Humanoid-robotics-book/docs/module-3-isaac/capstone-perception-pipeline', 'fbd'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/module-3-isaac/overview',
                component: ComponentCreator('/Humanoid-robotics-book/docs/module-3-isaac/overview', '1c5'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/module-3-isaac/week-10-navigation',
                component: ComponentCreator('/Humanoid-robotics-book/docs/module-3-isaac/week-10-navigation', '5b1'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/module-3-isaac/week-8-isaac-sim',
                component: ComponentCreator('/Humanoid-robotics-book/docs/module-3-isaac/week-8-isaac-sim', '18f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/module-3-isaac/week-9-perception',
                component: ComponentCreator('/Humanoid-robotics-book/docs/module-3-isaac/week-9-perception', '78b'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/module-4-vla/assignments',
                component: ComponentCreator('/Humanoid-robotics-book/docs/module-4-vla/assignments', 'e31'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/module-4-vla/introduction',
                component: ComponentCreator('/Humanoid-robotics-book/docs/module-4-vla/introduction', '654'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/module-4-vla/week11-manipulation',
                component: ComponentCreator('/Humanoid-robotics-book/docs/module-4-vla/week11-manipulation', 'ab8'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/module-4-vla/week12-cognitive-brain',
                component: ComponentCreator('/Humanoid-robotics-book/docs/module-4-vla/week12-cognitive-brain', 'cbc'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Humanoid-robotics-book/docs/module-4-vla/week13-capstone',
                component: ComponentCreator('/Humanoid-robotics-book/docs/module-4-vla/week13-capstone', '79e'),
                exact: true,
                sidebar: "tutorialSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
