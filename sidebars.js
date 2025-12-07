/**
 * Creating a sidebar enables you to:f
 - Create an ordered group of docs
 - Render a sidebar in the docs "browse" section
 - Facilitate custom sidebar

By default, Docusaurus generates a sidebar from the docs folder structure.
It can be changed by creating a sidebars.js file and specifying it in the siteConfig.

Learn more at: https://docusaurus.io/docs/sidebar#sidebar-categorization
*/

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  // By default, Docusaurus generates a sidebar from the docs folder structure
  tutorialSidebar: [
    'intro',
    {
      type: 'category',
      label: 'Foundations',
      items: [
        'foundations/overview',
        'foundations/what-is-humanoid-robotics',
        'foundations/core-subsystems',
        'foundations/modern-examples',
        'foundations/future-trajectory',
      ],
    },
    {
      type: 'category',
      label: 'Module 1: ROS 2 Nervous System',
      items: [
        'module-1-ros2/overview',
        'module-1-ros2/week-3-foundations',
        'module-1-ros2/week-4-sensors-tf',
        'module-1-ros2/week-5-control-ai',
        'module-1-ros2/assignments',
        'module-1-ros2/capstone-nervous-system',
      ],
    },
    {
      type: 'category',
      label: 'Module 2: Digital Twin (Simulation)',
      items: [
        'module-2-simulation/overview',
        'module-2-simulation/week-6-gazebo-setup',
        'module-2-simulation/week-7-unity-integration',
        'module-2-simulation/sensor-simulation',
        'module-2-simulation/assignments',
      ],
    },
    {
      type: 'category',
      label: 'Module 3: Isaac AI Brain',
      items: [
        'module-3-isaac/overview',
        'module-3-isaac/week-8-isaac-sim',
        'module-3-isaac/week-9-perception',
        'module-3-isaac/week-10-navigation',
        'module-3-isaac/assignments',
        'module-3-isaac/capstone-perception-pipeline',
      ],
    },
    {
      type: 'category',
      label: 'Module 4: Vision-Language-Action',
      items: [
        'module-4-vla/introduction',
        'module-4-vla/week11-manipulation',
        'module-4-vla/week12-cognitive-brain',
        'module-4-vla/week13-capstone',
        'module-4-vla/assignments',
      ],
    },
    {
      type: 'category',
      label: 'Hardware Guide',
      items: [
        'hardware-guide/workstation-specs',
        'hardware-guide/edge-kits',
        'hardware-guide/robot-options',
        'hardware-guide/cloud-vs-onpremise',
      ],
    },
    {
      type: 'category',
      label: 'Appendix',
      items: [
        'appendix/installation-guides',
        'appendix/troubleshooting',
        'appendix/glossary',
        'appendix/resources',
      ],
    },
  ],

  // But you can create a sidebar manually
  /*
  tutorialSidebar: [
    'intro',
    'hello',
    {
      type: 'category',
      label: 'Tutorial',
      items: ['tutorial-basics/create-a-document'],
    },
  ],
   */
};

module.exports = sidebars;