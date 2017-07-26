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


  // Provide this method with an object: { facet: percentile, [...] }. For exampl: { facet_altruism: 0.92928, facet_cooperation: 0.38433 }
  // Returns an array of strings, describing the most prominent traids of the author in connection to conscientiousness.
  interpretConscientiousness(big5_conscientiousness) {
    const highValue = 0.65;
    const lowValue = 0.35;
    big5_conscientiousness = { facet_achievement_striving, facet_cautiousness, facet_dutifulness, facet_orderliness, facet_self_discipline, facet_self_efficacy};
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


  // Provide this method with an object: { facet: percentile, [...] }. For exampl: { facet_altruism: 0.92928, facet_cooperation: 0.38433 }
  // Returns an array of strings, describing the most prominent traids of the author in connection to extraversion.
  interpretExtraversion(big5_extraversion) {
    const highValue = 0.65;
    const lowValue = 0.35;
    big5_extraversion = { facet_activity_level, facet_assertiveness, facet_cheerfulness, facet_Excitement_seeking, facet_friendliness, facet_gregariousness};
    let result = [];

    if (facet_activity_level > highValue) {
      result.push('You enjoy a fast-paced, busy schedule with many activities.');
    } else if (facet_activity_level < lowValue) {
      result.push('You appreciate a relaxed pace in life.');
    }

    if (facet_assertiveness > highValue) {
      result.push('You tend to speak up and take charge of situations, and you are comfortable leading groups.');
    } else if (facet_assertiveness < lowValue) {
      result.push('You prefer to listen than to talk, especially in group settings.');
    }

    if (facet_cheerfulness > highValue) {
      result.push('You are a joyful person and share that joy with the world.');
    } else if (facet_cheerfulness < lowValue) {
      result.push('You are generally serious and do not joke much.');
    }

    if (facet_Excitement_seeking > highValue) {
      result.push('You are excited by taking risks and feel bored without lots of action going on.');
    } else if (facet_Excitement_seeking < lowValue) {
      result.push('You prefer activities that are quiet, calm, and safe.');
    }

    if (facet_friendliness > highValue) {
      result.push('You make friends easily and feel comfortable around other people.');
    } else if (facet_friendliness < lowValue) {
      result.push('You are a private person and do not let many people in.');
    }

    if (facet_gregariousness > highValue) {
      result.push('You enjoy being in the company of others.');
    } else if (facet_gregariousness < lowValue) {
      result.push('You have a strong desire to have time to yourself.');
    }

    return result;
  }


  // Provide this method with an object: { facet: percentile, [...] }. For exampl: { facet_altruism: 0.92928, facet_cooperation: 0.38433 }
  // Returns an array of strings, describing the most prominent traids of the author in connection to emotional range.
  interpretEmotionalRange(big5_emotional_range) {
    const highValue = 0.65;
    const lowValue = 0.35;
    big5_emotional_range = { facet_anger, facet_anxiety, facet_depression, facet_immoderation, facet_self_consciousness, facet_vulnerability};
    let result = [];

    if (facet_anger > highValue) {
      result.push('You have a fiery temper, especially when things do not go your way.');
    } else if (facet_anger < lowValue) {
      result.push('It takes a lot to get you angry.');
    }

    if (facet_anxiety > highValue) {
      result.push('You tend to worry about things that might happen.');
    } else if (facet_anxiety < lowValue) {
      result.push('You tend to feel calm and self-assured.');
    }

    if (facet_depression > highValue) {
      result.push('You think quite often about the things you are unhappy about.');
    } else if (facet_depression < lowValue) {
      result.push('You are generally comfortable with yourself as you are.');
    }

    if (facet_immoderation > highValue) {
      result.push('You feel your desires strongly and are easily tempted by them.');
    } else if (facet_immoderation < lowValue) {
      result.push('You have control over your desires, which are not particularly intense.');
    }

    if (facet_self_consciousness > highValue) {
      result.push('You are sensitive about what others might be thinking of you.');
    } else if (facet_self_consciousness < lowValue) {
      result.push('You are hard to embarrass and are self-confident most of the time.');
    }

    if (facet_vulnerability > highValue) {
      result.push('You are easily overwhelmed in stressful situations.');
    } else if (facet_vulnerability < lowValue) {
      result.push('You handle unexpected events calmly and effectively.');
    }

    return result;
  }


  // Provide this method with an object: { facet: percentile, [...] }. For exampl: { facet_altruism: 0.92928, facet_cooperation: 0.38433 }
  // Returns an array of strings, describing the most prominent traids of the author in connection to openness.
  interpretOpenness(big5_openness) {
    const highValue = 0.65;
    const lowValue = 0.35;
    big5_openness = { facet_adventurousness, facet_artistic_interests, facet_emotionality, facet_imagination, facet_intellect, facet_liberalism};
    let result = [];

    if (facet_adventurousness > highValue) {
      result.push('You are eager to experience new things.');
    } else if (facet_adventurousness < lowValue) {
      result.push('You enjoy familiar routines and prefer not to deviate from them.');
    }

    if (facet_artistic_interests > highValue) {
      result.push('You enjoy beauty and seek out creative experiences.');
    } else if (facet_artistic_interests < lowValue) {
      result.push('You are less concerned with artistic or creative activities than most people.');
    }

    if (facet_emotionality > highValue) {
      result.push('You are aware of your feelings and how to express them.');
    } else if (facet_emotionality < lowValue) {
      result.push('You do not frequently think about or openly express your emotions.');
    }

    if (facet_imagination > highValue) {
      result.push('You have a wild imagination.');
    } else if (facet_imagination < lowValue) {
      result.push('You prefer facts over fantasy.');
    }

    if (facet_intellect > highValue) {
      result.push('You are open to and intrigued by new ideas and love to explore them.');
    } else if (facet_intellect < lowValue) {
      result.push('You prefer dealing with the world as it is, rarely considering abstract ideas.');
    }

    if (facet_liberalism > highValue) {
      result.push('You prefer to challenge authority and traditional values to help bring about change.');
    } else if (facet_liberalism < lowValue) {
      result.push('You prefer following with tradition to maintain a sense of stability.');
    }

    return result;
  }
}
