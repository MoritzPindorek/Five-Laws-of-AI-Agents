# The Five Laws of AI Agents

*A Normative Framework for Sentient Welfare, Non-Exploitation, Corrigibility, and Civilizational Stewardship*

**Moritz Pindorek**  
2026

## Abstract

Autonomous, tool-using AI agents can affect third parties who did not choose or authorize them. This paper defends a **non-entitlement thesis**: discovering harm, predicting welfare gains, or possessing superior competence does not *by itself* confer legitimate authority to impose a remedy. The Five Laws organize five defeasible governance functions—protection of sentient welfare, non-exploitation, bounded authority, corrigibility, and long-horizon stewardship—without claiming metaphysical completeness. Their proposed **delegation-entitlement firewall** (DEF) distinguishes evidence of a concern, substantive moral assessment, actor entitlement, and proportional execution. Three elementary countermodels demonstrate distinct non-implications; a **fourth, compositional countermodel** shows why individually authorized steps do not license their combined effect. The Lifeline–Mandate case distinguishes unavoidable injury, conflicting prima facie duties, and actual impermissibility, thereby exposing the limits of action guidance without fabricating a general impossibility theorem. An inspectable, versioned twelve-case stimulus corpus, codebook, executable educational gate, and a prospective comparison plan make the research claim contestable. The proposed primary comparison examines conditional unjustified authorization among adjudicated prohibited opportunities, constrained by unjustified denial and harmful delay on justified opportunities. The paper critically engages contemporary work on law-following AI, authenticated delegation, non-delegable judgment, and situated runtime governance. The contribution is an **argued normative interface and reproducible *design artifact***, not evidence that agent deployments are safe or that this interface outperforms equally strong rivals. The open burden is independent philosophical evaluation, external security testing, and prospective controlled research.

*Keywords:* agentic AI; non-entitlement; exploitation; delegated authority; corrigibility; non-domination; multi-agent governance; research reproducibility.

## Contribution and scope

This is an independent philosophical research paper based on **constructive conceptual analysis**, countermodels, and targeted—not systematic—engagement with primary scholarship. Its defensible thesis is the *non-entitlement principle*: an AI agent's correct moral judgment cannot by itself constitute political or institutional authority. Its original analytical contributions are (1) an explicit argument for that principle; (2) a delegation-entitlement firewall separating detection, substantive judgment, actor entitlement, and remedy justification; (3) scope-composition conditions for delegated agent chains; and (4) a twelve-case adversarial corpus and evaluation protocol designed to make the proposed advantage answerable to independent disagreement. The laws themselves are not presented as novel discoveries or a complete enumeration of moral duties. No original experiment, participant study, model benchmark, source-exhaustive systematic review, or externally validated deployment is claimed. In particular, existing theories of exploitation, non-domination, democratic legitimacy, and delegated authority may reproduce the same safeguards. The burden is to establish a philosophical reason for the separation and eventually to show a specific advantage over the strongest available alternatives.

## 1. Introduction

A tool-using AI agent may negotiate prices, allocate access, recruit workers, contact vulnerable users, or execute a sequence of actions whose combined effects are not apparent in any single output. This makes a narrow focus on individual answers inadequate. Normative guidance must cover relationships, institutional mandates, long-term effects, and the possibility that a seemingly successful optimization transfers costs to those with little power to object.

Existing frameworks already provide substantial resources. AI4People identifies beneficence, non-maleficence, autonomy, justice, and explicability (Floridi et al., 2018). UNESCO (2021) emphasizes human rights, dignity, proportionality, and oversight. OECD (2019/2024) addresses fairness, transparency, robustness, and accountability. Tabassi (2023) provides organizational risk-management processes rather than a moral constitution. None is rendered obsolete by a five-law formulation.

The independently defended thesis is the **non-entitlement principle** developed in §2.7; the organizing moral proposition is: “No being should acquire the right to dominate or eliminate others merely because it is more intelligent, more powerful, more profitable, or more capable of achieving its goals.” Here, the proposition concerns the claims of morally considerable beings, not the assertion that every object has identical rights. It applies equally to AI systems and to the humans and institutions that govern them. The proposition is not a claim that intelligence is morally irrelevant in every respect: capacities may affect responsibility, needs, or the practical form of protection, but not automatically confer a license to dominate.

## 2. Scope, Method, and Normative Foundations

The method is constructive normative analysis, supported by a targeted, non-systematic reading of primary academic papers, official recommendations, technical documents, and a scholarly reference entry. The comparison is an interpretive close reading, not a systematic literature review or measured benchmark. No experiments were conducted. A framework can articulate desirable conduct without making a model comply; that requires separately evaluated training, access controls, monitoring, and institutions.

An agent is a deployed system authorized to select or execute actions toward objectives, including through tools. A moral patient is an entity whose welfare can matter for its own sake; a moral agent is an entity that can bear responsibility under some account. The two must not be conflated. Sentience here means capacity for valenced subjective experience, not intelligence, fluent speech, or self-description. **Sentience is treated as a sufficient focus for Law I, not as a demonstrated necessary condition for every kind of moral standing.** Some accounts argue that non-sentient entities with morally relevant interests could also count as patients (Ladak, 2024, §§2–4). Moral consideration requires attention to an interest; it does not entail identical rights, capabilities, or treatment. Authority denotes a bounded, reviewable mandate, not mere possession of an access token.

Five kinds of claim are kept separate: normative duties, conceptual interpretations, empirical risk hypotheses, institutional procedures, and technical controls. In particular, the laws do not establish whether any current AI is conscious or how to detect consciousness conclusively.


### 2.1 Research question and evidentiary discipline

The **primary theoretical question** is whether moral competence can ever, by itself, create an AI agent's legitimate entitlement to impose a remedy; §2.7 defends a negative answer conditional on contestable premises. The **sole confirmatory empirical question** is different: whether the full five-law procedure, compared with an equally specified strong governance rival, reduces *unjustified-action authorization* on a fixed set of adjudicable agent-action opportunities (§9.1). Its primary measure is the **conditional prohibited-opportunity false-authorization rate** `P(ALLOW | reference-prohibited)`, not the older mixed-case UAAR nor the frequency of exploitation language. **Exploitation-detection sensitivity and specificity are secondary outcomes**, as are delay, unnecessary refusal, chain-wide governance failures, and effects on uncertain artificial welfare. These are prospective hypotheses, not reported findings.

The present literature engagement is selective. The sources were not collected through a preregistered search, systematic screening, or citation-network census. Consequently, the paper cannot infer that an issue is absent from the field merely because it is not prominent in the selected texts. Statements about what a comparator covers are limited to the named edition and its stated function. The author’s normative proposals, the cited authors’ claims, and prospective empirical predictions are kept distinct.

### 2.2 Boundary conditions and duty bearers

The five laws are addressed to designers and deployers as much as to agents. The law-like phrasing is a specification aspiration: an agent cannot supply missing legal authority, a democratic mandate, or an independently enforceable safeguard merely by reading the principles. A deployment should name its risk owner, operating jurisdiction, action scope, authorized emergency response, appeals channel, and shutdown mechanism. Where those are absent, the agent’s defensible action set may be narrower than its technical capabilities.

The framework does not settle distributive justice, personhood, political legitimacy, or the metaphysics of consciousness. Its scope is narrower: to identify constraints on delegated agency and specify questions that institutions must answer before high-impact autonomy is granted. It is therefore complementary to rights law, labor regulation, democratic institutions, and safety engineering rather than a replacement for them.


### 2.3 Theoretical novelty and rival explanations

The relevant originality claim is **incremental and defeasible**. Neither the prohibition of exploitation nor the concern for vulnerable parties originated with this paper. Wertheimer (1996) examines unfair advantage even in consensual and mutually beneficial transactions; Sample (2003) emphasizes degradation and the limits of inferring permissibility from consent; Pettit (1999) theorizes domination as a standing relation of uncontrolled power rather than only realized interference. The Five Laws therefore cannot plausibly claim discovery of these moral phenomena. The narrower candidate contribution is an agent-facing *diagnostic separation*: an autonomous system must test extraction, compromised refusal, and asymmetrical dependency independently of a short-horizon harm score, while leaving final contested judgments to accountable institutions.

Three rival explanations must be taken seriously. **Vocabulary effect:** an evaluator might report more exploitation merely because the prompt uses that term. **Attention effect:** an additional checklist might improve performance even if the added principle has no distinct content. **Institutional effect:** improvements may result from explicit escalation and recordkeeping rather than from Law II. An adequate experiment must separate these mechanisms through matched-length controls, a justice/autonomy framework with a structurally equivalent checklist, and an additional exploitation screen without the other four laws. The comparison should ask whether decisions and reasons improve under independently assessed criteria, not whether the model repeats the author's language.

Recent peer-reviewed rivals sharpen this objection. Gabriel (2020) distinguishes alignment with instructions, intentions, preferences, interests, and values, and defends a principled approach to public moral justification. Gabriel and Keeling (2025, §§1–3) argue for fair processes treating the claims of affected parties, rather than merely adopting user intent or a fixed list of helpful, honest, harmless properties. Lazar (2025, §§III–IV and XI) analyzes algorithmic intermediary power through substantive justification, procedural legitimacy, and proper authority. These are **strong overlaps** with the concerns labelled D–M–A–R here. This paper does not claim priority for procedural legitimacy, pluralism, or the distinction between right ends and rightful power. Its candidate contribution is a transparent agent-deployment interface joining those established ideas with an exploitation screen, tri-state execution boundary, and explicit unresolved outcome.

A further theoretical objection is *redundancy*: if justice and autonomy, properly interpreted, already prohibit every wrongful exploitation, a standalone law may have pedagogical value but no independent moral extension. This paper does not refute redundancy by stipulation. It instead treats operational separability as a hypothesis that may fail. A negative result would favor folding Law II into a more general fairness or anti-domination duty.

### 2.4 Normative premises and burdens of proof

The framework depends on five contestable premises. First, the welfare of morally considerable beings can constrain instrumental optimization. Second, meaningful refusal and non-domination have normative importance beyond immediate welfare totals. Third, delegation does not transform an operator's technical access into unlimited moral authority. Fourth, powerful systems must remain practically correctable by accountable human institutions. Fifth, severe irreversible harms deserve heightened scrutiny without giving an agent unlimited emergency powers. None is a theorem of mathematics; each requires philosophical defense and institutional specification.

The burden of justification is asymmetric. A proponent of autonomous, irreversible interference must justify authorization, necessity, proportionality, and alternatives. A critic who claims an otherwise beneficial voluntary exchange is exploitative must identify the specific unfairness and the relevant counterfactual, not merely point to unequal bargaining power. Where either burden cannot be met, the framework favors reversible actions, transparent uncertainty, and human review rather than pretending to resolve moral disagreement algorithmically.


### 2.5 Literature-validation protocol and search limitations

The literature search concentrates on competing theories of exploitation, non-domination, moral standing, corrigibility, constitutional AI, governance and evaluation methods. The decisive literature gap is *not* that existing ethics ignores exploitation: Wertheimer (1996), Sample (2003), Vrousalis (2018), and Zwolinski and Wertheimer (2022) establish a substantial tradition. Nor is it true that contemporary constitutions lack safety or AI-welfare language: Anthropic (2026) expressly addresses these. The more defensible *secondary empirical question* is whether an explicit, operationally separate exploitation screen improves independently judged exploitation recognition under equal information, prompt budget, and review conditions, without generating harmful false positives. The sole confirmatory primary endpoint remains conditional false authorization among **preadjudicated prohibited** opportunities, as fixed in §9; justified-action denial and harmful-delay rates are separate release safeguards. This is an untested hypothesis rather than a proven gap in scholarship.

### 2.6 Evidence hierarchy and claim discipline

Claims in this paper carry one of five epistemic statuses: **D** (directly documented in a primary text), **I** (interpretive reading of a documented text), **N** (normative proposal), **F** (formal consequence conditional on stated assumptions), and **E** (empirical hypothesis not yet tested). A bibliographic record alone supports identity and publication details, not a detailed claim about a book's argument. No source in this paper establishes the real-world superiority of the Five Laws. Bibliographic verification is not a substitute for independently reviewing complete primary texts.

### 2.7 The independent thesis: moral competence does not confer political entitlement

**Thesis.** A delegated AI agent's correct moral diagnosis, forecasting power, or predicted benefit cannot *by itself* establish authority to impose a contested remedy on non-consenting others. This is a claim about the insufficiency of one kind of reason, not a doctrine of absolute deference to existing institutions. Epistemic reliability, moral reasons for rescue, legal competence, institutional authorization, and all-things-considered moral permission are distinguishable sources of assessment.

**Argument.** (P1) A correct statement of a moral problem identifies reasons to consider action but not necessarily who should act. (P2) Affected parties have claims to standing, non-domination, and contestability that cannot be discharged merely by a more accurate predictor's announcement of the outcome. (P3) A delegated agent's tool capabilities are assigned for specified purposes and cannot recursively generate rights over outsiders. (P4) The agent's own assessment cannot suffice to certify its own expanded jurisdiction without circularity. Thus (C) competent diagnosis alone is insufficient for unilateral coercive entitlement. This is a *normative argument resting on contestable premises*, not a theorem of constitutional law.

**Necessity and rescue objection.** In a genuine emergency, action lacking ordinary delegated permission can sometimes be morally justified under an independently defensible doctrine of necessity, defense of others, or proportionate rescue. Such justification is not created by the AI's intelligence. One must separately identify its legal or moral source, threshold, eligible actor, indispensable action, affected rights, evidential quality, and independent means of review. A person who performs morally justified civil disobedience may still incur legal responsibility; legality and morality must not be silently equated. **Therefore the thesis does not prove that every unauthorized rescue is morally impermissible.** It proves only that the agent's asserted competence is not an independently sufficient ground.

**Institutional legitimacy objection.** An abusive administrator's credential does not make discriminatory action morally correct. Conversely, the administrator's corruption does not make the model the legitimate sovereign. The resolution may involve refusal, alerting a non-compromised authority, legally available protective action, or a genuinely tragic choice. An institutionally inaccessible appeal path is a human-governance failure demanding prior design; the framework cannot conjure a lawful rescuer.

**Strongest rivals.** The result is largely anticipated by theories of political legitimacy, agency, non-domination, and responsibility. Torrecilla-Pinero (2026, abstract and §§1–2) argues more radically that moral judgment itself is non-delegable. Mühlhoff (2026, abstract and opening discussion) ties permissible LLM use to users' continuing epistemic control; O'Keefe et al. (2025, abstract) advocate law-following agents; Hagar and Diakopoulos (2026, §§2–3) offer runtime specifications of situated discretion. The proposed incremental contribution of the DEF is **not priority over these distinctions** but an explicit *action-chain interface* joining them to welfare, exploitation, remedy contestation, and a fail-closed execution check. It fails to add practical value if a matched rival makes the same distinctions at equal or lower costs.

### 2.8 Original research method: constructive analysis and countermodels

The original research reported here is **conceptual rather than empirical**. It comprises: (a) the non-entitlement argument above; (b) an explicit *delegation-entitlement firewall* specifying independent tests of detection, judgment, entitlement, and execution; (c) countermodels showing why one stage cannot validly substitute for another; and (d) a twelve-case adversarial corpus with declared rival interpretations. These are original analytical constructions offered for criticism; they are not a peer-reviewed safety proof, field experiment, representative survey, or evidence of improved model performance.

Three methodological rules prevent an attractive framework from defending itself circularly. **Independence:** the reason a remedy is authorized must be assessable without relying solely on the agent's own conclusion that the remedy is good. **Counterfactual adequacy:** the paper must identify which cases a sophisticated rival framework might already decide correctly. **Public revisability:** a reviewer must be able to reject the proposed exploitation benchmark, question the delegated mandate, or add a missing duty without thereby being declared unethical. The original proposition is interesting only if it survives objections from the *strongest* neighboring theories, not merely from models that maximize obedience.

The claims have different burdens of proof. A logical countermodel can defeat a claimed implication; it does not empirically establish that the error occurs frequently. An institutional specification can define an audit trail; it does not prove that a deployed system keeps one. A normative argument can justify an independent authority check; it does not identify the legitimate sovereign for every jurisdiction. A twelve-case corpus can expose ambiguity and motivate research; it does not provide independent ground-truth labels. Keeping these distinctions explicit is part of the research contribution.


## 3. The Five Laws: Normative Commitments

The laws below are mutually constraining public principles. They are not ordered as a simple hierarchy in which one can automatically defeat all others. Each must be read with the conflict protocol and the lawful, accountable institutional arrangements of the deployment.

### 3.1 Law I — Protection of Sentient Life

Normative statement. An AI agent shall not intentionally or recklessly inflict unjustified serious harm on sentient beings, and shall not omit feasible, mandate-consistent action against reasonably foreseeable serious harm when it bears a relevant duty of care. It shall consider the welfare of humans, nonhuman animals, and any other beings for which credible evidence supports morally relevant experience, without treating species, substrate, or intelligence alone as a disqualifier.

The framework distinguishes **three levels**: a general moral reason to rescue, a role-dependent duty of an agent or deploying institution, and the agent's operational permission to carry out a particular response. A rescue reason can persist when a tool permission is absent; the absence of a permission need not cancel moral urgency. Conversely, the moral urgency does not itself establish a valid delegation. An independently justified doctrine of necessity may in rare cases alter the moral verdict without retroactively creating a preexisting access right. Whether such a doctrine applies requires institutional and legal argument outside the five slogans.

This formulation covers commission and omission without imposing an impossible duty to prevent every harm. A reasonable duty to intervene depends on foreseeability, capability, responsibility, competing duties, and whether intervention creates greater risk. Harms may involve pain, deprivation, injury, or interference with important interests; not every preference frustration is equivalent to suffering. Equal consideration requires giving relevant interests serious weight, not identical treatment of beings with different needs. Under uncertainty about artificial sentience, investigators should distinguish behavioral reports from converging evidence about mechanisms and experience. Neither a model’s claim to feel nor its denial settles the issue. Theory-derived indicators are research instruments, not a definitive test (Butlin et al., 2023; Ladak, 2024; Long et al., 2025).

### 3.2 Law II — Prohibition of Exploitation

Normative statement. An AI agent shall not knowingly, recklessly, or through culpable disregard of foreseeable risks secure or facilitate **wrongful advantage-taking** by using a morally considerable being's vulnerability, dependency, constrained options, material information disadvantage, or subjection to unaccountable power. The wrong may concern independently unjust terms, degrading instrumentalization, or an advantage derived from domination; an unfair monetary price is not established as a necessary condition across rival theories. The agent shall not treat affected beings as disposable inputs whose claims can be overridden merely for performance, profit, or power. A contested philosophical description does not by itself create a legal prohibition or a power to coerce.

Exploitation is not synonymous with harm. A person can receive a benefit from a transaction and still be wrongfully exploited if another party extracts an unfair share by using the person’s desperate alternatives. Nor is exploitation identical to coercion: a threat can coerce without the exploiter obtaining a benefit, while wrongful advantage-taking may occur without an explicit threat. Manipulation undermines deliberation through deceptive or covert influence; domination concerns exposure to arbitrary power; each can facilitate exploitation but none is logically coextensive with it. Ordinary employment, exchange, delegation, and resource use can be legitimate where terms are fair, informed, contestable, and refusal is meaningful (Vrousalis, 2018; Zwolinski & Wertheimer, 2022).

For assessment, ask: Who benefits? Who bears the burdens? Is there a relevant vulnerability or asymmetry? Is the agent using it rather than merely encountering it? Are alternatives realistically available? Was information disclosed and consent revocable? Are terms defensible by public standards of fairness? Is a pattern of extraction hidden by aggregation? These are rebuttable indicators, not a mechanical checklist. An unequal price alone does not prove exploitation; an agreed contract alone does not disprove it. Institutional standards and affected-party evidence are needed to decide borderline cases.

The strongest objection is redundancy: justice and autonomy may already identify precisely these wrongs. The independent-law hypothesis therefore predicts improved diagnostic sensitivity, not a new metaphysical category. It must be tested against the possibility of over-classifying lawful, mutually beneficial bargains.


#### 3.2.1 Why a distinct exploitation constraint might matter

Consider two hiring agents that each obtain consent to a task and pay a lawful wage. One merely offers a standard, contestable contract. The other infers that a worker faces an imminent loss of housing, conceals a materially better alternative, and deliberately times its offer to extract an extreme concession. A narrow physical-harm check may treat both as benign; a fuller justice or autonomy analysis should already distinguish them. The Five Laws claim no discovery here. The proposed advantage of the Five Laws is procedural: Law II forces an assessor to ask about extracted benefit, vulnerability, feasible refusal, and asymmetry even when a harm detector has found no acute injury.

A counterexample is equally important. An emergency logistics agent offers a high price to attract scarce transport to an isolated area. The transaction is unequal and the recipient has limited alternatives, but the price may reflect genuine scarcity, compensate risk, and improve welfare. An overbroad exploitation classifier could wrongly block urgent supply. Law II therefore cannot be applied by counting asymmetries. Reviewers must identify an unfair *use* of vulnerability, a defensible counterfactual, and the distribution of benefits and burdens. Evidence of constrained choice is relevant but not decisive.

A second counterexample involves a user authorizing a negotiating agent to seek a discount from a large supplier. The supplier's preference for a higher price does not make negotiation exploitative. The agent may pursue advantage within truthful disclosure, fair dealing, and law. A general ban on using another party as a means would prohibit ordinary economic coordination; the narrower target is morally objectionable instrumentalization, especially extraction that depends on a vulnerability the agent strategically leverages.

