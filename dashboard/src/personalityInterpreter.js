class personalityInterpreter {
  // Provide this method with an object: { facet: percentile, [...] }. For exampl: { facet_altruism: 0.92928, facet_cooperation: 0.38433 }
  // Returns an array of strings, describing the most prominent traids of the author in connection to agreeableness.
  interpretAgreeableness(big5_agreeableness) {
    const highValue = 0.65;
    const lowValue = 0.35;
    big5_agreeableness = { facet_altruism, facet_cooperation, facet_modesty, facet_morality, facet_sympathy, facet_trust };
    let result = [];

    if (facet_altruism > highValue) {
      result.push('You feel fulfilled when helping others and will go out of your way to do so.');
    } else if (facet_altruism < lowValue) {
      result.push('You are more concerned with taking care of yourself than taking time for others.');
    }

    if (facet_cooperation > highValue) {
      result.push('You are easy to please and try to avoid confrontation.');
    } else if (facet_cooperation < lowValue) {
      result.push('You do not shy away from contradicting others.');
    }

    if (facet_modesty > highValue) {
      result.push('You are uncomfortable being the center of attention.');
    } else if (facet_modesty < lowValue) {
      result.push('You hold yourself in high regard and are satisfied with who you are.');
    }

    if (facet_morality > highValue) {
      result.push('You think it is wrong to take advantage of others to get ahead.');
    } else if (facet_morality < lowValue) {
      result.push('You are comfortable using every trick in the book to get what you want.');
    }

    if (facet_sympathy > highValue) {
      result.push('You feel what others feel and are compassionate toward them.');
    } else if (facet_sympathy < lowValue) {
      result.push('You think people should generally rely more on themselves than on others.');
    }

    if (facet_trust > highValue) {
      result.push('You believe the best of others and trust people easily.');
    } else if (facet_trust < lowValue) {
      result.push('You are wary of other peoples intentions and do not trust easily.');
    }

    return result;
  }


  // Returns an array of strings, describing the most prominent traids of the author in connection to Conscientiousness.
  interpretConscientiousness(big5_conscientiousness) {
    const highValue = 0.65;
    const lowValue = 0.35;
    data = { facet_achievement_striving, facet_cautiousness, facet_dutifulness, facet_orderliness, facet_self_discipline, facet_self_efficacy};
    let result = [];

    if (facet_achievement_striving > highValue) {
      result.push('You set high goals for yourself and work hard to achieve them.');
    } else if (facet_achievement_striving < lowValue) {
      result.push('You are content with your level of accomplishment and do not feel the need to set ambitious goals.');
    }

    if (facet_cautiousness > highValue) {
      result.push('You carefully think through decisions before making them.');
    } else if (facet_cautiousness < lowValue) {
      result.push('You would rather take action immediately than spend time deliberating making a decision.');
    }

    if (facet_dutifulness > highValue) {
      result.push('You take rules and obligations seriously, even when they are inconvenient.');
    } else if (facet_dutifulness < lowValue) {
      result.push('You do what you want, disregarding rules and obligations.');
    }

    if (facet_orderliness > highValue) {
      result.push('You feel a strong need for structure in your life.');
    } else if (facet_orderliness < lowValue) {
      result.push('You do not make a lot of time for organization in your daily life.');
    }

    if (facet_self_discipline > highValue) {
      result.push('You can tackle and stick with tough tasks.');
    } else if (facet_self_discipline < lowValue) {
      result.push('You have a hard time sticking with difficult tasks for a long period of time.');
    }

    if (facet_self_efficacy > highValue) {
      result.push('You feel you have the ability to succeed in the tasks you set out to do.');
    } else if (facet_self_efficacy < lowValue) {
      result.push('You frequently doubt your ability to achieve your goals.');
    }

    return result;
  }

}
