# Sample Workflow Layout

Most complex workflows come with a few caveats:

1) **Long waiting times**: Between each step, in certain workflows like say ML there maybe long waiting times (waiting for training,preprocessing to finish, waiting for resources to be provisioned etc). This can lead to wastage of resources provisioned to the DAG in the long term.

    **Solution**: Use multiple DAGs (different DAG definitions altogether) that run independently of eachother in fashion like this:

    - DAG1 - Preprocess data and dump all preprocessed data to disk/db/cache.

    `DAG1 Triggers DAG2 before exiting and passes all relevant information to DAG2.`

    - DAG2 - Train Model and dump all trained data to disk/db/cache.

    `DAG2 Triggers DAG3 before exiting and passes all relevant information to DAG3.`

    ...and so on.

    This way the DAGs are independent of eachother and will provide consistent tracking. You can also scale this example to work when there is additional user input being awaited, which could take days.

    Example: A simple Support ticket workflow.

    - DAG1 is triggered when user creates a support ticket via support.

    - DAG1 ends its operation by assigning a support agent.

    - Agent logs in, helps customer and triggers DAG2 which tracks all his work. (Onboard user, update ticket status, offer help, escalate issue).

    `This may take days between escalations as everyone who has dealt with customer care knows. It would be a waste to have an instance running for days with no input.`

    - DAG3 would be triggered when a new escalation happens or it could be same DAG2 with another agent depending on how you create your DAGs.


## Conclusion

In conclusion one can design a resource efficient DAG without compromising on the actual workflow.
