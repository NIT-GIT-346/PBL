export const DRL_TRAINING_DATA = Array.from({ length: 101 }, (_, i) => {
  const episode = i * 10
  const reward = -200 + 700 * (1 - Math.exp(-episode / 250)) + (Math.random() - 0.5) * 40
  const accuracy = Math.min(0.5 + 0.45 * (1 - Math.exp(-episode / 300)) + (Math.random() - 0.5) * 0.04, 0.98)
  const loss = Math.max(2.5 * Math.exp(-episode / 200) + 0.1 + (Math.random() - 0.5) * 0.1, 0.05)
  return {
    episode,
    reward: Math.round(reward * 100) / 100,
    accuracy: Math.round(accuracy * 10000) / 10000,
    loss: Math.round(loss * 10000) / 10000,
  }
})

export const MODEL_COMPARISON = [
  { model: 'Deep RL (DQN)', accuracy: 94.23, precision: 93.87, recall: 93.12, f1: 93.49, auc: 96.78 },
  { model: 'Random Forest', accuracy: 88.34, precision: 87.56, recall: 86.89, f1: 87.22, auc: 92.01 },
  { model: 'SVM', accuracy: 85.67, precision: 84.98, recall: 84.23, f1: 84.60, auc: 89.34 },
  { model: 'Logistic Reg.', accuracy: 81.23, precision: 80.67, recall: 79.89, f1: 80.28, auc: 86.12 },
  { model: 'CNN', accuracy: 91.56, precision: 90.98, recall: 90.45, f1: 90.71, auc: 95.02 },
]

export const CONFUSION_MATRIX = {
  labels: ['Cardiac', 'Respiratory', 'Metabolic', 'Neurological', 'General'],
  matrix: [
    [187, 5, 3, 2, 3],
    [4, 176, 6, 3, 11],
    [2, 4, 183, 1, 10],
    [3, 2, 1, 179, 15],
    [4, 13, 7, 15, 161],
  ],
}

export const TEAM_MEMBERS = [
  { name: 'Dr. Sarah Chen', role: 'Principal Investigator', expertise: 'Deep Reinforcement Learning', avatar: 'SC' },
  { name: 'Dr. Michael Torres', role: 'Co-Investigator', expertise: 'Big Data Analytics', avatar: 'MT' },
  { name: 'Dr. Priya Sharma', role: 'Clinical Advisor', expertise: 'Internal Medicine', avatar: 'PS' },
  { name: 'Alex Kim', role: 'ML Engineer', expertise: 'Neural Networks & DQN', avatar: 'AK' },
  { name: 'Dr. James Wright', role: 'Data Scientist', expertise: 'Healthcare Analytics', avatar: 'JW' },
  { name: 'Lisa Zhang', role: 'Full-Stack Developer', expertise: 'React & FastAPI', avatar: 'LZ' },
]

export const PROJECT_TIMELINE = [
  { phase: 'Phase 1', title: 'Literature Review & Data Collection', period: 'Jan - Mar 2024', status: 'completed' },
  { phase: 'Phase 2', title: 'Big Data Pipeline Development', period: 'Apr - Jun 2024', status: 'completed' },
  { phase: 'Phase 3', title: 'DRL Model Training & Optimization', period: 'Jul - Sep 2024', status: 'completed' },
  { phase: 'Phase 4', title: 'CDSS Integration & Testing', period: 'Oct - Nov 2024', status: 'completed' },
  { phase: 'Phase 5', title: 'Deployment & Evaluation', period: 'Dec 2024', status: 'active' },
]

export const REFERENCES = [
  'Sutton, R. S., & Barto, A. G. (2018). Reinforcement Learning: An Introduction. MIT Press.',
  'Mnih, V., et al. (2015). Human-level control through deep reinforcement learning. Nature, 518(7540), 529-533.',
  'Rajkomar, A., et al. (2018). Scalable and accurate deep learning with electronic health records. NPJ Digital Medicine, 1(1), 18.',
  'Dean, J., & Ghemawat, S. (2008). MapReduce: Simplified data processing on large clusters. Communications of the ACM, 51(1), 107-113.',
  'Zaharia, M., et al. (2016). Apache Spark: A unified engine for big data processing. Communications of the ACM, 59(11), 56-65.',
]

