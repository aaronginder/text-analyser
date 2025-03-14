# Text Analyser

## Description

This project aims to predict the sentiment of text and perform topic categorization. It analyzes customer reviews to extract valuable insights about sentiment patterns and key discussion topics. The analysis is based on Trustpilot reviews data with over 123,000 customer reviews across 22 business categories.

## Features

- Sentiment analysis using VADER
- Topic modeling with Latent Dirichlet Allocation (LDA)
- Text preprocessing including tokenization and stopword removal
- Visualization of topic-sentiment relationships

## Key Findings

The analysis identified seven distinct topics in customer reviews:

- **Product Quality** - Discussion about quality, durability, and condition of products
- **Billing** - Comments related to payments, charges, refunds, and pricing
- **General Feedback** - Overall satisfaction and recommendations
- **User Experience** - Comments about ease of use, interface, and customer journey
- **Delivery** - Feedback on shipping, packaging, and timing
- **Customer Service** - Mentions of support quality and issue resolution
- **Price** - Specific discussion of cost and value
Sentiment analysis revealed that "Billing" topics have the highest average sentiment score, while "Product Quality" has the lowest, suggesting customers are most satisfied with payment processes but most critical about product quality issues.

### Topic-Sentiment Distribution

![Topic-Sentiment Distribution Boxplot](assets/output-boxplot.png)
*Figure 1: Boxplot showing sentiment distribution across different topics*

### Overall Sentiment Distribution

![Overall Sentiment Distribution Histogram](assets/output-histogram.png)
*Figure 2: Histogram of sentiment scores across all customer reviews*

## Installation

Clone the repository:

```bash
git clone https://github.com/aaronginder/text-analyser.git
```

Install dependencies using Poetry:

```bash
poetry install
```

## Usage

The project includes a Jupyter notebook in the exploration directory that demonstrates the full analysis pipeline.

## Data

The project uses Trustpilot reviews data for training and evaluation, located in the data directory.

## Development

### Setting up the development environment

Install Poetry:

```bash
pip install poetry
```

Install dependencies:

```bash
poetry install
```

### Building

To build the project:

```bash
poetry build
```

### Committing changes

This project uses semantic-release to automate the release process. Follow the conventional commits specification for commit messages.

Example:

- `feat: add new sentiment analysis model`
- `fix: correct topic classification bug`
- `docs: update installation instructions`

### Releasing

Releases are automated using semantic-release based on commit messages. Merging to the main branch will trigger a release. The project supports different release branches:

- `main`: production releases
- `develop`: development releases
- `alpha`, `beta`, `rc`: prerelease versions

## Configuration

Configuration is managed via config.yml.

### License

This project is licensed under the MIT License - see the LICENSE file for details.