class personalityInterpreter {
  const highValue = 0.65;
  const lowValue = 0.35;

  // Provide this method with an object: {facet: percentile, [...]. For exampl: {facet_altruism: 0.92928, facet_cooperation: 0.38433}
  // Returns an array of strings, describing the most prominent traids of the author in connection to agreeableness.
  interpretAgreeableness(big5_agreeableness) {
    big5_openness = {facet_altruism, facet_cooperation, facet_modesty, facet_morality, facet_sympathy, facet_trust};
    let result = [];

    if (Altruism > highValue) {
      result.push('You feel fulfilled when helping others and will go out of your way to do so.');
    } else if (Altruism < lowValue) {
      result.push('You are more concerned with taking care of yourself than taking time for others.');
    }

    if (Cooperation > highValue) {
      result.push('You are easy to please and try to avoid confrontation.');
    } else if (Cooperation < lowValue) {
      result.push('You do not shy away from contradicting others.');
    }

    if (Modesty > highValue) {
      result.push('You are uncomfortable being the center of attention.');
    } else if (Modesty < lowValue) {
      result.push('You hold yourself in high regard and are satisfied with who you are.');
    }

    if (Morality > highValue) {
      result.push('You think it is wrong to take advantage of others to get ahead.');
    } else if (Morality < lowValue) {
      result.push('You are comfortable using every trick in the book to get what you want.');
    }

    if (Sympathy > highValue) {
      result.push('You feel what others feel and are compassionate toward them.');
    } else if (Sympathy < lowValue) {
      result.push('You think people should generally rely more on themselves than on others.');
    }

    if (Trust > highValue) {
      result.push('You believe the best of others and trust people easily.');
    } else if (Trust < lowValue) {
      result.push('You are wary of other peoples intentions and do not trust easily.');
    }

    return result;
  }

/*
  // Returns an array of strings, describing the most prominent traids of the author in connection to Conscientiousness.
  interpretConscientiousness(data) {
    data = {AchievementStriving, Cautiousness, Dutifulness, Orderliness, SelfDiscipline, SelfEfficacy};
    let result = [];

    if (AchievementStriving > highValue) {
      result.push('You set high goals for yourself and work hard to achieve them.');
    } else if (AchievementStriving < lowValue) {
      result.push('You are content with your level of accomplishment and do not feel the need to set ambitious goals.');
    }

    if (Cautiousness > highValue) {
      result.push('You carefully think through decisions before making them.');
    } else if (Cautiousness < lowValue) {
      result.push('You would rather take action immediately than spend time deliberating making a decision.');
    }

    if (Dutifulness > highValue) {
      result.push('You take rules and obligations seriously, even when they are inconvenient.');
    } else if (Dutifulness < lowValue) {
      result.push('You do what you want, disregarding rules and obligations.');
    }

    if (Orderliness > highValue) {
      result.push('You feel a strong need for structure in your life.');
    } else if (Orderliness < lowValue) {
      result.push('You do not make a lot of time for organization in your daily life.');
    }

    if (SelfDiscipline > highValue) {
      result.push('You can tackle and stick with tough tasks.');
    } else if (SelfDiscipline < lowValue) {
      result.push('You have a hard time sticking with difficult tasks for a long period of time.');
    }

    if (SelfEfficacy > highValue) {
      result.push('You feel you have the ability to succeed in the tasks you set out to do.');
    } else if (SelfEfficacy < lowValue) {
      result.push('You frequently doubt your ability to achieve your goals.');
    }

    return result;
  }
  */
}
