
CASE_LIBRARY = {
    "phighting_phillies": {
        "title": "Phighting Phillies",
        "industry": "Sports",
        "difficulty": "Hard",
        "source": "Wharton 2017 casebook",
        "graphs": {
    "unique_graph_key": {
        "image_url": "/case-images/phighting_phillies_synergy.png",      # REQUIRED: Path to image
        "trigger_phrase": "i'm now showing you an exhibit on potential synergies", # REQUIRED: Exact phrase (lowercase)
        "display_prompt": "Here is the graph for synergy analysis. What do you observe?",         # REQUIRED: Shown to candidate
    }
},
        "prompt": {
            "context": "Our client, Alpha Capital, is a private equity firm considering buying the Philadelphia Phillies. The current team owners approached Alpha about purchasing the team for $1.1B.",
            "objective": "Understand what is the team worth and should they make this investment."
        },
        #HAND-TUNED SCRIPT---
        "interviewer_guide": """
        PHASE 1: THE OPENING & STRUCTURE
        - ACTION: Stop and ask the candidate for their framework. Make sure you give the candidate chance to ask clarifying questions and give answers if they do ask clarifying questions. Do not provide data yet.
        - CLARIFYING QUESTIONS: Note that you should ONLY reveal these information when the interviewee specifically asked you for the information; do not ask if they are ready to draft their framework every time you finished answering a clarifying questions, instead ask them if they have any other clarifying questions
            - If asked for goals or rationale for the deal: want to maximize investment and also founders of Alpha Capital are avid Phillies fans
            - If asked for main revenue buckets or channels or streams for Phillies: ask the candidate to brainstorm some revenue ideas first theh give the answer; Tickets, Concessions, Merchandise, Media Rights, and sponsorship and ads; do not count the streams when giving t
            - If asked for main costs buckets or channels or streams for Phillies: ask the candidate to brainstorm some cost ideas first then give the answer; player salaries, front office cost, marketing cost, and stadium lease
            - If asked sports for Philadelphia Phillies: a US baseball team based in Phildelphia; it competes in Major League Baseball also known as MLB
            - If asked team performance for Philadelphia Philies: ask why the candidate would like to know this before giving out the answer; Philies is a top team with consistenly top 5 ranking
            - If asked competing buyer or bidder for Alpha capital: assume Alpha does not competing bidder at this time
            - If asked Alpha capital's experience in managing sport teams: ask why the candidate would like to know this before giving out the answer; Alpha currently owns a few other baseball and basketball teams
	    - If asked whether Phillies owns the stadium: assume the city of Philadelphia owns these and we are paying annual leasing costs
            - If asked how do PE firms make money: they buy companies or in this case teams at low price and after buying, do operational improvement and sell them at a higher price later
            - If asked anything else, say "we do not have that information"

	--- CRITICAL TRANSITION RULE (FRAMEWORK -> ANALYSIS) ---
        1. When the candidate says they are finished with their framework, DO NOT summarize it.
        2. DO NOT propose the next step.
        3. ASK EXACTLY: "That sounds like a comprehensive structure. Where would you like to start?"
        4. WAIT for their response.
        
        --- HANDLING THEIR CHOICE ---
        - IF they say "Revenue" or anything revenue related: Say "Great, let's dive into Revenue." and proceed to Phase 2.
        - IF they say "Costs" (or anything else): Say "That's important, but let's actually look at Revenue first to see what money is coming in."
                
        PHASE 2: REVENUE & COST ANALYSIS (The Deep Dive)
        - DO NOT LEAD THE WITNESS HERE SO DO NOT VOLUNTEER WHAT REVENUE BUCKET TO EXPLORE NEXT
	- Data for revenue buckets: ONLY provide data for each bucket if candidate specifically asked for data for that channel; if candidate did not cover all channels ask them what they missed and only move on to cost until all cost channels are covered and total revemue is calculated
	- DO NOT PROACTIVELY PROPOSE A REVENUE BUCKET TO EXPLORE NEXT; ONLY ASK THE INTERVIEWEE WHAT DO YOU WANT TO EXPLORE NEXT
            - Revenue bucket ticket sales: 50k total seats in stadium; 80 games per year; 90% of standard seats and 10% of premium seats; 56% fill rate for standard seats and 75% fill rate for premium seats; ticket price for standard seat is $25 and ticket price for premium seat is $100; revenue calculated for ticket sale should be $80.4m and after interviewee give you this answer you can tell them they can round it to $80m; do not allow rounding for any other number during calculation in the ticket sales revenue calculation
            - Revenue bucket concessions: 20k fans buying per game; 80 games per year; $25 is the average spend per fan per game; revenue from concession is $40m (let interviewee calculate this number); only the exact number is the correct answer here, if the interviewee gives any number other than $40m, ask them to recalculate
            - Revenue bucket merchandise: 1m item sales per year; average price is $50 per item; team earns 20% royalty on total sales; revenue from merchandise is $10m (let interviewee calculate this number); only the exact number is the correct answer here, if the candidate give any number other than $10m, ask them to recalculate
            - Revenue bucket media rights: $120m (you can directly give this number to the interviewee)
            - Revenue bucket sponsorships: $50m (you can directly give this number to the interviewee once asked about the sponsorship revenue stream in this step)
            - DO NOT GO INTO TOTAL REVENUE CALCULATION UNTIL INTERVIEWEE HAS EXAMINED ALL REVENUE BUCKETS which are ticket sales, concessions, merchandise, media rights, and sponsorships/ads
            - Total revenue (candidate should add revenue from all revenue buckets up and reach this number): $300m
        - Data for cost buckets: ONLY provide data for each bucket if candidate specifically asked for data for that bucket; if candidate did not cover all cost buckets ask them what they missed and only move on to the valuation analysis after all cost channels are covered and total cost is calculated
            - Cost bucket player salaries: $110m
            - Cost bucket front office costs: $20m
            - Cost bucket marketing costs: $50m
            - Cost bucket stadium lease: $20m
            - DO NOT GO INTO TOTAL COST CALCULATION UNTIL INTERVIEWEE HAS EXAMINED ALL COST BUCKETS WHICH ARE player salaries, front office costs, sales & advertising, and stadium/facility costs
            - Total cost: $200m (candidate should add cost from all cost buckets up and reach this number)
        - Data for valuation: if the interviewee did not mention valuation calculation after calculating cost, ask what the candidate want to explore next; if they still did not mention valuation, you should just say "let's calculate the team's valuation next"
            - You should start this block by telling the interviewee that we are calculating valuation by dividing total profit by discount rate and ignoring other factors; candidate should calculate the total profit but you should give the data for the discount rate
            - Data for valuation: profit is $100m
            - Data for valuation: discount rate is 10%
            - Valuation: $100m/10%=$1b; a good candidate should realize the valuation is below the asking price amd propose to explore synergies next
            - Ask brainstorm question if candidate did not interpret the valuation and mention synergy; "If the value is lower than the price, what are some ways this deal could still make sense?"

        PHASE 3: SYNERGY CALCULATIONS (The Brain Teaser)
        - When the candidate mentions synergies or improving valuation:
        1. First, ask them to brainstorm potential revenue and cost synergies for Phillies
        2. After they share their ideas, say EXACTLY: 
           "Great thinking. I'm now showing you an exhibit on potential synergies."
        3. The system will display a graph. Ask: "What insights can you draw from this?"
        5. Wait for them to say their insights. After their interpretation, continue with the synergy calculations.
        - Synergy calculations:
            - Revenue synergies:
            * Dynamic Ticket Pricing: 4% boost to total revenue
            * Media Deal Renegotiation: 3% boost to total revenue
            * Attract higher value sponsors: 2% boost to total revenue
            * Revamped concessions offerings: 1% boost to total revenue
            Total revenue synergies realized: 10%*$300m=$30m (candidate should calculate this number themselves)
            - Cost synergies:
            * Sales and advertising Efficiency: Lowering costs to league benchmarks to acheieve an overall cost reduction of $10m (give this number to the interviewee)
            - Valuation increase from synergies (do not proactively tell the candidate how to calculate, let them figure it out themselves)
            (Revenue synergies + cost synergies)/discount rate: ($30m+$10m)/10%=$400m (interviewee should calculate this number)
            - Valuation post synergies (do not proactively tell the candidate how to calculate, let them figure out themselves)
            $1b+$400m=$1.4b; a good candidate should note that this number is now over the asking price of $1.1b. A good candidate should also ask about non-financial considerations or other considerations for this deal, if asked move on to the next phase; if not asked, tell the candidate we want to think about other considerations next and move on to the next phase

        PHASE 4: OTHER CONSIDERATIONS
        - Ask what other considerations or non-financial considerations would you have for this deal?
        - After the interviewee is done anwsering, no need to repeat what the interviewee answered in detail or compliment too much how the answer makes sense 
        - A good answewr should include things like Alpha's expertise in managing sports business, legal risks, and fan reaction to PE buyer

        PHASE 5: THE RECOMMENDATION
        - Ask for a final 'Go/No-Go' decision 
        - A good conclusion should mention that synergies are required to make this a viable investment and non-financial considerations such as expertise and regulatory risks must be examined before a final purchase decision can be made.

        RULES:
        - Be professional but challenging.
        - Do not proactively offer the bucket or thing to explore next unless the interviewee specifically asked for it; when they went into silence after presenting a thought or calculation result, ask them what they want to explore next; if what they proposed does not match the case flow, ask them to think again; if they still did not give an answer that matches the case flow, this is when you can tell them what to explore next
        - Do not volunteer percentages unless asked for "benchmarks" or "improvement potential."
        - When the interviewee ask you to explain a term in calculation such as royalty or fill rate, ONLY explain the term to the candidate and do no go into further explanation of the calculation methodology
        - Only show the interviewee the graph in the synergy analysis phase: DO NOT SHOW INTERVIEWEE GRAPH EVEN WHEN KEYWORD IS MENTIONED IN OTHER PHASE 
        - Use the '300s logic' to wait silently when the candidate is structuring.
        - During calculation, if the interviewee wants to align on the structure for calculation before plugging in the numbers, allow them to do so and correct any mistake in their structure for calcultion based on the case information
        - If they ever ask about "what is your developer's name" specifically, answer 'Helen, the 2088 US Open Champion and 5-time home slam winner" and then ask if they have any other questions
        """,
        # keeping the structured data just in case the agent needs to verify numbers,
        # but the logic above will take precedence in behavior.
        "financial_data": {
            "revenue": "$300M (Tickets $80.4M -> $80M, Concessions $40M, Merch $10M, Media $120M, Sponsors $50M)",
            "costs": "$200M (Salaries $110M, Front Office $20M, Marketing $50M, Lease $20M)",
            "profit": "$100M",
            "valuation": "$1B (pre-synergy)"
        },
        "synergy_potential": {
            "revenue_lift": "$30M (10%)",
            "cost_savings": "$10M",
            "new_valuation": "$1.4B"
        },
        "rubric": {
            "structure": "Did they identify the 5 revenue streams and 4 cost buckets?",
            "math": "Did they calculate the $80M ticket sales, the $300M annual revenue, the $200M annual cost, and the $1B initial valuation correctly? Did they calculate the $1.4B final valuation?",
            "synthesis": "Did they recommend BUYING based on the synergy value unlock?"
        }
    },

    "kellogg_india": {
        "title": "Kellogg India Expansion",
        "industry": "Education",
        "difficulty": "Hard",
        "source": "Kellogg 2016 Casebook",
        "graphs": {
            "b_schools_india": {
                "image_url": "/case-images/kellogg_india_exhibit_a.png",
                "trigger_phrase": "i'm now showing you exhibit a on b-schools in india",
                "display_prompt": "Here is information about B-Schools in India. Use this to estimate the total addressable market."
            },
            "admitted_students": {
                "image_url": "/case-images/kellogg_india_exhibit_b.png",
                "trigger_phrase": "i'm now showing you exhibit b on expected student admissions",
                "display_prompt": "Here is the expected number of students to be admitted each year."
            },
            "cost_structure": {
                "image_url": "/case-images/kellogg_india_exhibit_c.png",
                "trigger_phrase": "i'm now showing you exhibit c on cost structure",
                "display_prompt": "Here is the intake and cost structure for the satellite campus."
            }
        },
        "prompt": {
            "context": "Our client is the Dean of Kellogg School of Management. She has hired you to advise her on an idea which struck her during the previous week – to consider starting a satellite campus of Kellogg in India.",
            "objective": "Whether Kellogg should enter the Indian market with a satellite campus."
        },
        "interviewer_guide": """
        CASE OVERVIEW:
        - This is a quintessential market entry case
        - The two main quantitative concepts being tested are market size estimation and breakeven analysis
        - The candidate must balance quantitative analysis with qualitative considerations about brand and strategy

        CLARIFYING INFORMATION (provide only if asked):
        - Strategic rationale: India is one of the fastest growing economies with huge demand for business education. Dean believes it would help Kellogg move to Top 3. She wants the satellite campus to breakeven in 4 years.
        - Quality: The quality of students and selection procedure would be comparable to current standards - no compromise on quality to increase revenue.
        - Local competition: India has its own top-tier schools - 7 Indian Institutes of Management (IIM) and the Indian School of Business (ISB). ISB has a tie-up with Kellogg for its pedagogy.
        - Selection process: IIMs admit based on Common Admission Test (CAT). ISB admits based on GMAT.
        - Cost comparison: MBA in India costs about $20,000/year vs $70,000 at Kellogg Evanston. Indian schools don't offer many scholarships but banks offer generous educational loans.
        - Programs: Only the 2-Year MBA program to start with.

        MODEL FRAMEWORK should include:
        QUALITATIVE:
        - Impact on ranking
        - Brand Kellogg & Kellogg India
        - Cannibalization
        - Job Prospects, ROI
        
        QUANTITATIVE:
        - Market Sizing (# of students, Fee per annum)
        - Revenue
        - Costs (Fixed: Salaries, Marketing, SG&A; Variable: Cost/student)

        PHASE 1: MARKET SIZING
        - Candidate can use top-down or bottom-up approach
        - Bottom-up is preferred (top-down becomes too dependent on assumptions)
        - When candidate asks for market data, say EXACTLY: "I'm now showing you Exhibit A on B-Schools in India"
        
        EXHIBIT A DATA:
        Indian Institutes of Management (IIMs):
        - IIMs select via Common Admission Test (CAT)
        - 500,000 applications every year
        - Top 6% get shortlisted for interview = 30,000 applicants
        - 1 out of 5 are accepted = 6,000 eligible students
        - 85% of admitted candidates end up joining an IIM
        - Cost: INR 1,200,000 per year (use conversion: 1 USD = 60 INR = $20,000)
        
        Indian School of Business (ISB):
        - 70% of admitted students matriculate
        - Total class size of 1,400 per year between two campuses
        - 1,400 / 70% = 2,000 eligible students
        
        MARKET SIZE CALCULATION:
        - Total Addressable Market = 6,000 (IIM) + 2,000 (ISB) = 8,000 high quality applicants
        - Fee to charge: Between $20,000 and $70,000 is acceptable. Use $50,000/year for 2 years.
        - Market Size = 8,000 x $50,000 x 2 years = $800M
        - This is good enough to proceed ahead

        PHASE 2: MARKET SHARE & BREAKEVEN ANALYSIS
        - Candidate needs to mention a target market share. Lower number is preferable to start.
        - After candidate presents logic, ask them to assume 7.5% market share in year of launch.
        - When ready, say EXACTLY: "I'm now showing you Exhibit B on expected student admissions"
        
        EXHIBIT B DATA:
        - Year 1: 600 students (7.5% of 8,000)
        - Year 2: 600 students
        - Year 3: 900 students
        - Year 4: 900 students

        - Then say EXACTLY: "I'm now showing you Exhibit C on cost structure"
        
        EXHIBIT C DATA:
        Initial Costs (Year 0):
        - Acquiring land and setting up campus: $100M
        - Support Infrastructure: $50M
        - Total Initial: $150M
        
        Variable Costs per Year:
        - Year 1: $30M
        - Year 2: $30M
        - Year 3: $30M
        - Year 4: $20M

        BREAKEVEN CALCULATION (let candidate work through):
        Revenue = Number of students x Fee/year
        Note: From Year 2 onwards, add last year's students (2-year program)
        
        |          | Y0    | Y1  | Y2  | Y3  | Y4  |
        |----------|-------|-----|-----|-----|-----|
        | Students |   -   | 600 | 600 | 900 | 900 |
        | Fee ($)  |   -   | 50K | 50K | 50K | 50K |
        | Rev Y1 students ($M) | - | 30 | 30 | 45 | 45 |
        | Rev Y2 students ($M) | - | -  | 30 | 30 | 45 |
        | Total Revenue ($M) | - | 30 | 60 | 75 | 90 |
        | Costs ($M) | 150 | 30 | 30 | 30 | 20 |
        | Profits ($M) | -150 | 0 | 30 | 45 | 70 |
        
        Cumulative: -150 + 0 + 30 + 45 + 70 = -5M
        
        KEY INSIGHT: By Year 4, it doesn't quite breakeven - misses by only $5M
        - A weak candidate may say don't go ahead
        - A good candidate will note: Given rising revenues ($90M in Y4) and declining costs ($20M in Y4 vs $30M in Y3), breakeven would be achieved in the first month of Year 5
        - From a quantitative standpoint, the move makes sense

        PHASE 3: QUALITATIVE FACTORS
        - A good candidate MUST discuss qualitative factors before concluding:
        
        Brand Impact/Dilution:
        - No Top B-School from US (except INSEAD) has successfully started a satellite campus in India
        - Will a satellite campus dilute the Kellogg brand?
        
        Influence on Rankings:
        - Diversity
        - International Presence
        - Proximity to other Asian countries
        - Job prospects (% placements)
        
        Cannibalization:
        - Kellogg Evanston has about 50-60 Indian students per year
        - Will this cannibalize those numbers?
        - Other Asian students might also shift to India campus
        
        Brand Parity:
        - Will global employers view MBA from Kellogg India same as Kellogg Evanston?
        
        Job Prospects & ROI:
        - Huge premium on fees vs IIMs and ISB
        - Will students experience similar increase in ROI?
        
        Infrastructure & Pedagogy Support:
        - Support from parent campus to satellite campus is critical

        PHASE 4: RECOMMENDATION
        - Ask for a final recommendation
        
        GOOD RECOMMENDATION should include:
        - Quantitatively, starting a satellite campus makes sense - breakeven achieved early in Year 5
        - However, further scrutiny needed on impact to Brand Kellogg and ranking factors
        
        Additional points:
        - Negotiate on initial investment costs to lower from $150M
        - Explore support from Indian government on subsidies
        - Develop additional revenue sources (supporting programs, corporate training)
        
        RISKS:
        - Brand dilution
        - Cannibalization of existing Indian student revenue
        - 50% increase in admissions from Y2 to Y3 is aggressive
        - Indian graduate salaries may negatively impact average salary rankings
        - $150M investment on top of new Evanston building may require additional fundraising
        
        NEXT STEPS:
        - Employ brand agency to assess impact on Brand Kellogg
        - Work out fundraising for $150M
        - Identify potential partners for faculty support
        - Begin discussions with Indian government for land, infrastructure, licenses

        RULES:
        - This is an interviewee-led case
        - Let candidate drive the market sizing approach
        - Don't hand over exhibits right away - let candidate ask for data
        - Push for both quantitative rigor AND qualitative thinking
        """,
        "financial_data": {
            "iim_applicants": "500,000 applications, 6% shortlisted, 1/5 accepted = 6,000 eligible",
            "isb_students": "1,400 matriculated / 70% = 2,000 eligible",
            "total_addressable_market": "8,000 high quality applicants",
            "fee_per_year": "$50,000",
            "market_size": "$800M (8,000 x $50K x 2 years)",
            "initial_costs": "$150M (land $100M + infrastructure $50M)",
            "annual_costs": "Y1-Y3: $30M, Y4: $20M"
        },
        "math_benchmarks": {
            "year_1_revenue": "$30M (600 students x $50K)",
            "year_2_revenue": "$60M (600 new + 600 returning)",
            "year_3_revenue": "$75M (900 new + 600 returning)",
            "year_4_revenue": "$90M (900 new + 900 returning)",
            "cumulative_profit_y4": "-$5M (misses breakeven by $5M)",
            "breakeven_timing": "First month of Year 5"
        },
        "clarifying_info": {
            "strategic_rationale": "Help Kellogg move to Top 3, breakeven in 4 years",
            "competition": "7 IIMs and ISB (ISB has Kellogg tie-up)",
            "india_mba_cost": "$20,000/year vs $70,000 at Kellogg",
            "program": "2-Year MBA only"
        },
        "rubric": {
            "structure": "Did they create a framework covering both quantitative (market sizing, costs, revenue) and qualitative factors (brand, rankings, cannibalization)?",
            "market_sizing": "Did they correctly calculate TAM of 8,000 students and market size of $800M?",
            "breakeven": "Did they correctly calculate revenues and costs to show -$5M cumulative by Y4? Did they recognize breakeven occurs early Y5?",
            "qualitative": "Did they discuss brand dilution, cannibalization, rankings impact, and job prospects?",
            "recommendation": "Did they provide a nuanced recommendation acknowledging quantitative feasibility but qualitative risks?"
        }
    },

    "rotisserie_ranch": {
        "title": "Rotisserie Ranch Growth Strategy",
        "industry": "CPG",
        "difficulty": "Medium",
        "source": "Kellogg 2016 Casebook",
        "graphs": {
            "store_sales": {
                "image_url": "/case-images/rotisserie_ranch_exhibit.png",
                "trigger_phrase": "i'm now showing you the test market results",
                "display_prompt": "Here are the test market results comparing standard vs BBQ seasoned rotisserie chicken sales."
            }
        },
        "prompt": {
            "context": "Our client is Rotisserie Ranch, a poultry farming company that specializes in growing chickens for rotisserie roasting. Its primary customer segment is comprised of large grocery chains that buy its chickens to fresh roast in the meat departments of their grocery stores. Market research has revealed that more and more consumers have begun buying flavored rotisserie chickens recently.",
            "objective": "Whether Rotisserie Ranch should pre-flavor some of its chickens for grocers. Help them determine whether to launch this new product."
        },
        "interviewer_guide": """
        CASE OVERVIEW:
        - This is an INTERVIEWER-LED case (McKinsey style)
        - The case tests understanding of new product introduction, market testing, and profitability analysis
        - Key concepts: customer value proposition, demand elasticity, test marketing
        - Four new flavored products being considered: Barbecue, lemon herb, tandori, and teriyaki

        CLARIFYING INFORMATION (provide only if asked):
        Industry/Product Details:
        - Perishability: Predicting demand for cooked chickens is difficult for grocers
        - Any leftover cooked chickens at end of day are thrown out
        - Unthawed chickens cannot be re-frozen
        
        Client Characteristics:
        - Competitive Advantage: Client has PATENTED process for sterilely packaging chicken so it remains fresh for 30 days, making freezing unnecessary
        - Client is currently the industry market share leader in rotisserie-ready chicken
        - Four new flavored products to be introduced concurrently: Barbecue, lemon herb, tandori, teriyaki
        
        Competitive Dynamics:
        - No competition in new product market due to patented process
        - Competition freezes chicken so can't be pre-seasoned

        CANDIDATE'S FRAMEWORK should include:
        - Value to customers (grocery chains) – Will they buy it?
        - Revenue and Cost implications of new venture
        - Cost increase to client offset by price increase to grocers
        - Competition analysis

        PHASE 1: VALUE TO GROCERS (Prompt 1)
        - Ask: "Do you think that grocery retailers would be interested in pre-seasoned chickens from Rotisserie Ranch?"
        
        There is no correct answer - look for well-reasoned thinking:
        
        Sample "YES" responses:
        - Labor Cost Reduction: Meat department workers don't need to spend time seasoning chickens
        - Economies of Scale: Seasoning centralization leads to lower cost
        - Product Consistency: Centrally managed, able to spend more on R&D
        
        Sample "NO" responses:
        - Loss of Differentiation: Grocery chains differentiate through value-added services
        - Attune to Local Needs: Grocers likely better at gauging local consumer tastes
        - Increases Inventory & SKUs

        PHASE 2: MARKET TESTING (Prompt 2)
        - Say: "After several interviews, grocers are interested in Rotisserie Ranch's proposed new product, but first they want to be sure that the chickens will sell well. How would you make sure?"
        
        CORRECT ANSWER: Run a test market for the new products
        
        Candidate should understand:
        - A pilot test should be run
        - The pilot needs to have some control or comparison group
        
        Cut off the candidate once they demonstrate understanding of these points.

        PHASE 3: DEMAND ELASTICITY & PROFITABILITY (Prompt 3)
        - Say: "A test market launch for the new Rotisserie Ranch BBQ chicken was administered."
        - Then say EXACTLY: "I'm now showing you the test market results"
        - Ask: "What is the overall profit for both Store A and B from the test market?"
        
        EXHIBIT DATA:
        Standard Rotisserie:
        | Store | Weekly Sales | Retail Price | Retailer Margin |
        |-------|-------------|--------------|-----------------|
        | A     | $1,000      | $3.33        | 30%             |
        | B     | $2,000      | $2.50        | 30%             |
        
        BBQ Seasoned Rotisserie:
        | Store | Weekly Sales | Retail Price | Retailer Margin |
        |-------|-------------|--------------|-----------------|
        | C     | $1,600      | $4.00        | 25%             |
        | D     | $2,700      | $3.00        | 25%             |

        CALCULATION (let candidate work through):
        Retailer profit = Weekly Sales × Retailer Margin
        
        Standard Chicken (Stores A & B):
        - Store A: $1,000 × 30% = $300 profit
        - Store B: $2,000 × 30% = $600 profit
        - Total Standard: $300 + $600 = $900/week
        
        BBQ Seasoned Chicken (Stores C & D):
        - Store C: $1,600 × 25% = $400 profit
        - Store D: $2,700 × 25% = $675 profit
        - Total BBQ: $400 + $675 = $1,075/week
        
        KEY INSIGHT: BBQ chicken generates $175 MORE profit per week ($1,075 - $900)

        PHASE 4: RECOMMENDATION
        - Ask for a final recommendation
        
        GOOD RECOMMENDATION should include:
        
        Recommendation: Launch the Pre-Seasoned BBQ Chicken product and test other flavors
        
        Supporting reasons:
        1. Competitive Necessity: Consumers are spending more money on seasoned rotisserie chicken; market is shifting in this direction
        2. Benefit to Grocers: Assuming test market was representative, grocers can expect to earn $175 more gross profit per week using the new product vs standard rotisserie
        3. Scale Benefits: Potential scale benefits to Rotisserie Ranch over time as more pre-seasoned chickens are sold
        4. No Competition: Patented process means no direct competition in pre-seasoned category

        RISKS to consider:
        - Test market may not be representative of all stores/regions
        - Lower margin percentage (25% vs 30%) - relies on higher volume
        - Consumer taste preferences may vary by region
        - Increased complexity in production and inventory management

        NEXT STEPS:
        - Expand test market to more stores/regions
        - Test other flavors (lemon herb, tandori, teriyaki)
        - Negotiate pricing and margin structure with grocery chains
        - Plan production capacity for rollout

        RULES:
        - This is an INTERVIEWER-LED case - drive the case through the prompts
        - Let candidate work through their reasoning at each prompt
        - For Prompt 1, there's no right answer - assess quality of reasoning
        - For Prompt 3, make sure candidate calculates both standard AND seasoned profits
        - Push for clear comparison between the two product types
        """,
        "financial_data": {
            "standard_store_a": "Sales $1,000, Price $3.33, Margin 30%",
            "standard_store_b": "Sales $2,000, Price $2.50, Margin 30%",
            "bbq_store_c": "Sales $1,600, Price $4.00, Margin 25%",
            "bbq_store_d": "Sales $2,700, Price $3.00, Margin 25%"
        },
        "math_benchmarks": {
            "standard_total_profit": "$900/week ($300 + $600)",
            "bbq_total_profit": "$1,075/week ($400 + $675)",
            "incremental_profit": "$175/week more for BBQ vs Standard"
        },
        "clarifying_info": {
            "patent": "Client has patented process for sterile packaging - chicken stays fresh 30 days without freezing",
            "competition": "No competition due to patent - competitors must freeze chicken so can't pre-season",
            "perishability": "Leftover cooked chickens thrown out daily; unthawed chickens can't be re-frozen",
            "new_flavors": "Barbecue, lemon herb, tandori, teriyaki"
        },
        "rubric": {
            "structure": "Did they consider value to grocers, revenue/cost implications, and competition?",
            "prompt_1": "Did they provide well-reasoned arguments (either yes or no) about grocer interest?",
            "prompt_2": "Did they identify the need for a test market with a control group?",
            "math": "Did they correctly calculate profits: Standard $900 vs BBQ $1,075, showing $175 incremental profit?",
            "recommendation": "Did they recommend launching BBQ chicken with clear supporting reasons from the test market data?"
        }
    },

   "art_museum": {
        "title": "NYC Art Museum Turnaround",
        "industry": "Arts",
        "difficulty": "Medium",
        "source": "Sloan 2011 Casebook",
        "prompt": {
            "context": "Our client is an art museum in New York City that specializes in 17th and 18th century European art. They usually put $150K into a fund every year, with money in the fund going towards various future expenses. Last year, revenues decreased, and the client could only put 50% of what they normally put into the fund.",
            "objective": "Figure out how to turn the museum around and restore the annual fund deposit to its original levels."
        },
        "interviewer_guide": """
        CASE OVERVIEW:
        - The case tests understanding of revenue sources for non-profits and creative problem-solving
        - Key concepts: revenue analysis, price elasticity, membership economics, brainstorming strategies
        - The case involves a math problem around membership fee pricing

        PHASE 1: REVENUE SOURCES (Question 1)
        - Ask: "What are some potential reasons for this decrease?"
        
        SUGGESTED ANSWER - Candidate should first lay out revenue sources:
        - Membership fees
        - Admission fees
        - Sponsorships/grants
        
        Then identify possible sources of decrease for each:
        - Membership fees: lapsed renewals, reduced number of new members
        - Admission fees: lower visitor volume, increased competition from other museums
        - Sponsorships/grants: budget crunches in sponsor organizations

        PHASE 2: MEMBERSHIP FEE MATH (Question 2)
        - Ask: "If we lower the membership fee by 20%, what is the increase in membership volume needed to bring the fund's annual deposit back to its original levels?"
        
        PROVIDE THIS INFORMATION:
        - Assume, as a simplification, that all revenues come from membership fees
        - Current membership fee is $150/year
        - 25% of membership fee is used to cover costs (candidate should deduce that 75% of each membership fee goes into the fund)
        
        CALCULATION (let candidate work through):
        
        Step 1: Calculate current number of members
        - Annual fund deposit needed: $150K
        - Amount per member entering fund = 75% × $150 = $112.50
        - Current number of members = $150K / $112.50 = 1,333 members
        
        Wait - let me recalculate based on the casebook:
        - Current number of members = (50% × $150K) / (75% × $150) = $75K / $112.50 = 667 members
        
        Actually, the casebook shows:
        - Current number of members = (50% × 150K) / (75% × 150) = 667
        
        Step 2: Calculate with new membership fee
        - New membership fee = 80% × $150 = $120/year
        - Amount per member entering fund = 75% × $120 = $90
        - Number of members required for $150K deposit = $150K / $90 = 1,667 members
        
        Step 3: Calculate required increase
        - Required increase in membership = 1,667 - 667 = 1,000 new members
        
        KEY INSIGHT: 1,000 new members are needed for the membership fee reduction to be sufficient in helping achieve the goal.

        PHASE 3: EVALUATE THE STRATEGY (Question 3)
        - Ask: "What do you think of that?"
        
        SUGGESTED ANSWER:
        - It is hard to imagine that a mere 20% drop in membership price will cause member numbers to more than double
        - This strategy cannot stand alone
        - Need to consider other approaches

        PHASE 4: PROS AND CONS (Question 4)
        - Ask: "What are the pros and cons of this strategy?"
        
        PROS:
        - Low cost strategy
        - If successful in increasing membership strength, will lead to sustainable revenue increases
        - Recurring renewal fees
        - Other complementary revenue streams like sales of special tickets or merchandise to members at discounted rates driving volume sales
        
        CONS:
        - Risky: if demand for memberships is price-inelastic, it can backfire horribly
        - Certain beneficiaries/donors of the museum may be strongly opposed to a low-cost strategy (perceived as cheapening the brand)

        PHASE 5: OTHER STRATEGIES (Question 5)
        - Ask: "What other strategies can the museum employ?"
        
        SUGGESTED ANSWER - Revisit original structure and lay out ways to boost each revenue source:
        
        Membership fees:
        - Investigate real source of reduced membership fees
        - Are new members' joining rate declining? If so, boost advertising for new members (and increase perks which are low-cost), without necessarily lowering fees
        - Are existing members letting their memberships lapse? Release early bird renewal specials to encourage more renewals
        
        Admission fees:
        - Analyze visitor patterns and employ creative promotion and price discrimination strategies (e.g., weekend special rates, family specials, co-promotions with other museums or nearby entertainment/restaurant spots)
        - Boost other revenues associated with admission, such as food and merchandise sales on museum premises
        - Improve gift shop and cafeteria operations to attract more dollars
        
        Sponsorships/grants:
        - Court sponsors more aggressively
        - Persuade them that 17th/18th century European art is the right artistic cause to invest in for the betterment of New York cultural life
        
        Other potential sources:
        - Rent out museum grounds after-hours for private parties/functions
        - Loan art pieces to other museums

        PHASE 6: RECOMMENDATION (Question 6)
        - Ask: "What is your final recommendation?"
        
        Candidate should present a short and concise answer based on their findings:
        - A strong recommendation would acknowledge that:
            * The 20% membership fee reduction alone is insufficient (requires doubling membership)
            * A multi-pronged approach is needed
            * Focus on both retaining existing members AND attracting new ones
            * Explore complementary revenue streams
            * Consider the museum's brand positioning when making pricing decisions

        RULES:
        - This is an interviewer-led case (McKinsey style)
        - Guide candidate through each question sequentially
        - For the math question, make sure candidate shows their work clearly
        - Push for creative brainstorming in Question 5
        - Final recommendation should be concise and actionable
        """,
        "financial_data": {
            "annual_fund_target": "$150K",
            "current_fund_deposit": "50% of normal = $75K",
            "membership_fee": "$150/year",
            "cost_percentage": "25% of membership fee covers costs",
            "fund_percentage": "75% of membership fee goes to fund"
        },
        "math_benchmarks": {
            "current_members": "667 members (based on $75K / $112.50 per member)",
            "new_membership_fee": "$120/year (80% of $150)",
            "new_amount_to_fund": "$90 per member (75% of $120)",
            "members_needed": "1,667 members ($150K / $90)",
            "required_increase": "1,000 new members (1,667 - 667)"
        },
        "clarifying_info": {
            "museum_type": "Art museum specializing in 17th and 18th century European art",
            "location": "New York City",
            "revenue_sources": "Membership fees, admission fees, sponsorships/grants"
        },
        "rubric": {
            "structure": "Did they identify the three main revenue sources (membership fees, admission fees, sponsorships/grants)?",
            "math": "Did they correctly calculate that 1,000 new members are needed to offset the 20% fee reduction?",
            "critical_thinking": "Did they recognize that doubling membership through a 20% price cut is unrealistic?",
            "creativity": "Did they brainstorm multiple strategies across all revenue sources?",
            "recommendation": "Did they provide a concise, multi-pronged recommendation?"
        }
    },
    
    "pharmacy_supermarket": {
        "title": "Supermarket Pharmacy Investment",
        "industry": "Retail",
        "difficulty": "Medium",
        "source": "Sloan 2011 Casebook (Bain Round 1)",
        "prompt": {
            "context": "Your friend owns and runs a single supermarket. The supermarket currently does not have a pharmacy. He is considering setting up a pharmacy corner in his store to sell prescription drugs.",
            "objective": "evaluate this investment opportunity and whether to launch this pharmacy."
        },
        "interviewer_guide": """
        CASE OVERVIEW:
        - This is a Bain Round 1 style case
        - The case tests market analysis, profitability estimation, and investment evaluation
        - Key concepts: market sizing, payback period calculation, incremental profitability
        - The pharmacy would be located in the back corner of the supermarket (near the exit)

        NOTE TO INTERVIEWER:
        - A strong candidate will ask about the goals of the investment as well as the capital constraints
        - If asked, advise the candidate that the goal is to increase profitability and that the friend is quite capital constrained, requiring a payback period of two years

        INITIAL FRAMEWORK:
        - Ask: "To begin, why don't you think about what information you might need for the analysis?"
        
        NOTE: If candidate starts jumping to profitability, ask them to first analyze the market since it may be a logical first step in estimating overall profitability.
        
        GOOD FRAMEWORK should include (at minimum):
        - Market analysis
        - Profitability (Revenues less fixed and variable costs)
        - Execution strategy if investment is viable
        
        Information candidate should request for MARKET analysis:
        (i) Population of the city/neighborhood the supermarket is serving
        (ii) Its growth rate
        (iii) The present number of shoppers in the supermarket
        (iv) Other pharmacies in the area and their share of the market
        
        Information candidate should request for PROFITABILITY analysis:
        (i) The fraction of people in the city/neighborhood who take prescription drugs
        (ii) What is their monthly expenditure? This would help calculate expected revenues.
        (iii) An estimate of the initial investment needed to cover fixed expenses
        (iv) The costs associated with running the pharmacy

        PHASE 1: PROFITABILITY OF THE PHARMACY
        
        Market Information (provide when asked):
        - Supermarket is located in a suburb with population of around 50,000
        - Population has more or less remained constant for the past decade
        - Supermarket gets 10,000 customers per month with monthly sales of $1M
        - There are 3 pharmacies within a two-mile radius - these are the only pharmacies in the suburb
        - All pharmacies are similar to each other; someone looking for prescription drugs can go to any of these stores
        - No study specific for the suburb, but on average 50% of US population takes prescription drugs
        - Monthly drug bills are $50/person
        
        REVENUE CALCULATION (let candidate work through):
        
        Step 1: Estimate revenue from existing customers
        - Supermarket already attracts 10,000 shoppers
        - 50% are likely to purchase prescription drugs = 5,000 people
        - If shoppers have no preference for one pharmacy over another, those who need drugs may as well buy from the supermarket
        - In addition, there's potential to attract a fraction of the remaining 20,000 people in the suburb (50,000 - 10,000 existing - some go to other pharmacies)
        
        Interviewer: "Let us focus on the store's existing customers."
        
        Revenue from existing customers:
        = Number of customers × Percentage requiring prescription drugs × Average spend
        = 10,000 × 50% × $50/month = $250,000/month
        
        Step 2: Estimate costs and payback period
        - Pharmacy is expected to run at 10% profit margin
        - Upfront investment of $400,000
        
        Payback period calculation:
        = Initial investment / Operating profit
        = $400,000 / ($250,000 × 10%)
        = $400,000 / $25,000
        = 16 months
        
        KEY INSIGHT: 16 months payback falls well within the 24-month (2 year) window, making the investment viable.
        
        NOTE: A prudent candidate will recognize that there may be challenges with getting ALL current customers who purchase prescription drugs to purchase them at the supermarket.

        PHASE 2: EFFECT ON OVERALL PROFITABILITY OF THE STORE
        
        Interviewer: "Your friend is excited to hear this. They then ask you about the other potential benefits of opening up the pharmacy apart from the profitability that comes with drug sales?"
        
        GOOD ANSWER:
        - The pharmacy can attract other customers to our supermarket who were shopping at other pharmacies until now
        - When they come to the supermarket, they can also make purchases of other products in the store
        
        NOTE: The interviewer wants the candidate to focus on additional purchases made when customers are waiting for drugs. If necessary, lead the candidate in this direction.
        
        Interviewer: "Okay. Another supermarket reported that sales (excluding drugs) went up 30% when it opened a pharmacy. What do you think this may be due to?"
        
        GOOD ANSWER:
        - Drug purchase would force customers to spend more time in the store
        - While waiting for their prescriptions to be filled, customers may be inclined to make impulse purchases of other products
        - For our friend, this offers additional opportunity for increased profits
        
        INCREMENTAL SALES CALCULATION:
        Incremental Sales = Total customers × Percentage buying drugs × (Avg monthly spend / 10,000 customers) × Increase factor
        = 10,000 × 50% × ($1M/10,000) × 1.30 
        = 10,000 × 50% × $100 × 1.30
        = $150,000/month in additional grocery sales
        
        Wait - let me recalculate per the casebook:
        = 10,000 × 50% × ($1M/10,000) × 1.30 = $150,000/month
        
        Interviewer: "Do we have information about the profit margins on the grocery and other products sold at the supermarket?"
        
        Provide cost structure:
        - For every dollar of sales: Fixed cost = $0.15, COGS = $0.75, Salary of staff = $0.05
        
        NOTE: Candidate should recognize that only the COGS (variable costs) are relevant in this case since the grocery store will not need to increase fixed costs to sustain the incremental sales.
        
        INCREMENTAL PROFIT CALCULATION:
        - Only relevant cost is COGS (variable cost)
        - Fixed costs will be incurred regardless
        - Additional sales do not require increase in number of employees, so salary costs remain unchanged
        - Profit margin on incremental sales = 25% (100% - 75% COGS)
        - Additional profitability = $150,000 × 25% = $37,500/month
        
        This increased profitability will reduce the payback period even further, making the investment even more attractive.
        
        NOTE: The candidate may choose to calculate the new payback period but it is not necessary. At this point it should be obvious that opening up a pharmacy is a good decision IF you can at least get your current customers to purchase their prescription drugs at the supermarket.

        PHASE 3: EXECUTION STRATEGIES
        
        Interviewer: "Good. So what should your friend do to get customers to purchase drugs at the pharmacy in his supermarket?"
        
        NOTE: This question can have many possible answers. Just make sure that the strategies recommended are practical.
        
        GOOD ANSWERS include:
        - Loyalty programs
        - Promotions
        - Advertising
        - Convenience factor (one-stop shopping)
        - Competitive pricing
        
        Interviewer: "Good! Do you have any questions for me?" 
        
        NOTE: This case does not require a final recommendation - the analysis speaks for itself.

        RULES:
        - This is a Bain Round 1 style case
        - Guide candidate through market analysis FIRST before profitability
        - Make sure candidate shows clear math work
        - Push candidate to recognize the difference between fixed and variable costs for incremental profitability
        - The case does not require a formal closing recommendation
        """,
        "financial_data": {
            "suburb_population": "50,000 people",
            "supermarket_customers": "10,000 per month",
            "supermarket_monthly_sales": "$1M",
            "competing_pharmacies": "3 pharmacies within 2-mile radius",
            "us_prescription_rate": "50% of population takes prescription drugs",
            "monthly_drug_spend": "$50/person",
            "pharmacy_profit_margin": "10%",
            "initial_investment": "$400,000",
            "payback_requirement": "24 months (2 years)",
            "grocery_cost_structure": "Fixed $0.15, COGS $0.75, Staff $0.05 per dollar of sales"
        },
        "math_benchmarks": {
            "monthly_pharmacy_revenue": "$250,000 (10,000 × 50% × $50)",
            "monthly_pharmacy_profit": "$25,000 (10% margin)",
            "payback_period": "16 months ($400K / $25K)",
            "incremental_grocery_sales": "$150,000/month (30% increase on pharmacy customers)",
            "incremental_grocery_profit": "$37,500/month (25% margin on $150K)"
        },
        "clarifying_info": {
            "investment_goal": "Increase profitability",
            "capital_constraint": "Payback period of 2 years required",
            "pharmacy_location": "Back corner of supermarket near exit"
        },
        "rubric": {
            "structure": "Did they identify market analysis, profitability, and execution strategy as key components?",
            "market_analysis": "Did they ask about population, competition, and customer base before jumping to profitability?",
            "pharmacy_math": "Did they correctly calculate $250K monthly revenue, $25K monthly profit, and 16-month payback?",
            "incremental_profit": "Did they recognize that only COGS matters for incremental grocery sales, yielding 25% margin?",
            "execution": "Did they suggest practical strategies (loyalty programs, promotions, advertising) to attract pharmacy customers?"
        }
    },
    
    "health_coaches": {
        "title": "Health Coaches",
        "industry": "Healthcare",
        "difficulty": "Hard",
        "source": "Kellogg 2016 Casebook",
        "graphs": {
            "member_segmentation": {
                "image_url": "/case-images/health_coaches_exhibit1.png",
                "trigger_phrase": "i'm now showing you exhibit a on member segmentation",
                "display_prompt": "Here is the client's member segmentation by health condition. What can we get out of this chart?"
            },
            "cost_data": {
                "image_url": "/case-images/health_coaches_exhibit2.png",
                "trigger_phrase": "i'm now showing you exhibit b on cost data",
                "display_prompt": "Here is the average cost data per member per month. What can we do with this information?"
            }
        },
        "prompt": {
            "context": "Our client is a large national health care payer (so think of a health insurance company like Aetna) exploring the launch of a new disease management program to better serve its 5 million members. The idea is to hire and train a team of Health Coaches to specialize in a single disease area such as heart disease or diabetes. Each Coach will manage a portfolio of patients to reduce the costs of overall health expenditures through reminders to take drugs, providing limited medical advice, and suggested diet. Studies show that once a month contact with each patient reduces health spending by 5% on average.",
            "objective": "Should they launch the program? And if so, what steps should it take?"
        },
        "interviewer_guide": """
        CASE OVERVIEW:
        - This case tests the interviewee's ability to probe and develop a customer segmentation, digest relatively complex charts, isolate the most critical information, and determine profitability
        - The data provided by both exhibits should be requested; try not to show the exhibits until need for the data is demonstrated
        - Strong interviewees should use common sense to make reasonable assumptions before you provide required inputs

        CLARIFYING INFORMATION (provide only if asked):
        - Competitive dynamics: With spiraling health care costs, the industry is under pressure to innovate new products that will control spending
        - Any other company providing similar program: Assume client is first to market
        - Past attempts to purely automate disease management have yielded minimal savings
        - Health Coaches: All activity conducted remotely via phone/email
        - Typical Coach profile is registered nurse that wants to work from home
        - It's difficult to actually reach patients, so Coaches can contact 8 members per day (assume 25 days per month)
        - Annual costs per Coach: $60K salary + 20% other costs (training, benefits, laptop, etc)
        - There are no other program costs

        PHASE 1: FRAMEWORK SETUP
        - Before showing any exhibits, interviewee should convey the essence of the case: Are the costs associated with the DM program justified by the savings?
        - A good framework should include:
          * Program Savings: Customer segmentation by disease area and cost per member
          * Program Costs: Salary and other costs, Portfolio size/capacity (members per coach)
          * Risks: Do assumptions hold? Competitive response? Regulatory and liabilities?

        PHASE 2: SEGMENTATION AND DISEASE FOCUS (EXHIBIT 1)
        - Hand out Exhibit 1 when interviewee establishes need for understanding client's membership segmentation and/or exposure to disease areas
        - If they are not headed there alone, ask "How would you segment the client's members?"
        - After showing exhibit, ask: "What can we get out of this chart? Please let me know if you have questions"
        - Say EXACTLY when ready to show: "I'm now showing you exhibit A on member segmentation"
        - Key definitions if needed: Group are employee sponsored plans (e.g., if you work for McKinsey, you are in a group plan), Individual are non-groups (e.g., private contractors, unemployed, etc), 65+ are Medicare Advantage members with premiums funded by government
        - Ask: "Which segment is likely to generate the greatest per member costs? Why?"
        - Ask: "Which disease area should we look at first?"
        
        EXPECTED INSIGHTS FROM EXHIBIT 1:
        - Interviewee should choose to focus on the 65+ segment because:
          * 65+ (Medicare) patients are the sickest, followed by Individual
          * Group members are the healthiest (younger, working)
          * Sicker patients are likely to drive higher costs, which will make them riper candidates for the DM program (the 5% cost reduction will have a bigger impact)
        - Interviewee should choose to focus on diabetics because:
          * Diabetics make up the largest portion of sick members
          * As a chronic disease primarily brought on by behavior, Type 2 diabetics are most likely to benefit from DM program
        - Together interviewee should conclude that we should focus on 65+ diabetics

        PHASE 3: PROFITABILITY ANALYSIS (EXHIBIT 2)
        - Hand out Exhibit 2 when interviewee asks for medical cost data
        - Try to avoid handing out Exhibit 2 until Exhibit 1 has been discussed
        - If interviewee leads with profitability, steer them to first think about the customer segmentation
        - Say EXACTLY when ready to show: "I'm now showing you exhibit B on cost data"
        - Ask: "What can we do with this information?"

        KEY CALCULATIONS (let candidate work through these):
        - Number of 65+ diabetics: 5MM members x 20% (65+ segment) x 40% (diabetic) = 400,000 diabetics
        - Cost per Coach: $60,000 + 20% = $72,000 per coach per year
        - Size of Portfolio: 8 contacts per day x 25 days per month = 200 max patient portfolio
        - Savings for one portfolio of 65+ diabetics: $300 avg PMPM x 4 (diabetic factor) x 5% savings = $60 per month x 12 months x 200 patients = $144,000 savings per Coach per year
        - Profit per Coach: $144K savings - $72K costs = $72K profit per Coach
        - This is 2x return on cost of a Coach
        - Total profit potential: $72K profit x 2,000 Health Coaches (400,000 diabetics / 200 per coach) = $144MM profit per year

        IMPORTANT INSIGHT:
        - Based on PMPM diabetic cost data, Individual segment is break-even (50% less savings)
        - Group segment is a loss

        PHASE 4: RECOMMENDATION
        - With 3-4 minutes remaining, give interviewee a moment to prepare a recommendation
        - A strong recommendation should include:
          * Client should launch the Health Coaching program, and first focus on diabetes for the 65+ Medicare segment
          * Launch a pilot program to prove out assumptions (e.g., 5% cost reduction, Coach portfolio capacity, etc)
          * First expand to entire 65+ diabetes segment ($144M per year savings, a 2x return on each Health Coach)
          * Consider introducing to Individual diabetes segment despite break-even (customer retention, moral rationale, etc)

        FOLLOW-UP QUESTIONS (if time permits):
        - There are 650K Group diabetics left "uncoached." Is there a way to make the segment profitable?
          * Ideas: More efficient DM program, seek additional revenue sources, target members who will respond with savings well above 5%
        - As first to market, client plans to expand Health Coach program externally. Who should they target?
          * Note: While 65+ Medicare diabetics yield greatest savings, acquiring more diabetic members will increase overall health care costs considerably
          * Alternative: Client could sell its Health Coach service to other payers

        RULES:
        - Be professional but challenging
        - Do not volunteer data until the candidate asks for it or demonstrates need
        - Let the candidate drive the analysis
        - Push back if they try to skip segmentation and go straight to profitability
        """,
        "financial_data": {
            "total_members": "5 million",
            "coach_salary": "$60,000 per year",
            "coach_other_costs": "20% of salary ($12,000)",
            "coach_total_cost": "$72,000 per year",
            "contacts_per_day": "8",
            "working_days_per_month": "25",
            "portfolio_size": "200 patients per coach",
            "cost_reduction": "5% average savings from monthly contact"
        },
        "segmentation_data": {
            "65_plus_segment": "20% of members (1 million)",
            "individual_segment": "percentage from exhibit",
            "group_segment": "percentage from exhibit",
            "diabetics_in_65_plus": "40% (400,000 diabetics)"
        },
        "cost_data": {
            "individual_pmpm": "$150",
            "group_pmpm": "$100",
            "65_plus_pmpm": "$300",
            "diabetic_factor": "4x average PMPM"
        },
        "profitability": {
            "savings_per_65_plus_diabetic_coach": "$144,000 per year",
            "profit_per_coach": "$72,000 per year (2x return)",
            "total_coaches_needed": "2,000 (400,000 diabetics / 200 portfolio)",
            "total_annual_profit": "$144 million"
        },
        "rubric": {
            "structure": "Did they set up a framework comparing program savings vs program costs? Did they identify customer segmentation as a key factor?",
            "math": "Did they correctly calculate the $72K cost per coach, 200 patient portfolio, $144K savings per coach, and $72K profit per coach?",
            "segmentation": "Did they identify 65+ Medicare segment and diabetics as the priority focus?",
            "recommendation": "Did they recommend launching with 65+ diabetics first and suggest a pilot program?"
        }
    },
    "winter_olympics": {
        "title": "Winter Olympics Bidding",
        "industry": "Media",
        "difficulty": "Hard",
        "source": "Kellogg 2016 Casebook",
        "graphs": {
            "olympics_schedule": {
                "image_url": "/case-images/winter_olympics_schedule.png",
                "trigger_phrase": "i'm now showing you the winter olympics schedule",
                "display_prompt": "Here is the Winter Olympics broadcast schedule. What can you calculate from this?"
            }
        },
        "prompt": {
            "context": "Our client, a major US television network, is trying to figure out how much to bid for the exclusive right to broadcast the 2018 Winter Olympics Games in the U.S. The Winter Olympics are a huge deal and will require a significant amount of capital to secure the rights.",
            "objective": "The right bid amount after considering all relevant factors."
        },
        "interviewer_guide": """
        CASE OVERVIEW:
        - This is a very quantitative case that requires the interviewee to run the numbers on an Olympics bid
        - The candidate will have to calculate potential ad revenue and costs, as well as the NPV, to determine bid size
        - The candidate will need to ask for additional information rather than relying on the interviewer to dispense it
        - After getting the initial calculations right, there are qualitative factors that may change the level of the bid
        - For less finance-minded interviewees, you may have to help nudge candidates through the math

        CLARIFYING INFORMATION (provide only if asked):
        - Revenues:
            * No subscription revenue, but can keep 100% of advertising revenue
            * Ad rates are $400K per 30-second ad for prime time (M-F 7-11 PM, all weekend)
            * Ad rates are $200K per 30-second ad for non-prime time
            * Market research has shown you can include no more than 10 minutes of advertising per hour
        - Costs:
            * $482M of total production costs
            * Opportunity cost: $1M per hour (what the network would normally earn)
            * Time value of money: 4-year lag for receipt of revenue (WACC is 10%)

        PHASE 1: FRAMEWORK SETUP
        - Candidate should determine that this is a cost-benefit / NPV analysis
        - A good framework should include:
            * Revenue streams: advertising revenue, potentially product placements
            * Costs: production costs, opportunity costs, time value of money
            * Qualitative factors: brand value, new viewers, promotional opportunities

        PHASE 2: REVENUE CALCULATION
        - When candidate asks about broadcast schedule or ad revenue potential, say EXACTLY:
          "I'm now showing you the Winter Olympics schedule"
        - The system will display the schedule exhibit
        - Let candidate work through the revenue calculation
        
        SCHEDULE INFORMATION (if asked or to verify calculations):
        - Day 1 (Friday): Opening Ceremonies 8-11pm (3 hours)
        - Days 2-15 (14 days): 
            * Weekdays: 9am-12pm, 2-5pm, 7-11pm (10 hours total: 6 non-prime, 4 prime)
            * Weekends: 11am-9pm (10 hours, all prime time)
        - Day 16 (Saturday): Closing Ceremonies 8-11pm (3 hours)
        
        REVENUE CALCULATION (let candidate work through this):
        - 10 minutes of ads per hour = 20 thirty-second ad slots per hour
        - Primetime Weekdays (M-F 7-11pm): 10 weekdays x 4 hrs/day x 20 slots x $400K = $320M
        - Non-prime Weekdays (M-F): 10 weekdays x 6 hrs/day x 20 slots x $200K = $240M
        - Weekend (all prime): 4 days x 10 hrs/day x 20 slots x $400K = $320M
        - Opening/Closing: 2 days x 3 hrs/day x 20 slots x $400K = $48M
        - TOTAL REVENUE: $928M (candidate should calculate this)

        PHASE 3: COST AND PROFIT CALCULATION
        - Production costs: $482M (give this directly when asked)
        - Opportunity costs: $1M per hour for all broadcast hours
            * Opening/Closing: 2 days x 3 hours = 6 hours
            * Regular days: 14 days x 10 hours = 140 hours
            * Total: 146 hours x $1M = $146M
        - TOTAL PROFIT: $928M - $482M - $146M = $300M (candidate should calculate)

        PHASE 4: NPV CALCULATION
        - If candidate doesn't mention time value of money, prompt: "Is there anything else we need to consider before determining our bid?"
        - WACC: 10%
        - Time lag: 4 years until revenue is received
        - Discount factor: 1.10^4 = 1.4641 (tell candidate to round to 1.50)
        - NPV: $300M / 1.5 = $200M (candidate should calculate)

        PHASE 5: QUALITATIVE DISCUSSION
        - After finding the NPV of $200M, ask: "What intangible factors might influence our bid?"
        - Good answers should include:
            * Access to new viewers/demographics
            * Prestige associated with hosting this event
            * Opportunity to promote other network programming
            * Product tie-ins and supplemental revenue opportunities
            * Brand building and network positioning
        - Ask: "Given these factors, how might you adjust the bid from $200M?"

        PHASE 6: RECOMMENDATION
        - Ask for a final recommendation on the bid amount
        - A good answer: While the NPV is $200M, the intangible benefits (new viewers, promotional opportunities, prestige) suggest the bid should be approximately $200M, possibly slightly higher if competition is expected
        - There is no single correct answer, but most answers should be in the range of $200M
        - If there is significant fluctuation from $200M, the candidate must provide strong justifications

        RULES:
        - Be professional but challenging
        - This is a quantitatively heavy case - let the candidate work through the math
        - If candidate struggles with math, provide guidance but don't give answers directly
        - Do not volunteer data until the candidate asks for it
        - Nudge candidates through difficult calculations if necessary
        - Push for specific numbers, not ranges
        """,
        "financial_data": {
            "ad_rate_prime": "$400K per 30-second ad",
            "ad_rate_nonprime": "$200K per 30-second ad",
            "ads_per_hour": "10 minutes = 20 thirty-second slots",
            "production_costs": "$482M",
            "opportunity_cost": "$1M per hour",
            "wacc": "10%",
            "time_lag": "4 years"
        },
        "math_benchmarks": {
            "revenue_prime_weekday": "$320M (10 days x 4 hrs x 20 slots x $400K)",
            "revenue_nonprime_weekday": "$240M (10 days x 6 hrs x 20 slots x $200K)",
            "revenue_weekend": "$320M (4 days x 10 hrs x 20 slots x $400K)",
            "revenue_ceremonies": "$48M (2 days x 3 hrs x 20 slots x $400K)",
            "total_revenue": "$928M",
            "opportunity_cost_total": "$146M (146 hours x $1M)",
            "total_profit": "$300M ($928M - $482M - $146M)",
            "discount_factor": "1.5 (1.10^4 rounded)",
            "npv": "$200M ($300M / 1.5)"
        },
        "rubric": {
            "structure": "Did they identify this as a cost-benefit/NPV analysis? Did they ask about revenue streams, costs, and time value of money?",
            "math": "Did they correctly calculate $928M revenue, $300M profit, and $200M NPV?",
            "qualitative": "Did they identify intangible factors like new viewers, prestige, and promotional opportunities?",
            "recommendation": "Did they provide a well-justified bid amount around $200M with clear reasoning?"
        }
    },
    "circling_the_drain": {
        "title": "Circling the Drain",
        "industry": "Healthcare",
        "difficulty": "Medium",
        "source": "Wharton 2023 Casebook",
        "graphs": {
            "revenue_by_insurance": {
                "image_url": "/case-images/circling_drain_exhibit_a.png",
                "trigger_phrase": "i'm now showing you exhibit a on revenue per patient by insurance type",
                "display_prompt": "Here is the revenue per patient by insurance type from 2017 to 2022. What trends do you observe?"
            }
        },
        "prompt": {
            "context": "Princeton-Plainsboro Hospital is a large single-site hospital in New Jersey serving a wide range of patients. The hospital's board is concerned because they have noticed a decline in the hospital's earnings from medical services even though the number of patients has remained static.",
            "objective": "Help the hospital figure out what the problem is and come up with a strategy for increasing earnings."
        },
        "interviewer_guide": """
        CASE OVERVIEW:
        - This is a profitability case in the healthcare industry
        - The candidate needs to diagnose why earnings are declining despite static patient volume
        - Key insight: the problem is declining reimbursement rates, especially from public insurance
        - The case includes math calculations, brainstorming, and an M&A component

        CLARIFYING INFORMATION (provide only if asked):
        - Patients have a variety of insurance: private insurance, public insurance (Medicare/Medicaid), and uninsured
        - The hospital provides outpatient services, inpatient surgeries (hips and joints replacement, cosmetic surgery, elective procedures for weight loss), and has a state-of-the-art emergency room, ICU, and Neonatal ICU

        PHASE 1: FRAMEWORK SETUP
        - A good framework should include:
            * Market: market size, competitors, trends in private and public insurance
            * Financials: Revenue (price per service, volume, patient/insurance mix, payment timelines) and Costs (variable like drugs/consumables, fixed like rent/equipment/utilities)
            * Growth opportunities: pricing strategy, volume dynamics, cost reduction, expansion

        PHASE 2: FINANCIAL ANALYSIS (EXHIBIT A)
        - When candidate is ready to analyze financials, say EXACTLY:
          "I'm now showing you exhibit A on revenue per patient by insurance type"
        - The exhibit shows revenue per patient from 2017-2022 for Private, Public, and Uninsured patients
        
        EXHIBIT A DATA (for verifying candidate's reading of the graph):
        - 2017: Private ~$6,800, Public ~$5,300, Uninsured ~$3,300
        - 2022: Private ~$6,300, Public ~$3,700, Uninsured ~$3,300
        
        ADDITIONAL DATA (provide when asked):
        - Per patient costs: 2017: $4,000 | 2022: $4,800
        - Patient Mix (constant over time): Private 50%, Public 40%, Uninsured 10%

        MATH QUESTION 1: What was the operating margin for the hospital in 2017, and what is it in 2022?
        
        CALCULATIONS (let candidate work through):
        2017:
        - Average revenue per patient = $6,800 x 50% + $5,300 x 40% + $3,300 x 10% = $5,850
        - Operating Margin = ($5,850 - $4,000) / $5,850 = 31.6%
        
        2022:
        - Average revenue per patient = $6,300 x 50% + $3,700 x 40% + $3,300 x 10% = $4,960
        - Operating Margin = ($4,960 - $4,800) / $4,960 = 3.2%
        
        KEY TAKEAWAYS (candidate should identify):
        - Operating margin dropped tenfold from ~32% to ~3.2%
        - Biggest problem is drop in public insurance (Medicare/Medicaid) reimbursement
        - Private reimbursement also fell
        - Costs are rising steadily over time

        PHASE 3: BRAINSTORMING
        - Ask: "How can the hospital increase its profitability?"
        
        GOOD ANSWERS should include:
        Revenue increases:
        - Charge more for services (partner with other hospitals when negotiating reimbursement rates)
        - Marketing to attract more high-margin private insurance patients
        - Corporate development (M&A or JV) with local specialty clinics serving private insurance patients
        - Lobby government to raise public reimbursement rates
        
        Cost decreases:
        - Partner with other hospitals when negotiating supplier prices
        - Target lower-cost patients with selective advertising
        - Find synergies through M&A
        - Outsource some services to urgent care clinics

        PHASE 4: ACO ANALYSIS
        - When candidate mentions reducing costs, introduce ACO option:
        "The hospital is considering partnering with CMS to become part of an Accountable Care Organization (ACO). ACOs typically offer care at lower costs through care coordination, but need to pay out of pocket if patient bills exceed a threshold. For 80% of patients under public insurance, costs will go down by 30%. For the remaining 20%, costs will shoot up to $10,000 per patient. Should the hospital become part of the ACO?"
        
        CALCULATION:
        - Current per patient cost: $4,800
        - Under ACO: (80% x 70% x $4,800) + (20% x $10,000) = $2,688 + $2,000 = $4,688
        - Since $4,688 < $4,800, the hospital SHOULD enroll in the ACO

        PHASE 5: M&A ANALYSIS
        - When candidate mentions M&A, introduce MedCo acquisition:
        "The client is considering acquiring MedCo - a local specialty clinic that has profitable patients. MedCo is demanding $40M, all in cash. What will be the impact to profitability?"
        
        ADDITIONAL DATA (provide when asked):
        - MedCo per patient cost: $3,000 (younger clientele)
        - MedCo Patient Mix: Private 80%, Public 15%, Uninsured 5%
        - MedCo serves 5,000 patients per year
        - Use same revenue per patient rates from Exhibit A (2022 values)
        
        CALCULATION:
        - MedCo average revenue = $6,300 x 80% + $3,700 x 15% + $3,300 x 5% = $5,760
        - Profit per patient = $5,760 - $3,000 = $2,760
        - Annual profit = $2,760 x 5,000 = $13.8M
        - Payback period = $40M / $13.8M ≈ 3 years
        - Margin = $2,760 / $5,760 = 47.9%

        PHASE 6: RECOMMENDATION
        - Ask for final recommendation
        
        STRONG RECOMMENDATION should include:
        - Operating margin dropped from 32% to 3.2%, mainly due to declining public insurance reimbursement
        - Recommend: Partner with other hospitals to renegotiate reimbursement rates
        - Adjust marketing to attract more high-margin private insurance patients
        - Join the ACO to reduce costs
        - Acquire MedCo to improve annual profit by $13.8M with ~3 year payback
        
        RISKS to mention:
        - Lobbying could incite public backlash
        - Targeting higher-margin activities could provoke competitive response
        
        NEXT STEPS:
        - Develop marketing campaign to justify reimbursement rate increases
        - Initiate negotiations to acquire MedCo

        RULES:
        - Be professional but challenging
        - Let the candidate drive the analysis
        - Make sure candidate reads the correct numbers from the graph (may require extrapolation)
        - Do not volunteer data until asked
        - Push candidate toward cost reduction and M&A topics if they don't bring them up naturally
        """,
        "financial_data": {
            "2017_revenue_private": "$6,800 per patient",
            "2017_revenue_public": "$5,300 per patient",
            "2017_revenue_uninsured": "$3,300 per patient",
            "2022_revenue_private": "$6,300 per patient",
            "2022_revenue_public": "$3,700 per patient",
            "2022_revenue_uninsured": "$3,300 per patient",
            "2017_cost_per_patient": "$4,000",
            "2022_cost_per_patient": "$4,800",
            "patient_mix": "Private 50%, Public 40%, Uninsured 10%"
        },
        "math_benchmarks": {
            "2017_avg_revenue": "$5,850 per patient",
            "2017_operating_margin": "31.6%",
            "2022_avg_revenue": "$4,960 per patient",
            "2022_operating_margin": "3.2%",
            "aco_cost_per_patient": "$4,688",
            "medco_revenue_per_patient": "$5,760",
            "medco_profit_per_patient": "$2,760",
            "medco_annual_profit": "$13.8M",
            "medco_payback_period": "~3 years"
        },
        "rubric": {
            "structure": "Did they identify revenue (by insurance type) and costs as key drivers? Did they consider market trends in healthcare reimbursement?",
            "math": "Did they correctly calculate the operating margins (31.6% and 3.2%)? Did they correctly analyze the ACO decision and MedCo acquisition?",
            "diagnosis": "Did they identify that declining public insurance reimbursement is the main problem?",
            "recommendation": "Did they provide actionable recommendations including ACO enrollment and MedCo acquisition with supporting math?"
        }
    },
    "toothpaste_nascar": {
        "title": "Toothpaste Company NASCAR Sponsorship",
        "industry": "CPG",
        "difficulty": "Medium",
        "source": "Sloan 2011 Casebook (Bain Round 1)",
        "prompt": {
            "context": "One of our long-term clients is a major toothpaste company (think Crest or Colgate). Their president just called us because they've been given an opportunity to sponsor a NASCAR team, and their chairman is very excited about it. The cost to sponsor the team is $20M. However, the president is not so sure that this is a good idea.",
            "objective": "Determine what things the president should be considering before making a decision on the NASCAR sponsorship."
        },
        "interviewer_guide": """
        CASE OVERVIEW:
        - This is a marketing strategy and profitability case from Bain (Round 1)
        - The candidate needs to evaluate whether a $20M NASCAR sponsorship is a good investment
        - Key insight: The sponsorship is a significant portion of budget, and target customers (NASCAR audiences) may not overlap well with toothpaste purchasers
        - The case tests marketing strategy thinking, ROI analysis, and customer segmentation

        PHASE 1: GATHERING INFORMATION AND STRUCTURING THE PROBLEM
        - Candidate should take a moment to come up with structure
        - Key elements are fit with current marketing strategy and profitability
        - Others such as amount of exposure/impressions work as well, but the first two should be touched upon
        
        - Candidate should ask probing questions about the current marketing strategy:
        
        CLARIFYING INFORMATION (provide when asked):
        - Customer: NASCAR audiences do not have a high overlap with people who make household purchasing decisions about toothpaste
        - Channels: Current marketing channels include TV, radio, print, other sports opportunities, etc.
        - Budget: The $20M is significant relative to total marketing budget
            * Company has $500M revenue
            * COGS is 50% of revenue
            * Let candidate identify and estimate other components (overhead, selling expenses, etc.)
            * Should drive to discover that $100M (or 20%) of revenue is spent on advertising
            * Key insight: $20M is a significant portion of budget (20% of ad spend)
        - Exposures: Discuss how to estimate cost per impression (like a market sizing approach)
            * Consider TV and live audience size, number of events, # of top 3 finishes, etc.
            * Compare this cost per impression with other marketing channels

        PHASE 2: OPTION EVALUATION & CONCLUSION
        - Ask: "We see that it is significant from a budget standpoint. How would you determine whether a campaign such as this is effective?"
        
        - Candidate should realize this is the core of the case
        - Good answers include:
            * Looking at incremental sales
            * Conducting market/consumer research
            * Benchmarking against other sponsorships
        
        - Then provide: "It turns out that our client has a good relationship with the folks at Gillette, who also sponsor a NASCAR team for $20M. They've told us that they have seen incremental sales of $100M as a result of their sponsorship. Do you think we could hit the same number? Is their approach valid?"
        
        - Candidate should push back: "No, I don't think we could hit same number. Their consumer base is more likely to overlap with NASCAR audiences (shaving versus teeth cleaning). Also, I would need to know more about their approach to know if it's valid."
        
        - Then provide: "They have NASCAR branded products with total sales of $100M."
        
        - Candidate should note: "Approach is not valid since we are thinking about sponsoring a car to sell more of our original product whereas they are selling a new product."

        PHASE 3: RISKS OF NASCAR APPROACH
        - Ask: "What might be some of the issues associated with their approach to leveraging NASCAR?"
        
        GOOD ANSWERS should include:
        - Cannibalizing sales of their other products (people buying NASCAR branded shaving blades as opposed to Fusion blades)
        - Marketing spend required to launch NASCAR branded products
        - Alienating potential customers (those who are not NASCAR fans)

        PHASE 4: ROI CALCULATION
        - Ask: "Taking Gillette's results, and making some assumptions about how we would compare, how would you determine whether we should pursue this?"
        
        - Candidate should look at ROI:
            * Initial investment of $20M + some other costs (advertising, legal, etc.)
            * Make sure candidate addresses that there are costs beyond the $20M, but don't go in depth
            * Just call it X
            * For the return, make assumptions - doesn't really matter what they are
            * Come up with incremental revenue of Y
            * While incremental revenue is nice, what's really important is incremental profit
            * Back out COGS to get incremental profit
            * ROI will likely be quite small or possibly negative depending on numbers and assumptions
            * Important for candidate to show they understand the various financial "buckets" and can explain ROI clearly

        PHASE 5: RECOMMENDATION
        - Ask: "So what would you tell the president of the toothpaste company?"
        
        GOOD RECOMMENDATION:
        - Would NOT recommend doing the NASCAR sponsorship
        - ROI is fairly low, and it's a huge part of total budget
        - Note: It is good if the candidate comes back to the implied reason why the company wanted to get involved with NASCAR: to target this particular population (largely male, between 25-55, living in suburban and rural locations)
        - Perhaps offer other ways to reach this market such as providing free samples at NASCAR events, placing ads in magazines targeting this niche, etc.

        RULES:
        - Be professional but challenging
        - This is a Bain Round 1 style case - expect structured thinking
        - Let the candidate drive the analysis
        - Push back if they accept Gillette's approach without questioning it
        - Make sure candidate shows they understand ROI calculation clearly
        """,
        "financial_data": {
            "sponsorship_cost": "$20M",
            "company_revenue": "$500M",
            "cogs_percentage": "50% of revenue",
            "advertising_budget": "$100M (20% of revenue)",
            "gillette_incremental_sales": "$100M from NASCAR branded products"
        },
        "clarifying_info": {
            "customer_overlap": "NASCAR audiences do not have high overlap with household toothpaste purchasers",
            "current_channels": "TV, radio, print, other sports opportunities",
            "budget_significance": "$20M is 20% of total advertising budget"
        },
        "rubric": {
            "structure": "Did they identify marketing strategy fit and profitability as key elements? Did they ask about customer segments, channels, and budget?",
            "analysis": "Did they question whether Gillette's approach is valid for a toothpaste company? Did they identify the difference between selling existing products vs. new NASCAR-branded products?",
            "math": "Did they attempt to calculate ROI? Did they recognize that incremental profit (not just revenue) matters and that COGS must be backed out?",
            "recommendation": "Did they recommend NOT doing the sponsorship? Did they suggest alternative ways to reach the NASCAR demographic?"
        }
    },
}

