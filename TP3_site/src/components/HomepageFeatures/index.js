import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Catálogo completo',
    emoji: '📖',
    description: (
      <>
        Adicione, edite, pesquise e remova livros com ISBN único e controlo de
        exemplares disponíveis.
      </>
    ),
  },
  {
    title: 'Empréstimos sem esforço',
    emoji: '🔁',
    description: (
      <>
        Prazo de 14 dias, limite por utente e <strong>multa automática</strong> por
        atraso na devolução.
      </>
    ),
  },
  {
    title: 'Simples e testado',
    emoji: '✅',
    description: (
      <>
        Apenas Python, sem dependências, com <code>pytest</code> a cobrir as regras
        de negócio.
      </>
    ),
  },
];

function Feature({emoji, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center" style={{fontSize: '4rem'}} aria-hidden="true">
        {emoji}
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
