from production import AND, OR, NOT, PASS, FAIL, IF, THEN, \
     match, populate, simplify, variables
from zookeeper import ZOOKEEPER_RULES

# This function, which you need to write, takes in a hypothesis
# that can be determined using a set of rules, and outputs a goal
# tree of which statements it would need to test to prove that
# hypothesis. Refer to the problem set (section 2) for more
# detailed specifications and examples.

# Note that this function is supposed to be a general
# backchainer.  You should not hard-code anything that is
# specific to a particular rule set.  The backchainer will be
# tested on things other than ZOOKEEPER_RULES.


def backchain_to_goal_tree(rules, hypothesis):
    return rule_match_goal_tree(hypothesis,rules)



def rule_match_goal_tree(hypothesis,rules):
    subtrees = [hypothesis]
    for rule in rules:
        for consequent in rule.consequent():
            binding = match(consequent,hypothesis)
            if binding is not None:
                subtrees.append(antecedents_goal_tree(rule,rules,binding))
    return simplify(OR(subtrees))


def antecedents_goal_tree(rule,rules,binding):
    subtrees = []
    if type(rule.antecedent()) != type(''):
        for antecedent in rule.antecedent():
            hypothesis = populate(antecedent,binding)
            subtrees.append(rule_match_goal_tree(hypothesis,rules))
        return simplify(rule.antecedent().__class__(subtrees))
    else:
        hypothesis = populate(rule.antecedent(),binding)
        subtrees.append(rule_match_goal_tree(hypothesis,rules))
        return simplify(OR(subtrees))
        
        
        

# Here's an example of running the backward chainer - uncomment
# it to see it work:
#print backchain_to_goal_tree(ZOOKEEPER_RULES, 'opus is a penguin')
