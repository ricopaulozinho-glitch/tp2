// @ts-check
import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'BiblioConsole',
  tagline: 'Gestão de biblioteca simples, rápida e na consola',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  // TODO: alterar para o URL real (ex.: https://<utilizador>.github.io)
  url: 'https://exemplo.github.io',
  baseUrl: '/biblioconsole/',

  // TODO: alterar para o utilizador/organização e repositório reais
  organizationName: 'grupo-ade',
  projectName: 'biblioconsole',

  onBrokenLinks: 'throw',

  i18n: {
    defaultLocale: 'pt',
    locales: ['pt'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          editUrl: 'https://github.com/grupo-ade/biblioconsole/tree/main/TP3_site/',
        },
        blog: {
          showReadingTime: true,
          editUrl: 'https://github.com/grupo-ade/biblioconsole/tree/main/TP3_site/',
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        respectPrefersColorScheme: true,
      },
      navbar: {
        title: 'BiblioConsole',
        logo: {
          alt: 'Logótipo BiblioConsole',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Documentação',
          },
          {to: '/blog', label: 'Blog', position: 'left'},
          {to: '/equipa', label: 'Equipa', position: 'left'},
          {
            href: 'https://github.com/grupo-ade/biblioconsole',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Documentação',
            items: [
              {label: 'Introdução', to: '/docs/intro'},
              {label: 'Guia de utilização', to: '/docs/utilizacao/emprestimos'},
              {label: 'Arquitetura', to: '/docs/desenvolvimento/arquitetura'},
            ],
          },
          {
            title: 'Projeto',
            items: [
              {label: 'Blog', to: '/blog'},
              {label: 'GitHub', href: 'https://github.com/grupo-ade/biblioconsole'},
            ],
          },
        ],
        copyright: `UC Ambientes de Desenvolvimento Colaborativo · ISE – Universidade do Algarve · ${new Date().getFullYear()}`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
        additionalLanguages: ['bash', 'python', 'json'],
      },
    }),
};

export default config;
