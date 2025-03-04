import datetime
from typing import Dict, Callable

from smart_home.core.system import HomeAutomationSystem


class Rule:
    """Represents an automation rule in the system."""
    
    def __init__(self, name: str, condition_fn: Callable, action_fn: Callable, enabled: bool = True):
        """Initialize a new rule.
        
        Args:
            name: Human-readable name for the rule
            condition_fn: Function that determines if the rule should trigger
            action_fn: Function that executes when the rule is triggered
            enabled: Whether the rule is initially enabled
        """
        self.name = name
        self.condition_fn = condition_fn
        self.action_fn = action_fn
        self.enabled = enabled
        self.last_triggered = None
        
    def evaluate(self, system: HomeAutomationSystem) -> bool:
        """Evaluate the rule condition and trigger action if needed.
        
        Args:
            system: The home automation system to evaluate against
            
        Returns:
            True if the rule was triggered, False otherwise
        """
        if not self.enabled:
            return False
            
        if self.condition_fn(system):
            self.action_fn(system)
            self.last_triggered = datetime.datetime.now()
            return True
            
        return False


class RulesEngine:
    """Engine that manages and evaluates automation rules."""
    
    def __init__(self, home_system: HomeAutomationSystem):
        """Initialize a new rules engine.
        
        Args:
            home_system: The home automation system to control
        """
        self.home_system = home_system
        self.rules: Dict[str, Rule] = {}
        
    def add_rule(self, rule: Rule) -> str:
        """Add a rule to the engine.
        
        Args:
            rule: The rule to add
            
        Returns:
            The ID assigned to the rule
        """
        import uuid
        rule_id = str(uuid.uuid4())
        self.rules[rule_id] = rule
        return rule_id
        
    def remove_rule(self, rule_id: str) -> bool:
        """Remove a rule from the engine.
        
        Args:
            rule_id: ID of the rule to remove
            
        Returns:
            True if the rule was found and removed, False otherwise
        """
        if rule_id in self.rules:
            del self.rules[rule_id]
            return True
        return False
        
    def enable_rule(self, rule_id: str) -> bool:
        """Enable a rule.
        
        Args:
            rule_id: ID of the rule to enable
            
        Returns:
            True if the rule was found and enabled, False otherwise
        """
        if rule_id in self.rules:
            self.rules[rule_id].enabled = True
            return True
        return False
        
    def disable_rule(self, rule_id: str) -> bool:
        """Disable a rule.
        
        Args:
            rule_id: ID of the rule to disable
            
        Returns:
            True if the rule was found and disabled, False otherwise
        """
        if rule_id in self.rules:
            self.rules[rule_id].enabled = False
            return True
        return False
        
    def evaluate_all_rules(self):
        """Evaluate all rules in the engine."""
        for rule_id, rule in self.rules.items():
            triggered = rule.evaluate(self.home_system)
            if triggered:
                self.home_system.log_event("rule_triggered", {
                    "rule_id": rule_id,
                    "rule_name": rule.name,
                    "timestamp": datetime.datetime.now().isoformat()
                })