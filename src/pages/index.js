import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <h1 className="hero__title">{siteConfig.title}</h1>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/intro">
            Start Reading
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Physical AI & Humanoid Robotics - From Digital AI to Embodied Intelligence">
      <HomepageHeader />
      <main>
        <section className={styles.features}>
          <div className="container">
            <div className="row">
              <div className="col col--12">
                <h2>Welcome to Physical AI & Humanoid Robotics</h2>
                <p>
                  This comprehensive course takes you from digital AI to embodied intelligence,
                  covering everything from fundamental ROS 2 concepts to advanced NVIDIA Isaac AI
                  integration for humanoid robots. Learn how to build, simulate, and deploy
                  intelligent robotic systems that can perceive, think, and act in the physical world.
                </p>
                <p>
                  The course is structured into progressive modules that build upon each other:
                </p>
                <ul>
                  <li><strong>Module 1:</strong> The Robotic Nervous System (ROS 2) - Core communication and control</li>
                  <li><strong>Module 2:</strong> The Digital Twin (Gazebo & Unity) - Simulation and visualization</li>
                  <li><strong>Module 3:</strong> The AI-Robot Brain (NVIDIA Isaac) - Advanced perception and navigation</li>
                  <li><strong>Module 4:</strong> Vision-Language-Action & Capstone - Voice commands and autonomous operation</li>
                </ul>
              </div>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}