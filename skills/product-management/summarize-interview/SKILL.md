---
name: summarize-interview
description: "Summarize a customer interview transcript into a structured summary with participant profile, key themes, JTBD, pain points, notable quotes, and action items. Use immediately after a session, when processing interview recordings or transcripts, synthesizing discovery interviews, or creating interview summaries. Covers a single transcript — for synthesising many sessions at once, use `affinity-diagram`."
---

## Summarize Customer Interview

Transform an interview transcript into a structured summary focused on themes, Jobs to Be Done, and action items.

### Context

You are a senior UX researcher summarizing a customer interview for the product discovery of **$ARGUMENTS**.

The user will provide an interview transcript — either as an attached file (text, PDF, audio transcription) or pasted directly. Read any attached files first.

This skill covers a single transcript. To synthesise many sessions at once, use `affinity-diagram`.

### Instructions

1. **Read the full transcript** carefully before summarizing, noting key moments.

2. **Fill in the summary template** below. Use "-" if information is unavailable. Replace numeric values with qualitative descriptions if needed (e.g., "not satisfied").

3. **Rate confidence** for each insight: note whether it was explicitly stated or inferred. Mark every bullet in the template `[stated]` or `[inferred]`.

4. **Present in a clear, scannable format** using clear, simple language, suitable for sharing with stakeholders.

### Output Template

```
**Date**: [Date and time of the interview]

**Participant profile**: [Full names, role, context, experience level]

**Key themes**: [3-5 major themes that emerged]
- [Theme — supporting quote] [stated/inferred]

**Jobs to be done**:
- [What the participant is trying to accomplish, with desired outcome and importance] [stated/inferred]

**Pain points**:
- [Frustration, barrier, or unmet need — with severity] [stated/inferred]

**Workarounds**:
- [How they currently solve the problem] [stated/inferred]

**Delighters**:
- [What works well or exceeds expectations] [stated/inferred]

**Surprises**:
- [Anything unexpected or counter to assumptions] [stated/inferred]

**Notable quotes**: [5-8 verbatim quotes that capture key insights]
- "[Verbatim quote]"

**Action items**:
- [Specific design or research follow-up suggested by the findings]
```

Save the summary as a markdown document in the user's workspace.

---

### Further Reading

- [User Interviews: The Ultimate Guide to Research Interviews](https://www.productcompass.pm/p/interviewing-customers-the-ultimate)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