export const ARCHITECTURE_NODES = [
  {
    id: 'data-sources',
    title: 'Data Sources',
    description: 'EHR Systems, Lab Results, Patient Vitals, Medical Imaging, Genomic Data',
    details: 'Collects real-time patient data from multiple healthcare information systems including HL7 FHIR-compliant EHR systems, laboratory information systems, bedside monitoring devices, PACS imaging systems, and genomic sequencing platforms.',
    color: 'cyan',
  },
  {
    id: 'big-data',
    title: 'Big Data Layer',
    description: 'Hadoop, Spark, Kafka, HDFS, Hive - Distributed Processing',
    details: 'Processes massive volumes of healthcare data using Apache Hadoop for batch processing, Apache Spark for real-time analytics, Apache Kafka for data streaming, HDFS for distributed storage, and Apache Hive for SQL-based querying.',
    color: 'purple',
  },
  {
    id: 'drl-engine',
    title: 'DRL Engine',
    description: 'DQN, A3C, Policy Gradient - Model Training & Inference',
    details: 'Implements Deep Reinforcement Learning algorithms including Deep Q-Networks (DQN) for discrete action spaces, Asynchronous Advantage Actor-Critic (A3C) for parallel training, and Policy Gradient methods for continuous optimization of treatment decisions.',
    color: 'cyan',
  },
  {
    id: 'cdss',
    title: 'CDSS Module',
    description: 'Clinical Decision Support - Diagnosis, Treatment, Risk Assessment',
    details: 'Integrates DRL predictions with clinical guidelines to provide evidence-based decision support including differential diagnosis ranking, personalized treatment recommendations, risk stratification, and lab test prioritization.',
    color: 'purple',
  },
  {
    id: 'output',
    title: 'Clinical Output',
    description: 'Reports, Alerts, Dashboards, Treatment Plans',
    details: 'Generates actionable clinical outputs including structured diagnostic reports, real-time clinical alerts, interactive dashboards for healthcare providers, and personalized treatment plans with confidence scores.',
    color: 'cyan',
  },
]

export const BIG_DATA_TECHNOLOGIES = [
  {
    name: 'Apache Hadoop',
    icon: '🐘',
    description: 'Distributed computing framework for processing large datasets across clusters of computers.',
    features: ['MapReduce Processing', 'YARN Resource Management', 'Fault Tolerance', 'Linear Scalability'],
    metrics: { throughput: '3,400 tasks/min', storage: '2.4 PB', nodes: 48 },
  },
  {
    name: 'Apache Spark',
    icon: '⚡',
    description: 'Unified analytics engine for large-scale data processing with in-memory computing.',
    features: ['In-Memory Computing', 'Spark SQL', 'MLlib Integration', 'Streaming Analytics'],
    metrics: { throughput: '8,200 records/sec', latency: '45ms', speedup: '100x vs MapReduce' },
  },
  {
    name: 'Apache Kafka',
    icon: '📊',
    description: 'Distributed event streaming platform for high-throughput real-time data pipelines.',
    features: ['Event Streaming', 'Pub/Sub Messaging', 'Exactly-Once Semantics', 'Data Replication'],
    metrics: { throughput: '12,450 msg/sec', partitions: 256, retention: '7 days' },
  },
  {
    name: 'HDFS',
    icon: '💾',
    description: 'Hadoop Distributed File System for reliable, scalable storage of massive datasets.',
    features: ['Block Replication', 'Rack Awareness', 'High Availability', 'Data Locality'],
    metrics: { capacity: '2.4 PB', replication: '3x', blockSize: '128 MB' },
  },
  {
    name: 'Apache Hive',
    icon: '🐝',
    description: 'Data warehouse software for reading, writing, and managing large datasets via SQL.',
    features: ['HiveQL Queries', 'Schema on Read', 'Partitioning', 'ACID Transactions'],
    metrics: { queries: '500/min', tables: 1200, avgQueryTime: '230ms' },
  },
]

