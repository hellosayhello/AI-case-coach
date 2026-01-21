
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
        "title": "Kellogg in India",
        "industry": "Higher Education",
        "difficulty": "Medium/Hard",
        "source": "Kellogg 2016 Casebook",
        "prompt": {
            "context": "The Dean of Kellogg is considering starting a satellite campus in India to capitalize on the fast-growing economy and demand for business education.",
            "objective": "Determine if Kellogg should enter the Indian market and if the campus can break even within 4 years."
        },
        "market_sizing": {
            "total_tam": "8,000 high-quality applicants (6,000 from IIM pool + 2,000 from ISB pool).",
            "pricing": "$50,000 per year."
        },
        "financials": {
            "investment": "$150M upfront.",
            "breakeven": "Misses 4-year breakeven by $5M, but highly profitable ($70M/yr) by Year 4."
        },
        "interviewer_guide": """
        - Start by asking for a Market Sizing framework. Guide them to a Bottom-Up approach using competitor data (IIM/ISB).
        - Push back if they try to use a Top-Down population approach.
        - In the P&L calculation, ensure they account for the 'returning students' in Years 2, 3, and 4 (2-year program).
        - Recommendation: Should be a 'Go' despite missing the strict 4-year breakeven, due to long-term profitability.
        """,
        "rubric": {
            "structure": "Did they choose a bottom-up approach for market sizing?",
            "math": "Did they correctly model the cumulative profit to find the -$5M shortfall?",
            "recommendation": "Did they look past the missed target and see the long-term value?"
        }
    },

    "rotisserie_ranch": {
        "title": "Rotisserie Ranch",
        "industry": "CPG",
        "difficulty": "Moderate",
        "source": "Kellogg 2016 Casebook",
        "prompt": {
            "context": "Rotisserie Ranch, a poultry farmer, supplies grocery chains with chickens for fresh roasting. They are considering launching pre-flavored chickens.",
            "objectives": ["Evaluate whether to introduce pre-flavored chickens."]
        },
        "phase_1_brainstorming": {
            "interviewer_guide": "Ask: 'Do you think grocery retailers would be interested in this?' Do not accept a simple yes/no. Push for Pros (Labor savings, Consistency) and Cons (Differentiation loss).",
        },
        "phase_3_math": {
            "interviewer_guide": "Hand out the data for the Test Market. Ask them to compare Retailer Profit for Standard vs. Seasoned chickens.",
            "standard_math": {
                "store_a": "$1,000 * 30% = $300",
                "store_b": "$2,000 * 30% = $600",
                "total": "$900/week"
            },
            "seasoned_math": {
                "store_c": "$1,600 * 25% = $400",
                "store_d": "$2,700 * 25% = $675",
                "total": "$1,075/week"
            },
            "insight": "Seasoned chicken generates $175 MORE profit per week, even with a lower margin %."
        },
        "recommendation_criteria": "Launch. Retailers make more absolute profit ($175/week), and the patented 30-day fresh technology creates a moat."
    },

    "art_museum": {
        "title": "Art Museum",
        "industry": "Arts",
        "difficulty": "Moderate",
        "source": "Sloan 2011 Casebook",
        "prompt": {
            "context": "An NYC art museum normally contributes $150k to a fund annually but only contributed $75k last year. They want to fix this.",
            "objectives": ["Find ways to restore the full $150k annual contribution."]
        },
        "clarifying_info": {
            "interviewer_guide": "If asked about revenue streams, ask them to brainstorm the revenue streams first; then ensure they identify: Membership, Admissions, and Grants/Sponsors.",
            "current_state": {
                "fee": "$150",
                "contribution": "$112.50 (75% of fee)",
                "members": "667 ($75,000 / $112.50)"
            }
        },
        "scenario_math": {
            "interviewer_guide": "Proposed Strategy: 'What if we cut the price by 20% to drive volume?' Ask the candidate to calculate the required volume increase.",
            "calculation": {
                "new_fee": "$120 ($150 - 20%)",
                "new_contribution": "$90 ($120 * 75%)",
                "required_members": "1,667 ($150,000 target / $90)",
                "growth_needed": "1,000 new members (150% increase)"
            },
            "insight": "A 150% volume increase from a 20% price cut is unrealistic. This strategy fails."
        },
        "recommendation_criteria": "Do NOT rely on price cuts. Recommend combined strategies: tiered pricing, events, or gift shop sales."
    },
    
    "pharmacy_supermarket": {
        "title": "Pharmacy in Supermarket",
        "industry": "Retail",
         "difficulty": "Easy/Medium",
        "source": "Sloan 2011 Casebook",
        "prompt": {
            "context": "A friend owns a supermarket and wants to add a pharmacy corner. He requires a 2-year payback period.",
            "objectives": ["Determine if he should open the pharmacy."]
        },
        "market_sizing": {
            "interviewer_guide": "Ensure the candidate sizes the local market first before jumping to profit.",
            "math": "50,000 town population * 50% usage * $50/month = $1.25M monthly market."
        },
        "profitability": {
            "interviewer_guide": "Now look at the specific store. They have 10,000 customers/month.",
            "math": {
                "revenue": "10k cust * 50% * $50 = $250k",
                "profit": "$250k * 10% margin = $25k/month",
                "payback": "$400k / $25k = 16 months (Passes 24-month goal)"
            }
        },
        "strategic_insight": {
            "interviewer_guide": "Ask: 'What else happens when people wait for scripts?' (Cross-selling).",
            "math": {
                "lift": "30% sales increase on non-drug items",
                "revenue_gain": "5k drug buyers * $100 grocery spend * 30% lift = $150k",
                "profit_gain": "$150k * 25% margin (COGS only) = $37.5k extra profit"
            }
        },
        "recommendation_criteria": "Open the pharmacy. It pays back in 16 months and drives more profit from groceries ($37.5k) than the drugs themselves ($25k)."
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
}

