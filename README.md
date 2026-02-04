---
## Twitter Sentiment Monitor for ML Discussions

### Problem

Tracking public sentiment around Machine Learning topics on Twitter is noisy, rate limited, and difficult to process in near real time without blocking or data loss. This project explores a lightweight, async first backend pipeline for collecting and analyzing short form social data under those constraints.

### What this system does

This service fetches recent tweets related to Machine Learning keywords, cleans and normalizes the text, and performs sentiment classification to surface aggregate sentiment trends and representative samples.

The system is designed to prioritize throughput and responsiveness over model complexity, making it suitable for rapid sentiment monitoring rather than offline analytics.

### Architecture overview

* Asynchronous tweet fetching to avoid blocking on network IO
* Text normalization and cleaning using deterministic rules
* Sentiment classification using a lightweight NLP model
* Aggregation layer to compute sentiment distribution and sample outputs

The design intentionally avoids heavy ML pipelines in favor of predictable execution and fast iteration.

### Key design decisions

* Asyncio is used to handle IO bound workloads without introducing external message queues
* TextBlob is chosen for sentiment scoring due to its simplicity and low operational overhead
* Processing is done in memory to reduce latency and complexity
* Output is optimized for human inspection rather than long term storage

This tradeoff makes the system easy to extend while keeping runtime behavior transparent.

### Technologies

* Python
* Asyncio
* Twikit
* TextBlob
* Regular Expressions

### Running the project

1. Clone the repository
2. Install dependencies from `requirements.txt`
3. Add Twitter credentials to `t_code.py`
4. Run the script and provide a search keyword when prompted

### Example output

Search keyword: Machine Learning
Positive: 55 percent
Negative: 10 percent
Neutral: 35 percent

### Scope and limitations

* This is not a production grade sentiment model
* Sarcasm and domain specific language are not fully handled
* Twitter API rate limits apply
* Results are intended for trend inspection, not decision automation

---