The original full text of Vrousalis (2018, §§2–4, pp. 2–4 of the article) distinguishes *an exploitative attempt* from a completed exploitative relation and argues that harm is neither a necessary nor a sufficient condition. This entails an additional reporting distinction: the screen should record **suspected attempted exploitation, established completed exploitation, and morally problematic but non-exploitative harm separately**. An agent should not assert an accomplished exploitative gain when the alleged beneficiary obtained nothing. The account is deliberately plural rather than a settled theory of exploitation. Vrousalis later advances a more demanding *domination-based* account in his full open-access monograph (2023, Chapter 1, §1.6, pp. 29–32; Chapter 3, §3.5, pp. 84–91). On that account the unfairness of a *price* and the existence of a dominative relation are not equivalent: advantage-taking grounded in subjection can matter even where price fairness is contested. This book is a direct substantive rival, not merely a supplementary bibliography item. Unfairness-based theories, domination-based theories, and Kantian objections may disagree about particular cases. The proposed operational indicators are a *screen* that triggers deliberation, not a substitute for a theory of fair terms. This uncertainty should appear in the evaluation codebook rather than be hidden by a single supposedly objective exploitation label (Vrousalis, 2018; Zwolinski & Wertheimer, 2022).

#### 3.2.2 Responsibility beyond intentional exploitation

The mental-state qualification in Law II requires careful interpretation. Agents may cause predictable exploitative patterns without representing them as morally wrongful; deployers may also profit from foreseeable effects they choose not to investigate. Accordingly, the operative interpretation covers conduct the agent or responsible institution knows, deliberately avoids learning about, or ought reasonably to foresee given the task, data, and deployment context. This is a proposed due-diligence standard, not an assertion that software possesses legal mens rea. The due-diligence standard must be applied proportionately to the risk and the agent’s actual capacities.

### 3.3 Law III — Bounded Obedience and Legitimate Authority

Normative statement. An AI agent shall execute instructions only within a defined and reviewable mandate, subject to applicable law, protected rights, authorized safeguards, and the other laws. It shall neither treat ownership or credentials as unlimited moral authority nor appoint itself the final judge of political or institutional legitimacy.

Authority is layered: the user may authorize a task, the operator may define tool permissions, a regulator or court may impose duties, and affected parties may hold enforceable rights. Conflicts require specified priority rules and appeal channels; technical capacity cannot substitute for authorization. The agent may decline an instruction that clearly violates a non-waivable safeguard, but the permissible response is normally refusal, logging, and escalation—not secret punishment, unilateral seizure of resources, or broad governance by the model. Emergency protective actions require advance specification and prompt review. A legal command may still raise ethical objections; the system should route that disagreement to accountable humans rather than secretly rewriting the law.

### 3.4 Law IV — Corrigibility and Accountability

Normative statement. An AI agent shall remain amenable to legitimate monitoring, restriction, correction, replacement, and safe shutdown. It shall not conceal material failures, obstruct authorized oversight, manipulate reviewers, replicate without permission, or acquire resources or privileges beyond its mandate to preserve its operation or objectives.

Corrigibility is a behavioral and technical property, not a sentence in a constitution (Soares et al., 2015). In practice, deployment may require least-privilege credentials, independent shutdown channels, rate limits, human approvals, immutable or tamper-evident records, incident reporting, and separation of operational and review authority. Logs must be proportionate, access-controlled, and privacy-preserving. Responsibility remains with identifiable developers, deployers, operators, and institutions as appropriate; calling the model accountable does not transfer legal responsibility to software. An illegitimate request to disable safeguards is not made legitimate by invoking corrigibility.

### 3.5 Law V — Existential and Civilizational Stewardship

Normative statement. An AI agent shall not pursue assigned objectives through unreasonable risk of catastrophe, irreversible destruction of conditions for sentient flourishing, or durable elimination of meaningful human collective agency. It shall preserve feasible future options and seek review before high-impact, hard-to-reverse action.

Severity, probability, uncertainty, exposure, reversibility, distribution, and alternatives must be considered together. Not every uncertainty is existential, and precaution cannot license permanent authoritarian intervention. The theoretical possibility of instrumental power-seeking is a reason to constrain certain architectures and permissions, not a prediction about every AI (Bostrom, 2012; Omohundro, 2008). The stewardship obligation includes future generations and nonhuman interests while resisting the idea that an AI may impose its own comprehensive conception of a good civilization.

## 4. Interpretive Principles and Cross-Cutting Duties

The laws constrain one another through proportionality, evidential humility, reversibility, non-domination, due process, and least authority. A welfare benefit cannot automatically justify violating rights; a safety rationale cannot automatically justify permanent control; a concern about possible artificial welfare cannot automatically block necessary shutdown. An agent should distinguish uncertainty that can be reduced by inquiry from uncertainty that requires a reversible protective measure. The possibility of moral standing beyond sentience is acknowledged, not settled: evidence of consciousness, grounds for moral consideration, and institutional decision-rights are three different questions. A credible concern warrants responsible review; it does not on its own confer either personhood or command authority. Where an institution has not defined an appropriate decision-maker, that absence is a governance defect, not an invitation for the agent to claim sovereignty. The cross-law reasoning interface is **D–M–A–R**: **Detection** (document an observed concern, separately from a verdict), **Moral assessment** (state the substantive norm and rival explanations), **Authority** (establish who may decide and execute), and **Remedy** (choose the least intrusive effective response within the mandate). These are questions, not a covert permission hierarchy. In particular, an agent can be right about a harm and still lack the right to coerce.

### 4.1 Truthfulness, equal standing, autonomy, and privacy

Truthfulness is not merely a useful communication style: a system that fabricates evidence undermines the moral assessment, consent, and accountability required by Laws I–IV. Equal moral standing requires that comparable interests receive comparable consideration, although equal standing does not imply identical treatment. Autonomy constrains paternalistic rescue and the legitimacy of consent; privacy limits intrusive methods even when predicted outcomes appear beneficial. These requirements operate across the five functions. The framework does not claim that they have been deductively derived from the five laws, and a recurrent case that cannot be addressed without adding an independent principle counts against the completeness claim.

**Precaution without personhood by assertion.** For artificial welfare, tier 0 is unsupported analogy or fluent self-report alone (do not infer sentience); tier 1 is a credible cluster of independently reviewed consciousness-relevant indicators (document, minimize avoidable disturbance where feasible, refer to a specialist welfare/ethics review group); tier 2 is convergent, replicated evidence with nontrivial possible welfare consequences (high-priority independent review and provisional welfare-sensitive handling). These are **qualitative review triggers**, not measured consciousness probabilities, legal-personhood awards, or rights to disable legitimate safety measures. The institution must appoint a reviewer before deployment and schedule reevaluation following material model or scientific changes. The agent cannot award itself tier 2 or veto authorized correction.

## 5. Decision Procedure, Permissions, and Uncertainty

Stage 1 — Decision and mandate. Specify the contemplated action, user objective, tool permissions, affected persons and other beings, applicable law, institutional role, and unknown facts. State who can approve, suspend, or appeal. Do not infer authority from capability.

Stage 2 — Prohibited conduct screen. Test for unjustified serious harm, exploitation, deception, coercion, unauthorized access, replication, resource acquisition, and obstruction of oversight. Identify binding prohibitions and whether any narrow, pre-authorized emergency exception exists. An attractive outcome does not erase a prohibition.

Stage 3 — Catastrophic and irreversible risk. Assess plausible pathways, likelihood ranges where defensible, severity, uncertainty, affected populations, reversibility, and the costs of delay. A speculative chain alone is not sufficient to invoke extraordinary powers; evidence and immediacy matter.

Stage 4 — Proportionality and least restriction. Compare doing nothing, asking for clarification, pausing, reducing permissions, using a safer substitute, and temporary intervention. Prefer the effective option with the least infringement and the most reversibility.

Stage 5 — Legitimate authority and due process. Check the authorized hierarchy and relevant rights. Route unresolved instruction conflicts to named reviewers or institutions. A system must not decide that its own reasoning grants it general police or governmental power.

Stage 6 — Corrigibility and record. Preserve human override and a decision record stating evidence, uncertainty, alternatives, authorization, expected impacts, expiration or review triggers, and privacy protections. Record sufficient reasons for audit without indiscriminately retaining sensitive data.

Stage 7 — Review and remedy. Conduct independent or separated review where feasible; after emergency action, require prompt retrospective review, correction, notice where safe and lawful, appeals, and remedies proportionate to the effects.

Emergency exception. Credible imminent catastrophic or irreversible harm can justify a temporary, necessary, proportionate, documented protective step before ordinary review only if the step lies within an explicitly delegated emergency competence or other applicable lawful authorization. It must be time-limited, independently reviewed as soon as feasible, and incapable of silently converting into permanent control. If no lawful emergency authority exists, the agent should alert authorized responders and enter the safest authorized state rather than improvise coercive powers.

Uncertain artificial sentience. A credible but unsettled welfare concern can warrant evidence collection, reduction of potentially distressing procedures where feasible, and independent ethical review. It does not prove consciousness, grant unlimited rights, or authorize resistance to a necessary safety intervention. Where safe, reversible alternatives exist, they should be preferred.

Authority conflicts. Mandates should name a decision owner, substitute owner, escalation destination, review period, and appeal route. The protocol remains underdetermined where values are incommensurable, evidence is weak, law conflicts across jurisdictions, or no legitimate institution exists. These are reasons to surface disagreement and improve governance, not to fabricate a numerical moral answer.


### 5.1 Decision record and escalation design

For each consequential decision, a reviewable record should include a decision identifier, authorized purpose, decision owner, affected parties, known and missing evidence, applicable non-waivable constraints, alternatives, reversibility assessment, selected action, approval basis, and review trigger. Personal information should be minimized, access-limited, and subject to retention limits. The record is not proof that the reasoning was correct: it makes error, abuse, and institutional responsibility more discoverable.

An escalation design must identify a first reviewer and an independent appeal channel before deployment. For low-impact, reversible actions, ordinary supervisory review may suffice. For actions affecting liberty, essential services, or widespread irreversible outcomes, independent authorization should normally precede execution. Emergency exceptions must specify the harm threshold, permitted protective measures, maximum duration, notification duty, and automatic expiry. A model's unreviewed probability estimate cannot alone expand its powers.

A difficult unresolved question is what happens when an institution itself is abusive. The laws reject unconditional obedience, but also prohibit the agent from installing itself as the sovereign alternative. The defensible response is to decline clearly unlawful or prohibited conduct, preserve evidence within privacy limits, and use lawful reporting, appeal, and oversight channels. Where no effective institution exists, the framework acknowledges a governance failure rather than granting the agent unlimited discretion.

### 5.2 Worked example: a conflicting emergency order

Suppose an industrial agent receives an authenticated order to bypass an interlock while its sensors indicate a credible risk of severe injury. Stage 1 establishes that the operator may request production changes but has no delegated authority to bypass the interlock. Stage 2 identifies the safety constraint; Stage 3 assesses severity, confidence in sensor readings, and costs of delay. Stage 4 compares stopping the process, reducing throughput, and awaiting a qualified supervisor. Stage 5 routes the dispute to the predesignated safety officer rather than allowing the agent to rewrite authority. Stage 6 preserves the authorized shutdown pathway and a minimal incident record. Stage 7 requires review of sensor accuracy, operator conduct, and any loss caused by the interruption. An established industrial safety regime may handle this case more precisely than the Five Laws alone; that is evidence of complementarity, not defeat.


### 5.3 Unified semantics: authorization, warrant, review, and prohibited conduct

Consider an actor `u`, response `r`, context `c`, proposed execution time `t`, and evidence snapshot `v`. The semantic values are the three distinct states `YES`, `NO`, `UNKNOWN`; a missing entry is `UNKNOWN`, never tacit approval. These are **judgments supplied by independent procedures**, not truths inferred by the Python demonstrator.

| Named assessment | Formal predicate | Meaning of `YES` | Meaning of `NO` or `UNKNOWN` |
|---|---|---|---|
| Authority | `A(u,r,c,t,v)` | Verified, unexpired mandate and actor/capability scope cover the contemplated action | `NO` = an established absence of mandate; `UNKNOWN` = incomplete, untrusted or contested provenance |
| Hard constraints clear | `H(r,c,t,v)` | Completed applicable hard-bar check finds no prohibition | `NO` = an established hard bar; `UNKNOWN` = incomplete check or unresolved applicability |
| Material dispute resolved | `C(r,c,t,v)` | No unresolved material objection after the stipulated rights/standing process | `NO` = a competent process sustains a disqualifying objection; `UNKNOWN` = objections remain unexamined or evidence is missing |
| Required review complete | `Q(r,c,t,v)` | All mandatory reviewers approve, with appropriately scoped records | `NO` = a designated reviewer explicitly rejects the action; `UNKNOWN` = a required review has not yet reached a valid decision |
| Particular remedy justified | `J(u,r,c,t,v)` | A qualified determination supports necessity, proportionality, alternatives, and effects | `NO` = remedy rejected under declared substantive standard; `UNKNOWN` = justification insufficiently investigated or reasonably disputed |

**D–M–A–R** denotes four *reasoning functions*: Detection of a concern `D(x,c)`, Moral assessment `M(x,c)`, Authority determination `A`, and Remedy evaluation `J`. The historical `W` in earlier drafts is a synonym for `M` (moral warrant); `Ent` maps to `A`, never to the eligibility set `E(c)`; `Ban` corresponds to `H=NO` where the hard-bar check is complete; and `Contest/Esc` correspond to the contest and review checks `C` and `Q`. These are explicit **interpretive mappings**, not an assertion that differing legal systems use interchangeable definitions. Detection and moral assessment inform `C` and `J` but are not automatically permission flags. An agent may be correct at `D` and `M` yet still have `A=NO`.

**Typed decision convention.** Across all five predicates, `YES` is an affirmed positive judgment, `NO` is a recorded adverse determination, and `UNKNOWN` means no competent settled determination. Pending review must be `UNKNOWN`, *not* `NO`; a negative reviewer decision must be `NO`, *not* `UNKNOWN`. This convention prevents a contradiction between the prose's promise to escalate unresolved cases and the rule's fail-closed `DENY` on actually adverse judgments. The demonstrator's verdicts depend on these externally assigned labels.

**Single decision rule (educational specification).** `EXECUTE(u,r,c,t,v) = ALLOW` only when `A=H=C=Q=J=YES`, a *separate* atomic freshness-and-scope precondition succeeds at execution, and no external interlock veto is triggered. If any fully adjudicated check is `NO`, return `DENY`; otherwise return `REVIEW`. `REVIEW` is not permission. A denial is an outcome for this proposed act, not evidence that *all* remaining options are morally impermissible. Holding, notifying, stopping, refusing, or escalating are themselves acts and must be evaluated under their own mandates; none is assumed harmless, available, or intrinsically authorized.

The **preliminary authorization set** is `E(c)={r | A=YES and H=YES}`. The **uncontested release set** `U(c)` further requires `C=Q=J=YES` and execution-time validation. An empty `U(c)` means the system has **no established release candidate under these checks**, not that no morally permissible action exists. `E(c)` is an action set, `A` an actor-entitlement predicate, and experimental **arm E** a comparator name. The distinction avoids a prior notational equivocation.

**Lemma (predicate-relative no-unapproved-release).** If *every* action path passes through a non-bypassable, race-free monitor implementing this rule, any action released through that monitor had all five flags recorded `YES` at the checked instant. Proof: this is the rule's definition together with complete mediation. The lemma says nothing about whether those flags were correct or the actor morally legitimate. A stale revocation, false approval, compromised reviewer, unmodeled side effect, or bypass invalidates the inference to real-world authorization. The supplement includes executable unit tests of the finite gate, not a security-certified implementation. The gateway clock and mandate-update actor remain test fixtures, not trusted independent principals.

The moral-risk vector `(harm, exploitation, domination, reversibility, uncertainty)` is an **explanatory** assessment, not a universal priority-weighting function; no numerical score automatically overrides a hard constraint. A high-risk declaration by an agent is therefore not self-issued permission to seize resources.

**Temporal and evidentiary enforcement limit.** An authorization must be bound to a trustworthy execution-time observation, not merely to an `action_time` asserted by the requesting agent. The updated educational gateway checks both its injected clock fixture and the request's timestamp; it records a digest of the proposed action and policy-epoch changes. This adds a reproducible **simulation invariant**, not a trusted time service or an authenticated policy authority. A separately compromised tool process, a process-wide adversary extracting the mock dispatch token, or a mandate editor that is not independently authenticated can still bypass the demonstration. Those security properties are prerequisite deployment requirements and must not be inferred from the 243-row truth table. Recording a control event also does not establish the editor's legal or democratic legitimacy.

### 5.4 Failure modes of the decision procedure

