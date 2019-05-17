# Budget
Don't edit this - the RPPR generater populates this section

# Research Design
DREAM challenges are an instrumental tool for harnessing the wisdom of the broader scientific community to develop computational solutions to biomedical problems. While previous DREAM challenges have worked with complex biological data as well as sensitive medical data, running DREAM Challenges with Electronic Health Records present unique complications, patient privacy being at the forefront of those concerns. Previous challenges have developed a technique known as the Model to Data (MTD) approach to maintain the privacy of the data. We will be using this MTD approach, facilitated by docker, on an OMOP dataset provided by the University of Washington to make development of models standardized.

# Methodology
We will ask participants of this DREAM Challenge to predict the future mortality status of currently living patients within our OMOP repository. After participants predict, we will evaluate the model performances against a gold standard benchmark dataset. We will carry out this DREAM challenge in three phases.

The Open Phase will be a preliminary testing and validation phase. In this phase, the Synpuf synthetic OMOP data will be used to test submitted models. Participants will submit their predictive models to our system where those models will train and predict on the split Synpuf dataset. The main objectives of the first phase are to allow the participants to become familiar with the submission system, to allow the organizers to work out any issues in the pipeline, and to give participants a preliminary ranking on the performance of their model.

The Leaderboard Phase will be the prospective prediction phase carried out on UW OMOP data. Participants will submit their models which will have a portion of the UW OMOP repository available to them for training, making predictions on all living patients who have had at least one visit in the previous month. They will predict whether these patients will be deceased in the next 6 months by assigning a probability score to each of the patients. Participants will be expected to setup up their own training dataset but the patient numbers for which a prediction is expected will be provided to the docker models.

The Validation Phase will be the final evaluation phase where challenge admins are able to finalize the scores of the models.

# Expected Outcomes
1. Code and Dockerized package for deploying an evaluation harness (e.g. Model to Data) for predictive algorithms applied against an OMOP CDM.
2. NCATS deployed and hosted evaluation harnesss using the OMOP CDM (see Deliverable #1) populated with SynPUFF data.
3. Best practices and Standard Operating Procedure documentation for prospective model evaluation and benchmarking on EHR data.
4. Library of Dockerized algorithms for prediction of patient mortality - acquired through EHR DREAM Challenge - with performance metrics.

# Deliverables
1. Code and Dockerized package for deploying an evaluation harness (e.g. Model to Data) for predictive algorithms applied against an OMOP CDM.
2. NCATS deployed and hosted evaluation harnesss using the OMOP CDM (see Deliverable #1) populated with SynPUFF data. 
3. Best practices and Standard Operating Procedure documentation for prospective model evaluation and benchmarking on EHR data.
4. Library of Dockerized algorithms for prediction of patient mortality - acquired through EHR DREAM Challenge - with performance metrics.

# Timeline (monthly)
 Due Date | Milestone    | Status     | 
|:----------|:--------------:|------------:|
Feb 4 | Complete the aggregation and quality assessment of the UW cohort that will be used in the study. | [Done](https://github.com/data2health/DREAM-Challenge/milestone/1)
Feb 27 | Conduct an internal evaluation by applying previously developed models to the UW cohort. | [Ongoing](https://github.com/data2health/DREAM-Challenge/milestone/2)
March 6 | Survey the CTSAs to find which sites have mortality and 30-day re-admission prediction models that would be willing to participate. | [Not Started](https://github.com/data2health/DREAM-Challenge/milestone/3)
March 20 | Build the Synapse pilot challenge site with instructions for participating in the challenge. | [Ongoing](https://github.com/data2health/DREAM-Challenge/milestone/4)
April | Build the infrastructure for facilitating the DREAM challenge, using Docker, Synapse, and UW servers. | [Ongoing](https://github.com/data2health/DREAM-Challenge/milestone/5)
June | **Phase 1**: Have a period of time where the parties identified in step 1 submit their models to predict on UW patients. This will not be a prospective evaluation. | [Not Started](https://github.com/data2health/DREAM-Challenge/milestone/6)
Summer | **Phase 2**: Prospectively evaluate model performances, evaluating accuracy and recall between models. | [Not Started](https://github.com/data2health/DREAM-Challenge/milestone/7)
Jan 2020 | Make scripts and documentation available for the CTSAs. | [Ongoing](https://github.com/data2health/DREAM-Challenge/milestone/8)

# Potential Pitfalls and Alternative Strategies
In this Challenge, we are asking participants to submit mortality prediction algorithms that are trained using data to which they have direct accesss, or to do more limited (blinded) training on data provided within the UW EHR system. In the former case, the models may not generalize well to the UW validation cohort, and in the latter case, training on hidden data - using a Docker container - may not provide sufficient information to robustly train a model. To overcome both of these limitations, we will explore the use of simulated data derived from the underlying distributions of the EHR cohort. This will facilitate model training as data scientists are accustomed, i.e. working directly with the data, while simultaneously not distributing sensitive patient information.   
