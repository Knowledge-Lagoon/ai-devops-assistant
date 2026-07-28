# Jenkins Pipeline Basics

## Purpose
This document provides a basic structure for Jenkins Pipeline questions.

## Example declarative pipeline

```groovy
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building application'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying application'
            }
        }
    }
}
```

## Common pipeline stages

- Checkout source code
- Restore dependencies
- Build
- Test
- Package artifact
- Security scan
- Publish artifact
- Deploy
- Post-deployment validation

## RAG metadata

- technology: jenkins
- topic: pipeline
- doc_type: example
- source_type: curated-starter