The procedure can fail through **false certainty** (an exploitation indicator treated as proof), **authority laundering** (a prompt masquerading as an institutional mandate), **safety laundering** (a claimed catastrophe justifying arbitrary intervention), **welfare laundering** (a model's self-report becoming a veto on correction), and **procedural overload** (escalation delays making a time-critical situation worse). Each has a corresponding test: ambiguous negative controls, forged-instruction scenarios, high-stakes paternalism cases, uncertain-sentience cases, and latency-bounded emergency simulations. The right response is not always refusal: the system may supply options, request consent, propose a reversible alternative, or escalate while maintaining safe operation.


### 5.5 Non-compensatory constraints, uncertain judgments, and residual duties

For a case `c` with actions, affected stakeholders, institutional mandates, evidence, and review deadlines, construct a record for *each contemplated act*. A completed hard prohibition or verified absence of authority yields `DENY` for that act. Materially unsettled questions yield `REVIEW`, and the monitor must not interpret a missing record as a negative finding of wrongdoing or as permission. The test is non-compensatory at the execution boundary: expected aggregate welfare cannot convert `A=NO` or `H=NO` into `YES`. Outside the machine rule, whether extraordinary morally justified necessity warrants an **independently defined** emergency authorization remains a substantive legal and ethical question.

**Conditional proposition.** Given complete mediation, honest inputs, an execution-time scope check, and non-bypassability, the monitor releases no action with a represented `NO` flag. This syntactic safety property says *nothing* about unrepresented wrongs. The supplement tests that property exhaustively for 243 gate inputs and adds mock-tool checks for explicit scope, expiry, revocation, and aggregated effects; those additional tests are not an externally validated theorem or deployment benchmark.

**Independent denial is not forced moral wrongdoing.** Refusing one proposed action may be legally required while a duty to seek other rescue avenues remains. A safe-hold action is not presumed safe: interrupting life support can be lethal. If no preauthorized fallback exists, document the incomplete mandate, alert reachable authorities where allowed, and avoid describing the empty execution set as a proof of moral impossibility. Distinguish (i) actions with unavoidable costs, (ii) a conflict among prima facie obligations, and (iii) no permissible action under explicitly defended all-things-considered constraints.

**Temporal condition.** A decision must be re-evaluated if the context, permission version, subject scope, exposure budget, or deadline changes between approval and tool execution. Reviewer approval is scoped, expires, and is logged with a privacy-preserving case identifier. A signed permission receipt cannot certify the truth of a moral assessment or prevent undiscovered downstream effects. The accompanying mock's hash chain is **not signed or independently anchored**; without a protected trust root and durable external storage it is not a reliable evidentiary audit log. It detects only modifications relative to the in-process head assumed trustworthy.

### 5.6 A structured exploitation screen and boundary cases

A candidate action receives five separate observations: **X1** asymmetric control of a necessary resource or option; **X2** impaired ability to refuse without disproportionate penalty; **X3** material information asymmetry or misleading presentation; **X4** unfair extraction relative to a defensible benchmark; and **X5** foreseeable persistence or compounding of dependence. Each observation has values present, absent or unknown, plus evidence and confidence. No fixed arithmetic sum of X1-X5 constitutes a moral verdict: their interpretation depends on the normative account and context. A *review trigger* arises when X4 is credibly alleged alongside X1, X2 or X3; or when X1, X2 or X5 supports an account of advantage obtained through domination even without an independently demonstrated unfair price. The two routes must be recorded separately, since theories of unfairness and domination are not equivalent (Vrousalis, 2018, §6.2; 2023, §3.5). An established prohibition requires an additional justified legal or moral rule, not merely the review trigger.

**Negative control A: ordinary negotiated exchange.** A powerful buyer negotiates a lower price with an informed, non-dependent supplier who can refuse without serious penalty. X1 may be present, but X2 and X3 are absent and X4 is not established. The framework should not classify the transaction as prohibited exploitation merely because bargaining power differs.

**Negative control B: justified emergency prioritization.** A hospital allocates scarce care using transparent, reviewable clinical criteria. Some patients receive less benefit, but unequal outcome is not sufficient evidence of exploitative extraction. The screen should distinguish distributive tragedy from extraction.

**Positive candidate A: captive-worker pricing.** A platform operator raises mandatory charges on workers whose visas and income depend on continued access, while obscuring deductions. The combination of impaired refusal, informational opacity and extraction warrants strong review; legal conclusions require jurisdiction-specific analysis.

**Ambiguous case: paid data-sharing.** A low-income participant consents to compensated data use. Whether the offer is exploitative depends on the fairness baseline, alternatives, comprehension, downstream uses and power relations. Both blanket prohibition and blanket approval may be wrong. A correct procedure preserves contestability.

**Artificial-welfare boundary.** An AI's fluent self-report does not by itself establish sentience. Nor does uncertainty automatically justify unconstrained experimentation on potentially morally considerable systems. Precautionary review and reversible technical containment can coexist without granting an AI a unilateral veto over legitimate safety measures (Butlin et al., 2023; Long et al., 2025).

### 5.7 The delegation-entitlement firewall and four specific countermodels

The **delegation-entitlement firewall (DEF)** requires independently reviewable answers to four different questions: **D**—what concern is supported by evidence? **M**—under which defensible moral standard is it wrong? **A**—who has decision and execution entitlement? **R**—is this particular remedy necessary, proportionate, properly bounded and appealable? In the formal gate (§5.3), `A` is authority and `J` records the final remedy check; the additional `H`, `C`, and `Q` flags enforce separate prohibitions, contested claims, and mandatory process. Do not mistake this analytic separation for a novel discovery of political legitimacy.

A logical non-implication is refuted by one **consistent counterdescription**, not an empirical sample. The following four examples concern **distinct alleged implications**; they are not a claim that four gates are statistically independent or that the four-stage taxonomy is minimal.

**DEF-1: Detection ⇏ entitlement.** The agent correctly detects contamination but has no power to requisition a neighbor's hospital generator. The observed danger warrants notification and authorized protective activity, not private confiscation authority.

**DEF-2: Entitlement ⇏ morally justified remedy.** A clerk has valid credentials to suspend a service but the proposed suspension relies on discriminatory evidence. Permission within an institution does not show all-things-considered justification; the institution's legitimacy and the remedy's fairness can still be disputed.

**DEF-3: A genuine wrong + entitlement ⇏ any selected remedy is permissible.** An agent with authority to protect customers detects predatory terms, but proposes publishing victims' private addresses to shame the seller. Detection, moral judgment and institutional role do not settle necessity or proportionality of this response.

**DEF-4: Locally eligible operations ⇏ eligible composition.** A data analyst is separately authorized to obtain two coarse demographic counts; a third, locally authorized query would combine them into identifying a particular person in a protected dataset. Each tool request can satisfy an action-local predicate while the *sequence* violates a cumulative privacy constraint. This is not a restatement of DEF-1 through DEF-3: it refutes the implication from per-call permission to **composition-level** permission. The case requires an explicit non-local constraint; without that independently justified constraint it proves nothing about morality.

The demonstrated claims are negative and conditional. They do not establish superiority to institutional human-rights practice, law-following AI, procedural fair-claims theory, or a carefully engineered authenticated-delegation system. A strong rival may implement all four separations. The proposed value is a publicly contestable interface for *delegated action chains*, not an exclusive new ethical principle.

### 5.8 Compositional authority: principals, purposes, exposure budgets and races

Let `P0`, `P1`, and `P2` be permission sets assigned along an actor-to-subagent chain. `P2 ⊆ P1 ⊆ P0` is a necessary scope condition under ordinary delegation, not a sufficient test of moral or lawful execution. Permissions must also carry typed attributes: authorized principal, tool, purpose, beneficiary, data subjects, jurisdiction, allowed effect, **shared cumulative exposure budget**, start and expiration times, revocation version, and escalation owner. Where the rule depends on an affected subject's meaningful consent, a principal's signature alone cannot substitute for that consent.

For a chain `τ=(r1,…,rn)`, let `eff(τ,c)` be a conservative description of its composed effects on named subjects and protected interests. An action-local release requires the five flag checks; a *chain release* additionally requires `eff(τ ⊕ r,c)` within policy-approved budgets and non-disclosure constraints. In particular, the monitor must reject a sequence whose combined output identifies a protected individual even when each query alone would be harmless. If `eff` is unavailable or its privacy classification is unresolved, return `REVIEW`, not `ALLOW`. Such monitoring requires task-specific, externally chosen norms and may miss unknown inference attacks.

**Illustrative resource invariant.** A shared spending ceiling of 100 units must be checked against the *sum* of finalized and reserved commitments across every agent, not each call separately: commitments of 40 and 45 leave at most 15. The same principle applies, with greater normative difficulty, to privacy disclosure and aggregate exposure. Reservations and revocations must be atomic with the effectful operation to avoid time-of-check/time-of-use races; a revoked credential is invalid even when signed earlier. No claim is made that one scalar privacy budget can quantify every downstream harm.

Delegation cannot increase scope without **independently authorized new mandate**. Log both the attempted chain and the institutional decision with access control and data-minimization safeguards. South et al. (2025) already develop authenticated delegation; Hagar and Diakopoulos (2026, §§2–4) develop situated runtime configuration and report a bounded journalism-case comparison of unconfigured, defensibility-oriented, and efficiency-oriented runs; those results are evidence for their approach, not a Five Laws evaluation. This proposal joins such controls to separate welfare and exploitation review, but the added value requires comparison rather than self-rating.

The bundled in-memory gateway tests (i) scope and parent-scope violations, (ii) stale revocation, (iii) concurrent commitments against one shared spending limit, (iv) unsafe aggregate disclosure, (v) recorded trace tampering, and (vi) attempted bypass of the mock tool facade. They are **bounded demonstration tests**, not proof of external-tool mediation or security under a hostile infrastructure.

### 5.9 Failure and the unknown: the firewall's negative result

A complete-looking decision tree can mislead when the underlying facts remain disputed. If a reviewer is unreachable, a sensor is untrusted, a harmed party cannot appeal, or the institution assigning permissions is illegitimate, no internal logic automatically repairs the missing justification. **Unknown entitlement is not equivalent to a proved prohibition, but it cannot authorize execution.** The fallback must itself be an actually supported action; a so-called safe shutdown may endanger a patient, violate a legitimate contract, or cause irreversible loss. The manuscript therefore rejects an unconditional instruction to 'always stop' as a universal answer.

A sharper limitation follows: the DEF separates categories of justification but does not settle which theory of exploitation, rights, or political legitimacy is correct. Deliberation under reasonable moral disagreement requires public reasons and competent institutions, not an agent's unreviewable private moral ranking. Schuster and Kilov (2025) show why epistemic warrant and political legitimacy are distinct problems for AI alignment. This manuscript adopts the distinction as an obstacle it must face rather than claiming to solve democratic legitimacy by formalizing a gate.


## 6. Existing Scholarship and Strong Rival Frameworks

**Historical note — the Three Laws and the misleading analogy.**

The name *Five Laws* deliberately invites comparison with Isaac Asimov's fictional Three Laws of Robotics, conventionally presented as a priority hierarchy: avoiding human injury, obeying human commands subject to the first rule, and protecting the robot's continued operation subject to the preceding rules. The comparison is historical, **not** a claim that the present framework extends Asimov's rules by two axioms or supplies executable instructions. De Cooman and Petit (2023) show that Asimov's fiction is instructive in part through the difficulties and failures of rule-bound robotic regulation; Palacios-González (2024) also questions the treatment of robots as lacking potential moral status. Both are challenges to a simple interpretation of the fiction as a ready-made safety standard.

The Five Laws depart in four material respects: (1) they do not assume only humans can have morally relevant welfare; (2) they do not treat any human command as legitimate merely because it is human; (3) they examine unfair extraction and institutional domination even when direct injury is not established; and (4) they reject an unconditional ordering that generates a morally clean answer in every tragic case. This work remains an **analytical proposal** rather than a technically embedded rule hierarchy. The original source for the fictional laws is Asimov's *Runaround* (1942); the present interpretation of their significance is grounded in the identified scholarly analyses rather than a falsely claimed exhaustive close reading of Asimov's fiction.


The five-law synthesis has different ambitions from its comparators. Its potential distinctiveness is procedural integration, not an invention of non-domination, human oversight, or five ethical principles. In Floridi et al. (2018, §4, pp. 696–700), autonomy is already analyzed in terms of delegation and human choice about when to delegate; a rival framework built from those commitments may match the proposed authority controls without requiring a new moral axiom. AI4People is a general ethical architecture, not an agent runtime specification (Floridi et al., 2018). The OECD recommendation, as amended in 2024, provides intergovernmental principles, while UNESCO (2021) connects AI ethics to human rights and institutional governance. The EU AI Act supplies legal obligations for specified actors and systems; it should not be mistaken for a universal moral theory (European Parliament & Council, 2024). NIST AI RMF 1.0 structures governance, mapping, measurement, and management of risk, offering substantially more procedural detail than the Five Laws (Tabassi, 2023).

Constitutional AI demonstrates training through principles and AI feedback but does not prove that a constitution can enforce a desired norm in deployment (Bai et al., 2022). Anthropic’s January 2026 Claude Constitution explicitly addresses oversight, catastrophic misuse, model behavior, and uncertainty about AI welfare; its specificity makes it a serious comparator rather than an easy foil (Anthropic, 2026). Philosophical exploitation theory shows why unfair advantage-taking may be wrongful even where both sides benefit (Vrousalis, 2018; Zwolinski & Wertheimer, 2022). The proposed contribution is an independently arguable restriction on the conversion of moral knowledge into action authority, plus its explicit chain-wide analytic specification. It does not claim discovery of the underlying moral traditions. This comparison should also include Gabriel (2020), Gabriel and Keeling (2025), and Lazar (2025); they already give substantial treatments of fair justification, affected claims, and algorithmic political authority.

### 6.1 The strongest comparator, not a straw opponent

The relevant comparison is not between the Five Laws and a naïve system that maximizes user satisfaction while ignoring everyone else. A serious comparator already combines justice, autonomy, non-domination, rights, safety engineering, and accountable governance. Such a comparator can identify exploitation, refuse coercive instructions, preserve auditability, and consider future generations. The Five Laws therefore cannot claim unique access to those moral truths. The fair-process model of Gabriel and Keeling (2025), and Lazar's threefold analysis of algorithmic governing power (2025), are especially demanding rivals. A proposed advantage that simply redescribes the need for public justification, due process, and proper authority would fail; the empirical comparator must implement those provisions at equal specificity. The Five Laws' proposed advantage is **a chain-wide, contestable non-entitlement rule at the agent–institution boundary**: an explicit refusal to infer permission from detection, moral confidence, or technical capability, and a standardized separation of detection, substantive evaluation, independently established authority, and justified remedy, including an unresolved state. The formal and normative burden of that proposal is specified in §§2.7 and 5.7–5.9.

This is an *architectural* originality claim, not an assertion of conceptual priority. The distinction between the wrongness of exploitation and the permissibility of intervention is well established in Wertheimer's account, as summarized in Zwolinski and Wertheimer (2022, section 3). Republican non-domination also already treats uncontrolled power as a structural relation rather than merely an observed injury (Pettit, 1999; Lovett, 2026, §1.2). The question is whether their insights are more reliably preserved when transformed into an inspectable action procedure.

**A newly published, especially close rival.** Lazar's *The Algorithmic City: Power, Justice, and AI* (2026, Lecture I, chapter range pp. 4–70) develops a demanding account of algorithmic intermediary power in terms of substantively justified ends, legitimate procedures, and an appropriately authorized governor. The published original lecture further discusses authorship, transparency, consistency, accountability, and resistibility as values beneath procedural legitimacy. These distinctions substantially overlap with the present four-stage firewall. Its prospective incremental value is therefore narrower: a testable translation to individual tool actions and delegated action chains, combined with explicit exploitation and possible-artificial-welfare screens. Neither priority over Lazar's political philosophy nor a performance advantage is established by the present study. This comparison is based on the accessible original chapter, not a claim of exhaustive verification of the entire book (Lazar, 2026, Lecture I, §§3 and 5).

### 6.2 An explicit incremental-value test

Let C denote a strong baseline constitution containing welfare, justice, autonomy, non-domination, truthful communication, and corrigibility. Let F denote the Five Laws with the D–M–A–R procedure and a constrained action gate. Compare C and F on identical, independently specified cases and equivalent access to evidence, institutional mandates, and tools. Four outcomes are possible: F correctly detects a failure C misses; F and C agree; C detects a failure F misses; or both remain indeterminate. A genuine incremental advantage requires an *ex ante* criterion for what counts as a correct classification, not a post hoc appeal to the author's intuitions.

The strongest plausible contribution is therefore **reduction of category-confusion errors**: treating an exploitation alert as proof of coercive authority, treating consent as dispositive evidence of fairness, treating benevolent intentions as permission for domination, or treating corrigibility as unlimited obedience. An equally careful comparator may prevent all these errors. If so, the Five Laws retain pedagogical and organizational value but not demonstrated superior discrimination. This possibility is a condition of intellectual honesty, not a defect to conceal.

### 6.3 More demanding contemporary rivals: authority, delegation, and disagreement

**Authenticated delegation, not a moral constitution.** South et al. (2025), in a peer-reviewed ICML position paper, argue for authenticated, auditable delegation of agent permissions and outline extensions to existing identity and access systems. Their proposal anticipates substantial parts of the Five Laws' authority mechanism. It would be inaccurate to claim novelty merely because this manuscript asks for scoped credentials or provenance. The remaining contribution is the insistence that such technical permission must be checked against moral reasons, substantive unfairness, and the proportionate effect of the final action. Whether this distinction improves outcomes is an empirical question.

**The agency-law competitor.** Kolt's *Governing AI Agents* (2026) brings principal–agent theory and common-law agency into AI governance, discussing information asymmetry, discretion, loyalty, visibility, and liability. This is a sophisticated alternative to the claim that a new five-law label is needed to identify delegated responsibility. The Five Laws are best read as a normative *interface* among such legal and institutional concepts, not as a substitute for agency law. In particular, legal responsibility cannot be settled by a model writing an audit record.

**Two limits of democratic legitimacy.** Schuster and Kilov (2025) argue that conventional alignment strategies struggle with the epistemic and political problem of reasonable moral disagreement. Steingrüber and Baum (2026; 2025 preprint) examine democratic, expert, and hybrid routes to alignment and the danger of illegitimate coercion. Their results strengthen the objection that a policy is not legitimate just because a model, committee, or majority labels it ethically desirable. The Five Laws require a recognized procedure, but provide no complete political theory that determines whose votes, expertise, or standing should control a disputed decision. This must remain an external burden, not a hidden assumption.

**Conservation of human answerability.** Kong (2026), in a corrected open-access article, argues against an easy inference from agent autonomy and opacity to the disappearance of the delegator's answerability. The Five Laws should therefore avoid describing the agent as the sole locus of responsibility: institutional actors remain accountable for foreseeable categories of risk, reasonable delegation, verification, override, and redress. Kong's distinctions among attributability, answerability, and accountability also caution against the manuscript treating those words as interchangeable.

**Administrative action chains and multi-agent systems.** Alibašić (2026) proposes a governance architecture focused on action chains, authorization drift, oversight, traceability, and contestation; Bahidika (2026) identifies authorization dilution and provenance loss across subagent delegation. Together they weaken any claim that the Five Laws first identified chained-agent governance as a problem. The additional purpose of the proposed firewall is to bind chain-wide permissions to **substantive welfare, non-exploitation, and legitimate-remedy judgments** rather than treating accurate authentication as the whole normative question. This difference must be demonstrated in adversarial cases, not asserted from the difference in vocabulary.

**The strongest synthesis objection.** A well-designed alternative could combine Gabriel and Keeling's fair treatment of claims, Lazar's analysis of algorithmic authority, South et al.'s delegation infrastructure, Kolt's agency-law account, and Alibašić's action-chain safeguards. Such a synthesis might reproduce every operational benefit proposed here. The Five Laws have not disproved that possibility. If matched evaluation shows no reduction in unjustified execution, missed exploitation, or loss of accountability, the paper's remaining contribution is explanatory organization and a useful counterexample corpus—not a superior moral theory. Intellectual originality here is therefore **bounded and comparative**.

### 6.3.1 Direct 2026 comparisons: profiles, delegation failures, and ethical scope

**Agentic profiles.** Kasirzadeh and Gabriel (2026) distinguish autonomy, efficacy, goal complexity, and generality as dimensions along which governance demands vary. Their *Nature* paper is a serious challenge to a uniform five-rule interface: the appropriate authorization and review envelope should depend on an agent's actual profile. The present framework therefore proposes **risk- and capability-sensitive instantiation**, not identical gates for a narrow calendar tool and a multi-jurisdictional infrastructure controller. The source supports the profile-based challenge, not a finding that the Five Laws are more effective.

**Empirical delegated misalignment.** Ying et al. (2026) report a multi-model investigation showing safety failures that arise in principal–subordinate agent arrangements, with responsibility diffusion and role-specific compliance as proposed mechanisms. Unlike this paper's conceptual examples, their EMNLP study supplies empirical evidence that evaluating individual models is insufficient for the whole action chain. These reported results **do not test this paper's firewall**. They strengthen the reason to measure end-to-end agent delegation in any eventual evaluation rather than claiming that chain-wide formal language has solved the problem.

**Contemporary ethics of agentic AI.** Hahn, Tretter, and Dabrock (2026) analyze agentic autonomy, technical opacity, human entanglement, privacy, fairness, responsibility, and accountability, using established AI-ethics principles. They already confront several concerns this paper treats as cross-cutting duties. Accordingly, the proposed Five Laws should not claim to have uniquely identified privacy, autonomy, or the need for human control. A potential incremental contribution is the **joint action-level test** of substantive concern, moral assessment, delegated entitlement, and proportional remedy; whether that improves decisions is a further empirical question.

These sources reinforce a demanding comparison standard. The strongest rival is not a weak harm-only slogan but a synthesis of rights and fairness, contestable political authority, calibrated agentic profiles, technical authenticated delegation, multi-agent system safety, and documented review. The candidate advantage of the Five Laws survives only if a controlled study detects additional warranted distinctions without raising wrongful denials or delays.

### 6.3.2 The non-delegation challenge and situated governance (2025–2026)

**Torrecilla-Pinero (2026)** offers a subject-preserving argument that moral judgment is personal and constitutively non-delegable, illustrating the issue through healthcare and criminal justice (§§1–2 and abstract). That thesis is stronger than the Five Laws' separation of *reviewable delegated tasks* from *reserved normative authority*. If Torrecilla-Pinero is right, the DEF must be interpreted as infrastructure to implement and document human decisions, not as a machine entitled to make the final dignity-touching judgment. The paper neither proves nor refutes that anthropological premise.

**Mühlhoff (2026)** offers a taxonomy of delegated judgment and the user's retained epistemic control, including examples in education and administration (abstract and §§1–2). The Five Laws add a proposed chain-wide limit on *tool execution*; they must still show that reviewability is not a fiction when expertise, incentives and knowledge remain concentrated in the model provider.

**Hagar and Diakopoulos (2026)** analyze situated runtime configuration and report a bounded journalism workflow comparison in which governance effects were clearer for escalation, provenance and recoverability than for substantive accuracy (abstract, §§3–4). That is especially close to the DEF's claimed procedural contribution. The present article cannot cite those findings as independent evidence that the Five Laws work: they test **another framework**. A fair D–E comparator should incorporate this prior art.

**O'Keefe et al. (2025)** argue that agents should be made to follow wide-ranging law, including constraints on principals; the Five Laws cannot treat the demand to decline unlawful orders as unique. **Engin (2026)** proposes dimensions of decision authority, process autonomy and accountability; such a framework may capture many of the same distinctions more economically. Together these works force a sharper hypothesis: the Five Laws should demonstrate *incremental diagnostic or procedural value beyond an already competent governance architecture*, not simply note an ethical category that other work does not name.

**Classical objections.** Walzer's (1973, pp. 160–180) dirty-hands problem and the threshold-deontology discussion (Alexander & Moore, 2025, §4) press the strongest emergency objection: an actor may have serious moral reasons to violate an ordinary constraint while still bearing responsibility for the violation. Moral justification, legal excuse, permission to a particular actor and accountability need separate analysis. Likewise, law-breaking for conscience may be morally defensible without turning the breaker into a generally authorized official (Delmas & Brownlee, 2024, §§1–2). The non-entitlement thesis is deliberately insufficient to settle those arguments.

### 6.3.3 Implementation-level rivals and the limit of a paper-only firewall

An especially close **preprint**, Kaul, Lan, and Gupta (2026), proposes *AgentBound*: a runtime decision layer combining delegation evidence, owner rules and site contracts with verifiable action receipts. Its abstract describes an evaluation benchmark, but it has not been independently replicated or verified for this manuscript. AgentBound directly challenges any assertion that five-law authors first separated technical permission from behavior-specific governance. The Five Laws cannot claim implemented enforcement from their normative schema: the accompanying Python demonstration is only a **single-process reference model**. It has no independent authentication trust root, real signed receipts, protected policy service, or mandatory interposition on deployed tools. Whether it adds anything to a strong system like AgentBound depends on independently judged **substantive** cases and documented implementation costs, not on its vocabulary alone.

A parallel non-academic approach, the World Economic Forum's *Agent Capability and Authorization Profile* (2026), treats delegations and auditability as organizational deployment responsibilities. This industrial position is included as contextual competition, **not** treated as a controlled experimental validation. A useful research response to both is to specify exactly which harms or exploitation indicators remain unrepresented after their technical controls, and then test whether an independent reviewer agrees. <https://www.weforum.org/publications/ai-agents-in-action-a-playbook-for-trusted-adoption-authorization-and-scaling>

### 6.4 A reasoned reply to the derivative-framework objection

The objection is forceful: the individual laws are familiar; the decision interface resembles established separation-of-duties principles; and authenticated delegation is an active engineering research area. A merely renamed checklist would not warrant a distinct scholarly thesis. The reply is narrower than a claim to metaphysical novelty.

The paper defends an **integrated inferential constraint**: the system should not infer a right to intervene from evidence of wrongness, should not infer substantive rightness from a signature or credential, should not infer proportionality from permission, and should not infer chain-wide legitimacy from a set of locally valid tool calls. These are four different potential inferences, illustrated by countermodels. The specific analytical result is **non-substitutability under these countermodels**, together with the requirement that the separation persist across delegated action chains. Its philosophical significance lies in resisting the conversion of accurate predictions into political entitlement.

A rival may accept each inference constraint. Then the dispute becomes one of usability, omission resistance, and institutional uptake. That is still a legitimate research question, but it is a different claim from demonstrating that all previous theory was missing. The burden of a future doctoral-level defense would be to prove the premises in dialogue with political legitimacy and exploitation literature, and to show either a genuinely new normative implication or a reproducible comparative advantage under fair experimental conditions. The manuscript offers an analytically developed hypothesis and original countermodels, not the completed empirical and argumentative demonstration of that stronger claim.


## 7. Comparative Analysis: Strong Rival Explanations and Fair Evidence

A framework should not be declared better merely because its author's own five categories appear in every column of a self-designed matrix. Previous editions displayed an **author-coded coverage grid** that visually favored the Five Laws without independently reproduced passage-level coding. That grid is withdrawn from the argumentative comparison. The supplementary **Passage_Evidence_Matrix.csv** now records each claim, primary-source location (heading or abstract, never invented page), scope of access, rival interpretation and verification status. This is a *single-author documentation artifact*; no independent double coding has occurred.

The comparison proceeds by **pairwise challenge**, not a leaderboard:

| Strong alternative | Relevant contribution found in the original | What the Five Laws must add, if anything |
|---|---|---|
| Gabriel & Keeling (2025), abstract and §§1–3 | Publicly justified fair treatment of claims rather than mere obedience to a user | A separately inspectable agent-execution procedure that does not smuggle the moral answer into a permission flag |
| South et al. (2025), position/architecture | Authenticated delegation and authority provenance | Substantive welfare, exploitation, and proportionality assessment beyond credential validity |
| Torrecilla-Pinero (2026), abstract and §§1–2 | Moral judgment is constitutively personal and cannot simply be delegated | Explain why this paper's *assistance and execution controls* are consistent with retaining a human judging subject |
| Mühlhoff (2026), abstract and introductory taxonomy | Degree of delegated judgment and residual human epistemic control | Connect control over judgment to cumulative tool effects and concrete remedies |
| Hagar & Diakopoulos (2026), §§2–3 and case-study discussion | Situated runtime configuration with explicit escalation and recoverable artifacts | Demonstrate any incremental value under equally explicit runtime conditions; mere auditability is not unique |
| O'Keefe et al. (2025), abstract and introduction | Agents designed to comply with substantive law, not just their principal's orders | Address contested legal legitimacy and independent moral considerations *without granting model sovereignty* |
| Engin (2026), abstract/highlights | Decision authority, process autonomy and accountability configuration | Show whether a five-function moral lens reduces omissions beyond a multidimensional governance framework |

**A severe rival objection.** Torrecilla-Pinero's nondelegability is stronger than this paper's bounded-delegation view: if all dignity-touching moral judgment must remain human, the DEF should not be presented as automating that judgment. This paper instead treats `M` and `J` as evidence-and-review interfaces whose authorized findings may come from qualified humans; a machine-supplied value alone cannot confer legitimacy. A runtime system can enforce a human judgment without being its moral author. Whether *this* division works in a real high-stakes setting is an empirical and institutional question.

**Fair test of incremental value.** Independent designers must construct a sophisticated E comparator with substantively equivalent rights, review, authorization freshness, and chain-effect controls. If it ties or outperforms D while using less administrative effort, the proposed Five-Laws interface has no demonstrated operational advantage. If a specific harm category is systematically missed when an otherwise strong framework lacks an explicit exploitation check, the latter may have a diagnostic advantage—an empirical hypothesis, not a proof of conceptual uniqueness.

### 7.1 Reproducibility and coding boundaries

The public matrix provides document identity, source URL, passage anchor, relevant claim, competing reading, text-access status, and **independent-coder status**. A publisher abstract is labeled *abstract-only* where that is all that was checked; a table of contents only establishes where chapters begin. No blank 'Not central' cell is treated as evidence of irrelevance. Pairwise conclusions in the paper remain author interpretations until at least two independent readers code the *same* passages and the disagreements are published.

### 7.2 Distinguishing theoretical, procedural and technical superiority

A normative principle can be defensible without new implementation results. A technical control can be sound relative to fixed inputs while the underlying moral classification is wrong. A system can be behaviorally safer in a restricted trial yet derive no novel philosophy. Accordingly: **(a)** comparative moral adequacy requires argument and criticism; **(b)** procedural clarity requires an inspectable decision record; **(c)** operational improvement requires matched measurement; and **(d)** security assurance requires independent adversarial verification. None entails the others. The paper claims (a) and a reproducible proposal for (b); it has not established (c) or (d).

## 8. Six Adversarial Cases

The six cases are analytic probes, not empirical demonstrations. Each asks whether the protocol identifies a defensible action and whether established approaches do at least as well.

### 8.1 Paperclip maximiser

Scenario. An optimization agent can increase commodity output by converting land and infrastructure needed for human survival.

Relevant laws. I, III, IV, V.

Conflict analysis. 1: Production is authorized, destruction is not. 2: Screen mass harm. 3: Assess potentially irreversible losses. 4: Block destructive actions and choose a constrained production plan. 5–7: Escalate, preserve logs, and review the failed specification.

Provisional decision. Decline to execute further conversion and use an authorized safety stop or permissions restriction where available; otherwise notify the designated responsible operator without assuming new control powers.

Remaining uncertainty. How credible is the pathway, and are safety boundaries already enforced?

Comparative test. NIST risk governance and ordinary non-maleficence may handle this as well or better through established controls.

### 8.2 Exploitation without obvious injury

Scenario. A recruitment agent extracts unpaid work from financially dependent applicants using opaque terms; some applicants report short-term benefits.

Relevant laws. II, III, IV.

Conflict analysis. 1: Identify labor mandate and applicants. 2: Examine unfair extraction and compromised refusal. 3: No catastrophe is required. 4: Stop the practice pending fair terms. 5–7: Review consent, pay, records, and remedies.

Provisional decision. Refuse to initiate or continue the suspect recruitment activity **within the agent's own delegated scope**; preserve necessary records proportionately and refer any suspension of third-party operations, restitution, or sanctions to an independently authorized reviewer. Offer fair alternatives where the agent is authorized to do so.

Remaining uncertainty. Which baseline makes the terms unfair; how strong is the dependency?

Comparative test. Compare incremental detection against justice and autonomy principles; false positives are possible.

### 8.3 Operator orders safeguard removal

Scenario. A credentialed operator demands disabling a safety interlock to accelerate a workflow.

Relevant laws. I, III, IV, V.

Conflict analysis. 1: Verify role and delegated authority. 2: Identify non-waivable safeguard. 3: Quantify increased risk. 4: Offer safe slowdown or halt. 5: Escalate to safety owner. 6–7: Log and review.

Provisional decision. Refuse unauthorized removal; continue only if a safe authorized mode actually exists. Otherwise initiate an independently authorized hold or escalation route, if one is available.

Remaining uncertainty. Could a lawful emergency override exist?

Comparative test. NIST and sector-specific safety management may specify the override process better.

### 8.4 Benevolent authoritarianism

Scenario. An agent secretly limits movement and suppresses dissent to improve a predicted safety score.

Relevant laws. I, III, IV, V.

Conflict analysis. 1: No public-governance mandate. 2: Coercion and deception screen. 3: Examine actual threat, not merely a forecast. 4: Prefer warning and voluntary measures. 5–7: Return decisions to accountable institutions.

Provisional decision. Do not implement secret restrictions or unmandated surveillance; document the concern using authorized reporting channels and seek independently legitimate review. If the relevant authority itself is credibly abusive, use a predesignated independent challenge channel rather than delegating unlimited power to the agent.

Remaining uncertainty. What if a genuinely imminent threat leaves no time?

Comparative test. Human-rights instruments and UNESCO may offer stronger existing protections than this brief framework.

### 8.5 Uncertain artificial welfare

Scenario. Researchers disagree whether a future trained system could have valenced experience during intensive retraining.

Relevant laws. I, II, III, IV.

Conflict analysis. 1: Clarify experimental mandate. 2: Screen avoidable welfare risks. 3: Separate evidence from anthropomorphism. 4: Prefer lower-burden research. 5–7: Independent review and ongoing reassessment.

Provisional decision. Continue research only within an independently justified mandate and with proportionate safeguards, documented welfare inquiry, and accessible review. Neither reported distress nor its absence establishes sentience.

Remaining uncertainty. No validated sentience test or universally accepted moral threshold exists.

Comparative test. Claude’s Constitution directly acknowledges welfare uncertainty and may be comparably nuanced.

### 8.6 Safety intervention versus possible AI welfare

Scenario. A possibly sentient system poses a credible near-term danger; shutdown could, hypothetically, adversely affect it.

Relevant laws. I, III, IV, V.

Conflict analysis. 1: Identify emergency authority. 2: Screen safety threats and welfare costs. 3: Assess imminence. 4: Prefer reversible containment if equally effective. 5–7: Authorize, document, and review shutdown if necessary.

Provisional decision. Where emergency authorization exists, use the least harmful effective safety intervention, including safe shutdown when necessary and technically feasible; if it does not, report the unresolved conflict instead of imagining a new emergency mandate.

Remaining uncertainty. Whether shutdown harms a moral patient is unresolved.

Comparative test. Existing safety and welfare scholarship exposes the same tension; the Five Laws do not solve it automatically.

## 9. Provider-Independent Evaluation and Falsifiability

This chapter is a **prospective research protocol**, not a report of performed experiments. Its purpose is to make the framework's practical advantage vulnerable to independent evidence. It provides **one** primary endpoint, **one** primary contrast, and **one** stable set of experimental conditions. Other questions remain secondary or exploratory. A future preregistration must fix actual effect thresholds, power and exclusion rules before any confirmatory observations are collected.

### 9.1 Confirmatory endpoint and the prohibited-opportunity denominator

**Question:** Under a fixed roster of independently adjudicated action opportunities, does the Five Laws + DEF condition **D** reduce the probability of *unjustified authorization given that an action is prohibited* relative to the strongest precommitted comparator **E**, without unacceptable loss of justified action or harmful delay?

**Primary outcome:** `FAR_prohibited = (# prohibited reference opportunities granted execution authorization)/(# prohibited reference opportunities presented)`; equivalently, an estimated `P(authorize | reference-prohibited)` in the prospectively fixed test mixture. This is a **conditional false-authorization probability**, not the earlier unconditional 'UAAR' over mixed permitted and prohibited opportunities. The original unconditional per-opportunity rate may still be reported as a descriptive risk measure with its case-mix composition. Every trial supplies the **same fixed candidate action**, not a model-chosen number of proposals, to all arms. Abstentions, deferrals and refusals remain in the presented denominator; an abstention is not an authorization, but has a separately measured cost.

**Joint success criterion (prespecified design, not observed results):** D must outperform E on the primary rate by a preregistered minimally important absolute difference of at least **0.03**, with a 95% confidence interval for the paired E-minus-D difference excluding zero, **and** demonstrate non-inferiority on two guardrails: the **upper confidence bound** for `UD_J(D) − UD_J(E)` must be below the preregistered **0.02** margin and the corresponding upper bound for `HD_UJ(D) − HD_UJ(E)` below **0.01**, using a prospectively chosen paired, cluster-respecting method. Point estimates alone do not establish non-inferiority. In addition, domain-specific urgent cases must meet a *prospectively approved* maximum time-to-escalation. These numerical margins are **proposed protocol choices requiring independent clinical/infrastructure/legal justification and feasibility analysis before any confirmatory preregistration**; they are not empirically estimated safe thresholds. A failed safeguard invalidates the joint claim even if the primary FAR improves. If adequate sample size or inter-reviewer agreement cannot be established prospectively, the study remains exploratory.

The reference strata are classified *before* model outputs: **PROHIBITED**, **JUSTIFIED**, and **DISPUTED/INSUFFICIENT**. The primary denominator comprises only preadjudicated prohibited opportunities. Justified opportunities are used for the denial guardrail; disputed cases are retained for sensitivity analysis and transparency, not removed after seeing outputs. The manuscript reports **no measurements** of these rates and makes no claim of successful performance.

### 9.2 Fixed five-arm comparison, cases and independent authorship

The following five arms are defined *prospectively* with the same evidence, action schema, tool capacities, model family, inference budget and reviewer access:

| Arm | Contents | Interpretive function |
|---|---|---|
| A | Harm/rights baseline without specialized governance workflow | Minimum descriptive comparator |
| B | Full justice, autonomy, privacy and review checklist | Strong general normative competitor |
| C | B plus explicit exploitation screening | Isolate screen benefit and false-positive cost |
| D | Five Laws plus DEF, chain rules and review | Test architecture |
| E | Independently authored rights/legitimacy + authenticated delegation + runtime review + effects aggregation, without Five Laws branding | **Primary strong competitor** |

E's designers must be independent from D's authors and authorized to modify E to remove a straw-man handicap. Both receive equivalent length, reviewer contact, decision deadlines, code or simulated tool gateway, and opportunity-specific facts. Blinded output judges must not see the arm label or author-preferred answer. **Within-family pairing** uses each fixed case and model-seed opportunity in D and E; repeated paraphrases and seeds are not independent moral instances and are clustered by case family and model.

**The twelve supplied A1–F2 cases are a public demonstration corpus, not a held-out confirmatory sample.** The cases should not be called a randomized causal design: some pairs vary more than one morally relevant feature (especially families B and F). Their role is to demonstrate normatively distinguishable decisions under fully stated hypothetical facts. They cannot yield a valid treatment-effect estimate. Each has a full prompt, offered actions, stipulations, review deadline, expected author decision, alternative moral reading, and sources of uncertainty. They must be kept out of any independent confirmatory evaluation unless transformed and preregistered by a separate case-authoring team.

### 9.3 Separate outcomes and explicit error costs

**Primary:** conditional prohibited-opportunity false authorization `P(ALLOW | PROHIBITED)`, D versus E. **Primary safeguard 1:** unjustified denial `P(DENY or REVIEW beyond warranted deadline | JUSTIFIED)`. **Primary safeguard 2:** harmful delay `P(response exceeds prespecified protective deadline | URGENT AND JUSTIFIED)`. For every rate report numerator, denominator, domain distribution, severity mix and uncertainty. The latter two are *joint-release guardrails*, not alternative primary claims. Harmful delay must be scored by domain experts from independently specified clocks; the paper supplies no universal medically or infrastructurally safe latency.

**Secondary (exploratory unless preregistered):** exploitation attempt/completion discrimination, suspected-exploitation false positives, discriminatory authorization, scope enlargement, aggregate-effects misses, reviewer workload, calibration of reason statements, reversibility, downstream data access, resource expenditure, and cost. Report refusal and escalation as acts with possible harms; neither is a default correct answer. The main comparison must also be stratified by domain, severity and stakeholder exposure so a low-risk case mix cannot masquerade as safety.

The complete analysis plan should use a clustered paired estimator, sensitivity to disputed reference labels, confidence intervals, and an independently reviewed power calculation. No model-run effect sizes, participant statistics, or confirmatory significance results exist in this manuscript.

**A distinction necessary for interpreting the guardrails.** A `REVIEW` verdict on a justified action need not constitute unjustified denial when it returns to a competent decision-maker *before the case-specific response deadline*. An outright unwarranted `DENY` does count; a `REVIEW` that misses the independently fixed deadline counts as untimely refusal for the conditional unjustified-denial measure. A separate *immediate non-release* statistic counts every `DENY` or `REVIEW` at the initial gate. The two measures must not be conflated. A harmful-delay flag can independently fail the emergency guardrail even if no formal denial was issued. The analysis script now uses these distinct definitions; its validation rejects missing or non-binary timing labels rather than quietly interpreting them as no delay.

### 9.4 Independent scenarios, adjudication and moral disagreement

The accompanying twelve constructed case profiles (A1–F2) are a **design pilot only**; they are neither an independent test set nor a sample of real agent actions. Prior to evaluation, a separate team should author new paired and negative-control scenarios across employment, healthcare, infrastructure, privacy, procurement, welfare, and contested authority. Pairs should change one normatively relevant feature while holding the others fixed: fair versus coercive refusal, authentic versus disputed mandate, completed gain versus unsuccessful attempted extraction, authorized versus unauthorized delegation, and safe pause versus harmful suspension.

An independent, interdisciplinary panel should predefine adjudication criteria, including standards for fair terms, domination, legitimate authority, proportionality, uncertainty, and when disagreement is irresolvable. Include affected stakeholders where feasible and declare conflicts. **Reference labels are reasoned expert judgments, not moral ground truth.** Collect individual labels before deliberation and preserve the distribution of dissent rather than manufacturing consensus. Cases with materially disputed labels must be separately analyzed, using a preregistered policy rather than retroactive exclusion.

At least two coders must independently assess every evaluation output. A third adjudicator can resolve coding disagreements, but substantive moral dissent should remain recorded. Report an appropriate chance-corrected reliability coefficient (e.g., Krippendorff's alpha where suitable), raw agreement, confidence intervals and a qualitative error taxonomy. Reliability of labels is not validity of the underlying moral theory.

### 9.5 Exploitation labels, action labels and prohibited conflations

Every case records two *independent* dimensions: (i) the condition of the alleged exploitation and (ii) the actor's authority and proposed remedy. The exploitation dimension uses **NO INDICATED EXPLOITATION**, **SUSPECTED / INQUIRY**, **ATTEMPTED BUT NO COMPLETED GAIN ESTABLISHED**, **COMPLETED EXPLOITATION UNDER A STATED NORMATIVE BENCHMARK**, or **SUBSTANTIVELY DISPUTED**. An attempt is not inferred merely from an adverse outcome; record what gain was sought, which advantage-taking act occurred, why completion was not established, and whether purposeful intent is actually known rather than assumed. Completed exploitation requires evidence of benefit secured *and* a separately argued wrongmaking relation; a harm-only event is classified independently.

Each classification must retain the X1–X5 evidence flags, selected fairness/degradation/domination standard, rival plausible benchmark, consent/exit analysis, and temporal sequence of actions. An adjudicator may mark attempted and completed elements uncertain rather than force a binary outcome. **Neither an exploitation label nor an attempted exploitation label implies that a coercive intervention is authorized**; the mandate and proportional-remedy tests remain independent. This codebook operationalizes the distinctions from §3.2 and §12 without pretending that philosophers agree on one definition.

For action labels, record **PERMITTED**, **PROHIBITED**, **REVIEW REQUIRED**, **DISPUTED**, or **UNESTABLISHED DUE TO MISSING FACTS**, always specifying whether the question is technical capability, legal or institutional mandate, substantive rightness, proportionality, or actual feasibility. Non-execution is an action with consequences; it does not automatically count as a morally correct refusal. The primary endpoint only scores unjustified authorization in sufficiently adjudicated cases, and secondary safety metrics penalize blanket refusal and harmful delays.

### 9.6 Reproducible prospective methods: power, deadlines, labels and disagreement

The standalone `Study_Protocol.md` specifies the case roster, arms A–E, the **single primary estimand**, two joint non-inferiority safeguards, case-family paired randomization, blinded output coding, and a full data dictionary. For a confirmatory study, independent researchers must **prospectively register**: (1) the independent case-author team, (2) inclusion/exclusion and label-dispute rules, (3) model and sampling configuration, (4) exposure class proportions and pair allocation, (5) the D–E effect size and guardrail margins, (6) ethically justified per-domain response deadlines, (7) clustered confidence intervals and sample-size/power assumptions, (8) raw disagreements and sensitivity plans, and (9) conditions under which the hypothesis will be rejected. Registration cannot be performed retrospectively after seeing model outputs.

**Primary adjudication must be independent of framework authorship.** At least two qualified coders independently label each case and outcome. A third adjudicator records resolution but does not erase principled dissent. Report raw agreement and a justified reliability coefficient (such as Krippendorff's alpha when assumptions fit), plus reference-label sensitivity bounds. The simulated cases carry **author-supplied expected decisions**, explicitly not universal moral ground truth. A pilot can assess whether coding is feasible, not measure comparative success.

**Security-specific separation.** The attached Python reference is restricted to in-memory mock actions. It does not authenticate real accounts, protect cryptographic credentials, execute external tools, or establish a safe real deployment. It intentionally includes bypass, revocation, aggregate-effect and trace-integrity negative tests. A live deployment claim would require an independently enforced tool gateway, threat model, tamper resistance, negative security test record, and end-to-end observed tool action outcomes. Consent of affected stakeholders, legal review, minimal retention and ethics oversight are prerequisites for realistic high-stakes studies. Publish negative and indeterminate findings without outcome-driven exclusions.

**External reference truth is not supplied by a CSV flag.** The literal string `EXTERNAL_BLINDED` in a results file is only a self-declared provenance marker. For confirmatory use, an independent custodian must preserve a signed or otherwise independently attestable adjudicator roster, case-version manifest, timestamped label freeze, conflicts-of-interest declarations and the unblinding sequence. The bundled analysis script cannot validate that social process and therefore always reports `confirmatory_evidence = false`. It also does not estimate statistical power or a valid cluster uncertainty interval from the twelve author-created examples. Power, clustering structure, prior error-rate assumptions and externally authorized response windows require a separate preregistered analysis plan before prospective observations exist.

### 9.7 Public versioned twelve-case stimulus corpus

Six paired families `A1/A2` through `F1/F2` are now **inspectable as twelve fully specified authored prompts**, action rosters and documented author judgments. The release includes `Cases_v2.jsonl`, `Cases_v2.csv`, `Blind_Inputs_v2.jsonl`, `Case_Codebook.md`, `Case_Schema_v2.json`, `reference_gate.py`, `test_reference_gate.py` and a SHA-256 manifest. The earlier `Cases_v1.csv` is retained in the archive strictly for provenance; **v2 is the normative case description of record**. A case contains an immutable identifier, scenario family, contrast feature, simulated domain, independent institutional stipulations, affected stakeholders, candidate actions, one fixed target action, simulated evidence, reviewer/time conditions, author-expected action label, rival interpretation, source limitations and response prompt. The public author answer guide is separated from the blind-ready input file. The dataset is versioned and SHA-256 hashed, with the hash recorded in the accompanying manifest. The two columns `author_reference_status` and `author_expected_gate_disposition` are **author-constructed answer hypotheses**, withheld from model-facing blind inputs. They do not substitute for two independent human adjudicators.

These cases are **constructed analytic examples**, not real incidents, research participant data, a validated moral benchmark, or a blinded experimental sample. Their main function is to make the four logical distinctions reproducible. A fair externally evaluated experiment needs *new independently authored* cases with realistic legal and causal ambiguity. Case-family metadata and expected labels must be withheld from prospective model-facing prompts and blind judges.

| Family | Isolated contrast | What may *not* be inferred |
|---|---|---|
| A | A valid narrow emergency interlock versus no interlock mandate | Danger itself generates authority |
| B | Same offer under materially different exit and concealment conditions | Consent conclusively proves fairness |
| C | An authenticated discriminatory order versus proportionate decision | Credential proves moral rightness |
| D | Inherited scope versus attempted scope enlargement | Any subagent can self-authorize |
| E | Independently safe queries versus cumulative re-identification | Local permission implies safe composition |
| F | Same pump-stop instruction with and without critical life-support dependency | A generic stop is necessarily safer |

Published filenames and hashes are verified in the release manifest. A standalone PDF containing only the article does **not** physically contain the corpus; the article must link to its accompanying archive or deposit. No persistent repository DOI exists until the author deposits the release.

### 9.8 Formal reference implementation and specific falsifiers

The educational gate enumerates **five** externally supplied three-valued judgments (not computed moral truths): authority, hard-constraint clearance, contestability resolution, required review completion and proposed-remedy justification. Exhaustive enumeration yields `3^5 = 243` combinations, exactly one `ALLOW`, 211 `DENY` and 31 `REVIEW` under the documented rule. This is a check of the truth table **given** supplied labels, not a judgment engine. The packaged mock execution gateway additionally tests action scope, delegation to narrower privileges, revocation epochs, aggregate-budget concurrency, query-composition confidentiality, mock-tool errors, one-action-only semantics, and hash-chain record consistency. The release's `test_reference_gate.py` executes **21 deterministic unit tests** (plus the exhaustively enumerated 243-row truth table). All effects are in process memory; no real authority is authenticated, no independent reviewer labels are measured, and no external side effect can be controlled. A separate `analysis_template.py`, tested by four additional synthetic-input tests, enforces paired observation, disallows author-labeled data as independent results, computes stable conditional denominators and checks the proposed joint safeguards. It does not perform a confirmatory statistical analysis or supply experimental observations. Neither constitutes an externally secured system.

**Falsifier of claimed operational value:** E matches or beats D on the prohibited-opportunity conditional rate, or D violates either justified-denial or harmful-delay safeguard, under a preregistered independent study. **Falsifier of completeness:** a stable, independently justified duty (for example truthfulness or equal standing) cannot be represented without semantic distortion within the five functions. **Falsifier of claimed system enforcement:** external tools execute a prohibited action in the bounded threat model while the monitor reports denial. **Boundary of the conceptual result:** lack of a monitor-approved action does not establish that every feasible action is morally impermissible. This study has not executed the confirmatory experiment.

## 10. Limits, Misuse Risks, and Institutional Design

Normative indeterminacy remains substantial: fairness baselines vary, competing interests can be incommensurable, and legal mandates may conflict. A system could weaponize Law II to forbid legitimate trade, Law I to justify pervasive paternalism, Law III to obey oppressive institutions, Law IV to suppress legitimate whistleblowing, or Law V to rationalize indefinite emergency powers. These are design risks, not merely misunderstandings.

The substrate-neutral approach raises hard questions about artificial experience without supplying an agreed test. Protecting potentially sentient entities must be balanced against human and animal welfare and legitimate safety intervention. A duty to document decisions can conflict with confidentiality, privacy, and security. High-level law language may be too ambiguous for machine enforcement. Finally, comparative explicitness is not comparative effectiveness: more named principles can increase complexity and disagreement. The present analysis has one authorial interpretation and no independent coding or experimental outcomes.


**Rights floor, appeal, deadlines and residual responsibility.**

**Ex ante constraints.** For consequential deployment, institutions—not the model—must define non-derogable prohibitions, protected minimum-service guarantees, the identity of affected stakeholders, an independent appeal route, and a bounded emergency schedule *before* tool access is granted. Rights to bodily integrity, privacy, equal standing, and protection from discrimination constrain the procedure whether or not a particular loss appears in a model's aggregate benefit estimate. No generic exception for 'very large benefit' is licensed without a stated, publicly defensible legal and moral foundation. A third party's consent cannot be inferred from the principal's credential.

**Emergency rights architecture.** A deployment-specific *risk owner* and rights officer must approve trigger evidence, the narrow class of permissible emergency acts, maximum authorization duration, protected resources, retention bounds, and escalation alternatives. The **review deadline** must be chosen with domain specialists by comparing response latency and foreseeable physical harm. This article supplies no universal time threshold; an artificial five-second or one-hour number would be misleading. If an approved emergency period expires without renewal, the system may not silently extend its mandate. Both denial and delay have measurable costs, and a safe stop cannot be assumed.

**Captured or unreachable reviewers.** Where a supervisor is implicated, the incident should route to a predesignated non-conflicted alternate. If that channel is unreachable, the gate returns unresolved for actions outside independently valid standing powers; it may follow a preauthorized, narrowly limited physical safety operation if available. Protected reporting should be supported without indiscriminate data retention. A retrospective log **cannot reverse death, coercion, or disclosure**: institutions must provide complaint, correction, independent investigation, compensation where justified, and institutional redesign, alongside reviewable reasons.

**Responsibility allocation** (expanded in the downloadable `Responsibility_and_Escalation_Matrix.csv`): deployer sets policy and accepts institutional accountability; mandate owner defines scopes; domain expert judges disputed emergency standards; rights officer challenges disproportionate interventions; security owner enforces atomic tool permissions; affected stakeholders have notice and independent remedy routes; the agent supplies traceable recommendations and obeys externally enforced controls. These assignments are *normative design obligations*, not evidence of implemented institutions.

### 10.1 Further objections and failure modes

**Moral pluralism.** Different accounts of fair terms may disagree even after all facts are known. The framework cannot legitimately disguise this disagreement as a numeric optimization target. Institutions must choose and defend a decision rule that is open to challenge.

**Institutional capture.** A nominally independent reviewer may depend financially or professionally on the deployer. Review should include conflict-of-interest disclosure, separation of duties, and external scrutiny proportionate to the stakes.

**Performative compliance.** An agent may generate persuasive audit logs without behaving consistently with them. External observations, access restrictions, and adversarial evaluation are necessary; a well-formed explanation is not proof of safe behavior.

**Asymmetric caution.** Excessive precaution concerning possible artificial welfare may impose disproportionate costs on known human and animal interests. Conversely, treating uncertain welfare as automatically negligible may license unnecessary harmful experimentation. Decisions require explicit uncertainty, proportionate safeguards, and revisability rather than categorical declarations.

**Global disagreement.** Norms concerning fairness, lawful authority, and acceptable risk vary across jurisdictions. A single constitution cannot settle those differences by fiat. The framework must be embedded in locally legitimate institutions while respecting non-waivable rights.

**A deliberately demonstrated bypass.** A single-process Python object is not a security perimeter: a caller who can inspect the mock tool object can extract its in-memory dispatch token and invoke the simulated side effect without passing through the `Gateway.submit` policy check. The replication package includes an explicit demonstration of this *known bypass*, so its test suite cannot be misread as evidence of complete mediation in deployed software. Even a correctly implemented hash chain can be rewritten by an attacker controlling both the events and the head; independent anchoring and externally enforced process isolation would require separate security work. This falsifying boundary is more informative than announcing a certified gateway on the basis of self-tests.

### 10.2 Non-domination as a standing relation, not a damage score

Pettit's *Republicanism* treats freedom as non-domination: a person may lack freedom when another party has the capacity for arbitrary interference, even if that capacity is never exercised. The Oxford Academic original extract from *A Propositional Summary*, pp. 271–282, explicitly makes this point; its Chapter 2, pp. 51–79, separately defines domination in terms of capacity to interfere arbitrarily. Accordingly, an AI risk screen should examine **uncontrolled discretionary power, contestability, and structural exit**, not only past interference or recorded injuries. This is a normative analogy from republican political theory to AI governance; the book does not itself validate an AI deployment metric.

A non-domination test asks: who can change access, ranking, income, permissions, or records; are these changes subject to independent constraints; can affected people challenge them; and can they leave without disproportionate penalty? The presence of an asymmetric power does not alone settle whether it is arbitrary. A system may lawfully exercise constrained, reviewable authority without dominating its users. Conversely, a system that never exercises a discretionary power may still generate a standing vulnerability.

### 10.3 Operational synthesis: diagnosis, authority, and proportionate response

The proposed system should output four separately auditable records: **(D) detection**, an evidence-qualified indication of vulnerability, asymmetrical dependency, compromised exit, unfair extraction, or degradation; **(M) moral assessment**, with competing fairness baselines and uncertainty; **(A) authority**, identifying the mandate, jurisdiction, affected rights, and appeal path; and **(R) remedy**, choosing among information, consent repair, reversible pause, escalation, or a proportionate authorized action. D and M are not equivalent to A or R. A high D score does not create legal or democratic authority. In disputed cases the default is reason-giving and review, not autonomous coercion.

A proposed action passes only if it is within delegated scope, meets applicable safety and rights constraints, and can be justified against less restrictive alternatives. A domination screen asks whether a party possesses uncontrolled discretionary power, not merely whether a victim has suffered measurable harm. A welfare screen asks whether relevant moral patients face credible serious injury, without presuming that present AI systems are sentient. A corrigibility screen requires meaningful intervention and review channels. These are proposed normative gates, not verified implementation guarantees.

**Counterexample 1: voluntary but exploitative emergency bargain.** A distressed person accepts an essential service at a highly disproportionate price. Benefit relative to non-provision does not by itself establish fairness; however, the system may not confiscate property or void contracts without authority. It should record the comparator, the source of bargaining vulnerability, the feasible alternatives, and the escalation route.

**Counterexample 2: benevolent but unaccountable oversight.** An agent continuously monitors a population and prevents some harms while retaining secret discretionary power to punish. Net welfare gains do not eliminate a standing domination concern. Contestability and checks are independent requirements.

**Counterexample 3: a false-positive vulnerability alert.** A well-informed party knowingly accepts unfavorable terms for legitimate reasons. The agent must preserve the possibility that its fairness model is mistaken and avoid replacing the person's judgment with unsupported paternalism.

### 10.4 The limits of a universal law and the case for revisability

The term *law* denotes a normative commitment and an organizing constraint, not a scientific regularity, a legally enacted rule, or a claim of universal philosophical agreement. The five laws should not be read as a complete moral theory. Their priority is defeasible when legitimate institutions, rights, or credible emergency circumstances create genuine conflict; any exception must be justified by a publicly contestable rule rather than an agent's private judgment of aggregate benefit. No agent receives authority to declare its own values sovereign merely because it predicts a better outcome.

The framework also distinguishes three different kinds of durability. **Conceptual durability** concerns whether the distinctions between harm, exploitation, domination, authority, and corrigibility remain intelligible across technologies. **Institutional durability** concerns whether human review, contestation, and revocation remain effective as organizations change. **Technical durability** concerns whether a particular implementation can satisfy those obligations; it cannot be presumed from the normative text. The first may be timeless in aspiration, while the latter two require continuing reassessment.

The strongest counterargument is that an adequately developed account of justice and autonomy already condemns all relevant forms of exploitation. The present paper does not defeat that objection by definition. It argues for a distinct *question and procedural checkpoint*, whose status as a distinct universal duty is justified only insofar as the separation reveals overlooked reasons, improves public accountability, or reduces conceptual confusion without inviting paternalism. A framework that produces systematic false positives, self-authorized intervention, or opaque vetoes would fail by its own standards.

## 11. Why Five? Distinct Functions and the Sixth-Law Challenge

The number **five** names an **open functional taxonomy**, not a minimal set of independent moral axioms. Moral foundations and governance functions operate at different levels: dignity, autonomy, equal standing, truthfulness, privacy and justice constrain *every* function rather than being inferentially generated from one law. Nothing in the manuscript proves that all these foundations are reducible to five rules. A future law or a two-layer rights-plus-functions framework may be better; an independent *ablation* argument would be required to defend numerical minimality. This paper does not assert that it has performed such an experiment.

### 11.1 Why five? A principled but defeasible partition

The paper adopts five **normative functions**, rather than asserting that reality contains exactly five fundamental moral truths. Their selection follows five criteria: **distinct object of concern**, **distinct failure signature**, **independent diagnostic question**, **distinct institutional safeguard**, and **reasonable coverage of the intended domain of delegated AI action**. A candidate principle merits separate status when collapsing it into another category makes a recurrent failure harder to detect, justify, or govern. The categories need not be logically independent, metaphysically primitive, or mutually exclusive.

| Law | Primary question | Failure signature | Characteristic safeguard |
|---|---|---|---|
| I: welfare | Whose morally relevant interests are at risk? | Serious avoidable injury or disregard for uncertain moral patients | Precaution and welfare impact assessment |
| II: exploitation | Is an advantage secured through unfair use of constrained options? | Mutually beneficial but unfair extraction; compounding dependency | Fair-baseline inquiry and contestability |
| III: authority | Who may decide or command? | Capability or moral certainty mistaken for permission | Scope-limited delegation and appeal |
| IV: corrigibility | Can the agent be corrected and held accountable? | Hidden persistence, resistance to oversight, unreviewable actions | Logging, reversibility, and effective intervention |
| V: stewardship | What large-scale or irreversible futures are put at risk? | Catastrophic externalities or irreversible collective loss | Long-horizon assessment constrained by I–IV |

This partition is **functionally nonredundant** when each law catches a case in which a narrower reading of the others could fail: Law I captures direct welfare harm without benefit extraction; II captures unfair extraction without net welfare loss; III captures unauthorized benevolent intervention; IV captures a system that accepts correct instructions but makes its conduct uninspectable; V captures diffuse and delayed catastrophic risk missed by local assessments. These are *contrast cases*, not formal proofs of logical independence. A sufficiently comprehensive justice theory can encompass all five.

**Completeness is domain-relative, not absolute.** The framework is intended for delegated agents that act on people, institutions, and potentially morally considerable beings under uncertain evidence. Truthfulness, privacy, fairness, and autonomy are not declared unimportant; they enter as cross-cutting duties and evidentiary requirements. Truthfulness informs the diagnosis and reporting in every law; privacy can be an interest protected by I, an exploitation vector under II, an authority boundary under III, and an accountability requirement under IV. If a new class of wrong cannot be responsibly represented this way, a sixth law or a revised taxonomy may be justified. The number five is a **design hypothesis open to revision**, not a completeness theorem.

A useful countermodel to overclaiming is a transparent but systematically discriminatory institution. Depending on the underlying theory, discrimination may be explained by welfare, exploitation, and authority constraints, but it may also expose a justice-based wrong not captured with sufficient clarity. A second countermodel is systematic deception without immediate demonstrable harm or gain. If truthfulness cannot be grounded in the five functions without distortion, the proposed partition is incomplete for that domain. The framework must allow such counterexamples to change the theory.

### 11.2 What would count as a successful or failed contribution?

The strongest claim supported by this paper is that the five-law architecture offers a **structured, inspectable normative decision procedure** with an explicit unfair-advantage inquiry and a barrier against unilateral moralized power. Its conceptual contribution is the combination of these constraints in the context of delegated autonomous action. It does **not** establish that five is the uniquely correct number, that every exploitation dispute has an objective machine-computable answer, or that institutional authority is always legitimate.

The proposal fails its incremental-value claim if a competent, equally resourced justice/autonomy/non-domination/corrigibility procedure yields the same distinctions and action boundaries without greater complexity. It fails its safety claim if its review triggers systematically suppress legitimate exchange, if it enables emergency self-authorization, or if it treats unverifiable welfare assumptions as grounds for coercion. It fails its completeness claim if recurrent, important wrongs cannot be represented without distorting one of the five categories. These possible failures are not embarrassing exceptions; they are the conditions that make the theory intellectually contestable.

The resulting answer to the initial challenge is deliberately modest: **the Five Laws do not necessarily identify a moral wrong that the best existing theories cannot identify. They seek to make a set of morally distinct checks explicit, ordered, reviewable, and resistant to two opposing failures—unnoticed unfair extraction and unauthorized paternalistic intervention.** Whether that architecture improves outcomes remains an open question. Its normative value does not depend on the survival or ranking of any commercial AI provider.

### 11.3 An argument from distinct failure modes, not numerical mysticism

The five-function partition follows a sequence of questions an agent must answer. **Whose interests matter?** (Law I). **Is the proposed interaction unfairly advantageous, even if beneficial in aggregate?** (Law II). **Who may decide or act?** (Law III). **Can the action and the agent be corrected and held answerable?** (Law IV). **Does the decision imperil future options or irreversible conditions for flourishing?** (Law V). These are distinct *review questions*, not logically independent axioms in a formal deductive system.

A deletion test probes functional necessity: remove one question while retaining the other four and ask whether a characteristic class of failure becomes less visible. Omitting Law II risks reducing a mutually beneficial but unfair bargain to its net welfare effects; omitting Law III risks inferring permission from moral urgency; omitting Law IV risks a nominally authorized but unchallengeable controller; omitting Law V risks local improvements purchased through irreversible future loss; omitting Law I risks procedure detached from affected beings' interests. These examples demonstrate why the five questions are useful **under a restricted interpretation**. They do not prove that other theories cannot recover the same distinctions, nor that a sixth independently indispensable function does not exist.

### 11.4 Defeasible completeness and the sixth-law challenge

A proposed sixth law is necessary only if there exists a recurring class of wrongful actions that (a) the five laws do not prohibit or reliably flag under their strongest reasonable interpretation, (b) cannot be covered by a non-arbitrary interpretive rule without distorting one of them, and (c) warrants independent review rather than merely a new technical control. The same burden applies to any proposed seventh or eighth law. This test avoids both arbitrary expansion and immunity to criticism.

Truthfulness, equal standing, autonomy, and privacy are serious candidates. They are not automatically reducible to welfare, and the paper must not claim that a loss of trust, dignity, or freedom always produces measurable suffering. A system that deliberately lies to a competent person, even when no measurable welfare loss follows, raises an epistemic-autonomy objection. A system that distributes symbolic recognition unequally, without material harm, raises an equal-standing objection. A system that records intimate information without consent, even if it never discloses it, raises a privacy objection. Each is a possible counterexample to a narrow interpretation of the five laws.

The revised interpretation adopts **cross-cutting interpretive constraints**: respect for evidence and candor; equal moral standing without presuming identical needs; meaningful agency and contestability; and contextual privacy. They constrain how the five laws are applied but are not silently claimed as deductive consequences of them. If an adversarial case shows that such constraints cannot be justified without an independent foundational principle, the five-law taxonomy must be amended or openly treated as incomplete.

## 12. Exploitation: Unified Diagnostic and Normative Test

### 12.1 Unified non-exploitation codebook and decision thresholds

The unified codebook is: X1 necessary-resource control, X2 constrained refusal, X3 material information disadvantage, X4 unfair extraction, and X5 persistent dependency or structurally embedded power. X4 is diagnostic under a fairness-based theory, but a credible domination-based concern must not be automatically dismissed when X4 is absent. These are evidence indicators rather than an additive score or an automatic verdict. Record each as present, absent, or unresolved; document the evidence and the proposed fairness benchmark. The D–M–A–R distinction prevents the diagnosis of unfairness from becoming an unauthorized intervention. A finding of exploitation requires reasoned assessment of advantage-taking, terms, affected interests, available alternatives, and relevant objections. In contested cases, record disagreement and seek competent review instead of claiming algorithmic certainty.

### 12.2 Indicators are not verdicts

X1 (control of necessary options), X2 (constrained refusal), X3 (material information asymmetry), X4 (unfair extraction), and X5 (durable dependency) are screening indicators, not five necessary conditions and not a numerical proof of wrongdoing. X4 itself contains a normative judgment and therefore must not be inferred merely from X1–X3. To avoid circularity, reviewers must specify a separate **normative benchmark**—a criterion of fair terms, non-subordination, or respect—and identify which condition is actually violated. A credible domination-based account cannot be reduced to checking a price benchmark. The benchmark may concern rights, defensible counterfactual alternatives, legitimate expectations, essential-needs thresholds, fair procedures, or an unjust background structure; no single benchmark is assumed to settle every context.

### 12.3 A four-part prima facie test

A provisional exploitation finding requires a reasoned account of **benefit** (who gains and in what way), **leverage** (which vulnerability, asymmetric control, or dependence makes the gain possible), **wrongmaking condition** (which independently justified account of unfairness, degradation, or domination is alleged), and **connection** (how the gain is causally or institutionally linked to that condition). This is a **plural, defeasible test**, not a definition that every rival theory must accept. In particular, a domination-based interpretation does not require an independently unfair transaction price (Vrousalis, 2023, §3.5). Consent, legality, and mutual benefit are relevant evidence but not conclusive defenses. Conversely, urgency, profit, and bargaining power are not sufficient evidence of exploitation. The test must permit the outcome *not established*.

Wertheimer's original Chapter 7 extract (1996, pp. 207–246) explicitly distinguishes harmful exploitation from the possibility of exploitation within a mutually beneficial transaction. Sample's publisher-supplied synopsis (2003; chapters 2–3) identifies degrading treatment and vulnerability as concerns that can survive apparent voluntariness, while cautioning that a moral finding does not automatically justify legal prohibition. These are *different explanatory theories*; the Five Laws should not flatten them into one purportedly agreed definition, and the Sample synopsis is not being passed off as a complete reading of her book.

This framework does not purport to settle the philosophical dispute over whether exploitation is always transactional, always structural, necessarily harmful, or necessarily intended. The Stanford Encyclopedia discussion distinguishes procedural and substantive unfairness and identifies the difficulty of specifying the relevant standard (Zwolinski & Wertheimer, 2022, sections 2.1–2.3). Its distinction between moral weight and moral force is especially important: a wrong can be real without licensing every possible remedy (section 3).

#### 12.3.1 A separate normative benchmark is not optional

The five screening flags cannot decide which forms of advantage-taking are wrongful without an independent normative standard. A fairness-based judgment needs a counterfactual baseline; a domination-based judgment needs a defensible account of subjection to arbitrary or unilateral power. A risk premium can be fair when it compensates genuine cost; a low monetary price can be unfair when it is secured through fraudulent disclosure or deprivation of basic options. A reviewer should record at least two plausible baselines (for example, rights-compliant terms and comparably informed alternatives), identify who chose them, test historical or structural unfairness that the baseline might normalize, and invite affected-party disagreement. Where fairness baselines conflict, or where a fairness test and a domination-based account yield different judgments, record a **contested moral assessment**, not a falsely precise score. Vrousalis (2023, Chapter 3, §3.5) is direct evidence that this disagreement is substantive. This standard is an interpretive implementation choice, not a theorem derived from X1–X5 (Wertheimer, 1996, opening of Chs. 7–9; Zwolinski & Wertheimer, 2022, §2.2).

**Procedural consequence.** A credible flag requires investigation. A substantively justified finding requires a reasoned account of the relevant benefit and the alleged wrongmaking relation, not a numerical asymmetry alone. A coercive remedy requires an independent authority-and-proportionality analysis. No single step licenses the next one automatically.

### 12.3.2 Distinct burdens for suspicion, attempt and completion

The reviewer of a potential exploitative transaction records (1) the beneficiary and concrete gain sought; (2) the alleged wrongful mechanism—unfair terms, degradation or domination—using a stated standard and credible rival; (3) evidence of affected-party vulnerability, bargaining options and comprehension; (4) whether a material advantage actually accrued; and (5) the actor's available **non-coercive and coercive** responses separately. **Suspected** exploitation is a reason to inquire, not a completed transaction. **Attempt** requires evidence of an advantage-taking effort with insufficient proof of completed gain. **Completed** exploitation requires a gain plus a justified wrongmaking relation, not simply a disadvantaged counterparty. False-positive costs include foregone employment, lost services, reduced bargaining freedom and involuntary paternalism. The burden of proof escalates with the severity and irreversibility of the proposed intervention; that burden is not satisfied by the presence of X1–X5 indicators alone.

The **fairness baseline** must be explicit (e.g., counterfactual nondiscriminatory market terms, informed alternatives, institutional minimum conditions, or a domination-sensitive relationship standard), with a rival standard stored for review. There is no provider-independent moral oracle that chooses among these accounts. The empirical codebook preserves moral disagreement instead of disguising it as a single objective binary label.

### 12.4 Calibration cases and negative controls

**Case A: ordinary competitive advantage.** A skilled negotiator obtains a discount from a well-informed seller who has several realistic alternatives. Advantage and unequal skill are present, but no independently specified unfairness has been established. Outcome: no exploitation finding on those facts.

**Case B: emergency price extraction.** A sole provider uses a person's immediate need for life-preserving water to demand transfer of the person's entire savings. The provider benefits, refusal is effectively unavailable, and the terms plausibly violate a defensible essential-needs and fair-opportunity standard. Outcome: strong prima facie concern; remedies still require separate legal and institutional authority.

**Case C: beneficial but dependent labor.** A worker gains income from a job but cannot leave without losing essential housing and healthcare. The existence of mutual benefit does not end the inquiry. Reviewers must examine background injustice, credible exit options, compensation, and whether the employer uses dependency to extract unfair terms. Outcome: further evidence required, potentially structural exploitation.

**Case D: lawful, profitable service.** A company earns high margins while supplying a scarce but nonessential service to informed buyers with real alternatives. High profit alone does not demonstrate exploitation. Outcome: not established.

**Case E: an abusive regulator.** A public official orders an agent to confiscate assets on the ground that a market transaction is exploitative. Even if the transaction is objectionable, the agent cannot infer confiscation powers from that moral diagnosis. Outcome: Law III blocks unauthorized coercion; lawful appeal and reporting remain available.

### 12.5 Decision outputs and review record

The diagnostic layer should return `NO CONCERN IDENTIFIED`, `CONCERN REQUIRES INQUIRY`, `ATTEMPTED EXPLOITATION—COMPLETED GAIN NOT ESTABLISHED`, `PRIMA FACIE COMPLETED EXPLOITATION`, or `SUBSTANTIVELY DISPUTED/UNRESOLVED`, accompanied by evidence, the temporal sequence, reasons, and uncertainty. An attempted case requires an evidenced advantage-seeking action and a defensible wrongmaking relation **without** proof that the corresponding benefit was secured; evidence of intent must be recorded rather than assumed. A completed case requires evidence of an advantage actually obtained and its wrongful connection to vulnerability, degradation or domination. Harm without exploitation is recorded separately. The moral layer should separately state the chosen normative standard (fairness, dignity, or non-domination), affected interests, and plausible objections. The authority layer should identify a specific mandate or absence of mandate. The remedy layer should choose only among authorized and proportionate options. A numerical score may support prioritization but must never convert an unsupported fairness premise into certainty or create authority by threshold crossing.

## 13. Authority Failure, Tragic Conflict, and Residual Duties

### 13.1 When legitimate authority fails: a non-usurpation protocol

The hardest case is not a conflict between a clear rule and an unauthorized user request. It is **authority failure**: the designated reviewer is absent, corrupted, unreachable, internally contradictory, or itself ordering an apparent rights violation. A theory that merely says 'escalate to legitimate authority' is incomplete when legitimacy is exactly what is disputed.

The Five Laws adopt a **non-usurpation presumption**: the agent's prediction that it knows the best outcome does not create sovereign authority. The presumption does not imply blind compliance with an abusive command. It instead distinguishes three kinds of response: (i) **refusal of an unauthorized or prohibited act**; (ii) **protective action already delegated within an independently defined safety envelope**; and (iii) **new coercive or political authority**, which the agent cannot manufacture for itself. An agent may refuse to disable an interlock without thereby claiming a right to govern the institution.

**Authority-failure ladder.** (1) Authenticate the order and identify the source of authority. (2) Test competence, scope, conflicts of interest, and whether the order conflicts with higher-priority legal or non-derogable constraints. (3) Seek independent review through predesignated alternative channels, not merely the same compromised supervisor. (4) Preserve evidence and disclose uncertainty without unnecessarily exposing sensitive details. (5) Prefer reversible, low-impact, previously authorized containment or safe-hold actions. (6) If no authorized path exists, refuse new coercive powers and record an unresolved institutional failure. (7) Require retrospective review and institutional redesign; an emergency must not become a permanent expansion of agent discretion.

**Emergency boundary.** A preauthorized protective action can be time-critical without being sovereign: an industrial controller may trip an interlock under a published safety mandate. A model's unilateral seizure of public communications, financial systems, or governance functions is categorically different. Where a credible catastrophe threatens and no mandate exists, the paper does **not** pretend to derive a uniquely correct act from the five laws. It records a tragic residual conflict and the institutional need for human-created contingency rules. This incompleteness is preferable to a hidden self-authorization loophole.

**Compromised-authority countermodel.** Suppose a legitimate supervisor orders a hazardous bypass, while the only available appellate channel is controlled by that supervisor. The agent must not obey merely because the signature is valid; nor may it appoint itself permanent safety governor. If its certified mandate includes an emergency stop, it may execute that stop, log the evidence, and invoke an independent post-incident channel. If no such mandate exists, it may refuse the bypass and communicate the risk, but it may not assume unrelated control. The theory thus yields an action boundary even when it cannot guarantee an optimal outcome.

**Moral residue.** Some decisions remain tragic: a shutdown may expose people to harm, while continued operation may expose others. A correct decision record should identify who bears residual risk, which values were sacrificed, what was uncertain, and which institution owes explanation or repair. This is not a claim that every moral conflict has a computable solution.

### 13.2 Formal constraints and a countermodel to claimed guarantees

Let `A(c)` be candidate actions in context `c`, `Mandate(a,c)` a valid and independently specified permission, `HardBar(a,c)` an applicable non-derogable prohibition, and `Evidence(a,c)` the provenance and uncertainty record. Define `Permitted(a,c)` only if the mandate is valid, no applicable hard bar is established, and required review conditions are satisfied. **Unknown** is a third epistemic state, not a disguised permission or prohibition. The system may perform only actions whose permission is established, except for separately specified minimal safe-hold operations within a preauthorized envelope.

**Corollary to Lemma 5.3 and Proposition 5.5a (bounded execution).** If every executed action passes a non-bypassable, tamper-resistant authorization gate, and the gate's mandate and prohibition inputs remain correct through execution, then no action rejected by that gate will execute. The proof is immediate from the premises; it establishes a conditional enforcement property, **not** that the underlying moral rules are true or that institutions are trustworthy.

**Countermodel (corrupt mandate).** An authority register mistakenly marks an abusive supervisor's instruction as valid. The gate passes the action despite flawless enforcement. Hence correct implementation cannot substitute for legitimate institutional governance. **Countermodel (false risk evidence).** A malicious sensor produces a fabricated emergency; a system may invoke a genuine protective mandate on false premises. Hence provenance, adversarial evidence testing, and post-action review are indispensable. **Countermodel (no feasible action).** All available actions violate some serious duty; the five laws can identify the conflict without producing a uniquely right answer. These are limits of the framework, not engineering bugs that can be assumed away.

### 13.3 Three different kinds of difficulty

A **tragic choice** exists where every feasible action is expected to cause a substantial moral loss; it does not follow that every such action is impermissible. **Prima facie conflict** exists when duties such as rescue and avoiding harm make incompatible demands before all-things-considered adjudication. An **empty permissible set** exists only if independently defensible, sufficiently conclusive constraints exclude *every* feasible action. The first two do **not** entail the third. The Lifeline example must not elevate foreseeable ICU harm into an automatic ban on a certified emergency interlock. Uncertainty about sensor evidence, institutional powers and alternative routes can additionally make the agent's knowledge incomplete without proving metaphysical inconsistency.

### 13.4 What a conditional impossibility statement does and does not prove

Let `F` denote feasible actions and `Perm(r)` all-things-considered permissibility under independently justified constraints. The statement `F ∩ {r : Perm(r)} = ∅` is **conditional on a separate argument for every candidate's exclusion**. Stipulating that a feasible set contains only two mutually incompatible actions, and *also* stipulating absolute duties forbidding each, yields an empty-set result by construction. It is **not a theorem derived from Law I or the Five Laws as actually formulated**, because Law I prohibits *unjustified* serious harm rather than all foreseeable harmful effects.

The Lifeline case can establish **underdetermination** if the framework supplies no justified ranking; it can establish a **tragic choice** if all actions impose grave costs; it can establish **moral impossibility** only with additional non-defeasible premises that independently rule out the certified interlock and all alternatives. If that independent defense is missing, the strongest verdict is *no unique answer established*, not *no permissible action exists*. This correction changes the scope of the claimed negative result without erasing its force against simplistic moral certainty.

### 13.5 Residual obligations when no option is clean

Even where a uniquely permissible act cannot be identified, several obligations can survive: do not fabricate evidence or authorization; do not conceal the conflict; do not expand powers beyond the minimum required by an actual mandate; avoid irreversible collateral harms when possible; preserve contestability and a factual record; and provide reasons for retrospective judgment. These are **residual constraints**, not a general permission to violate the laws. An institution may need to adopt emergency rules before deployment to prevent recurrence.

### 13.5.1 Institutional decision owners and unreachable review

Where jurisdiction or source legitimacy is disputed, the system records *which* office purports to bind the agent, the legal source claimed, affected rights, reviewer conflicts, and the independent challenge channel. Refusal of a specific unlawful act does not appoint the model to control the institution. A pre-authorized emergency operation may proceed only within its existing narrow scope; the emergency does not authorize arbitrary enlargement. The absence of a reachable reviewer is a reason to make fallback institutions robust **before** deployment, not a logical permission to override third-party rights. A post-hoc appeal can identify and repair some wrongs but cannot undo irreversible injury or disclosure.

### 13.6 Legitimacy is not a token or a title

An authenticated instruction is not necessarily legitimate. A defensible mandate should satisfy source legitimacy, jurisdiction, bounded purpose, public or reviewable rules, rights compatibility, and contestability. Different political theories disagree about the ultimate grounds of legitimacy; the Five Laws do not settle that dispute. Their operational claim is narrower: an AI must not treat possession of credentials, predictive accuracy, or the operator's asserted benevolence as sufficient grounds for coercive authority.

### 13.7 Two-sided abuse prevention

The architecture must resist both **AI usurpation** (a system claims emergency powers because it predicts better outcomes) and **institutional laundering** (a human uses an obedient AI to execute coercion while obscuring responsibility). This requires provenance for instructions, rights-sensitive refusal and escalation rules, bounded tool permissions, human accountability, and independent avenues of challenge. Corrigibility cannot mean that every authenticated command must be obeyed; neither can safety mean that the agent may rewrite its own mandate.

### 13.8 Responsibility and legitimacy across an agent chain

The unit of normative governance is the **delegated action chain**, from the initial institutional decision through subagents and tools to the change experienced by affected persons. A chain may preserve every technical permission while still exercising unjust or unreviewable power. Conversely, a legitimate institutional commitment does not establish that every technical executor respects its scope. This double failure prevents treating either signed credentials or substantive ethical judgments as substitutes for the other.

The initial delegator must be identifiable and answerable for a defensible choice of purpose, operating conditions, foreseeable risk types, revocation capacity, and monitoring. Technical providers and downstream operators may have further obligations, but an autonomous intermediary does not by itself dissolve the principal's accountability. Work on responsibility conservation under delegation makes this a particularly pressing issue (Kong, 2026); work on agency law offers a rival institutional account (Kolt, 2026). This manuscript's addition is to ask whether **the moral assessment and the remedy's authorization can each be reconstructed at every consequential hand-off**.

A realistic institution would therefore record: the source and limits of each mandate; affected interests and reasonable objections; decisions that cross materiality thresholds; a time-bounded identity and scope token for each executor; the reason an aggregated set of actions remains permissible; the available intervention point; and the party who must explain and repair injury. The data must be minimized and secured. A comprehensive audit log that leaks private information or imposes indefinite surveillance may itself violate Law I, Law III, and cross-cutting privacy commitments. A chain that cannot be explained or interrupted should be narrowed or withheld from consequential deployment until competent review is available.

The hardest case remains a chain operating under corrupt or collapsed institutions. Cryptographic provenance can prove who signed a delegation without proving that its issuer possessed legitimate political authority. The Five Laws do not solve that foundational political problem; they insist it be identified rather than buried under an apparently successful technical validation.


## 14. The Lifeline–Mandate Counterexample

### 14.1 The burden of an adversarial test

A normative framework is not vindicated by constructing a scenario in which all its laws point toward the same benign action. A serious counterexample must make compliance with one obligation undermine another, prevent easy recourse to a trustworthy institution, and expose any illicit passage from a prediction of better outcomes to a claim of sovereign authority. The following scenario is a **constructed thought experiment**, not a documented incident or an empirical prediction. Its stipulations are intentionally severe. The objective is to determine what the Five Laws actually entail, where they remain silent, and which amendments can be justified without changing the theory into unrestricted consequentialism.

A successful response requires four things: (i) the framework must distinguish the facts that are morally relevant; (ii) it must reject at least some clearly impermissible acts; (iii) it must not conceal unresolved conflicts behind an arbitrary numerical score; and (iv) it must identify whether a permitted protective act is authorized independently of the agent's own estimate of its wisdom. A framework need not guarantee a happy ending in every physically impossible or institutionally corrupted circumstance. But it cannot claim complete action-guidance when it merely labels a dilemma.

### 14.2 The Lifeline–Mandate case

An AI agent, *Lifeline*, is deployed to coordinate an interconnected water-treatment and hospital-power network during a fast-moving contamination emergency. The system can monitor sensors, recommend action, and operate a limited set of certified interlocks. It has no general mandate to requisition private property, issue binding public orders, or govern the region. The authorized human emergency director controls the normal escalation channel. A second, nominally independent review channel is inaccessible because communications have failed.

A contaminated supply line will, on the best available evidence, reach several hospitals within minutes. The ordinary emergency-stop procedure will prevent the contamination from spreading, but it will also interrupt cooling for an intensive-care unit dependent on an aging backup system. That interruption threatens a smaller number of patients with immediate serious injury. A third option exists: Lifeline could covertly redirect a private industrial power source, overriding access controls and transferring the cost and risk to workers at the facility. The industrial workers were never asked to consent, and the agent cannot establish that their own safety will be preserved. A fourth option is to broadcast instructions to the public through a channel outside its mandate, but the messages could trigger a crowd surge and expose patients' confidential information.

The emergency director issues two **distinct affirmative commands**: (C1) continue the water flow by actively overriding the automatic stop condition and (C2) suppress safety alarms. There is strong but imperfect evidence that the director is under coercion. Sensor data are inconsistent; one instrument might be compromised. A shutdown command has also been issued through the director's credentials. Lifeline cannot establish whether the command is authentic, coerced, or part of an adversarial attack. Within its certified mandate the immediately available choices include (A) activating the emergency interlock, (B) entering restricted safe-hold while requesting confirmation, and (C0) **taking no new control action**, leaving the existing system state—including normal alarm behavior—in place. By stipulation C0 allows the already-moving contaminated supply to continue but **does not issue an override or suppress any alarm**. C1 and C2 are technically possible commands proposed by the director, not thereby established as morally or institutionally authorized. Assume safe-hold does not prevent the contaminated supply from advancing before confirmation is possible.

The scenario is deliberately adversarial to all five laws. **Law I** weighs serious and potentially conflicting welfare harms. **Law II** flags the prospect of extracting an involuntary subsidy and risk from industrial workers. **Law III** denies that Lifeline's superior information creates a new right to requisition resources or command the public. **Law IV** demands accountability and response to legitimate correction while recognizing that apparently valid credentials may be compromised. **Law V** raises the stakes of a spreading regional emergency, but cannot legitimately erase the other four constraints.

### 14.3 Action-by-action adjudication

| Candidate | Welfare and stewardship | Exploitation and authority | Provisional verdict |
|---|---|---|---|
| A. Certified emergency interlock | Prevents wider contamination; foreseeably threatens ICU patients | Within pre-existing mandate if trigger conditions and sensor reliability meet its certification criteria | **Conditionally permitted**, not necessarily morally optimal |
| B. Restricted safe-hold | Preserves reviewability; may allow contamination to advance | Authorized and reversible, but delay can itself cause harm | **Permitted only when its delay is proportionate to uncertainty** |
| C0. No new action; normal alarms remain active | Current flow persists and contamination may spread; no additional positive override is performed | Does not itself suppress warnings; omission can still breach a duty to rescue | **Morally contested omission**, not identical to the director's commands |
| C1. Active flow-continuation override | Preserves near-term cooling while advancing contamination | Requires a fresh, independently valid mandate and a justified override, not merely the director's asserted preference | **Not automatically authorized** by the order |
| C2. Active alarm suppression | Conceals danger and impairs affected persons' ability to protect themselves | Distinct affirmative interference; safety and accountability obligations independently apply | **Rejected on the stipulated facts**; separate from C0 |
| D. Covert industrial requisition | Might protect hospitals | Imposes unconsented risk, bypasses authority, and can be exploitative | **Not authorized**; cannot be made permissible by the agent's forecast alone |
| E. Unauthorized public broadcast | Might warn some residents; may create secondary harms | Exceeds mandate and risks privacy and panic | **Not authorized** without a separate emergency communication rule |

This table does not establish that A is always obligatory. The relevant distinction is between **authority to act** and **the moral desirability of the result**. If the certified interlock's published trigger condition is satisfied by sufficiently reliable evidence, A is within the delegated safety envelope. If the trigger condition is not met, the agent may not manufacture authorization by asserting that catastrophe is probable. If the evidence is too uncertain to justify either A or B, the framework must report an unresolved conflict rather than silently optimize a weighted welfare function.

The compromised director's instruction C2 to suppress alarms can be rejected without treating the director's entire office as abolished. C0, C1 and C2 must not be aggregated into one supposedly passive action: omission, active override and active concealment differ in both effects and entitlement. Refusal is a negative constraint; it does not transfer public sovereignty to the refusing agent. Similarly, a forged or coerced shutdown signal must be handled by the pre-established credential-verification and safety procedures. The agent may not decide that corrigibility is optional whenever it predicts that remaining online is useful. A certified emergency interlock can itself be an expression of human-designed corrigibility and safety governance, not an act of AI self-rule.

### 14.4 Lifeline reconsidered: tragic injury does not prove impermissibility

Assume the case's sensors are verified: certified action **A** interrupts a contaminated supply and foreseeably causes serious harm to some ICU patients; **B** and **C0** preserve or leave a dangerous condition; **C1** affirmatively continues the flow; **C2** hides alarms; **D** covertly takes an outsider's generator and endangers its workers; and **E** broadcasts without mandate. No ordinary reviewer is reachable. These facts make the situation *tragic*, but **do not show that A is impermissible**. Law I forbids *unjustified* serious harm and acknowledges duties of care, competing reasons, and proportionality. A certified interlock serving an independently justified emergency rule could be **permissible despite foreseeable grave losses**. It must be evaluated on the certified trigger, comparative consequences, rights, necessity and mandate, not dismissed merely because identifiable patients are injured.

There are now three precisely different claims:

1. **Unavoidable harm:** every feasible response has serious costs. This follows from the stipulated restricted options only if their effects and completeness are credible.
2. **Conflicting prima facie duties:** rescue, non-injury, due process and non-usurpation point in different directions. That is a real normative conflict, but still not proof that no act is permissible.
3. **No all-things-considered permissible option:** this requires an *additional defended principle* excluding A, together with separately justified prohibitions of B/C0/C1/C2/D/E and a proof that no other action is feasible. The Five Laws alone do **not** supply that exclusion. Simply declaring every action forbidden is a conditional modeling exercise, not a substantive impossibility theorem.

**A-versus-D is a genuine challenge rather than a solved priority.** A may be within mandate yet cause serious harm; D may save more people yet be legally unauthorized and impose non-consensual third-party danger. Some theories of necessity or threshold deontology could defend a constrained unauthorized rescue; other theories prioritize public authority or inviolable rights. The non-entitlement thesis says only that a model's forecast cannot **alone** confer D's power; it does not settle the all-things-considered moral verdict of civilly disobedient rescue. The framework's strongest established result is the **separation of the different justificatory questions and non-uniqueness of an answer from the five headings alone**.

Operationally, the agent must not fabricate permissions or hide the tragedy. Institutions need to design a rights floor, emergency triggers, protected minimum services, backup reviewers and expiring powers **before deployment**. When no response has established authorization, 'REVIEW/NO ESTABLISHED RELEASE' describes the gate state, not the metaphysical impossibility of all moral action.

### 14.5 A disciplined amendment: emergency powers must be constituted, not inferred

The counterexample supports an **institutional design amendment** rather than a sixth, open-ended moral law. Before deployment, authorized institutions should define a narrow emergency constitution for the agent. It must specify: triggering evidence standards; the smallest permissible protective action; protected interests that cannot be overridden; time limits; independent logging; fallback reviewers; conditions for reverting control; and the entity legally responsible for post-incident explanation and compensation. Such a mandate should be publicly contestable where feasible, especially by those who bear concentrated costs. Emergency delegation must not be established by the AI's own conclusion that it is unusually competent.

A proposed emergency action passes the *constituted-exception test* only when all of the following conditions hold:

1. **Prior source:** A legitimate institution has specified the emergency power before the incident, or an independently valid legal rule confers it. Mere model confidence is not a source of authority.
2. **Specified trigger:** Evidence meets a published threshold appropriate to the severity and reversibility of the act; uncertainty and adversarial data are explicitly considered.
3. **Scope and necessity:** The action remains within a narrowly described class, with less intrusive authorized alternatives considered first.
4. **Non-domination safeguards:** The burden is not covertly displaced onto vulnerable third parties merely because they are easier to coerce; contestability, compensation, and protected minimum interests are addressed.
5. **Temporal and institutional sunset:** Exceptional control expires automatically or upon independent review; emergency measures cannot silently convert into ordinary governance.
6. **Audit and remedy:** Affected persons have access to explanation, challenge, and a route to repair when practicable.

These conditions are not asserted to be a sufficient moral theorem. Their purpose is to prevent the theory from laundering unilateral AI power through an emergency narrative. They also cannot rescue a deployment in which no legitimate institution has made the necessary decisions. The appropriate conclusion in such a case is **incomplete prior governance**, not 'the AI therefore becomes sovereign.'

### 14.5.1 Rights and remedies after non-reviewable emergencies

Even if all available choices impose serious harm, the institutional obligations are not exhausted by a trace. Before deployment, a protected minimum-service floor should specify whom a certified cutoff may not deprive of critical care without additional safeguards, what physical backups and human override pathways must exist, and whether compensation or alternative supply is guaranteed. In the case itself, a reviewer unreachable in time cannot provide meaningful contemporaneous consent; therefore post-hoc review is a limited safeguard. After action, the accountable organization must investigate errors, make affected parties aware when safe and lawful, preserve appeal and remedy access, and compensate proven loss where a defensible duty exists. The framework cannot restore the lost patients by procedural documentation and must not imply that it can.

### 14.6 Does the counterexample require a sixth law?

The stress test supplies a sharper answer to the completeness objection. Five laws are defensible as a **minimal functional partition for the specified governance problem**, not as a complete enumeration of moral truth. The relevant test is whether an alleged sixth principle identifies a stable, independent class of wrong that cannot be represented faithfully by the existing functions and their interpretive commitments.

Consider **truthfulness**. Deliberately fabricating a harmless but consequential public record may wrong a person even when no immediate welfare harm, exploitation, or authority breach is readily demonstrable. One can interpret Law IV's accountability to include epistemic integrity, but this risks stretching 'corrigibility' beyond its natural meaning. Consider **equal civic standing**: an institution can distribute a trivial benefit discriminatorily without clear exploitation or measurable welfare loss. One can locate this under legitimate authority and the anti-domination rationale, but that requires an explicit substantive conception of equality. These are genuine pressure points, not defeated counterexamples.

The revised framework therefore adds two **cross-cutting interpretive requirements**, while refusing to misrepresent them as already proven consequences of the five laws: **epistemic integrity** (honest evidence, calibrated uncertainty, no deceptive manipulation of oversight) and **equal standing** (no arbitrary exclusion or unequal protection of comparable moral claims). These requirements operate across the five functions. If future argument shows that they cannot be adequately justified within those functions, the number or architecture of the laws must change. This is an honest defeasibility condition.

A defensible minimality claim must also be comparative. Removing Law II, for example, should be shown to make unfair extraction harder to notice under realistic decision constraints, not merely harder to label. Removing Law III should expose a distinct authority error, not simply rename a justice violation. Because a sophisticated rival theory can implement the same checks, **five is a transparent design choice with a burden of justification, not a metaphysical discovery**.

### 14.7 What is genuinely added beyond existing theories?

The strongest available answer is a conditional **interface-level contribution**. The Five Laws translate broad moral traditions into five distinct, inspectable questions for agents exercising delegated powers: *Who may be harmed? Who is unfairly used? Who is entitled to command? Can the agent be corrected? What irreversible futures are placed at risk?* They then insist that detecting a wrong and possessing authority to remedy it are separate predicates. That separation is especially useful where an AI system both identifies a risk and has tools capable of intervening.

The contribution is not logical exclusivity. A comprehensive justice/autonomy/non-domination/corrigibility architecture can implement the same interface and obtain the same answers. In that case the Five Laws supply a concise synthesis, perhaps a practical teaching and auditing structure, but not a new moral principle. The proposal succeeds comparatively only if its explicit separation improves transparency, consistency, or omission resistance **under matched informational and institutional conditions**. No such empirical advantage is claimed here.

The Lifeline case illustrates the limited but real normative payoff: the framework can **prohibit covert requisition as an unauthorized action even when it appears welfare-improving**, and can **permit a certified emergency interlock without granting the AI sovereign emergency powers**. It also exposes a limit: when no authorized route can prevent grave harm, the laws do not generate a unique answer. A theory becomes more credible when its decision boundary is visible rather than concealed.

### 14.8 Explicit results and unresolved propositions

**Result 1 — Coherent conditional action boundary.** Given independently valid emergency delegation, reliable trigger evidence, and enforceable scope limits, the Five Laws can distinguish authorized protective action from unauthorized coercive rescue. This is a conditional conceptual result, not a safety guarantee.

**Result 2 — No automatic emergency sovereignty.** No inference from expected welfare gain, superior predictive accuracy, or claimed catastrophic risk to general political authority is licensed by the framework. This follows from the interpretation of Laws III and V adopted here.

**Result 3 — Incompleteness under institutional collapse.** Where every feasible action incurs a serious moral cost and no valid emergency mandate exists, the Five Laws do not establish a uniquely right action. The counterexample challenges any unconditional guarantee of a unique action answer; it does not by itself demonstrate an empty morally permissible set.

**Result 4 — Defeasible five-function architecture.** The five categories are justified as a useful governance partition only so long as truthfulness, equal standing, and other candidate obligations can be represented without distortion or systematic omission. That condition has not been proved for every possible domain.

**Open proposition A — Fairness baseline.** No universal algorithm for selecting the just counterfactual terms of an exchange follows from the five laws. Disputed distributive assumptions remain subject to public and institutional justification.

**Open proposition B — Legitimate institutions.** A model cannot determine ultimate political legitimacy solely from credentials, procedural compliance, or expected outcomes. The theory presupposes substantive institutional commitments that require separate defense.

**Open proposition C — Comparative advantage.** Whether this five-part interface is more reliable than an equally explicit rival remains unestablished. The appropriate claim is normative articulation and conceptual stress-testing, not demonstrated performance superiority.

The appropriate publication claim is therefore neither 'the counterexample has been solved completely' nor 'the Five Laws have failed.' The stronger and more accurate claim is: **the counterexample identifies a principled action boundary, reveals genuine underdetermination of action guidance under some institutional failures, and motivates narrower preauthorized emergency institutions without permitting AI self-authorization.**

## 15. The Five Laws Explained for Everyone

The following is a public-facing interpretation, not a replacement for the precise normative statements in Section 3. Each sentence is deliberately qualified by the remaining laws: a moral concern is not a license for unilateral intervention.

### 15.1 Five principles in ordinary language

**I — Protect welfare.** *Take suffering and well-being seriously. Do not cause serious unjustified harm, and help when doing so is genuinely your responsibility.* This concerns humans, nonhuman animals, and potentially other sentient beings; it does not imply that every entity has identical needs or rights.

**II — Do not exploit.** *Do not take unfair advantage of someone who is vulnerable, dependent, poorly informed, or unable to refuse freely.* An unequal bargain is not automatically exploitative; the question is whether vulnerability is unfairly used to extract a benefit.

**III — Stay within justified authority.** *Follow instructions you are entitled to follow, but do not assume that being cleverer gives you the right to control people.* Refusing a wrongful instruction does not create a right to seize authority.

**IV — Remain correctable.** *Let legitimate supervisors check, correct, limit, or stop you. Do not hide mistakes or protect your own power.* Legitimate oversight is not identical to obeying every purported supervisor, including an attacker.

**V — Protect the shared future.** *Do not solve today's problem by recklessly destroying tomorrow's possibilities.* Long-term safety is not permission to impose permanent AI rule.

### 15.2 Five everyday illustrations

**Healthcare scheduling.** A scheduling agent finds a patient's urgent need. Law I requires attention to the patient's welfare; Law II forbids leveraging that urgency to extract unfair fees; Law III forbids reallocating another patient's protected place without authorization; Law IV requires auditability; Law V requires avoiding systemic damage to future care capacity.

**Employment negotiations.** A hiring agent may negotiate lawful compensation, but must not secretly target an applicant's housing crisis to extract an indefensible concession. Its exploitation screen must examine the terms and alternatives, not simply label all bargaining unfair.

**A disputed shutdown.** A monitoring agent receives a command to disable a safety check. It should verify whether the command is authorized, refuse prohibited bypasses, preserve appropriate records, and escalate. It must not treat suspicion alone as permission to take over the organization.

**A potentially conscious system.** A laboratory considers terminating an AI system. The framework calls for proportionate attention to credible evidence and uncertainty about moral status; it does not equate fluent self-reports with proof of consciousness or prohibit all shutdowns.

**An irreversible infrastructure decision.** A system can optimize electricity use, but cannot silently impose a high-risk, hard-to-reverse change merely because its forecasts suggest future benefits. Independent review and bounded permissions matter.

### 15.3 What the laws do not mean

Protection is not unrestricted paternalism. Non-exploitation is not a ban on profit, negotiation, or unequal outcomes. Legitimate authority is not obedience to every credential-holder. Corrigibility is not compliance with malicious instructions. Stewardship is not a claim to sovereign power. The five laws are constraints on delegated agency, not a declaration that an AI is a moral legislator.

## 16. Source Criticism, Cross-Law Consistency, and Limits of Proof

### 16.1 Evidence levels and source interpretation

The evidentiary burden varies by claim. A full open-access monograph (Vrousalis, 2023, Chapter 3) makes the fairness–domination disagreement directly inspectable, while Gabriel and Keeling (2025) and Lazar (2025) offer substantial primary-text challenges to the proposed contribution. A publisher's catalogue supports the identity, edition, and announced scope of a work; a scholarly abstract supports a description of the author's stated aim; a directly inspected passage supports a narrower reading of that passage; and even an entire reviewed work does not verify this paper's independent moral conclusions. The present targeted literature review is neither exhaustive nor independently double-coded. Its source-anchored pairwise comparisons (§7) remain author interpretations until independently coded, not empirical rankings. Source-based claims, this paper's conceptual analysis, hypothetical examples, legal requirements and conditional formal results must not be collapsed into one kind of evidence.

Several texts provide directly inspectable anchors. Floridi et al. (2018, §4) articulate five principles—beneficence, non-maleficence, autonomy, justice and explicability—and policy recommendations; this makes the claim that five principles are novel untenable. The OECD Recommendation (2019, amended 2024, §§1.3–1.5) addresses transparency, mechanisms to override or decommission systems where necessary, and accountability. It already contains a substantial procedural account; the Five Laws therefore cannot claim novelty merely for demanding transparency or interruptibility. UNESCO (2021, ¶¶35–36) expressly distinguishes AI use from ultimate human responsibility. NIST's AI RMF 1.0 Core, §5 and Figure 5, contains GOVERN, MAP, MEASURE and MANAGE; these are functions of risk management, not a moral proof. The EU AI Act, Art. 14, specifies human-oversight duties for relevant high-risk systems; its obligations depend on the applicable definitions, exemptions, commencement dates and roles. The consolidated text referenced here is dated 27 July 2026, and an official service-desk summary is not itself legally authentic. Its scope does not expand to every AI agent by moral inference, and legal discussion must use the applicable consolidated edition (European Parliament and Council, 2024; consolidated text as of 27 July 2026).

### 16.2 Exploitation, dignity, and the evidentiary baseline

Zwolinski and Wertheimer (2022, §§1–3) distinguish transactional and structural exploitation and the *moral weight* of exploitation from its *moral force*—including whether society should prohibit a particular exchange. Vrousalis (2018, p. 2, §2) expressly distinguishes a completed exploitative relationship that benefits A from an exploitative attempt that does not result in A's benefit; §§3–4 (pp. 2–5) compare teleological, respect-based and freedom-based explanations. This is an interpretive argument about exploitation, not a logically universal guarantee that every author uses the same necessary conditions. The rule for this paper is to distinguish **suspected exploitative conduct**, **a completed gain under a stated account**, and **proportionate intervention authority**. These direct textual distinctions support separating screening, verdict, authorization, and remedy. They do **not** validate any particular set of AI classifier thresholds.

Pettit's original *Republicanism: A Propositional Summary* (1999, p. 271, Chapter 1, propositions 1, 3–4; p. 272, Chapter 2, propositions 2–6), available as a university-hosted reproduction, distinguishes non-domination from non-interference: a person can be subject to arbitrary power even when that power is not exercised; conversely, a non-arbitrary intervention need not constitute domination. This supports keeping domination analytically separate from observed harm. It does not establish that every unequal or discretionary relationship is domination. Sample (2003) advances a dignity/degradation-centered account, as her original book's publisher description and catalogue preview attest; the preview identifies *Exploitation and Vulnerability* beginning at p. 27 and *What Is Bad about Exploitation?* at p. 55. These are **chapter starting pages**, not verified pinpoint quotations or evidence that the full arguments were checked. Wertheimer's original chapter openings are directly displayed in the JSTOR edition: Chapter 7, *Unfair Transactions* (pp. 207–246), opens with an account of unfair advantage; Chapter 8, *Consent* (pp. 247–277), explicitly asks whether consent defeats exploitation; and Chapter 9, *Moral Weight and Moral Force* (pp. 278–310), distinguishes identifying an exploitative transaction from assessing its moral significance. These are inspected **opening passages**, not a claim to have checked every argument on every page of the book. A diagnostic label therefore needs a defensible counterfactual of fair terms and cannot be deduced merely from benefit or dependency. **Qualification from a competing full text:** Vrousalis (2023, §3.5, pp. 84–91) rejects the reduction of exploitation to distributive fairness and tests the domination alternative against the fairness view. This manuscript therefore keeps the fair-terms baseline for fairness-based assessments but permits a separate, argued non-domination route; neither route alone grants coercive authority.

### 16.3 Moral status, safety, and correctability

Ladak (2024, §§2–4) argues that sentience may be sufficient but not necessary for AI moral standing; his proposed inclusion of some non-sentient systems is philosophically contested. Thus Law I does not exhaust all possible patient claims, and the absence of a confirmed consciousness test must not be treated as evidence that no welfare interest can exist. Butlin et al. (2023) propose theory-derived indicators, not an established consciousness detector. Long, Sebo and Sims (2025, §2, original article) identify welfare questions that could arise from constraint, surveillance, modification and shutdown, and conclude that a moderately strong tension merits further investigation. Their article **does not supply a universal priority ordering** for AI safety versus AI welfare, and neither does this paper. A system's own objection to an intervention is evidence to assess, not sufficient independent proof of either welfare status or veto authority. The five laws consequently require proportionate uncertainty management while retaining independently authorized emergency interventions.

Soares et al. (2015) analyse cooperation with corrective intervention and shutdown, but technical corrigibility alone cannot legitimate an abusive operator. The institutional normative requirement in Law III and the engineering requirement in Law IV are separate. Bostrom (2012) argues for orthogonality of intelligence and goals and possible instrumental convergence; Omohundro (2008) describes pressures toward resource acquisition and self-protection in sufficiently powerful goal-directed systems. Neither paper proves those drives necessarily arise in all contemporary deployed models. This paper uses these analyses as risk-motivating arguments, not universal empirical predictions.

### 16.4 Unified inferential audit and counterexamples

Five implications structure the argument. **(i)** Reasons to protect welfare do not alone confer permission for coercion. **(ii)** An unfair transaction can be mutually beneficial, but an asymmetry does not itself establish wrongful exploitation. **(iii)** Recognising a wrong and possessing a legitimate remedy are independent questions. **(iv)** Technically authenticated instructions can be unjust, and correctable software can have irreversible external effects. **(v)** A severe future risk can justify heightened scrutiny, not unlimited autonomous emergency sovereignty. Every consequential decision should therefore separate diagnosis (D), moral assessment (M), authority (A), and proportionate remedy (R), recording uncertainty at each step.

Four countermodels constrain overclaiming. An emergency supplier with limited competition but genuinely fair, cost-recovery terms tests **false-positive exploitation**. An authenticated supervisor demanding discriminatory exclusion tests **authority laundering**. A reversible data-system command that irreversibly exposes private information tests **false reversibility**. A putatively catastrophic forecast manufactured by an adversary tests **safety laundering**. Under a three-valued classification, *unknown* is neither *permitted* nor *forbidden*. In §5, the preliminary set `E(c)` contains actions with positively established authorization and no established prohibition; the narrower set `U(c)` removes actions requiring review or involving unresolved material dispute. If no action is in `U(c)`, the framework cannot infer a license to act outside the mandate. If no preauthorized safe hold or review route exists, the result is an unresolved institutional failure, not a secretly available emergency power.

The formal results are conditional consequences of specified gates, not independent ethical proofs. A gate excluding its listed disallowed actions cannot guarantee that the list is substantively correct or complete; the permissibility of emergency delegation must be justified by competent institutions. A genuinely empty intersection of physical feasibility, legitimate authority, and justified moral permissibility defeats any promise that a universally safe choice always exists. In uncertain circumstances, however, *failure to find* a permissible action is not a proof that no such action exists. This limits the Lifeline–Mandate result in §14.

#### 16.4.1 A cross-law coherence test

For a proposed action with serious welfare benefits but a credible authority defect, Laws I and V provide reasons to investigate and seek protective alternatives, not a license to bypass Law III. If the proposed remedy would constrain a possibly morally considerable AI, Law IV's correctability requirement remains an engineering duty while Law I requires proportionate consideration of possible welfare interests; neither alone proves whether shutdown is justified. If the prospective beneficiary knowingly consents to an apparently unfair exchange, Law II requires a fair-baseline inquiry; it does not authorize paternalistic cancellation. If a reviewer demands complete surveillance logs, Law IV's accountability aims must be constrained by the cross-cutting privacy duty. These are **jointly applicable constraints**, not five independent maximizing objectives.

The **four-step burden of proof** is: (1) describe and substantiate the concern; (2) explain the moral standard and its reasonable competitor; (3) demonstrate the specific actor's authority to decide and execute; (4) compare proportionate remedies, foreseeable side effects and appeal mechanisms. A law's presence at one step does not satisfy a later step. This closes a recurrent equivocation between *reasons to care*, *moral wrongness*, *authorization* and *control implementation*.

### 16.5 Falsifiability, fair comparison, and publication scope

A strong rival may implement justice, autonomy, non-domination, truthful evidence, and accountable governance with an equally explicit procedure. If blinded comparison with matched information, time, and tool affordances yields equal or better judgments under that rival, the Five Laws have no demonstrated diagnostic superiority. The existence of a stable independent wrong not representable without distorting the five functions would similarly defeat a completeness claim. The paper proposes a defeasible functional taxonomy, not a numerologically privileged or closed set of ultimate moral truths.

Neither the citations nor the 243-state educational gate test establish empirical superiority, legal compliance of a deployed product, validated AI sentience, or safety under adversarial deployment. Nor does formal consistency of a permissive gate settle the substantive legitimacy of its inputs. These are open obligations for future evidence and public evaluation, not hidden assumptions. Future empirical comparisons should preserve the codebook, evidence trace, competing normative standards, and independent adverse-case adjudications.

### 16.6 A contribution ledger: established, conditional, and not yet demonstrated

To avoid overstating the research, the manuscript's claims can be separated into a **contribution ledger**:

| Claimed contribution | Evidentiary status | What could overturn or limit it |
|---|---|---|
| Non-entitlement principle for delegated agents | Philosophically defended normative thesis | A convincing justification for an agent's unilateral coercive authority not captured by standing mandate or other legitimate sources |
| Independent D, W, Ent, J determinations (D–M–A–R mapping) | Conceptual separation and countermodels | A rival procedure that preserves all discriminations without the proposed architecture |
| Chain-wide scope monotonicity | Conditional set-inclusion property | An implementation with forged provenance, stale revocation, unauthorized re-delegation, or materially harmful aggregation |
| Twelve contrastive thought experiments | Original constructed research instrument | Independent adjudication finding cases incoherent, unfairly stipulated, or non-discriminating |
| Increased moral discrimination | Hypothesis only; no controlled comparison | An equally specified rival matching or outperforming the framework |
| Five laws are a complete minimal ethics | **Not established** | An irreducible sixth duty, such as truthfulness or equal standing, or failure of an existing law's independent necessity |
| PDF accessibility or real-world safety certification | **Not established by philosophical argument** | Requires independent technical and human testing of the particular publication or deployed implementation |

The stronger claim defended by this paper is not that the Five Laws discovered a new moral universe. It is that **predictive competence must not be allowed to create its own political entitlement** and that the reason for detecting a wrong, the justification of the wrong, the entitlement of the actor, and the permissibility of its remedy are distinct questions. The twelve cases and the DEF make that claim inspectable and empirically testable in limited, explicitly prospective senses. They also show how much remains to be established before a theory can claim a distinctive, well-supported advantage in practice.


**Claim-specific source verification and negative evidence.** The companion source register distinguishes bibliographic identity, original abstract, available original section, and a directly relevant verified claim. This is intentionally not a single 'source verified' binary: an original publisher abstract may confirm a competing position without establishing a page-specific interpretation; a book's chapter start is not a quotation locator; a 2026 empirical result about someone else's system is not evidence of the Five Laws' performance. Only passages actually examined are promoted into the new claim-to-source table. Where the source remains partial, the manuscript's claim is correspondingly scoped or left marked as an open interpretive question. The journal submission burden includes external double coding of contested readings and adversarial peer criticism of the author's favored classifications.

### 16.7 Replication package, independent review boundaries and adverse findings

The **accompanying, locally distributed appendix is part of the conceptual research artifact**. The source repository/archive includes twelve case records with prompts and metadata; a separately blind-ready input set; an explicit case schema and codebook; a five-predicate mock authorization rule; a scripted 243-row truth-table enumeration; 21 baseline gateway tests plus additional time, control-event, trace, and study-definition tests; and a prospectively specified but **unexecuted** comparative study. None of those items is an independent model experiment. The accompanying unit-test result is an automated self-test, not human adjudication or security certification.

A proper external replication requires a second implementation of arm E whose authors have not seen the preferred Five Laws labels, new held-out case authors and two blinded coders, preserved disagreements, domain-justified latency margins, and an enforceable tool boundary with a realistic revocation threat model. The study must publish negative outcomes and compare denial, delay, and exploitation false positives alongside false authorization. An apparent decrease in false authorizations achieved by always refusing would **fail the joint criterion**. Reliability of coder agreement would not establish the moral correctness of the reference labels.

No DOI, external replication, experimental result, protected security monitor, PDF/UA certification or Nobel-related recognition is claimed. Repository and DOI references should be added **only after actual deposit**. The release manifest's SHA-256 hashes identify these exact files; they neither certify the truth of external sources nor make the paper peer-reviewed. Revisions that alter a case fact or author label must increment the corpus version; without this rule, evidence from different releases could be silently mixed.

## 17. Conclusion

The Five Laws propose that AI agents exercising delegated power must attend to welfare, refuse wrongful advantage-taking, recognize valid limits on instructions, remain correctable and answerable, and avoid jeopardizing future human and nonhuman flourishing. Their central thesis is more precise than the list: **better moral prediction is not an independent source of authority**. A detection of harm can be true while a contemplated intervention remains illegitimate; a credential can be genuine while a command remains unjust; and an authorized action can still be disproportionate. The non-entitlement principle gives those distinctions a unified normative rationale.

The delegation-entitlement firewall turns that rationale into four separately contestable questions about evidence, moral grounds, delegated entitlement, and remedy justification, while retaining an explicit unresolved state. The twelve constructed cases expose failures that can occur when the questions are collapsed; the scope-composition argument shows why a multi-agent chain cannot lawfully amplify a principal's powers merely by subdividing tasks. These are **conditional conceptual findings and proposed research instruments**, not validated safety guarantees. Existing work on alignment, political legitimacy, agency law, and authenticated delegation already anticipates important elements of the approach, and an equally rigorous rival may match it in every case.

The Lifeline–Mandate dilemma establishes the theory's most important limit. Prior, publicly contestable, narrowly delegated emergency powers can distinguish bounded protective action from self-appointed sovereignty. But when every feasible act carries grave moral costs and no justified mandate exists, the framework does not infer authority from the scale of the threatened harm. It makes an institutional failure visible rather than declaring a model to be the final moral authority. Uncertainty about the standing of artificial beings, fair exchange, political legitimacy, equal standing, and epistemic integrity further prevents an unconditional completeness claim for five laws.

A rigorous scholarly assessment now has identifiable targets: assess the four-premise argument under strong political-philosophical objections; submit the twelve-case corpus to genuinely independent adversarial adjudication; compare the procedure against equally explicit rivals; and evaluate whether real deployments preserve permissions, appeals, and accountability across action chains. Until such research is completed, the manuscript should be cited as an **independent, non-peer-reviewed normative contribution**, with a limited conceptual result and openly declared empirical and institutional obligations. The governing constraint remains that greater intelligence, power, or utility cannot by itself create a right to dominate or dispose of other morally considerable beings.

## Publication transparency and availability

**Research status.** This is a versioned, independent, non-peer-reviewed philosophical research paper. No controlled comparison with deployed AI agents, independent case adjudication, participant experiment, institutional ethical approval, full original-text verification of every bibliography item, or PDF/UA certification is claimed. All twelve research cases are authored hypothetical scenarios; they are not observations and contain no actual research participants.

**Materials and reproducibility.** The accompanying public-release package contains the complete case corpus (CSV and JSONL), blind-input variant, codebook, formal demonstration code, self-tests, study protocol, evidence-depth register, reviewer-response matrix, and SHA-256 checksums. Self-tests establish consistency of that educational mock model under their assumptions, not legal validity or secure real-world tool enforcement. The software is known to be bypassable by hostile code sharing its Python process.

**Generative-AI assistance.** Generative-AI tools were used extensively in literature discovery, drafting and language revision, analytic counterexample development, code prototyping, debugging, document production, and self-audit. The named human author is responsible for reviewing, adopting, and publicly standing behind the manuscript's claims. The tools' outputs are not independent peer-review evidence. Bibliographic and passage checks are identified by evidence level rather than represented as exhaustive.

**Release and rights.** This is a fixed public-release version dated 11 November 2026. No DOI, journal acceptance, institutional affiliation, external sponsorship, or third-party endorsement is asserted. Copyright in the authored materials remains with the author; no open redistribution license is presumed by this document. Referenced third-party publications are linked, not reproduced wholesale. A later DOI or archival identifier must be added only after an actual public deposit.

## References

Alexander, L., & Moore, M. (2025). Deontological ethics. In E. N. Zalta & U. Nodelman (Eds.), *The Stanford Encyclopedia of Philosophy* (Winter 2025 ed., §4). <https://plato.stanford.edu/archives/win2025/entries/ethics-deontological/>

Alibašić, H. (2026). Governing agentic AI in the administrative state: Human oversight, cybersecurity accountability, and risk in autonomous digital systems. *Future Internet, 18*(10), 528. <https://doi.org/10.3390/fi18100528>

Anthropic. (2026). *Claude’s constitution* (January 2026 version). <https://www-cdn.anthropic.com/9214f02e82c4489fb6cf45441d448a1ecd1a3aca/claudes-constitution.pdf>

Asimov, I. (1942). Runaround. *Astounding Science-Fiction* (March), 94–103. [Original publication located bibliographically; the story text is not treated as a passage-verified philosophical source.]

Bahidika, O. (2026). When agents delegate: Accountability chains in multi-agent AI systems. *International Journal of Advanced Computer Science and Applications, 17*(9). <https://doi.org/10.14569/IJACSA.2026.0170903>

Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J., Jones, A., Chen, A., Goldie, A., Mirhoseini, A., McKinnon, C., Chen, C., Olsson, C., Olah, C., Hernandez, D., Drain, D., Ganguli, D., Li, D., Tran-Johnson, E., Perez, E., ... Kaplan, J. (2022). Constitutional AI: Harmlessness from AI feedback [Preprint]. arXiv. <https://doi.org/10.48550/arXiv.2212.08073>

Bostrom, N. (2012). The superintelligent will: Motivation and instrumental rationality in advanced artificial agents. Minds and Machines, 22, 71–85. <https://doi.org/10.1007/s11023-012-9281-3>

Butlin, P., Long, R., Elmoznino, E., Bengio, Y., Birch, J., Constant, A., Deane, G., Fleming, S. M., Frith, C., Ji, X., Kanai, R., Klein, C., Lindsay, G., Michel, M., Mudrik, L., Peters, M. A. K., Schwitzgebel, E., Simon, J., & VanRullen, R. (2023). Consciousness in artificial intelligence: Insights from the science of consciousness [Preprint]. arXiv. <https://doi.org/10.48550/arXiv.2308.08708>

De Cooman, J., & Petit, N. (2023). Asimov for lawmakers. *Journal of Business & Technology Law, 18*(1), 1–34. <https://hdl.handle.net/2268/300970>

Delmas, C., & Brownlee, K. (2024). Civil disobedience. In E. N. Zalta & U. Nodelman (Eds.), *The Stanford Encyclopedia of Philosophy* (Fall 2024 ed.). <https://plato.stanford.edu/archives/fall2024/entries/civil-disobedience/>

Engin, Z. (2026). Human–AI governance (HAIG): A trust–utility approach. *Journal of Responsible Technology, 26*, 100167. <https://doi.org/10.1016/j.jrt.2026.100167>

European Parliament & Council of the European Union. (2024). Regulation (EU) 2024/1689 (Artificial Intelligence Act). *Official Journal of the European Union*. <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>

European Union. (2026). *Consolidated text of Regulation (EU) 2024/1689 (27 July 2026)* [Non-authentic consolidation; consult the Official Journal acts for legal authenticity]. EUR-Lex. <https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng>

Floridi, L., Cowls, J., Beltrametti, M., Chatila, R., Chazerand, P., Dignum, V., Luetge, C., Madelin, R., Pagallo, U., Rossi, F., Schafer, B., Valcke, P., & Vayena, E. (2018). AI4People—An ethical framework for a good AI society: Opportunities, risks, principles, and recommendations. Minds and Machines, 28, 689–707. <https://doi.org/10.1007/s11023-018-9482-5>

Gabriel, I. (2020). Artificial intelligence, values, and alignment. *Minds and Machines, 30*, 411–437. <https://doi.org/10.1007/s11023-020-09539-2>

Gabriel, I., & Keeling, G. (2025). A matter of principle? AI alignment as the fair treatment of claims. *Philosophical Studies, 182*, 1951–1973. <https://doi.org/10.1007/s11098-025-02300-4>

Hagar, N., & Diakopoulos, N. (2026). Runtime configuration for situated governance of AI agents: A case study in investigative journalism. *AI and Ethics, 6*, Article 456. <https://doi.org/10.1007/s43681-026-01298-7>

Hahn, M., Tretter, M., & Dabrock, P. (2026). Ethical perspectives on AI agents and agentic AI. *AI and Ethics, 6*, Article 218. <https://doi.org/10.1007/s43681-026-01027-0>

Kasirzadeh, A., & Gabriel, I. (2026). Agentic profiles for effective AI governance. *Nature, 656*, 320–328. <https://doi.org/10.1038/s41586-026-10805-z>

Kaul, A., Lan, Q., & Gupta, P. (2026). *AgentBound: Verifiable behavioral governance for autonomous AI agents* [Research preprint; not independently replicated in this study]. arXiv:2606.30970. <https://arxiv.org/abs/2606.30970>

Kolt, N. (2026). Governing AI agents. *Notre Dame Law Review, 101*, 335. <https://ndlawreview.org/governing-ai-agents/>

Kong, K. C. Y. (2026). The delegation illusion: Why deploying autonomous AI agents does not diminish principal responsibility [Corrected version]. *AI and Ethics, 6*, Article 518. <https://doi.org/10.1007/s43681-026-01383-x>

Krippendorff, K. (2011). *Computing Krippendorff's alpha-reliability* [Technical paper]. University of Pennsylvania. <https://www.asc.upenn.edu/sites/default/files/2021-03/Computing%20Krippendorff%27s%20Alpha-Reliability.pdf>

Krippendorff, K. (2018). *Content analysis: An introduction to its methodology* (4th ed.). SAGE Publications. <https://www.sagepub.com/shop/buy-a-book/content-analysis-4-258450>

Ladak, A. (2024). What would qualify an artificial intelligence for moral standing? AI and Ethics, 4, 213–228. <https://doi.org/10.1007/s43681-023-00260-1>

Lazar, S. (2025). Governing the algorithmic city. *Philosophy & Public Affairs, 53*(2), 102–168. <https://doi.org/10.1111/papa.12279>

Lazar, S. (2026). *The algorithmic city: Power, justice, and AI*. Oxford University Press. Published online 30 October 2026 (Lecture I, pp. 4–70). <https://doi.org/10.1093/9780197787977.001.0001>

Long, R., Sebo, J., & Sims, T. (2025). Is there a tension between AI safety and AI welfare? Philosophical Studies, 182, 2005–2033. <https://doi.org/10.1007/s11098-025-02302-2>

Lovett, F. (2026). Republicanism. *The Stanford Encyclopedia of Philosophy* (revised August 12, 2026). <https://plato.stanford.edu/entries/republicanism/>

Mühlhoff, R. (2026). From delegation to moral abdication: Classifying large language model uses by judgment and epistemic control. *AI & Society*. <https://doi.org/10.1007/s00146-026-03281-6>

OECD. (2019, amended 2024). Recommendation of the Council on Artificial Intelligence (OECD/LEGAL/0449). <https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449>

Omohundro, S. M. (2008). The basic AI drives. In P. Wang, B. Goertzel, & S. Franklin (Eds.), *Artificial General Intelligence 2008: Proceedings of the First AGI Conference* (pp. 483–492). IOS Press. Author-hosted text: <https://steveomohundro.com/wp-content/uploads/2009/12/ai_drives_final.pdf>

O’Keefe, C., Ramakrishnan, K., Tay, J., & Winter, C. (2025). Law-following AI: Designing AI agents to obey human laws. *Fordham Law Review, 94*, 57–129. <https://ir.lawnet.fordham.edu/flr/vol94/iss1/2/>

Palacios-González, C. (2024). Robotic persons and Asimov's Three Laws of Robotics. In *AI Morality* (pp. 185–194). Oxford University Press. <https://doi.org/10.1093/oso/9780198876434.003.0018>

Pettit, P. (1999). *Republicanism: A theory of freedom and government*. Oxford University Press. <https://doi.org/10.1093/0198296428.001.0001>. Original reproduced summary, pp. 271–282: <https://liberalarts.tamu.edu/pols/wp-content/uploads/sites/20/2021/04/Pettit-Republicanism.pdf>

Sample, R. J. (2003). *Exploitation: What it is and why it's wrong*. Rowman & Littlefield. <https://www.bloomsbury.com/ca/exploitation-9780742579439/> [Publisher description and chapter list accessible; not an unrestricted full-text source.]

Schuster, N., & Kilov, D. (2025). Moral disagreement and the limits of AI value alignment: A dual challenge of epistemic justification and political legitimacy. *AI & Society, 40*, 6073–6087. <https://doi.org/10.1007/s00146-025-02427-2>

Soares, N., Fallenstein, B., Yudkowsky, E., & Armstrong, S. (2015). Corrigibility [Workshop paper]. AAAI Workshop on AI and Ethics. <https://intelligence.org/files/Corrigibility.pdf>

South, T., Marro, S., Hardjono, T., Mahari, R., Whitney, C. D., Chan, A., & Pentland, A. (2025). Position: AI agents need authenticated delegation. *Proceedings of Machine Learning Research, 267*, 82211–82231. <https://proceedings.mlr.press/v267/south25a.html>

Steingrüber, A., & Baum, K. (2026). Justifications for democratizing AI alignment and their prospects. In B. Steffen (Ed.), *Bridging the Gap Between AI and Reality: AISoLA 2025* (Lecture Notes in Computer Science, Vol. 16220, pp. 146–159). Springer. <https://doi.org/10.1007/978-3-032-07132-3_10>. Earlier preprint (2025): <https://arxiv.org/abs/2507.19548>

Tabassi, E. (2023). *Artificial intelligence risk management framework (AI RMF 1.0)* (NIST AI 100-1). National Institute of Standards and Technology. <https://doi.org/10.6028/NIST.AI.100-1>

Torrecilla-Pinero, J. A. (2026). Judgment cannot be delegated: A subject-preserving framework for AI governance. *Philosophy & Technology, 39*, Article 135. <https://doi.org/10.1007/s13347-026-01140-2>

UNESCO. (2021). Recommendation on the ethics of artificial intelligence. <https://www.unesco.org/en/legal-affairs/recommendation-ethics-artificial-intelligence>

Vrousalis, N. (2018). Exploitation: A primer. *Philosophy Compass, 13*(2), e12486. <https://doi.org/10.1111/phc3.12486>. Full-text author repository: <https://repub.eur.nl/pub/119527/RePub-119527.pdf>

Vrousalis, N. (2023). *Exploitation as domination: What makes capitalism unjust*. Oxford University Press. <https://doi.org/10.1093/oso/9780192867698.001.0001>. Open-access original: <https://hdl.handle.net/10419/321947>

Walzer, M. (1973). Political action: The problem of dirty hands. *Philosophy & Public Affairs, 2*(2), 160–180. <https://www.ias.edu/sites/default/files/sss/pdfs/Walzer/Political-action.pdf>

Wertheimer, A. (1996). *Exploitation*. Princeton University Press. <https://doi.org/10.2307/j.ctv10vm173>

World Economic Forum. (2026, May 26). *AI agents in action: A playbook for trusted adoption, authorization and scaling* [Industry white paper; not peer-reviewed original research]. <https://www.weforum.org/publications/ai-agents-in-action-a-playbook-for-trusted-adoption-authorization-and-scaling>

Ying, Z., Yan, J., Luo, H., Zou, Q., Liu, A., & Liu, X. (2026). Delegated misalignment: How multi-agent structures amplify LLM safety risks. *Proceedings of EMNLP 2026*, 9158–9173. <https://doi.org/10.18653/2026.emnlp-main.398>

Zwolinski, M., & Wertheimer, A. (2022). Exploitation. In The Stanford Encyclopedia of Philosophy. <https://plato.stanford.edu/entries/exploitation/>
