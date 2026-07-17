# Combatting Gender-Biased Performance Reviews with a Socratic AI Tool

This research focuses on gender-biased performance reviews in the workplace and how they can be combatted by integrating a conversational, automated web AI tool with a Socratic element. This approach prevents skill decay while addressing the "Black Box" dilemma and ensuring career advancement for women.

## System Architecture and Tech Stack

- **NLTK (Natural Language Toolkit)** — Uses a custom dictionary to search performance review language against word lists tagged as communal and aggressive/negative.
- **SpaCy (Machine Learning)** — Used to understand the context of sentences, extract objective business metrics like dates and project names, and remove Personally Identifiable Information (PII) before performing any analysis.
- **Streamlit** — Enables interactive, zero-trust web interfaces that break workflow by turning users into participants in a Socratic dialogue instead of just autocompleting their input.
- **Security Design** — Uses zero-trust architecture and client-side text anonymization to protect sensitive information in enterprise HR content, such as employees' personally identifiable information.

## Scenario A: The Subjective Trap

This scenario demonstrates how the system rejects a performance review submission when it is built on feedback deeply encoded in the employee's personality (e.g., *"Sarah is too aggressive"*). The system then prompts the manager to identify the observable behaviors that led to their use of specific gender-coded language.

A high **Language Objectivity Score** can then be achieved by providing an explanation grounded in concrete business metrics (e.g., *"She missed 3 deadlines on Project 4"*), leading to an objective resolution.

Initially, the system was designed as a dictatorial spellchecker. Its latest version incorporates an acknowledgment criterion that allows managers to accept moral responsibility for its use, transforming it into a pedagogical system with a Socratic element.

### Key Design Decisions

- Instead of delivering a strict "System Warnings" score for building trust, a **Language Objectivity Score** was implemented to rate objectivity. This shift helps users feel guided rather than judged, improving adoption.
- The pedagogical analyzer prevents skill decay by not letting users fall into "autopilot" mode, unlike standard AI checkers. It continually prompts users to revisit their performance review and articulate adequate reasons for their word choices.

## Future Work

Longitudinal A/B testing could be conducted to compare this tool against a standard HR system across multiple rounds of reviews to evaluate its training effectiveness.

## Live app password: admin123 https://capstone-bias-analyzer-globalhonors2026.streamlit.app/

## References

- Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction, 5*(CSCW1), 1–21.
- Chacon, A. (2025). The end of algorithm aversion. *AI & SOCIETY, 40*(4), 2331–2332.
- Gaucher, D., Friesen, J., & Kay, A. C. (2011). Evidence that gendered wording in job advertisements exists and sustains gender inequality. *Journal of Personality and Social Psychology, 101*(1), 109.
- Snyder, K. (2014). The abrasiveness trap: High-achieving men and women are described differently in reviews. *Fortune Magazine, 26*, 08–14.
- Macnamara, B. N., Berber, I., Çavuşoğlu, M. C., et al. (2024). Does using artificial intelligence assistance accelerate skill decay and hinder skill development without performers' awareness? *Cognitive Research, 9*, 46. https://doi.org/10.1186/s41235-024-00572-8
- Miller, T. (2023, June). Explainable AI is dead, long live explainable AI! Hypothesis-driven decision support using evaluative AI. In *Proceedings of the 2023 ACM Conference on Fairness, Accountability, and Transparency* (pp. 333–342).
- Kossow, N., Windwehr, S., & Jenkins, M. (2022). *Algorithmic transparency and accountability*. Transparency International.
- Workday Marketplace. (2026). Sentiment analysis with the AI Gateway | Workday Marketplace. Workday.com. https://marketplace.workday.com/en-US/apps/438040/sentiment-analysis-with-the-ai-gateway/overview
- Zonno, R. (2026). Gender inequalities in performance evaluation: A systematic literature review. *Equality, Diversity and Inclusion: An International Journal, 45*(9), 68–85.