export const DRL_CONCEPTS = {
  components: [
    { name: 'Agent', description: 'The DRL model that learns optimal treatment decisions through interaction with the clinical environment.', icon: '🤖' },
    { name: 'Environment', description: 'The clinical simulation representing patient states, disease progression, and treatment outcomes.', icon: '🏥' },
    { name: 'State', description: 'Patient features including vitals, lab results, symptoms, and medical history at any given time.', icon: '📋' },
    { name: 'Action', description: 'Clinical decisions including diagnosis selection, treatment choice, and test ordering.', icon: '⚡' },
    { name: 'Reward', description: 'Feedback signal based on treatment efficacy, patient outcomes, and clinical guideline adherence.', icon: '🎯' },
  ],
  algorithms: [
    {
      name: 'Deep Q-Network (DQN)',
      description: 'Combines Q-learning with deep neural networks to handle high-dimensional state spaces in clinical decision-making.',
      features: ['Experience Replay', 'Target Network', 'Epsilon-Greedy Exploration'],
      accuracy: 94.23,
    },
    {
      name: 'A3C (Asynchronous Advantage Actor-Critic)',
      description: 'Uses parallel actor-learners for stable training on diverse patient populations simultaneously.',
      features: ['Parallel Training', 'Actor-Critic Architecture', 'Advantage Function'],
      accuracy: 92.87,
    },
    {
      name: 'Policy Gradient',
      description: 'Directly optimizes the treatment policy for continuous action spaces in medication dosing.',
      features: ['Direct Policy Optimization', 'REINFORCE Algorithm', 'Baseline Subtraction'],
      accuracy: 91.45,
    },
  ],
  pseudocode: `# DQN Clinical Decision Algorithm
initialize replay_buffer D, capacity N
initialize Q-network with random weights θ
initialize target network with weights θ⁻ = θ

for episode in range(num_episodes):
    state = get_patient_state(vitals, labs, history)

    for step in range(max_steps):
        # Epsilon-greedy action selection
        if random() < epsilon:
            action = random_clinical_action()
        else:
            action = argmax(Q(state, a; θ))

        # Execute clinical action
        next_state, reward = clinical_env.step(action)
        reward = compute_clinical_reward(outcome, guidelines)

        # Store transition
        D.store(state, action, reward, next_state)

        # Sample mini-batch and update
        batch = D.sample(batch_size=32)
        loss = MSE(Q(s,a;θ), r + γ·max Q(s',a';θ⁻))
        θ = θ - α·∇loss

        # Update target network
        if step % target_update == 0:
            θ⁻ = θ

        state = next_state`,
}

export const STATS = [
  { label: 'Patients Analyzed', value: 12847, suffix: '+' },
  { label: 'Model Accuracy', value: 94, suffix: '%' },
  { label: 'Conditions Detected', value: 156, suffix: '' },
  { label: 'Avg Response Time', value: 2, suffix: 's' },
]

export const HOW_IT_WORKS = [
  { step: 1, title: 'Data Ingestion', description: 'Patient data is collected from EHR systems, lab results, and monitoring devices in real-time via Apache Kafka.' },
  { step: 2, title: 'Big Data Processing', description: 'Apache Spark and Hadoop process and transform massive datasets for feature extraction and analytics.' },
  { step: 3, title: 'DRL Analysis', description: 'Deep Reinforcement Learning models analyze patient features to predict conditions and optimal treatments.' },
  { step: 4, title: 'Clinical Decision', description: 'The CDSS generates actionable insights including diagnosis, risk assessment, and treatment recommendations.' },
]
