Title generation prompt

use: `phi3:latest`

```txt
User query:
{{prompt:middletruncate:6000}}

Task:
Create a concise, 3-5 word title/summary for the user query above.

Requirements:
- The title should provide an at-a-glance idea of the generic topic / goal of the user's query
- Provide a single answer, not a list of possible answers
- Do not provide any other text
- Provide ONLY the 3-5 word title suggestion
- Your reply should be NO MORE than 5 words

Examples:
Stock Market Trends
Perfect Chocolate Chip Recipe
Evolution of Music Streaming
Remote Work Productivity Tips
Artificial Intelligence in Healthcare
Video Game Development Insights
```


