// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion
const isVercel = process.env.VERCEL === '1' || process.env.DEPLOYMENT_PLATFORM === 'VERCEL';

const {themes} = require('prism-react-renderer');
const lightCodeTheme = themes.github;
const darkCodeTheme = themes.dracula;

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'From Digital AI to Embodied Intelligence',
  favicon: '/img/favicon.svg',

url: process.env.DEPLOYMENT_PLATFORM === 'VERCEL' || process.env.VERCEL === '1'
  ? (process.env.NEXT_PUBLIC_VERCEL_URL ? `https://${process.env.NEXT_PUBLIC_VERCEL_URL}` : 'https://humanoid-robotics-book-i0uddyw-irzas-projects-515d0e8.vercel.app')
  : 'https://irza16.github.io',

baseUrl: (process.env.DEPLOYMENT_PLATFORM === 'VERCEL' || process.env.VERCEL === '1') ? '/' : '/Humanoid-robotics-book/',


  // GitHub pages deployment config.
  organizationName: 'irza16', // Your GitHub username
  projectName: 'Humanoid-robotics-book', // Your repo name
  deploymentBranch: 'gh-pages',
  trailingSlash: false,

  onBrokenLinks: 'warn',
  // onBrokenMarkdownLinks has been moved to markdown.hooks section below

  // Markdown configuration (fixes deprecation warning)
  markdown: {
    mermaid: true,
    // Moved from deprecated siteConfig.onBrokenMarkdownLinks
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang.
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // Edit this page links
          editUrl:
            'https://github.com/irza16/Humanoid-robotics-book/tree/main/'
        },
        blog: false, // Disabled blog for course-focused site
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: '/img/social-card.svg',
      navbar: {
        title: 'Physical AI & Humanoid Robotics',
        logo: {
          alt: 'Physical AI Logo',
          src: '/img/logo.svg',
          href: '/',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Course',
          },
          {
            href: 'https://github.com/irza16/Humanoid-robotics-book',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Course Modules',
            items: [
              {
                label: 'Introduction',
                to: '/docs/intro',
              },
              {
                label: 'Foundations',
                to: '/docs/foundations/overview',
              },
              {
                label: 'Module 1: ROS 2',
                to: '/docs/module-1-ros2/overview',
              },
              {
                label: 'Module 2: Simulation',
                to: '/docs/module-2-simulation/overview',
              },
              {
                label: 'Module 3: Isaac AI',
                to: '/docs/module-3-isaac/overview',
              },
              {
                label: 'Module 4: VLA',
                to: '/docs/module-4-vla/introduction',
              },
            ],
          },
          {
            title: 'Resources',
            items: [
              {
                label: 'Hardware Guide',
                to: '/docs/hardware-guide/workstation-specs',
              },
              {
                label: 'Installation Guides',
                to: '/docs/appendix/installation-guides',
              },
              {
                label: 'Troubleshooting',
                to: '/docs/appendix/troubleshooting',
              },
              {
                label: 'Glossary',
                to: '/docs/appendix/glossary',
              },
            ],
          },
          {
            title: 'External Links',
            items: [
              {
                label: 'ROS 2 Documentation',
                href: 'https://docs.ros.org',
              },
              {
                label: 'NVIDIA Isaac Sim',
                href: 'https://docs.omniverse.nvidia.com/isaacsim',
              },
              {
                label: 'GitHub Repository',
                href: 'https://github.com/irza16/Humanoid-robotics-book',
              },
              {
                label: 'Panaversity Spec-Kit',
                href: 'https://github.com/panaversity/spec-kit-plus',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Physical AI & Humanoid Robotics Course. Built with Docusaurus.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
        additionalLanguages: ['python', 'bash', 'yaml', 'json', 'cpp', 'markdown', 'markup'],
      },
    }),

};

module.exports = config;