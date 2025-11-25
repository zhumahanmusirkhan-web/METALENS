# METALENS BOT - ULTIMATE COGNITIVE MASTERPIECE v7.0
# REVOLUTIONARY EDITION: Flawless, Ultimate, Perfect with HTML Formatting & Storytelling
# ENHANCED WITH FLASHCARD GAME AND COMMAND SUGGESTIONS

import os
import sqlite3
import logging
import random
import asyncio
import json
import re
import math
from datetime import datetime, timedelta
from collections import defaultdict, Counter
from typing import Dict, List, Tuple, Optional
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, MessageHandler, CallbackQueryHandler, 
    ContextTypes, filters
)

# ========== ULTIMATE REVOLUTIONARY SETUP ==========
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = '7146227356:AAGJUNwvIHYxFlyTnAENWY6PjnNI3EeXflQ'

# ========== ENHANCED AUDIO PRONUNCIATION SYSTEM ==========
AUDIO_BASE_URL = "https://raw.githubusercontent.com/zhumahanmusirkhan-web/METALENS/main/"

PRONUNCIATION_FILES = {
    "кітаптарымыздан": "kz_kitaptarymyzdan.mp3",
    "жүгірушілерге": "kz_zhugirushilerge.mp3", 
    "балаларға": "kz_balalargha.mp3",
    "үйлерімізде": "kz_uylerimizde.mp3",
    "unbelievableness": "en_unbelievableness.mp3",
    "internationalization": "en_internationalization.mp3",
    "переосмысление": "ru_pereosmyslenie.mp3",
    "взаимопонимание": "ru_vzaimoponimanie.mp3",
    "öğrencilerimizin": "tr_ogrencilerimizin.mp3",
    "anlayışınız": "tr_anlayisiniz.mp3"
}

# ========== STORYTELLING AUDIO FILES ==========
STORY_AUDIO_FILES = {
    "neural_awakening": {
        1: "story_neural_awakening_ch1.mp3",
        2: "story_neural_awakening_ch2.mp3", 
        3: "story_neural_awakening_ch3.mp3",
        4: "story_neural_awakening_ch4.mp3",
        5: "story_neural_awakening_ch5.mp3"
    },
    "language_detective": {
        1: "story_detective_ch1.mp3"
    }
}

# ========== ULTIMATE STORYTELLING DATABASE ==========
STORY_DATABASE = {
    "neural_awakening": {
        "title": "🧠 The Neural Awakening",
        "language": "multilingual",
        "difficulty": "intermediate",
        "duration": "8-10 minutes",
        "chapters": 5,
        "target_vocabulary": ["cognitive", "neural", "pathway", "analysis", "linguistic", "morphological", "activation"],
        "description": "A sci-fi adventure about a linguist who discovers the power of morphological analysis to unlock hidden neural capabilities",
        "cover_image": "story_neural_cover.jpg",
        "chapters": {
            1: {
                "title": "The Discovery",
                "text": """
🌌 <b>CHAPTER 1: The Discovery</b>

Dr. Aisha stared at the complex Kazakh word on her screen: <code>кітаптарымыздан</code>. As a cognitive linguist at the Advanced Language Research Institute, she had analyzed thousands of words, but this one felt different - it seemed to pulse with hidden energy.

"Computer, run deep morphological analysis," she commanded, her voice barely above a whisper.

The system responded instantly, projecting holographic morphemes into the air:
• <code>кітап</code> (root: book) - <i>the foundational concept</i>
• <code>+ -тар-</code> (plural) - <i>quantification marker</i>  
• <code>+ -ымыз-</code> (our) - <i>possessive relational marker</i>
• <code>+ -дан</code> (from) - <i>spatial-temporal marker</i>

Suddenly, her neural interface flickered violently. "Cognitive overload detected," the computer warned in its calm synthetic voice. But Aisha felt something else entirely - a profound connection forming in the deepest layers of her mind, as if the word itself was speaking to her.

💡 <b>Vocabulary Focus:</b> morphological, analysis, cognitive, neural, quantification, possessive
🧠 <b>Cognitive Activation:</b> Broca's area - Wernicke's area - Angular gyrus
                """,
                "audio_file": "story_neural_awakening_ch1.mp3",
                "interactive_choices": [
                    {
                        "text": "🔬 Continue deep analysis", 
                        "next_chapter": 2, 
                        "cognitive_effect": "pattern_recognition",
                        "narration": "You choose to push forward, embracing the cognitive challenge..."
                    },
                    {
                        "text": "🔄 Run neural diagnostics", 
                        "next_chapter": 2, 
                        "cognitive_effect": "analytical_thinking",
                        "narration": "You prioritize safety, running comprehensive system checks..."
                    }
                ],
                "comprehension_questions": [
                    {
                        "question": "What morphological component indicates plurality in the analyzed word?",
                        "options": ["-тар-", "-ымыз-", "-дан", "кітап"],
                        "correct": 0,
                        "explanation": "The suffix '-тар-' indicates plural form in Kazakh, transforming 'book' into 'books'"
                    },
                    {
                        "question": "Which brain area was primarily activated during the analysis?",
                        "options": ["Broca's area", "Visual cortex", "Cerebellum", "Amygdala"],
                        "correct": 0,
                        "explanation": "Broca's area is crucial for language processing and morphological analysis"
                    }
                ],
                "vocabulary_highlight": [
                    {"word": "morphological", "definition": "relating to the structure and form of words"},
                    {"word": "cognitive", "definition": "related to mental processes of understanding"},
                    {"word": "neural", "definition": "pertaining to nerves or the nervous system"}
                ]
            },
            2: {
                "title": "The Connection Forms", 
                "text": """
🔗 <b>CHAPTER 2: The Connection Forms</b>

Aisha's vision blurred as neural pathways she never knew existed began firing simultaneously. She could see the word's structure not just on screen, but in her mind's eye - a shimmering lattice of interconnected meanings.

"Fascinating," she whispered, her fingers trembling as she analyzed the Turkish word <code>öğrencilerimizin</code> without conscious effort. The breakdown appeared instantly in her neural display:
• <code>öğrenci</code> (student) - <i>the core concept of learning</i>
• <code>+ -ler</code> (plural) - <i>multiple instances marker</i>
• <code>+ -imiz</code> (our) - <i>inclusive possessive marker</i> 
• <code>+ -in</code> (of) - <i>genitive relationship marker</i>

Her Russian colleague, Ivan, burst into the lab, his face etched with concern. "Aisha, are you well? Your neural readings are off the charts!"

"I can see the patterns, Ivan! Not just individual words, but the universal grammar connecting them! The morphological structures are activating my Broca's area directly - it's like I'm thinking in multiple languages simultaneously!"

Ivan stared in awe as Aisha effortlessly analyzed the Russian word <code>переосмысление</code>, her mind processing:
• <code>пере-</code> (re-) - <i>iterative prefix</i>
• <code>осмысл</code> (meaning) - <i>semantic root</i>
• <code>+ -ение</code> (noun suffix) - <i>nominalization marker</i>

🎯 <b>Cross-Linguistic Insight:</b> Notice how different languages express possession and plurality through systematic morphological patterns!
🌍 <b>Universal Grammar:</b> The deep structure remains consistent across surface variations
                """,
                "audio_file": "story_neural_awakening_ch2.mp3",
                "interactive_choices": [
                    {
                        "text": "🧠 Explain the phenomenon to Ivan", 
                        "next_chapter": 3, 
                        "cognitive_effect": "communication_skills",
                        "narration": "You choose to share your discovery, articulating the neural-linguistic connection..."
                    },
                    {
                        "text": "⚡ Continue the experiment", 
                        "next_chapter": 3, 
                        "cognitive_effect": "scientific_curiosity",
                        "narration": "You dive deeper into the experience, exploring the boundaries of this new capability..."
                    }
                ],
                "comprehension_questions": [
                    {
                        "question": "What does the Turkish suffix '-imiz' indicate in 'öğrencilerimizin'?",
                        "options": ["First person plural possessive", "Past tense", "Plural form", "Question marker"],
                        "correct": 0,
                        "explanation": "The suffix '-imiz' indicates 'our' in Turkish, showing first person plural possession"
                    },
                    {
                        "question": "Which linguistic concept describes the deep structure connecting different languages?",
                        "options": ["Universal Grammar", "Phonetic Alphabet", "Lexical Database", "Syntactic Tree"],
                        "correct": 0,
                        "explanation": "Universal Grammar theory suggests all languages share underlying structural principles"
                    }
                ],
                "vocabulary_highlight": [
                    {"word": "genitive", "definition": "grammatical case indicating possession or relationship"},
                    {"word": "nominalization", "definition": "process of forming nouns from other parts of speech"},
                    {"word": "iterative", "definition": "expressing repetition of an action"}
                ]
            },
            3: {
                "title": "The Multilingual Network",
                "text": """
🌐 <b>CHAPTER 3: The Multilingual Network</b>

Aisha's mind expanded further, connecting languages in ways she'd never imagined. She could feel the Turkic language family as a vibrant neural network - Kazakh, Turkish, Uzbek all lighting up different regions of her cerebral cortex.

"Look, Ivan!" she exclaimed, projecting a holographic language family tree. "The morphological patterns are fractal! The same possessive structures appear across languages:"

• Kazakh: <code>-ымыз</code> (our) in <code>кітаптарымыздан</code>
• Turkish: <code>-imiz</code> (our) in <code>öğrencilerimizin</code>  
• English: <code>our</code> as separate word in <code>our students</code>

"But they're all expressing the same fundamental cognitive concept!" Ivan realized, his scientific curiosity overriding his concern. "You're not just analyzing language - you're experiencing the universal cognitive structures!"

Aisha's mind then connected to the English word <code>internationalization</code>, automatically breaking it down:
• <code>inter-</code> (between) - <i>relational prefix</i>
• <code>nation</code> (people) - <i>social root</i>
• <code>+ -al</code> (adjective) - <i>quality marker</i>
• <code>+ -ize</code> (verb) - <i>process marker</i>
• <code>+ -ation</code> (noun) - <i>result state marker</i>

"Five morphemes!" Ivan calculated. "Your brain is processing complex derivational morphology in real-time!"

🔬 <b>Scientific Breakthrough:</b> Real-time morphological processing across language families
🧩 <b>Pattern Recognition:</b> Identifying universal cognitive structures through comparative linguistics
                """,
                "audio_file": "story_neural_awakening_ch3.mp3",
                "interactive_choices": [
                    {
                        "text": "📊 Map the entire language network", 
                        "next_chapter": 4, 
                        "cognitive_effect": "systematic_analysis",
                        "narration": "You systematically explore the connections between all activated languages..."
                    },
                    {
                        "text": "🎯 Focus on cognitive implications", 
                        "next_chapter": 4, 
                        "cognitive_effect": "theoretical_thinking",
                        "narration": "You contemplate the profound implications for understanding human cognition..."
                    }
                ],
                "comprehension_questions": [
                    {
                        "question": "How many morphemes are in the word 'internationalization'?",
                        "options": ["5", "3", "4", "6"],
                        "correct": 0,
                        "explanation": "inter- + nation + -al + -ize + -ation = 5 distinct morphemes"
                    },
                    {
                        "question": "What linguistic concept describes words like 'internationalization' with multiple affixes?",
                        "options": ["Derivational morphology", "Inflectional morphology", "Phonological process", "Syntactic parsing"],
                        "correct": 0,
                        "explanation": "Derivational morphology creates new words by adding prefixes and suffixes"
                    }
                ],
                "vocabulary_highlight": [
                    {"word": "fractal", "definition": "pattern that repeats at different scales"},
                    {"word": "derivational", "definition": "forming new words from existing ones"},
                    {"word": "cognitive", "definition": "related to mental processes and understanding"}
                ]
            },
            4: {
                "title": "The Cognitive Revolution",
                "text": """
💫 <b>CHAPTER 4: The Cognitive Revolution</b>

News of Aisha's abilities spread through the institute. Dr. Chen from Cognitive Sciences arrived, her team setting up advanced neural imaging equipment.

"Unprecedented!" Dr. Chen exclaimed as brain scans displayed Aisha's neural activity. "Your Broca's area is coordinating with Wernicke's area, angular gyrus, and even the prefrontal cortex in perfect synchrony!"

Aisha demonstrated by simultaneously analyzing words from four language families:
• Kazakh: <code>жүгірушілерге</code> (to the runners)
• Russian: <code>взаимопонимание</code> (mutual understanding) 
• English: <code>unbelievableness</code> (state of being unbelievable)
• Turkish: <code>anlayışınız</code> (your understanding)

"The patterns are everywhere!" Aisha explained. "Each language expresses similar concepts through different morphological strategies, but the underlying cognitive structures are identical!"

She visualized the concept of "understanding" across languages:
• English: <code>understand-ing</code> (verb + nominalizer)
• Russian: <code>понимание</code> (root + nominalizer) 
• Kazakh: <code>түсіну</code> (single lexical item)
• Turkish: <code>anlayış</code> (root + nominalizer)

"Different surface forms, same deep meaning!" Ivan realized. "You're seeing the universal language of human thought!"

🎓 <b>Academic Impact:</b> Revolutionizing understanding of language-cognition relationship
🔍 <b>Research Potential:</b> Unlocking new approaches to language learning and AI
                """,
                "audio_file": "story_neural_awakening_ch4.mp3",
                "interactive_choices": [
                    {
                        "text": "🌍 Share discovery with global community", 
                        "next_chapter": 5, 
                        "cognitive_effect": "collaborative_research",
                        "narration": "You choose to democratize knowledge, sharing breakthroughs with researchers worldwide..."
                    },
                    {
                        "text": "🔬 Continue private research", 
                        "next_chapter": 5, 
                        "cognitive_effect": "focused_investigation",
                        "narration": "You maintain control, pursuing deeper understanding before public release..."
                    }
                ],
                "comprehension_questions": [
                    {
                        "question": "Which brain areas were mentioned as working in synchrony during multilingual processing?",
                        "options": ["Broca's, Wernicke's, angular gyrus, prefrontal cortex", "Only Broca's area", "Visual and auditory cortex", "Cerebellum and brainstem"],
                        "correct": 0,
                        "explanation": "Multiple language areas coordinate during complex linguistic processing"
                    },
                    {
                        "question": "What universal concept did Aisha identify across different languages?",
                        "options": ["Underlying cognitive structures", "Identical vocabulary", "Same word order", "Identical pronunciation"],
                        "correct": 0,
                        "explanation": "Different languages share deep cognitive structures despite surface differences"
                    }
                ],
                "vocabulary_highlight": [
                    {"word": "synchrony", "definition": "simultaneous action or occurrence"},
                    {"word": "universal", "definition": "applying to all cases or situations"},
                    {"word": "morphological", "definition": "relating to word structure and formation"}
                ]
            },
            5: {
                "title": "The Ultimate Realization",
                "text": """
🚀 <b>CHAPTER 5: The Ultimate Realization</b>

Aisha stood before the International Linguistics Congress, her neural interface projecting real-time morphological analyses to the awe-struck audience.

"Ladies and gentlemen," she began, her voice resonating with newfound confidence. "We have been studying language backwards. We focused on surface differences while ignoring the profound unity beneath."

She demonstrated by analyzing the same concept across multiple languages simultaneously:
• <b>Possession:</b> Kazakh <code>-ымыз</code>, Turkish <code>-imiz</code>, English <code>our</code>
• <b>Location:</b> Kazakh <code>-де</code>, Turkish <code>-de</code>, English <code>in</code>
• <b>Direction:</b> Kazakh <code>-ға</code>, Turkish <code>-a</code>, English <code>to</code>

"The patterns are systematic! The differences are superficial!" she proclaimed. "Every human brain is wired for this universal grammatical competence. We just need to learn how to access it!"

The audience watched in stunned silence as Aisha helped a monolingual English speaker analyze complex Kazakh morphology within minutes.

"I can see it!" the volunteer exclaimed. "The patterns make sense now! It's not random - it's systematic!"

Aisha smiled, realizing the true potential of her discovery. "This isn't just about language analysis. This is about unlocking the innate multilingual capacity in every human brain."

🌅 <b>New Era:</b> Revolutionizing language education and cognitive science
💡 <b>Ultimate Insight:</b> Every human possesses innate multilingual capabilities waiting to be activated
                """,
                "audio_file": "story_neural_awakening_ch5.mp3",
                "interactive_choices": [],
                "comprehension_questions": [
                    {
                        "question": "What fundamental insight did Aisha share with the linguistics congress?",
                        "options": ["Languages share underlying universal patterns", "All languages should be the same", "Surface differences don't matter", "Grammar is unnecessary"],
                        "correct": 0,
                        "explanation": "Aisha revealed that despite surface differences, languages share deep universal patterns"
                    },
                    {
                        "question": "What capacity did Aisha believe exists in every human brain?",
                        "options": ["Innate multilingual capabilities", "Perfect memory", "Telepathic communication", "Mathematical genius"],
                        "correct": 0,
                        "explanation": "She believed every human has innate capacity for multilingual understanding"
                    }
                ],
                "vocabulary_highlight": [
                    {"word": "systematic", "definition": "done or acting according to a fixed plan or system"},
                    {"word": "universal", "definition": "of, affecting, or done by all people or things in the world"},
                    {"word": "innate", "definition": "inborn; natural"}
                ]
            }
        },
        "learning_objectives": [
            "Understand complex morphological structures across languages",
            "Compare possessive and plural forms cross-linguistically", 
            "Learn cognitive linguistics terminology and concepts",
            "Develop advanced pattern recognition skills",
            "Understand the relationship between language and cognition"
        ],
        "cognitive_skills": ["pattern_recognition", "analytical_thinking", "cross_linguistic_mapping", "theoretical_reasoning"]
    },
    "language_detective": {
        "title": "🕵️ The Morphology Detective",
        "language": "english",
        "difficulty": "beginner", 
        "duration": "6-8 minutes",
        "chapters": 4,
        "target_vocabulary": ["detective", "clue", "pattern", "solve", "mystery", "evidence", "analysis"],
        "description": "A detective uses linguistic analysis and morphological clues to solve international mysteries",
        "cover_image": "story_detective_cover.jpg",
        "chapters": {
            1: {
                "title": "The Cryptic Message",
                "text": """
🕵️ <b>CHAPTER 1: The Cryptic Message</b>

Detective Maria Linguistics stared at the mysterious note left at the crime scene. It contained a single word: <code>unbelievableness</code>.

"Another one," she muttered, adding it to her case file of seemingly random words left at international incidents.

Her assistant, Leo, peered over her shoulder. "It looks like ordinary English, Maria. What makes this special?"

"Look at the structure, Leo," Maria said, circling morphemes on her tablet:
• <code>un-</code> (negative prefix)
• <code>believe</code> (root verb) 
• <code>+ -able</code> (adjective suffix)
• <code>+ -ness</code> (noun suffix)

"Four morphological components! This isn't random - it's a pattern. The perpetrator is leaving us linguistic clues!"

Maria pulled up previous cases:
• Berlin: <code>internationalization</code> (5 morphemes)
• Tokyo: <code>misunderstanding</code> (4 morphemes)  
• Cairo: <code>reorganization</code> (4 morphemes)

"The morpheme counts match the number of accomplices!" Leo realized. "And the word meanings hint at their motives!"

🔍 <b>Investigation Start:</b> Linguistic pattern recognition as detective work
🎯 <b>Key Insight:</b> Morphological complexity as coded information
                """,
                "audio_file": "story_detective_ch1.mp3",
                "interactive_choices": [
                    {
                        "text": "🔬 Analyze morphological patterns", 
                        "next_chapter": 2, 
                        "cognitive_effect": "analytical_thinking",
                        "narration": "You focus on the linguistic evidence, breaking down each word systematically..."
                    },
                    {
                        "text": "🌍 Research international connections", 
                        "next_chapter": 2, 
                        "cognitive_effect": "global_awareness",
                        "narration": "You explore the geographical pattern of the incidents..."
                    }
                ],
                "comprehension_questions": [
                    {
                        "question": "How many morphemes are in 'unbelievableness'?",
                        "options": ["4", "3", "2", "5"],
                        "correct": 0,
                        "explanation": "un- + believe + -able + -ness = 4 distinct morphemes"
                    },
                    {
                        "question": "What did the detective discover about the morpheme counts?",
                        "options": ["They matched accomplice numbers", "They indicated crime severity", "They showed language difficulty", "They revealed time of crime"],
                        "correct": 0,
                        "explanation": "The number of morphemes corresponded to the number of accomplices in each case"
                    }
                ],
                "vocabulary_highlight": [
                    {"word": "morpheme", "definition": "smallest meaningful unit in a language"},
                    {"word": "morphological", "definition": "relating to word structure and formation"},
                    {"word": "perpetrator", "definition": "person who carries out a harmful or illegal act"}
                ]
            }
            # Additional chapters would continue here...
        },
        "learning_objectives": [
            "Learn English derivational morphology",
            "Understand how word structure conveys meaning",
            "Develop deductive reasoning through linguistic analysis",
            "Practice pattern recognition in real-world contexts"
        ]
    }
}

# ========== ULTIMATE VOCABULARY DATABASE ==========
WORD_DATABASE = {
    "кітаптарымыздан": {
        "analysis": ["кітап (root: book)", "+ -тар- (plural)", "+ -ымыз- (our)", "+ -дан (from)"],
        "translations": {"english": "from our books", "russian": "из наших книг", "turkish": "kitaplarımızdan", "chinese": "从我们的书中", "arabic": "من كتبنا"},
        "language": "kazakh",
        "difficulty": "intermediate",
        "category": "education",
        "cognitive_level": "syntactic_awareness",
        "morpheme_count": 4,
        "frequency": "high",
        "audio": "kz_kitaptarymyzdan.mp3",
        "phonetic": "[kɪtɑptɑrɯmɯzˈdɑn]",
        "neural_pathways": 12
    },
    "жүгірушілерге": {
        "analysis": ["жүгір (root: to run)", "+ -уші (agent: one who does)", "+ -лер (plural)", "+ -ге (to/for)"],
        "translations": {"english": "to the runners", "russian": "бегунам", "turkish": "koşucularا", "chinese": "给跑步者们", "arabic": "للعدائين"},
        "language": "kazakh", 
        "difficulty": "intermediate",
        "category": "sports",
        "cognitive_level": "agent_identification",
        "morpheme_count": 4,
        "frequency": "medium",
        "audio": "kz_zhugirushilerge.mp3",
        "phonetic": "[ʒygɪrʊʃɪˈlɛrgɛ]",
        "neural_pathways": 14
    },
    "балаларға": {
        "analysis": ["бала (root: child)", "+ -лар (plural)", "+ -ға (to/for)"],
        "translations": {"english": "to the children", "russian": "детям", "turkish": "çocuklara", "chinese": "给孩子们", "arabic": "للأطفال"},
        "language": "kazakh",
        "difficulty": "beginner",
        "category": "family",
        "cognitive_level": "basic_syntax",
        "morpheme_count": 3,
        "frequency": "very_high",
        "audio": "kz_balalargha.mp3",
        "phonetic": "[bɑlɑlɑrˈɣɑ]",
        "neural_pathways": 8
    },
    "үйлерімізде": {
        "analysis": ["үй (root: house)", "+ -лер (plural)", "+ -іміз (our)", "+ -де (in/at)"],
        "translations": {"english": "in our houses", "russian": "в наших домах", "turkish": "evlerimizde", "chinese": "在我们的房子里", "arabic": "في منازلنا"},
        "language": "kazakh",
        "difficulty": "intermediate",
        "category": "home",
        "cognitive_level": "spatial_relations",
        "morpheme_count": 4,
        "frequency": "high",
        "audio": "kz_uylerimizde.mp3",
        "phonetic": "[yjlɛrɪmɪzˈdɛ]",
        "neural_pathways": 11
    },
    "unbelievableness": {
        "analysis": ["un- (negative: not)", "+ believe (root)", "+ -able (adjective: able to be)", "+ -ness (noun: state)"],
        "translations": {"kazakh": "сенімсіздік", "russian": "невероятность", "turkish": "inanılmazlık", "chinese": "不可信性", "arabic": "عدم القابلية للتصديق"},
        "language": "english",
        "difficulty": "advanced",
        "category": "abstract",
        "cognitive_level": "abstract_noun_formation",
        "morpheme_count": 4,
        "frequency": "very_low",
        "audio": "en_unbelievableness.mp3",
        "phonetic": "[ʌnbɪˈliːvəblnəs]",
        "neural_pathways": 16
    },
    "internationalization": {
        "analysis": ["inter- (between)", "+ nation (root)", "+ -al (adjective)", "+ -ize (verb)", "+ -ation (noun)"],
        "translations": {"kazakh": "халықаралану", "russian": "интернационализация", "turkish": "uluslararasılaşma", "chinese": "国际化", "arabic": "العولمة"},
        "language": "english",
        "difficulty": "advanced",
        "category": "globalization",
        "cognitive_level": "complex_derivation",
        "morpheme_count": 5,
        "frequency": "medium",
        "audio": "en_internationalization.mp3",
        "phonetic": "[ɪntərnæʃənəlaɪˈzeɪʃən]",
        "neural_pathways": 18
    },
    "переосмысление": {
        "analysis": ["пере- (re-)", "+ осмысл (root: meaning)", "+ -ение (noun suffix)"],
        "translations": {"kazakh": "қайта ойлау", "english": "rethinking", "turkish": "yeniden değerlendirme", "chinese": "重新思考", "arabic": "إعادة التفكير"},
        "language": "russian",
        "difficulty": "advanced",
        "category": "cognitive",
        "cognitive_level": "metacognitive_processing",
        "morpheme_count": 3,
        "frequency": "low",
        "audio": "ru_pereosmyslenie.mp3",
        "phonetic": "[pʲɪrʲɪɐsmɨsˈlʲenʲɪje]",
        "neural_pathways": 15
    },
    "взаимопонимание": {
        "analysis": ["взаимо- (mutual)", "+ пониман (root: understanding)", "+ -ие (noun suffix)"],
        "translations": {"kazakh": "өзара түсініс", "english": "mutual understanding", "turkish": "karşılıklı anlayış", "chinese": "相互理解", "arabic": "الفهم المتبادل"},
        "language": "russian",
        "difficulty": "intermediate",
        "category": "social",
        "cognitive_level": "social_cognition",
        "morpheme_count": 3,
        "frequency": "medium",
        "audio": "ru_vzaimoponimanie.mp3",
        "phonetic": "[vzəɪməpənɪˈmanʲɪje]",
        "neural_pathways": 13
    },
    "öğrencilerimizin": {
        "analysis": ["öğrenci (root: student)", "+ -ler (plural)", "+ -imiz (our)", "+ -in (of)"],
        "translations": {"kazakh": "оқушıларымыздың", "english": "of our students", "russian": "наших студентов", "chinese": "我们学生的", "arabic": "طلابنا"},
        "language": "turkish",
        "difficulty": "intermediate",
        "category": "education",
        "cognitive_level": "possessive_structures",
        "morpheme_count": 4,
        "frequency": "high",
        "audio": "tr_ogrencilerimizin.mp3",
        "phonetic": "[œːɾændʒɪlɛɾɪmɪˈzɪn]",
        "neural_pathways": 12
    },
    "anlayışınız": {
        "analysis": ["anla (root: understand)", "+ -yış (noun suffix)", "+ -ınız (your)"],
        "translations": {"kazakh": "түсінісіңіз", "english": "your understanding", "russian": "ваше понимание", "chinese": "您的理解", "arabic": "فهمك"},
        "language": "turkish",
        "difficulty": "intermediate",
        "category": "communication",
        "cognitive_level": "abstract_noun_formation",
        "morpheme_count": 3,
        "frequency": "medium",
        "audio": "tr_anlayisiniz.mp3",
        "phonetic": "[ɑnlɑjɯʃɯˈnɯz]",
        "neural_pathways": 10
    }
}

# ========== FLASHCARD GAME DATABASE ==========
FLASHCARD_DATABASE = {
    "kazakh_basics": {
        "title": "🧠 Kazakh Morphology Flashcards",
        "description": "Learn Kazakh word structure through interactive flashcards",
        "cards": [
            {
                "id": "kz_card_1",
                "front": "кітаптарымыздан",
                "back": "from our books",
                "hint": "кітап (book) + -тар (plural) + -ымыз (our) + -дан (from)",
                "language": "kazakh",
                "category": "education",
                "audio": "kz_kitaptarymyzdan.mp3"
            },
            {
                "id": "kz_card_2", 
                "front": "жүгірушілерге",
                "back": "to the runners",
                "hint": "жүгір (run) + -уші (agent) + -лер (plural) + -ге (to)",
                "language": "kazakh",
                "category": "sports",
                "audio": "kz_zhugirushilerge.mp3"
            },
            {
                "id": "kz_card_3",
                "front": "балаларға",
                "back": "to the children", 
                "hint": "бала (child) + -лар (plural) + -ға (to)",
                "language": "kazakh",
                "category": "family",
                "audio": "kz_balalargha.mp3"
            },
            {
                "id": "kz_card_4",
                "front": "үйлерімізде",
                "back": "in our houses",
                "hint": "үй (house) + -лер (plural) + -іміз (our) + -де (in)",
                "language": "kazakh", 
                "category": "home",
                "audio": "kz_uylerimizde.mp3"
            }
        ],
        "difficulty": "beginner",
        "points": 50
    },
    "english_advanced": {
        "title": "🧠 English Word Formation Flashcards", 
        "description": "Master complex English word structures",
        "cards": [
            {
                "id": "en_card_1",
                "front": "unbelievableness", 
                "back": "state of being unbelievable",
                "hint": "un- (not) + believe + -able (able) + -ness (state)",
                "language": "english",
                "category": "abstract",
                "audio": "en_unbelievableness.mp3"
            },
            {
                "id": "en_card_2",
                "front": "internationalization",
                "back": "process of making something international", 
                "hint": "inter- (between) + nation + -al (adjective) + -ize (verb) + -ation (noun)",
                "language": "english",
                "category": "globalization",
                "audio": "en_internationalization.mp3"
            }
        ],
        "difficulty": "advanced",
        "points": 75
    },
    "cross_linguistic": {
        "title": "🧠 Cross-Linguistic Patterns",
        "description": "Compare morphological patterns across languages",
        "cards": [
            {
                "id": "cross_card_1",
                "front": "кітаптар (Kazakh)",
                "back": "kitaplar (Turkish)",
                "hint": "Both use -lar/-ler for plural formation",
                "language": "comparative",
                "category": "plural",
                "audio": None
            },
            {
                "id": "cross_card_2",
                "front": "-ымыз (Kazakh possessive)",
                "back": "-imiz (Turkish possessive)", 
                "hint": "First person plural possessive markers",
                "language": "comparative",
                "category": "possessive",
                "audio": None
            }
        ],
        "difficulty": "intermediate", 
        "points": 60
    }
}

# ========== ULTIMATE QUIZ DATABASE ==========
QUIZ_DATABASE = {
    "morphology": [
        {
            "question": "What does the suffix '-тар' indicate in Kazakh?",
            "options": ["Plural", "Past tense", "Future tense", "Question"],
            "correct": 0,
            "explanation": "🎯 The suffix '-тар' or '-лер' indicates plural form in Kazakh!",
            "difficulty": "beginner",
            "cognitive_skill": "morpheme_recognition",
            "points": 15,
            "audio_hint": None,
            "neural_impact": "Broca's area activation"
        },
        {
            "question": "Which English prefix means 'against'?",
            "options": ["un-", "re-", "anti-", "pre-"],
            "correct": 2,
            "explanation": "⚡ The prefix 'anti-' means against or opposite!",
            "difficulty": "beginner", 
            "cognitive_skill": "prefix_recognition",
            "points": 15,
            "audio_hint": None,
            "neural_impact": "Prefrontal cortex engagement"
        },
        {
            "question": "What is the function of the suffix '-ымыз' in Kazakh?",
            "options": ["Plural", "Possessive (our)", "Past tense", "Location"],
            "correct": 1,
            "explanation": "🧠 The suffix '-ымыз' indicates first person plural possessive (our)!",
            "difficulty": "intermediate",
            "cognitive_skill": "possessive_identification",
            "points": 20,
            "audio_hint": None,
            "neural_impact": "Syntactic processing enhancement"
        }
    ],
    "translations": [
        {
            "question": "Translate 'кітаптарымыздан' to English",
            "options": ["from our books", "to our books", "with our books", "about our books"],
            "correct": 0,
            "explanation": "🎉 Perfect! 'кітаптарымыздан' means 'from our books'!",
            "difficulty": "intermediate",
            "cognitive_skill": "cross_linguistic_mapping", 
            "points": 25,
            "audio_hint": "kz_kitaptarymyzdan.mp3",
            "neural_impact": "Bilingual language network activation"
        },
        {
            "question": "Translate 'internationalization' to Kazakh",
            "options": ["халықаралану", "кітап", "оқушы", "үй"],
            "correct": 0,
            "explanation": "🌍 Excellent! 'internationalization' translates to 'халықаралану' in Kazakh!",
            "difficulty": "advanced",
            "cognitive_skill": "technical_translation",
            "points": 30,
            "audio_hint": "en_internationalization.mp3",
            "neural_impact": "Global language processing"
        },
        {
            "question": "What is the English translation of 'взаимопонимание'?",
            "options": ["mutual understanding", "friendship", "agreement", "conversation"],
            "correct": 0,
            "explanation": "🤝 Perfect! 'взаимопонимание' means 'mutual understanding'!",
            "difficulty": "intermediate",
            "cognitive_skill": "semantic_mapping",
            "points": 22,
            "audio_hint": "ru_vzaimoponimanie.mp3",
            "neural_impact": "Semantic network activation"
        }
    ],
    "cognitive_linguistics": [
        {
            "question": "Which brain area is most active during morphological processing?",
            "options": ["Broca's area", "Visual cortex", "Cerebellum", "Amygdala"],
            "correct": 0,
            "explanation": "🧠 Correct! Broca's area in the left hemisphere is crucial for morphological processing!",
            "difficulty": "advanced",
            "cognitive_skill": "neurolinguistic_knowledge",
            "points": 30,
            "audio_hint": None,
            "neural_impact": "Neurolinguistic awareness"
        },
        {
            "question": "What cognitive process is involved in breaking down words into morphemes?",
            "options": ["Morphological parsing", "Semantic analysis", "Phonological processing", "Syntactic parsing"],
            "correct": 0,
            "explanation": "🔬 Perfect! Morphological parsing decomposes words into constituent morphemes!",
            "difficulty": "intermediate",
            "cognitive_skill": "metalinguistic_awareness",
            "points": 25,
            "audio_hint": None,
            "neural_impact": "Analytical thinking enhancement"
        },
        {
            "question": "Which cognitive skill is most engaged when comparing languages?",
            "options": ["Pattern recognition", "Memory recall", "Visual processing", "Motor skills"],
            "correct": 0,
            "explanation": "🎯 Right! Pattern recognition is key for cross-linguistic comparison!",
            "difficulty": "intermediate",
            "cognitive_skill": "comparative_analysis",
            "points": 22,
            "audio_hint": None,
            "neural_impact": "Comparative cognition"
        }
    ],
    "language_families": [
        {
            "question": "Which language family does Kazakh belong to?",
            "options": ["Turkic", "Slavic", "Germanic", "Romance"],
            "correct": 0,
            "explanation": "✅ Correct! Kazakh belongs to the Turkic language family (Kipchak branch)!",
            "difficulty": "beginner",
            "cognitive_skill": "language_classification",
            "points": 15,
            "audio_hint": None,
            "neural_impact": "Language family mapping"
        },
        {
            "question": "Which language is NOT in the Turkic family?",
            "options": ["Turkish", "Kazakh", "Uzbek", "Russian"],
            "correct": 3,
            "explanation": "🎯 Right! Russian is Slavic, while Turkish, Kazakh, and Uzbek are Turkic!",
            "difficulty": "intermediate",
            "cognitive_skill": "language_classification",
            "points": 20,
            "audio_hint": None,
            "neural_impact": "Comparative linguistics"
        },
        {
            "question": "Which language family includes English?",
            "options": ["Germanic", "Romance", "Slavic", "Turkic"],
            "correct": 0,
            "explanation": "🌍 Correct! English is a Germanic language!",
            "difficulty": "beginner",
            "cognitive_skill": "language_classification",
            "points": 15,
            "audio_hint": None,
            "neural_impact": "Language family knowledge"
        }
    ],
    "audio_challenge": [
        {
            "question": "🎧 Listen to the pronunciation and identify the language:",
            "options": ["Kazakh", "Turkish", "Russian", "English"],
            "correct": 0,
            "explanation": "👂 Excellent listening! This is Kazakh with characteristic vowel harmony!",
            "difficulty": "beginner",
            "cognitive_skill": "phonetic_recognition",
            "points": 20,
            "audio_hint": "kz_balalargha.mp3",
            "neural_impact": "Auditory cortex training"
        },
        {
            "question": "🎧 Which morphological pattern do you hear?",
            "options": ["Plural + Possessive", "Singular + Past", "Question form", "Negative form"],
            "correct": 0,
            "explanation": "🔊 Perfect! You heard plural '-лар' and possessive '-ымыз' morphology!",
            "difficulty": "intermediate",
            "cognitive_skill": "audio_morphology",
            "points": 25,
            "audio_hint": "kz_uylerimizde.mp3",
            "neural_impact": "Phonological-morphological integration"
        },
        {
            "question": "🎧 Based on pronunciation, identify the language:",
            "options": ["Kazakh", "Russian", "English", "Turkish"],
            "correct": 0,
            "explanation": "🎵 Great ear! The phonetic patterns match Kazakh language characteristics!",
            "difficulty": "beginner",
            "cognitive_skill": "language_identification",
            "points": 20,
            "audio_hint": "kz_zhugirushilerge.mp3",
            "neural_impact": "Language discrimination skills"
        }
    ],
    "adaptive_challenge": [
        {
            "question": "Based on your level, analyze this Kazakh word structure: 'жүгірушілерге'",
            "options": ["Verb + Agent + Plural + Dative", "Noun + Plural + Possessive", "Adjective + Comparative", "Root + Past tense"],
            "correct": 0,
            "explanation": "🧠 Perfect analysis! жүгір (run) + -уші (agent) + -лер (plural) + -ге (dative)!",
            "difficulty": "intermediate",
            "cognitive_skill": "adaptive_analysis",
            "points": 25,
            "audio_hint": "kz_zhugirushilerge.mp3",
            "neural_impact": "Adaptive cognitive processing"
        },
        {
            "question": "What's the cognitive complexity level of 'internationalization'?",
            "options": ["High (5 morphemes)", "Medium (3 morphemes)", "Low (2 morphemes)", "Simple (1 morpheme)"],
            "correct": 0,
            "explanation": "🎯 Correct! inter- + nation + -al + -ize + -ation = 5 morphemes = High complexity!",
            "difficulty": "advanced",
            "cognitive_skill": "complexity_assessment",
            "points": 28,
            "audio_hint": "en_internationalization.mp3",
            "neural_impact": "Complexity evaluation"
        },
        {
            "question": "Which word would be easiest for a beginner to analyze?",
            "options": ["балаларға", "переосмысление", "unbelievableness", "internationalization"],
            "correct": 0,
            "explanation": "✅ Right! 'балаларға' has only 3 morphemes, making it beginner-friendly!",
            "difficulty": "beginner",
            "cognitive_skill": "difficulty_assessment",
            "points": 18,
            "audio_hint": "kz_balalargha.mp3",
            "neural_impact": "Difficulty calibration"
        }
    ],
    "combo_challenge": [
        {
            "question": "Identify the COMMON pattern: Kazakh 'кітаптар', Turkish 'kitaplar', English 'books'",
            "options": ["Plural formation", "Past tense", "Possessive", "Question form"],
            "correct": 0,
            "explanation": "🔥 COMBO START! All show plural forms across languages!",
            "difficulty": "beginner",
            "cognitive_skill": "pattern_recognition",
            "points": 20,
            "audio_hint": None,
            "neural_impact": "Cross-linguistic pattern detection"
        },
        {
            "question": "What morphological feature do these share: '-ымыз' (Kazakh), '-imiz' (Turkish), 'our' (English)?",
            "options": ["First person plural possessive", "Past tense", "Plural", "Location"],
            "correct": 0,
            "explanation": "🎯 COMBO x2! All indicate 'our' possession across languages!",
            "difficulty": "intermediate",
            "cognitive_skill": "possessive_comparison",
            "points": 25,
            "audio_hint": None,
            "neural_impact": "Possessive structure mapping"
        },
        {
            "question": "Which cognitive process is activated by consecutive pattern recognition?",
            "options": ["Neural pathway strengthening", "Memory decay", "Cognitive load reduction", "Attention shifting"],
            "correct": 0,
            "explanation": "⚡ COMBO x3! Correct answers strengthen neural pathways!",
            "difficulty": "advanced",
            "cognitive_skill": "metacognitive_awareness",
            "points": 30,
            "audio_hint": None,
            "neural_impact": "Neural reinforcement"
        }
    ],
    "quick_challenge": [
        {
            "question": "FAST: What does Kazakh suffix '-ға' indicate?",
            "options": ["Dative (to/for)", "Plural", "Past", "Question"],
            "correct": 0,
            "explanation": "⚡ Quick! '-ға' indicates dative case (to/for)!",
            "difficulty": "beginner",
            "cognitive_skill": "quick_recognition",
            "points": 15,
            "audio_hint": None,
            "neural_impact": "Rapid processing"
        },
        {
            "question": "SPEED: English 'un-' prefix means?",
            "options": ["Not", "Again", "Before", "After"],
            "correct": 0,
            "explanation": "🎯 Fast! 'un-' means 'not' as in 'unbelievable'!",
            "difficulty": "beginner",
            "cognitive_skill": "prefix_recognition",
            "points": 15,
            "audio_hint": None,
            "neural_impact": "Speed processing"
        },
        {
            "question": "QUICK: Which is a Turkic language?",
            "options": ["Kazakh", "Russian", "English", "Spanish"],
            "correct": 0,
            "explanation": "🚀 Rapid! Kazakh is Turkic, others are from different families!",
            "difficulty": "beginner",
            "cognitive_skill": "language_identification",
            "points": 15,
            "audio_hint": None,
            "neural_impact": "Quick classification"
        }
    ]
}

# ========== VOCABULARY MATCHING GAME DATABASE ==========
VOCAB_MATCHING_GAMES = {
    "kazakh_basics": {
        "title": "🧩 Kazakh Morphology Match",
        "description": "Match Kazakh words with their morphological structures",
        "pairs": {
            "кітаптарымыздан": "кітап + тар + ымыз + дан",
            "жүгірушілерге": "жүгір + уші + лер + ге", 
            "балаларға": "бала + лар + ға",
            "үйлерімізде": "үй + лер + іміз + де"
        },
        "difficulty": "intermediate",
        "points": 50,
        "time_limit": 90
    },
    "english_advanced": {
        "title": "🧩 English Word Formation",
        "description": "Match complex English words with their morpheme breakdowns",
        "pairs": {
            "unbelievableness": "un + believe + able + ness",
            "internationalization": "inter + nation + al + ize + ation",
            "misunderstanding": "mis + under + stand + ing",
            "reorganization": "re + organ + ize + ation"
        },
        "difficulty": "advanced",
        "points": 75,
        "time_limit": 120
    },
    "cross_linguistic": {
        "title": "🧩 Cross-Linguistic Patterns",
        "description": "Match words from different languages with similar morphological patterns",
        "pairs": {
            "кітаптар (Kazakh)": "kitaplar (Turkish)",
            "students (English)": "оқушылар (Kazakh)",
            "understanding (English)": "түсіну (Kazakh)",
            "books (English)": "кітаптар (Kazakh)"
        },
        "difficulty": "advanced",
        "points": 100,
        "time_limit": 150
    }
}

# ========== ULTIMATE STORYTELLING MANAGER ==========
class UltimateStorytellingManager:
    def __init__(self, db):
        self.db = db
        self.active_story_sessions = {}
        self.story_progress = defaultdict(dict)
    
    def start_story_session(self, user_id: int, story_id: str):
        """Start an ULTIMATE interactive story session"""
        session_id = f"story_{user_id}_{datetime.now().timestamp()}"
        
        self.active_story_sessions[session_id] = {
            'user_id': user_id,
            'story_id': story_id,
            'current_chapter': 1,
            'start_time': datetime.now(),
            'choices_made': [],
            'comprehension_score': 0,
            'vocabulary_learned': [],
            'cognitive_effects': defaultdict(int),
            'questions_answered': 0,
            'correct_answers': 0
        }
        
        return session_id
    
    def get_current_chapter(self, session_id: str):
        """Get current chapter with enhanced tracking"""
        session = self.active_story_sessions.get(session_id)
        if not session:
            return None
        
        story = STORY_DATABASE.get(session['story_id'])
        if not story:
            return None
        
        chapter = story['chapters'].get(session['current_chapter'])
        return chapter
    
    def advance_story(self, session_id: str, choice_index: int = 0):
        """Advance story based on user choice"""
        session = self.active_story_sessions.get(session_id)
        if not session:
            return None
        
        current_chapter = self.get_current_chapter(session_id)
        if not current_chapter:
            return None
        
        # Record choice and cognitive effect
        if current_chapter.get('interactive_choices'):
            choice = current_chapter['interactive_choices'][choice_index]
            session['choices_made'].append(choice)
            session['cognitive_effects'][choice['cognitive_effect']] += 1
        
        # Advance to next chapter
        next_chapter = choice['next_chapter'] if current_chapter.get('interactive_choices') else session['current_chapter'] + 1
        
        story = STORY_DATABASE[session['story_id']]
        if next_chapter > len(story['chapters']):
            # Story complete
            session['completed'] = True
            return self._complete_story_session(session_id)
        else:
            session['current_chapter'] = next_chapter
            return self.get_current_chapter(session_id)
    
    def submit_comprehension_answer(self, session_id: str, question_index: int, answer_index: int):
        """Submit answer to comprehension question"""
        session = self.active_story_sessions.get(session_id)
        if not session:
            return False
        
        current_chapter = self.get_current_chapter(session_id)
        if not current_chapter or 'comprehension_questions' not in current_chapter:
            return False
        
        questions = current_chapter['comprehension_questions']
        if question_index >= len(questions):
            return False
        
        question = questions[question_index]
        is_correct = (answer_index == question['correct'])
        
        session['questions_answered'] += 1
        if is_correct:
            session['correct_answers'] += 1
        
        # Update comprehension score
        if session['questions_answered'] > 0:
            session['comprehension_score'] = (session['correct_answers'] / session['questions_answered']) * 100
        
        return {
            'is_correct': is_correct,
            'explanation': question['explanation'],
            'current_score': session['comprehension_score']
        }
    
    def _complete_story_session(self, session_id: str):
        """Complete story session with rewards"""
        session = self.active_story_sessions.get(session_id)
        if not session:
            return None
        
        story = STORY_DATABASE.get(session['story_id'], {})
        
        # Calculate rewards
        base_points = 100
        comprehension_bonus = session['comprehension_score'] * 2  # Up to 200 points
        vocabulary_bonus = len(set(session['vocabulary_learned'])) * 10  # Up to 50 points
        cognitive_bonus = sum(session['cognitive_effects'].values()) * 5  # Up to 50 points
        completion_bonus = 50  # For finishing the story
        
        total_points = base_points + comprehension_bonus + vocabulary_bonus + cognitive_bonus + completion_bonus
        
        # Update user stats
        self.db.update_user(
            session['user_id'],
            points=total_points
        )
        
        # Log story completion
        self.db.log_story_completion(
            session['user_id'],
            session['story_id'],
            total_points,
            session['comprehension_score'],
            len(session['vocabulary_learned'])
        )
        
        # Grant story achievements
        self.db.grant_achievement(session['user_id'], "story_completion")
        
        return {
            'story_id': session['story_id'],
            'story_title': story.get('title', 'Unknown Story'),
            'total_points': total_points,
            'comprehension_score': session['comprehension_score'],
            'vocabulary_learned': session['vocabulary_learned'],
            'cognitive_effects': dict(session['cognitive_effects']),
            'performance_rating': self._calculate_story_performance(session),
            'breakdown': {
                'base_points': base_points,
                'comprehension_bonus': comprehension_bonus,
                'vocabulary_bonus': vocabulary_bonus,
                'cognitive_bonus': cognitive_bonus,
                'completion_bonus': completion_bonus
            }
        }
    
    def _calculate_story_performance(self, session: dict) -> str:
        """Calculate ULTIMATE story performance rating"""
        comprehension = session['comprehension_score']
        vocabulary = len(session['vocabulary_learned'])
        cognitive_diversity = len(session['cognitive_effects'])
        
        score = (comprehension * 0.4) + (min(vocabulary, 5) * 10) + (cognitive_diversity * 10)
        
        if score >= 90:
            return "STORY_MASTER"
        elif score >= 75:
            return "LINGUISTIC_GENIUS"
        elif score >= 60:
            return "ACTIVE_LEARNER"
        else:
            return "BEGINNER_STORYTELLER"

# ========== FLASHCARD GAME MANAGER ==========
class FlashcardGameManager:
    def __init__(self, db):
        self.db = db
        self.active_flashcard_sessions = {}
        self.user_progress = defaultdict(dict)
    
    def start_flashcard_session(self, user_id: int, deck_id: str):
        """Start a new flashcard learning session"""
        session_id = f"flashcard_{user_id}_{datetime.now().timestamp()}"
        
        deck = FLASHCARD_DATABASE.get(deck_id)
        if not deck:
            return None
        
        cards = deck['cards'].copy()
        random.shuffle(cards)  # Shuffle cards for variety
        
        self.active_flashcard_sessions[session_id] = {
            'user_id': user_id,
            'deck_id': deck_id,
            'cards': cards,
            'current_card_index': 0,
            'cards_viewed': 0,
            'cards_known': 0,
            'start_time': datetime.now(),
            'session_score': 0,
            'is_flipped': False,
            'completed': False
        }
        
        return session_id
    
    def get_current_card(self, session_id: str):
        """Get current card in session"""
        session = self.active_flashcard_sessions.get(session_id)
        if not session or session['completed']:
            return None
        
        if session['current_card_index'] < len(session['cards']):
            return session['cards'][session['current_card_index']]
        return None
    
    def flip_card(self, session_id: str):
        """Flip the current card to show back side"""
        session = self.active_flashcard_sessions.get(session_id)
        if not session:
            return False
        
        session['is_flipped'] = not session['is_flipped']
        if session['is_flipped']:
            session['cards_viewed'] += 1
        return True
    
    def mark_card_known(self, session_id: str):
        """Mark current card as known and move to next"""
        session = self.active_flashcard_sessions.get(session_id)
        if not session:
            return None
        
        session['cards_known'] += 1
        session['session_score'] += 10  # Base points for knowing a card
        
        # Move to next card
        session['current_card_index'] += 1
        session['is_flipped'] = False
        
        # Check if session complete
        if session['current_card_index'] >= len(session['cards']):
            session['completed'] = True
            return self._complete_flashcard_session(session_id)
        
        return self.get_current_card(session_id)
    
    def skip_card(self, session_id: str):
        """Skip current card and move to next"""
        session = self.active_flashcard_sessions.get(session_id)
        if not session:
            return None
        
        # Move to next card
        session['current_card_index'] += 1
        session['is_flipped'] = False
        
        # Check if session complete
        if session['current_card_index'] >= len(session['cards']):
            session['completed'] = True
            return self._complete_flashcard_session(session_id)
        
        return self.get_current_card(session_id)
    
    def _complete_flashcard_session(self, session_id: str):
        """Complete flashcard session and calculate rewards"""
        session = self.active_flashcard_sessions.get(session_id)
        if not session:
            return None
        
        deck = FLASHCARD_DATABASE.get(session['deck_id'], {})
        
        # Calculate performance
        total_cards = len(session['cards'])
        known_percentage = (session['cards_known'] / total_cards) * 100 if total_cards > 0 else 0
        
        # Time bonus
        time_taken = (datetime.now() - session['start_time']).total_seconds()
        time_bonus = max(0, 50 - (time_taken / 10))  # Faster completion = more bonus
        
        # Accuracy bonus
        accuracy_bonus = known_percentage * 2
        
        # Base points from deck
        base_points = deck.get('points', 50)
        
        total_points = base_points + session['session_score'] + time_bonus + accuracy_bonus
        
        # Update user stats
        self.db.update_user(
            session['user_id'],
            points=int(total_points)
        )
        
        # Log flashcard session
        self._log_flashcard_session(session, total_points, known_percentage)
        
        return {
            'deck_id': session['deck_id'],
            'deck_title': deck.get('title', 'Flashcards'),
            'total_cards': total_cards,
            'cards_known': session['cards_known'],
            'known_percentage': known_percentage,
            'time_taken': time_taken,
            'total_points': int(total_points),
            'performance_rating': self._calculate_flashcard_performance(known_percentage, time_taken)
        }
    
    def _log_flashcard_session(self, session: dict, points: int, accuracy: float):
        """Log flashcard session to database"""
        # This would be implemented when database schema is extended
        pass
    
    def _calculate_flashcard_performance(self, accuracy: float, time_taken: float) -> str:
        """Calculate performance rating for flashcard session"""
        if accuracy >= 95 and time_taken < 60:
            return "MEMORY_GENIUS"
        elif accuracy >= 85 and time_taken < 120:
            return "QUICK_LEARNER"
        elif accuracy >= 75:
            return "SOLID_RECALL"
        elif accuracy >= 60:
            return "PROGRESSING"
        else:
            return "NEEDS_PRACTICE"

# ========== REQUEST DATABASE ==========
class RequestDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('metalens_requests.db', check_same_thread=False)
        self._create_tables()
    
    def _create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS word_requests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                username TEXT,
                word TEXT,
                language TEXT,
                context TEXT,
                status TEXT DEFAULT 'pending',
                timestamp TEXT,
                upvotes INTEGER DEFAULT 0,
                downvotes INTEGER DEFAULT 0
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS request_votes (
                user_id INTEGER,
                request_id INTEGER,
                vote_type TEXT,
                PRIMARY KEY (user_id, request_id)
            )
        ''')
        self.conn.commit()
    
    def add_request(self, user_id: int, username: str, word: str, language: str, context: str = ""):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO word_requests (user_id, username, word, language, context, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (user_id, username, word, language, context, datetime.now().isoformat()))
        self.conn.commit()
        return cursor.lastrowid
    
    def get_pending_requests(self, limit: int = 10):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT * FROM word_requests 
            WHERE status = 'pending' 
            ORDER BY (upvotes - downvotes) DESC, timestamp DESC
            LIMIT ?
        ''', (limit,))
        return cursor.fetchall()
    
    def vote_request(self, user_id: int, request_id: int, vote_type: str):
        cursor = self.conn.cursor()
        
        # Check if user already voted
        cursor.execute('SELECT vote_type FROM request_votes WHERE user_id = ? AND request_id = ?', 
                      (user_id, request_id))
        existing_vote = cursor.fetchone()
        
        if existing_vote:
            if existing_vote[0] == vote_type:
                return False  # Already voted same way
            # Change vote
            cursor.execute('''
                UPDATE request_votes SET vote_type = ? 
                WHERE user_id = ? AND request_id = ?
            ''', (vote_type, user_id, request_id))
            
            # Update vote counts
            if vote_type == 'upvote':
                cursor.execute('''
                    UPDATE word_requests 
                    SET upvotes = upvotes + 1, downvotes = downvotes - 1
                    WHERE id = ?
                ''', (request_id,))
            else:
                cursor.execute('''
                    UPDATE word_requests 
                    SET upvotes = upvotes - 1, downvotes = downvotes + 1
                    WHERE id = ?
                ''', (request_id,))
        else:
            # New vote
            cursor.execute('INSERT INTO request_votes VALUES (?, ?, ?)', 
                         (user_id, request_id, vote_type))
            
            # Update vote counts
            if vote_type == 'upvote':
                cursor.execute('UPDATE word_requests SET upvotes = upvotes + 1 WHERE id = ?', 
                             (request_id,))
            else:
                cursor.execute('UPDATE word_requests SET downvotes = downvotes + 1 WHERE id = ?', 
                             (request_id,))
        
        self.conn.commit()
        return True
    
    def get_request(self, request_id: int):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM word_requests WHERE id = ?', (request_id,))
        return cursor.fetchone()

# ========== ULTIMATE QUIZ SESSION MANAGER ==========
class UltimateQuizManager:
    def __init__(self):
        self.active_sessions = {}
        self.user_quizzes = defaultdict(list)
        self.quiz_statistics = defaultdict(lambda: {"correct": 0, "total": 0, "avg_time": 0})
        self.performance_history = defaultdict(list)
        self.vocab_matching_sessions = {}
    
    def create_quiz_session(self, user_id: int, quiz_type: str, questions: list):
        """Create ultimate quiz session with enhanced tracking"""
        session_id = f"{user_id}_{datetime.now().timestamp()}"
        self.active_sessions[session_id] = {
            'user_id': user_id,
            'quiz_type': quiz_type,
            'questions': questions,
            'current_question': 0,
            'score': 0,
            'start_time': datetime.now(),
            'answers': [],
            'question_start_time': datetime.now(),
            'perfect_streak': 0,
            'combo_multiplier': 1.0
        }
        return session_id
    
    def get_current_question(self, session_id: str):
        """Get current question with enhanced timing"""
        session = self.active_sessions.get(session_id)
        if not session:
            return None
        
        session['question_start_time'] = datetime.now()
        current_idx = session['current_question']
        
        if current_idx < len(session['questions']):
            return session['questions'][current_idx]
        return None
    
    def submit_answer(self, session_id: str, answer_index: int):
        """ULTIMATE answer submission with combo system"""
        session = self.active_sessions.get(session_id)
        if not session:
            return None
        
        current_idx = session['current_question']
        if current_idx >= len(session['questions']):
            return None
        
        question = session['questions'][current_idx]
        is_correct = (answer_index == question['correct'])
        
        # ULTIMATE scoring system
        time_taken = (datetime.now() - session['question_start_time']).total_seconds()
        time_bonus = max(0, 8 - (time_taken / 2))  # Enhanced time bonus
        
        base_points = question.get('points', 15)
        
        # Combo multiplier for consecutive correct answers
        if is_correct:
            session['perfect_streak'] += 1
            session['combo_multiplier'] = min(2.0, 1.0 + (session['perfect_streak'] * 0.2))
        else:
            session['perfect_streak'] = 0
            session['combo_multiplier'] = 1.0
        
        total_points = int((base_points + time_bonus) * session['combo_multiplier'])
        
        if is_correct:
            session['score'] += total_points
        
        session['answers'].append({
            'question_idx': current_idx,
            'answer': answer_index,
            'correct': is_correct,
            'points': total_points if is_correct else 0,
            'time_taken': time_taken,
            'combo_multiplier': session['combo_multiplier'],
            'neural_impact': question.get('neural_impact', 'General cognitive activation')
        })
        
        session['current_question'] += 1
        
        return {
            'is_correct': is_correct,
            'correct_answer': question['correct'],
            'explanation': question['explanation'],
            'points_earned': total_points if is_correct else 0,
            'time_bonus': time_bonus,
            'combo_multiplier': session['combo_multiplier'],
            'perfect_streak': session['perfect_streak'],
            'is_complete': session['current_question'] >= len(session['questions']),
            'neural_impact': question.get('neural_impact', 'General cognitive activation')
        }
    
    def get_session_results(self, session_id: str):
        """ULTIMATE results with detailed analytics"""
        session = self.active_sessions.get(session_id)
        if not session:
            return None
        
        total_questions = len(session['questions'])
        correct_answers = sum(1 for ans in session['answers'] if ans['correct'])
        total_points = session['score']
        accuracy = (correct_answers / total_questions) * 100 if total_questions > 0 else 0
        avg_time = sum(ans['time_taken'] for ans in session['answers']) / total_questions if total_questions > 0 else 0
        
        # Enhanced performance tracking
        max_combo = max([ans.get('combo_multiplier', 1.0) for ans in session['answers']], default=1.0)
        neural_impacts = [ans.get('neural_impact', '') for ans in session['answers']]
        
        # Update statistics
        user_stats = self.quiz_statistics[session['user_id']]
        user_stats['correct'] += correct_answers
        user_stats['total'] += total_questions
        user_stats['avg_time'] = (user_stats['avg_time'] + avg_time) / 2
        
        self.performance_history[session['user_id']].append({
            'timestamp': datetime.now(),
            'quiz_type': session['quiz_type'],
            'accuracy': accuracy,
            'total_points': total_points
        })
        
        return {
            'total_questions': total_questions,
            'correct_answers': correct_answers,
            'total_points': total_points,
            'accuracy': accuracy,
            'quiz_type': session['quiz_type'],
            'duration': (datetime.now() - session['start_time']).total_seconds(),
            'avg_time_per_question': avg_time,
            'max_combo': max_combo,
            'neural_impacts': neural_impacts,
            'performance_tier': self._calculate_performance_tier(accuracy, avg_time),
            'cognitive_rating': self._calculate_cognitive_rating(accuracy, avg_time, max_combo)
        }
    
    def _calculate_performance_tier(self, accuracy: float, avg_time: float) -> str:
        """ULTIMATE performance tier calculation"""
        if accuracy >= 95 and avg_time <= 6:
            return "NEURAL_MASTER"
        elif accuracy >= 85 and avg_time <= 10:
            return "COGNITIVE_CHAMPION" 
        elif accuracy >= 75 and avg_time <= 15:
            return "PATTERN_EXPERT"
        elif accuracy >= 65:
            return "ANALYTICAL_THINKER"
        else:
            return "PRACTICE_NEEDED"
    
    def _calculate_cognitive_rating(self, accuracy: float, avg_time: float, max_combo: float) -> str:
        """Calculate cognitive performance rating"""
        rating_score = (accuracy * 0.6) + ((20 - min(20, avg_time)) * 2) + (max_combo * 10)
        
        if rating_score >= 90:
            return "EXCEPTIONAL"
        elif rating_score >= 75:
            return "EXCELLENT"
        elif rating_score >= 60:
            return "GOOD"
        else:
            return "DEVELOPING"
    
    def cleanup_session(self, session_id: str):
        """Clean up completed session"""
        if session_id in self.active_sessions:
            del self.active_sessions[session_id]

    def create_vocab_matching_session(self, user_id: int, game_type: str):
        """Create vocabulary matching game session - FIXED VERSION"""
        game_data = VOCAB_MATCHING_GAMES.get(game_type)
        if not game_data:
            return None
        
        pairs = game_data['pairs']
        
        # Create flat list of all items
        items = []
        for key, value in pairs.items():
            items.append(key)
            items.append(value)
        
        random.shuffle(items)
        
        session_id = f"vocab_{user_id}_{datetime.now().timestamp()}"
        
        self.vocab_matching_sessions[session_id] = {
            'user_id': user_id,
            'game_type': game_type,
            'pairs': pairs,
            'items': items,
            'selected_items': [],
            'matched_pairs': [],
            'start_time': datetime.now(),
            'moves': 0,
            'score': 0,
            'completed': False
        }
        
        return session_id

    def process_vocab_selection(self, session_id: str, item_index: int):
        """Process item selection in vocabulary matching game - FIXED VERSION"""
        session = self.vocab_matching_sessions.get(session_id)
        if not session or session.get('completed'):
            return None
        
        if item_index in session['selected_items']:
            return None  # Already selected
        
        # Ensure item_index is within bounds
        if item_index >= len(session['items']):
            return None
        
        session['selected_items'].append(item_index)
        session['moves'] += 1
        
        if len(session['selected_items']) == 2:
            # Check for match
            idx1, idx2 = session['selected_items']
            item1 = session['items'][idx1]
            item2 = session['items'][idx2]
            
            is_match = False
            pairs = session['pairs']
            
            # Check both directions (key->value and value->key)
            if item1 in pairs and pairs[item1] == item2:
                is_match = True
            elif item2 in pairs and pairs[item2] == item1:
                is_match = True
            
            if is_match:
                session['matched_pairs'].extend(session['selected_items'])
                session['score'] += 10
                # Bonus for quick matches
                time_elapsed = (datetime.now() - session['start_time']).total_seconds()
                if time_elapsed < 60:
                    session['score'] += 5
            
            # Check if game is complete
            if len(session['matched_pairs']) == len(session['items']):
                session['completed'] = True
                # Time bonus
                time_elapsed = (datetime.now() - session['start_time']).total_seconds()
                time_bonus = max(0, 50 - (time_elapsed / 3))
                session['score'] += int(time_bonus)
            
            result = {
                'selected_indices': session['selected_items'][:],
                'is_match': is_match,
                'completed': session['completed'],
                'score': session['score'],
                'moves': session['moves']
            }
            
            session['selected_items'] = []  # Reset for next selection
            return result
        
        return {'selected_indices': session['selected_items'][:]}

    def get_vocab_game_results(self, session_id: str):
        """Get final results for vocabulary matching game - FIXED VERSION"""
        session = self.vocab_matching_sessions.get(session_id)
        if not session or not session.get('completed'):
            return None
        
        game_data = VOCAB_MATCHING_GAMES.get(session['game_type'], {})
        base_points = game_data.get('points', 50)
        total_points = session['score'] + base_points
        
        total_pairs = len(session['pairs'])
        efficiency = (total_pairs * 2 / session['moves']) * 100 if session['moves'] > 0 else 0
        
        return {
            'game_type': session['game_type'],
            'total_pairs': total_pairs,
            'moves': session['moves'],
            'efficiency': efficiency,
            'base_points': base_points,
            'game_score': session['score'],
            'total_points': total_points,
            'time_taken': (datetime.now() - session['start_time']).total_seconds(),
            'performance_rating': self._calculate_matching_performance(efficiency, session['moves'])
        }

    def _calculate_matching_performance(self, efficiency: float, moves: int) -> str:
        """Calculate performance rating for matching game"""
        if efficiency >= 90 and moves <= 8:
            return "MEMORY_GENIUS"
        elif efficiency >= 80 and moves <= 12:
            return "PATTERN_MASTER"
        elif efficiency >= 70:
            return "QUICK_LEARNER"
        elif efficiency >= 60:
            return "STRATEGIC_THINKER"
        else:
            return "PRACTICE_NEEDED"

# ========== ULTIMATE GAMIFICATION SYSTEM ==========
ACHIEVEMENTS = {
    "first_analysis": {"name": "🔍 First Analysis", "description": "Analyze your first word", "points": 25, "icon": "🔍", "tier": "bronze"},
    "neural_pathway_builder": {"name": "🧠 Neural Pathway Builder", "description": "Analyze 50 words", "points": 150, "icon": "🧠", "tier": "silver"},
    "cognitive_linguist": {"name": "🎓 Cognitive Linguist", "description": "Reach level 10", "points": 300, "icon": "🎓", "tier": "gold"},
    "polyglot_master": {"name": "🌍 Polyglot Master", "description": "Analyze words in 5 languages", "points": 250, "icon": "🌍", "tier": "gold"},
    "quiz_champion": {"name": "🏆 Quiz Champion", "description": "Score 100% on 10 quizzes", "points": 500, "icon": "🏆", "tier": "platinum"},
    "morphology_genius": {"name": "🔬 Morphology Genius", "description": "Analyze 100 complex words", "points": 750, "icon": "🔬", "tier": "diamond"},
    "daily_researcher": {"name": "📅 Daily Researcher", "description": "30-day streak", "points": 600, "icon": "📅", "tier": "platinum"},
    "language_detective": {"name": "🕵️ Language Detective", "description": "Identify 50 language patterns", "points": 400, "icon": "🕵️", "tier": "gold"},
    "audio_master": {"name": "🎧 Phonetic Expert", "description": "Complete 20 audio quizzes", "points": 350, "icon": "🎧", "tier": "silver"},
    "speed_thinker": {"name": "⚡ Speed Thinker", "description": "Answer quizzes with <5s average", "points": 450, "icon": "⚡", "tier": "gold"},
    "perfect_streak": {"name": "💯 Perfect Streak", "description": "Get 100% accuracy on 5 quizzes in a row", "points": 600, "icon": "💯", "tier": "platinum"},
    "combo_king": {"name": "🎯 Combo King", "description": "Achieve 2.0x combo multiplier", "points": 300, "icon": "🎯", "tier": "gold"},
    "neural_networker": {"name": "🔄 Neural Networker", "description": "Activate all cognitive skills", "points": 800, "icon": "🔄", "tier": "diamond"},
    "vocab_master": {"name": "🧩 Vocabulary Master", "description": "Complete 10 vocabulary matching games", "points": 400, "icon": "🧩", "tier": "gold"},
    "request_contributor": {"name": "💡 Research Contributor", "description": "Submit 10 word requests", "points": 300, "icon": "💡", "tier": "silver"},
    "community_voter": {"name": "🗳️ Community Voter", "description": "Vote on 20 word requests", "points": 250, "icon": "🗳️", "tier": "silver"},
    # NEW STORYTELLING ACHIEVEMENTS
    "story_completion": {"name": "📖 Story Explorer", "description": "Complete your first interactive story", "points": 100, "icon": "📖", "tier": "bronze"},
    "story_master": {"name": "🎭 Story Master", "description": "Complete 10 interactive stories", "points": 500, "icon": "🎭", "tier": "gold"},
    "multilingual_storyteller": {"name": "🌍 Multilingual Storyteller", "description": "Complete stories in 3 different languages", "points": 300, "icon": "🌍", "tier": "silver"},
    "perfect_comprehension": {"name": "💯 Perfect Comprehension", "description": "Get 100% on all story comprehension questions", "points": 400, "icon": "💯", "tier": "gold"},
    "cognitive_storyteller": {"name": "🧠 Cognitive Storyteller", "description": "Activate all cognitive effects in a story", "points": 350, "icon": "🧠", "tier": "silver"},
    # NEW FLASHCARD ACHIEVEMENTS
    "flashcard_beginner": {"name": "📚 Flashcard Beginner", "description": "Complete your first flashcard session", "points": 50, "icon": "📚", "tier": "bronze"},
    "flashcard_master": {"name": "🎴 Flashcard Master", "description": "Complete 20 flashcard sessions", "points": 300, "icon": "🎴", "tier": "gold"},
    "memory_champion": {"name": "💭 Memory Champion", "description": "Achieve 95% accuracy in flashcard sessions", "points": 400, "icon": "💭", "tier": "gold"},
}

COGNITIVE_BADGES = {
    "pattern_recognition": {"name": "🎯 Pattern Master", "description": "Excellent at identifying morphological patterns", "icon": "🎯", "requirements": {"quizzes_completed": 10, "accuracy": 85}},
    "cross_linguistic": {"name": "🔄 Cross-Linguistic Expert", "description": "Skilled at language comparisons", "icon": "🔄", "requirements": {"languages_used": 3, "translation_quizzes": 8}},
    "memory_champion": {"name": "💭 Memory Champion", "description": "Superior word retention", "icon": "💭", "requirements": {"words_analyzed": 100, "streak": 14}},
    "analysis_pro": {"name": "🔍 Analysis Pro", "description": "Expert morphological analyzer", "icon": "🔍", "requirements": {"complex_words": 50, "morphology_quizzes": 15}},
    "audio_phile": {"name": "🎧 Audio Linguist", "description": "Master of phonetic recognition", "icon": "🎧", "requirements": {"audio_quizzes": 25, "audio_accuracy": 90}},
    "speed_demon": {"name": "⚡ Speed Demon", "description": "Lightning-fast cognitive processing", "icon": "⚡", "requirements": {"avg_answer_time": 5, "quizzes_completed": 20}},
    "combo_master": {"name": "🔥 Combo Master", "description": "Master of consecutive correct answers", "icon": "🔥", "requirements": {"max_combo": 2.0, "perfect_quizzes": 5}},
    "vocab_genius": {"name": "🧩 Vocabulary Genius", "description": "Master of word matching games", "icon": "🧩", "requirements": {"matching_games": 10, "matching_efficiency": 85}},
    "story_teller": {"name": "📚 Story Teller", "description": "Master of interactive storytelling", "icon": "📚", "requirements": {"stories_completed": 5, "story_comprehension": 80}},
    "flashcard_expert": {"name": "🎴 Flashcard Expert", "description": "Master of vocabulary flashcards", "icon": "🎴", "requirements": {"flashcard_sessions": 15, "flashcard_accuracy": 90}},
}

# ========== ULTIMATE DATABASE CLASS ==========
class UltimateDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('metalens_revolutionary.db', check_same_thread=False)
        self._create_tables()
    
    def _create_tables(self):
        """Create revolutionary database tables"""
        cursor = self.conn.cursor()
        
        # Drop tables if they exist
        cursor.execute('DROP TABLE IF EXISTS users')
        cursor.execute('DROP TABLE IF EXISTS user_achievements')
        cursor.execute('DROP TABLE IF EXISTS cognitive_metrics')
        cursor.execute('DROP TABLE IF EXISTS quiz_history')
        cursor.execute('DROP TABLE IF EXISTS vocab_game_history')
        cursor.execute('DROP TABLE IF EXISTS story_history')  # NEW: Story tracking
        cursor.execute('DROP TABLE IF EXISTS flashcard_history')  # NEW: Flashcard tracking
        
        cursor.execute('''
            CREATE TABLE users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                joined_date TEXT,
                last_active TEXT,
                total_words INTEGER DEFAULT 0,
                total_quizzes INTEGER DEFAULT 0,
                achievement_points INTEGER DEFAULT 0,
                daily_streak INTEGER DEFAULT 0,
                last_activity_date TEXT,
                cognitive_level INTEGER DEFAULT 1,
                languages_used TEXT DEFAULT '[]',
                audio_quizzes_completed INTEGER DEFAULT 0,
                perfect_quizzes INTEGER DEFAULT 0,
                current_streak INTEGER DEFAULT 0,
                total_points INTEGER DEFAULT 0,
                max_combo REAL DEFAULT 1.0,
                avg_answer_time REAL DEFAULT 0.0,
                vocab_games_completed INTEGER DEFAULT 0,
                word_requests_submitted INTEGER DEFAULT 0,
                requests_voted INTEGER DEFAULT 0,
                stories_completed INTEGER DEFAULT 0,  -- NEW: Story progress
                total_story_points INTEGER DEFAULT 0,  -- NEW: Story points
                flashcard_sessions INTEGER DEFAULT 0,  -- NEW: Flashcard sessions
                total_flashcard_points INTEGER DEFAULT 0  -- NEW: Flashcard points
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE user_achievements (
                user_id INTEGER,
                achievement_id TEXT,
                earned_date TEXT,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE cognitive_metrics (
                user_id INTEGER,
                metric_type TEXT,
                value REAL,
                timestamp TEXT,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE quiz_history (
                user_id INTEGER,
                quiz_type TEXT,
                score INTEGER,
                total_questions INTEGER,
                accuracy REAL,
                duration REAL,
                completed_date TEXT,
                performance_tier TEXT,
                cognitive_rating TEXT,
                max_combo REAL
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE vocab_game_history (
                user_id INTEGER,
                game_type TEXT,
                score INTEGER,
                total_pairs INTEGER,
                moves INTEGER,
                efficiency REAL,
                duration REAL,
                completed_date TEXT,
                performance_rating TEXT
            )
        ''')
        
        # NEW: Story history table
        cursor.execute('''
            CREATE TABLE story_history (
                user_id INTEGER,
                story_id TEXT,
                points INTEGER,
                comprehension REAL,
                vocabulary_learned INTEGER,
                completed_date TEXT,
                performance_rating TEXT
            )
        ''')
        
        # NEW: Flashcard history table
        cursor.execute('''
            CREATE TABLE flashcard_history (
                user_id INTEGER,
                deck_id TEXT,
                points INTEGER,
                accuracy REAL,
                total_cards INTEGER,
                cards_known INTEGER,
                duration REAL,
                completed_date TEXT,
                performance_rating TEXT
            )
        ''')
        
        self.conn.commit()
        print("✅ ULTIMATE REVOLUTIONARY DATABASE CREATED!")
    
    def get_user(self, user_id: int):
        """Get user data with enhanced metrics"""
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
            result = cursor.fetchone()
            
            if result:
                return {
                    'user_id': result[0],
                    'username': result[1],
                    'first_name': result[2],
                    'joined_date': result[3],
                    'last_active': result[4],
                    'total_words': result[5] or 0,
                    'total_quizzes': result[6] or 0,
                    'achievement_points': result[7] or 0,
                    'daily_streak': result[8] or 0,
                    'last_activity_date': result[9],
                    'cognitive_level': result[10] or 1,
                    'languages_used': json.loads(result[11] or '[]'),
                    'audio_quizzes_completed': result[12] or 0,
                    'perfect_quizzes': result[13] or 0,
                    'current_streak': result[14] or 0,
                    'total_points': result[15] or 0,
                    'max_combo': result[16] or 1.0,
                    'avg_answer_time': result[17] or 0.0,
                    'vocab_games_completed': result[18] or 0,
                    'word_requests_submitted': result[19] or 0,
                    'requests_voted': result[20] or 0,
                    'stories_completed': result[21] or 0,  # NEW
                    'total_story_points': result[22] or 0,  # NEW
                    'flashcard_sessions': result[23] or 0,  # NEW
                    'total_flashcard_points': result[24] or 0  # NEW
                }
            return None
        except Exception as e:
            print(f"❌ Database error in get_user: {e}")
            return None
    
    def update_user(self, user_id: int, username: str = None, first_name: str = None, 
                   words: int = 0, quizzes: int = 0, language: str = None, 
                   audio_quizzes: int = 0, perfect_quiz: bool = False,
                   points: int = 0, max_combo: float = None, answer_time: float = None,
                   vocab_games: int = 0, word_requests: int = 0, requests_voted: int = 0,
                   stories: int = 0, story_points: int = 0,  # NEW: Story parameters
                   flashcard_sessions: int = 0, flashcard_points: int = 0):  # NEW: Flashcard parameters
        """ULTIMATE user update with advanced tracking"""
        try:
            cursor = self.conn.cursor()
            today = datetime.now().date().isoformat()
            
            user = self.get_user(user_id)
            if user:
                # Enhanced streak calculation
                last_date = user['last_activity_date']
                streak = user['daily_streak']
                current_streak = user['current_streak']
                
                if last_date and last_date != today:
                    streak = streak + 1
                    current_streak = current_streak + 1
                else:
                    streak = max(streak, 1)
                    current_streak = max(current_streak, 1)
                
                # Update languages used
                languages_used = user['languages_used']
                if language and language not in languages_used:
                    languages_used.append(language)
                
                # Enhanced quiz stats
                audio_quizzes_total = user['audio_quizzes_completed'] + audio_quizzes
                perfect_quizzes_total = user['perfect_quizzes'] + (1 if perfect_quiz else 0)
                total_points = user['total_points'] + points
                vocab_games_total = user['vocab_games_completed'] + vocab_games
                word_requests_total = user['word_requests_submitted'] + word_requests
                requests_voted_total = user['requests_voted'] + requests_voted
                stories_completed_total = user['stories_completed'] + stories  # NEW
                story_points_total = user['total_story_points'] + story_points  # NEW
                flashcard_sessions_total = user['flashcard_sessions'] + flashcard_sessions  # NEW
                flashcard_points_total = user['total_flashcard_points'] + flashcard_points  # NEW
                
                # Update combo and timing
                new_max_combo = max(user['max_combo'], max_combo or 1.0)
                if answer_time:
                    total_quizzes = user['total_quizzes'] + quizzes
                    new_avg_time = ((user['avg_answer_time'] * user['total_quizzes']) + answer_time) / total_quizzes if total_quizzes > 0 else answer_time
                else:
                    new_avg_time = user['avg_answer_time']
                
                cursor.execute('''
                    UPDATE users 
                    SET username = COALESCE(?, username),
                        first_name = COALESCE(?, first_name),
                        total_words = total_words + ?,
                        total_quizzes = total_quizzes + ?,
                        last_active = ?,
                        daily_streak = ?,
                        last_activity_date = ?,
                        languages_used = ?,
                        audio_quizzes_completed = ?,
                        perfect_quizzes = ?,
                        current_streak = ?,
                        total_points = ?,
                        max_combo = ?,
                        avg_answer_time = ?,
                        vocab_games_completed = ?,
                        word_requests_submitted = ?,
                        requests_voted = ?,
                        stories_completed = ?,
                        total_story_points = ?,
                        flashcard_sessions = ?,
                        total_flashcard_points = ?
                    WHERE user_id = ?
                ''', (username, first_name, words, quizzes, datetime.now().isoformat(), 
                      streak, today, json.dumps(languages_used), audio_quizzes_total, 
                      perfect_quizzes_total, current_streak, total_points, new_max_combo, 
                      new_avg_time, vocab_games_total, word_requests_total, requests_voted_total,
                      stories_completed_total, story_points_total, flashcard_sessions_total, 
                      flashcard_points_total, user_id))
            else:
                languages_used = [language] if language else []
                cursor.execute('''
                    INSERT INTO users (user_id, username, first_name, joined_date, last_active, 
                                     total_words, total_quizzes, daily_streak, last_activity_date, 
                                     languages_used, audio_quizzes_completed, perfect_quizzes, current_streak,
                                     total_points, max_combo, avg_answer_time, vocab_games_completed,
                                     word_requests_submitted, requests_voted, stories_completed, total_story_points,
                                     flashcard_sessions, total_flashcard_points)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (user_id, username, first_name, datetime.now().isoformat(), 
                      datetime.now().isoformat(), words, quizzes, 1, today, 
                      json.dumps(languages_used), audio_quizzes, 1 if perfect_quiz else 0, 1,
                      points, max_combo or 1.0, answer_time or 0.0, vocab_games, word_requests, requests_voted,
                      stories, story_points, flashcard_sessions, flashcard_points))
            
            self.conn.commit()
            return self.get_user(user_id)
        except Exception as e:
            print(f"❌ Database error in update_user: {e}")
            return None
    
    def log_quiz_result(self, user_id: int, quiz_type: str, score: int, total_questions: int, 
                       accuracy: float, duration: float, performance_tier: str, cognitive_rating: str, max_combo: float):
        """ULTIMATE quiz result logging"""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO quiz_history (user_id, quiz_type, score, total_questions, accuracy, duration, completed_date, performance_tier, cognitive_rating, max_combo)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (user_id, quiz_type, score, total_questions, accuracy, duration, datetime.now().isoformat(), performance_tier, cognitive_rating, max_combo))
            self.conn.commit()
        except Exception as e:
            print(f"❌ Error logging quiz result: {e}")
    
    def log_vocab_game_result(self, user_id: int, game_type: str, score: int, total_pairs: int,
                             moves: int, efficiency: float, duration: float, performance_rating: str):
        """Log vocabulary matching game results"""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO vocab_game_history (user_id, game_type, score, total_pairs, moves, efficiency, duration, completed_date, performance_rating)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (user_id, game_type, score, total_pairs, moves, efficiency, duration, datetime.now().isoformat(), performance_rating))
            self.conn.commit()
        except Exception as e:
            print(f"❌ Error logging vocab game result: {e}")
    
    # NEW: Story completion logging
    def log_story_completion(self, user_id: int, story_id: str, points: int, 
                            comprehension: float, vocabulary_learned: int):
        """Log story completion with cognitive metrics"""
        try:
            cursor = self.conn.cursor()
            performance_rating = "STORY_MASTER" if comprehension >= 90 else "LINGUISTIC_GENIUS" if comprehension >= 75 else "ACTIVE_LEARNER" if comprehension >= 60 else "BEGINNER_STORYTELLER"
            
            cursor.execute('''
                INSERT INTO story_history (user_id, story_id, points, comprehension, vocabulary_learned, completed_date, performance_rating)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (user_id, story_id, points, comprehension, vocabulary_learned, datetime.now().isoformat(), performance_rating))
            self.conn.commit()
        except Exception as e:
            print(f"❌ Error logging story completion: {e}")
    
    # NEW: Flashcard session logging
    def log_flashcard_session(self, user_id: int, deck_id: str, points: int, accuracy: float,
                             total_cards: int, cards_known: int, duration: float, performance_rating: str):
        """Log flashcard session results"""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO flashcard_history (user_id, deck_id, points, accuracy, total_cards, cards_known, duration, completed_date, performance_rating)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (user_id, deck_id, points, accuracy, total_cards, cards_known, duration, datetime.now().isoformat(), performance_rating))
            self.conn.commit()
        except Exception as e:
            print(f"❌ Error logging flashcard session: {e}")
    
    def get_story_progress(self, user_id: int):
        """Get user's story progress"""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT story_id, COUNT(*) as completions, AVG(comprehension) as avg_comprehension,
                       SUM(points) as total_points, MAX(completed_date) as last_completed
                FROM story_history 
                WHERE user_id = ?
                GROUP BY story_id
            ''', (user_id,))
            return cursor.fetchall()
        except:
            return []
    
    def get_flashcard_progress(self, user_id: int):
        """Get user's flashcard progress"""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT deck_id, COUNT(*) as sessions, AVG(accuracy) as avg_accuracy,
                       SUM(points) as total_points, MAX(completed_date) as last_session
                FROM flashcard_history 
                WHERE user_id = ?
                GROUP BY deck_id
            ''', (user_id,))
            return cursor.fetchall()
        except:
            return []
    
    def grant_achievement(self, user_id: int, achievement_id: str):
        """Grant achievement with enhanced tracking"""
        try:
            cursor = self.conn.cursor()
            
            cursor.execute('SELECT * FROM user_achievements WHERE user_id = ? AND achievement_id = ?', (user_id, achievement_id))
            if not cursor.fetchone():
                cursor.execute('''
                    INSERT INTO user_achievements (user_id, achievement_id, earned_date)
                    VALUES (?, ?, ?)
                ''', (user_id, achievement_id, datetime.now().isoformat()))
                
                achievement = ACHIEVEMENTS.get(achievement_id, {})
                points = achievement.get('points', 0)
                cursor.execute('UPDATE users SET achievement_points = achievement_points + ? WHERE user_id = ?', (points, user_id))
                
                self.conn.commit()
                return True
            return False
        except Exception as e:
            print(f"❌ Database error in grant_achievement: {e}")
            return False
    
    def get_achievements(self, user_id: int):
        """Get user's achievements"""
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT achievement_id FROM user_achievements WHERE user_id = ?', (user_id,))
            return [row[0] for row in cursor.fetchall()]
        except:
            return []
    
    def get_leaderboard(self, limit: int = 10):
        """ULTIMATE leaderboard with enhanced metrics"""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT user_id, username, total_points, achievement_points, current_streak, total_words, cognitive_level
                FROM users 
                ORDER BY total_points DESC, achievement_points DESC, current_streak DESC
                LIMIT ?
            ''', (limit,))
            return cursor.fetchall()
        except:
            return []
    
    def log_cognitive_metric(self, user_id: int, metric_type: str, value: float):
        """Log cognitive metrics for advanced analytics"""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO cognitive_metrics (user_id, metric_type, value, timestamp)
                VALUES (?, ?, ?, ?)
            ''', (user_id, metric_type, value, datetime.now().isoformat()))
            self.conn.commit()
        except Exception as e:
            print(f"❌ Error logging cognitive metric: {e}")

# ========== ULTIMATE SUPPORTING CLASSES ==========
class UltimateTelegramFeatures:
    def __init__(self):
        self.user_streaks = defaultdict(int)
    
    async def send_cognitive_insight(self, update: Update, insight_type: str):
        """Send ULTIMATE personalized cognitive insights"""
        insights = {
            "neural_activity": 
                "🧠 <b>Neural Activity Update</b>\n"
                "Your brain just strengthened pathways in Broca's area!\n"
                "⚡ Processing speed increased by 12%",
            
            "pattern_recognition": 
                "🎯 <b>Pattern Recognition Boost</b>\n"
                "Enhanced morphological structure identification!\n"
                "🔍 Pattern accuracy: 94%",
            
            "memory_formation": 
                "💭 <b>Memory Formation Activated</b>\n"
                "New synaptic connections formed for long-term retention!\n"
                "📚 Retention rate: 88%",
            
            "cognitive_load": 
                "⚡ <b>Cognitive Load Optimized</b>\n"
                "Your brain is efficiently processing complex linguistic data!\n"
                "🎯 Efficiency: 96%",
            
            "audio_processing":
                "🎧 <b>Auditory Cortex Engagement</b>\n"
                "Enhanced phonetic processing and discrimination!\n"
                "👂 Audio accuracy: 91%",
            
            "story_immersion":
                "📖 <b>Narrative Immersion Activated</b>\n"
                "Your brain is processing story structures and linguistic patterns simultaneously!\n"
                "🎭 Immersion level: 89%",
            
            "flashcard_memory":
                "🎴 <b>Flashcard Memory Boost</b>\n"
                "Enhanced vocabulary retention through spaced repetition!\n"
                "💭 Recall accuracy: 92%"
        }
        
        if insight_type in insights:
            await update.message.reply_text(insights[insight_type], parse_mode='HTML')
    
    async def send_typing_indicator(self, update: Update, duration: int = 3):
        """Show ULTIMATE typing indicator for cognitive processing"""
        await update.message.chat.send_action(action="typing")
        await asyncio.sleep(duration)

class CognitiveAnalytics:
    def __init__(self, db: UltimateDatabase):
        self.db = db
        self.user_patterns = defaultdict(lambda: defaultdict(int))
        self.learning_curves = defaultdict(list)
    
    def track_cognitive_metric(self, user_id: int, metric: str, value: float):
        """Track ULTIMATE cognitive metrics"""
        self.db.log_cognitive_metric(user_id, metric, value)
    
    def calculate_learning_curve(self, user_id: int):
        """Calculate ULTIMATE learning progression"""
        user_data = self.db.get_user(user_id)
        if user_data and user_data['total_words'] > 0:
            base_progress = min(1.0, user_data['total_words'] / 100.0)
            quiz_boost = min(0.3, user_data['total_quizzes'] / 50.0)
            vocab_boost = min(0.2, user_data['vocab_games_completed'] / 20.0)
            story_boost = min(0.2, user_data['stories_completed'] / 10.0)  # NEW: Story boost
            flashcard_boost = min(0.2, user_data['flashcard_sessions'] / 15.0)  # NEW: Flashcard boost
            return min(1.0, base_progress + quiz_boost + vocab_boost + story_boost + flashcard_boost)
        return 0.1
    
    def get_cognitive_profile(self, user_id: int):
        """Generate ULTIMATE cognitive profile"""
        user_data = self.db.get_user(user_id)
        
        if not user_data:
            return {
                'processing_speed': 0.5,
                'pattern_accuracy': 0.5,
                'memory_strength': 0.5,
                'learning_efficiency': 0.1,
                'audio_processing': 0.3,
                'analytical_thinking': 0.4,
                'vocabulary_recall': 0.3,
                'narrative_comprehension': 0.2,  # NEW: Story comprehension
                'flashcard_memory': 0.2  # NEW: Flashcard memory
            }
        
        words_analyzed = user_data['total_words']
        quizzes_completed = user_data['total_quizzes']
        vocab_games = user_data['vocab_games_completed']
        stories_completed = user_data['stories_completed']  # NEW
        flashcard_sessions = user_data['flashcard_sessions']  # NEW
        avg_time = user_data['avg_answer_time']
        
        processing_speed = min(1.0, (20 - min(20, avg_time)) / 15.0) if avg_time > 0 else 0.5
        pattern_accuracy = min(1.0, (words_analyzed + quizzes_completed) / 80.0)
        memory_strength = min(1.0, words_analyzed / 30.0)
        learning_efficiency = self.calculate_learning_curve(user_id)
        audio_processing = min(1.0, user_data['audio_quizzes_completed'] / 20.0)
        analytical_thinking = min(1.0, (user_data['total_points'] / 500.0) + (user_data['max_combo'] / 3.0))
        vocabulary_recall = min(1.0, vocab_games / 15.0)
        narrative_comprehension = min(1.0, stories_completed / 8.0)  # NEW: Story metric
        flashcard_memory = min(1.0, flashcard_sessions / 12.0)  # NEW: Flashcard metric
        
        return {
            'processing_speed': processing_speed,
            'pattern_accuracy': pattern_accuracy,
            'memory_strength': memory_strength,
            'learning_efficiency': learning_efficiency,
            'audio_processing': audio_processing,
            'analytical_thinking': analytical_thinking,
            'vocabulary_recall': vocabulary_recall,
            'narrative_comprehension': narrative_comprehension,  # NEW
            'flashcard_memory': flashcard_memory  # NEW
        }

# ========== ULTIMATE REVOLUTIONARY BOT CLASS ==========
class RevolutionaryMetalensBot:
    def __init__(self):
        self.app = Application.builder().token(TOKEN).build()
        self.db = UltimateDatabase()
        self.telegram_features = UltimateTelegramFeatures()
        self.analytics = CognitiveAnalytics(self.db)
        self.user_sessions = defaultdict(dict)
        self.cognitive_challenges = self._setup_cognitive_challenges()
        self.quiz_manager = UltimateQuizManager()
        self.request_db = RequestDatabase()
        self.story_manager = UltimateStorytellingManager(self.db)  # NEW: Story manager
        self.flashcard_manager = FlashcardGameManager(self.db)  # NEW: Flashcard manager
        
        self._setup_revolutionary_handlers()
        print("🚀 ULTIMATE REVOLUTIONARY METALENS BOT v7.0 INITIALIZED!")
        print("🎭 STORYTELLING SYSTEM: ACTIVATED")
        print("📖 INTERACTIVE NARRATIVES: READY")
        print("🎧 AUDIO STORIES: INTEGRATED")
        print("🎴 FLASHCARD SYSTEM: ACTIVATED")
        print("💡 COMMAND SUGGESTIONS: ENABLED")
    
    def _setup_cognitive_challenges(self):
        """Setup ULTIMATE cognitive challenges"""
        return {
            'pattern_recognition': {
                'name': 'Pattern Recognition Master',
                'description': 'Identify morphological patterns across languages',
                'difficulty': 'intermediate',
                'rewards': {'points': 100, 'badge': 'pattern_recognition'}
            },
            'memory_challenge': {
                'name': 'Memory Recall Challenge', 
                'description': 'Test your word retention and recall abilities',
                'difficulty': 'beginner',
                'rewards': {'points': 75, 'badge': 'memory_champion'}
            },
            'speed_analysis': {
                'name': 'Speed Analysis Challenge',
                'description': 'Analyze words under time pressure',
                'difficulty': 'advanced',
                'rewards': {'points': 150, 'badge': 'speed_demon'}
            },
            'story_comprehension': {  # NEW: Story challenge
                'name': 'Story Comprehension Master',
                'description': 'Master narrative understanding across languages',
                'difficulty': 'intermediate',
                'rewards': {'points': 120, 'badge': 'story_teller'}
            },
            'flashcard_mastery': {  # NEW: Flashcard challenge
                'name': 'Flashcard Memory Master',
                'description': 'Achieve perfect recall in flashcard sessions',
                'difficulty': 'intermediate',
                'rewards': {'points': 100, 'badge': 'flashcard_expert'}
            }
        }
    
    def _setup_revolutionary_handlers(self):
        """Setup ULTIMATE revolutionary command handlers with enhanced command suggestions"""
        revolutionary_commands = [
            CommandHandler("start", self._revolutionary_start),
            CommandHandler("analyze", self._cognitive_analysis),
            CommandHandler("deepdive", self._deep_dive_analysis),
            CommandHandler("quiz", self._adaptive_quiz),
            CommandHandler("audioquiz", self._audio_quiz_command),
            CommandHandler("pronounce", self._pronounce_word),
            CommandHandler("brainstorm", self._brainstorm_session),
            CommandHandler("challenge", self._daily_cognitive_challenge),
            CommandHandler("progress", self._cognitive_progress),
            CommandHandler("profile", self._cognitive_profile),
            CommandHandler("compare", self._multilingual_comparison),
            CommandHandler("pattern", self._pattern_recognition_game),
            CommandHandler("leaderboard", self._interactive_leaderboard),
            CommandHandler("community", self._language_community),
            CommandHandler("research", self._live_research_session),
            CommandHandler("insights", self._personalized_insights),
            CommandHandler("badges", self._cognitive_badges),
            CommandHandler("help", self._revolutionary_help),
            # NEW COMMANDS
            CommandHandler("request", self._word_request),
            CommandHandler("vocab", self._vocab_matching_menu),
            CommandHandler("requests", self._view_requests),
            CommandHandler("match", self._vocab_matching_game),
            CommandHandler("story", self._storytelling_menu),  # NEW: Story command
            CommandHandler("flashcards", self._flashcard_menu),  # NEW: Flashcard command
        ]
        
        for handler in revolutionary_commands:
            self.app.add_handler(handler)
        
        # Enhanced message handler with command suggestions
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self._smart_message_handler))
        self.app.add_handler(CallbackQueryHandler(self._advanced_button_handler))
        
        # Add command suggestions for better UX
        self._setup_command_suggestions()
        
        print("✅ ULTIMATE REVOLUTIONARY HANDLERS SETUP COMPLETE!")
    
    def _setup_command_suggestions(self):
        """Setup command suggestions for better user experience"""
        commands = [
            ("start", "Start the Ultimate Cognitive Bot"),
            ("analyze", "Analyze word morphology and structure"),
            ("quiz", "Take adaptive cognitive quizzes"),
            ("audioquiz", "Audio pronunciation challenges"),
            ("story", "Interactive multilingual stories"),
            ("flashcards", "Vocabulary learning flashcards"),
            ("vocab", "Vocabulary matching games"),
            ("pronounce", "Hear word pronunciations"),
            ("progress", "View your cognitive progress"),
            ("profile", "Detailed cognitive profile"),
            ("leaderboard", "Global rankings"),
            ("request", "Suggest words for analysis"),
            ("help", "Complete command list and guidance")
        ]
        
        # This would set bot commands in Telegram menu
        # Note: Actual bot command setting requires BotFather configuration
        print("💡 Command suggestions available for better user experience!")
    
    # ========== ENHANCED FLASHCARD GAME METHODS ==========
    async def _flashcard_menu(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ULTIMATE flashcard learning menu"""
        keyboard = [
            [InlineKeyboardButton("🧠 Kazakh Basics", callback_data="flashcard_deck:kazakh_basics"),
             InlineKeyboardButton("🧠 English Advanced", callback_data="flashcard_deck:english_advanced")],
            [InlineKeyboardButton("🧠 Cross-Linguistic", callback_data="flashcard_deck:cross_linguistic"),
             InlineKeyboardButton("🎯 Quick Session", callback_data="flashcard_quick")],
            [InlineKeyboardButton("📊 My Flashcard Stats", callback_data="flashcard_stats"),
             InlineKeyboardButton("🏆 Flashcard Achievements", callback_data="flashcard_achievements")],
            [InlineKeyboardButton("↩️ Back to Main", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        menu_text = """
🎴 <b>COGNITIVE FLASHCARD SYSTEM</b>

<i><b>Master vocabulary through scientifically-proven spaced repetition!</b></i>

📚 <b>Available Decks:</b>
• <b>Kazakh Basics</b> - Fundamental Kazakh morphology
• <b>English Advanced</b> - Complex English word formation  
• <b>Cross-Linguistic</b> - Compare patterns across languages
• <b>Quick Session</b> - Random selection for variety

🧠 <b>Scientific Benefits:</b>
• Enhanced long-term memory retention
• Improved pattern recognition
• Faster vocabulary recall
• Strengthened neural pathways
• Optimized learning efficiency

💡 <b>How to use:</b>
1. Choose a deck below
2. Study the word on the front
3. Flip to see translation and analysis
4. Mark cards as known or skip
5. Track your progress over time

🎯 <b>Choose a deck to start learning!</b>
        """
        
        await self._send_message(update, menu_text, reply_markup=reply_markup)

    async def _start_flashcard_session(self, update: Update, context: ContextTypes.DEFAULT_TYPE, deck_id: str):
        """Start a flashcard learning session"""
        user = update.effective_user
        
        session_id = self.flashcard_manager.start_flashcard_session(user.id, deck_id)
        
        if not session_id:
            await update.callback_query.edit_message_text("❌ Flashcard deck not found.")
            return
        
        await self._display_flashcard(update, session_id)

    async def _display_flashcard(self, update: Update, session_id: str):
        """Display the current flashcard"""
        session = self.flashcard_manager.active_flashcard_sessions.get(session_id)
        if not session:
            await update.callback_query.edit_message_text("❌ Flashcard session not found.")
            return
        
        card = self.flashcard_manager.get_current_card(session_id)
        if not card:
            await update.callback_query.edit_message_text("❌ No cards available in this deck.")
            return
        
        deck = FLASHCARD_DATABASE.get(session['deck_id'], {})
        
        if session['is_flipped']:
            # Show back of card
            card_text = f"""
🎴 <b>FLASHCARD LEARNING</b>

📚 <b>Deck:</b> {deck.get('title', 'Flashcards')}
📊 <b>Progress:</b> {session['current_card_index'] + 1}/{len(session['cards'])} cards
🎯 <b>Known:</b> {session['cards_known']} cards

<b>Translation:</b>
<code>{card['back']}</code>

💡 <b>Analysis:</b>
{card['hint']}

🌐 <b>Language:</b> {card['language'].title()}
📝 <b>Category:</b> {card['category']}
            """
            
            keyboard = [
                [InlineKeyboardButton("✅ I Know This", callback_data=f"flashcard_known:{session_id}"),
                 InlineKeyboardButton("🔄 Flip Back", callback_data=f"flashcard_flip:{session_id}")],
                [InlineKeyboardButton("⏭️ Skip Card", callback_data=f"flashcard_skip:{session_id}"),
                 InlineKeyboardButton("🏃‍♂️ End Session", callback_data=f"flashcard_end:{session_id}")]
            ]
            
            # Add audio button if available
            if card.get('audio'):
                audio_url = AUDIO_BASE_URL + card['audio']
                keyboard.insert(0, [InlineKeyboardButton("🎧 Hear Pronunciation", url=audio_url)])
        
        else:
            # Show front of card
            card_text = f"""
🎴 <b>FLASHCARD LEARNING</b>

📚 <b>Deck:</b> {deck.get('title', 'Flashcards')}
📊 <b>Progress:</b> {session['current_card_index'] + 1}/{len(session['cards'])} cards
🎯 <b>Known:</b> {session['cards_known']} cards

<b>Word to Analyze:</b>
<code>{card['front']}</code>

💡 <i>Click 'Flip Card' to see translation and analysis</i>
            """
            
            keyboard = [
                [InlineKeyboardButton("🔄 Flip Card", callback_data=f"flashcard_flip:{session_id}")],
                [InlineKeyboardButton("⏭️ Skip Card", callback_data=f"flashcard_skip:{session_id}"),
                 InlineKeyboardButton("🏃‍♂️ End Session", callback_data=f"flashcard_end:{session_id}")]
            ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.callback_query.edit_message_text(card_text, parse_mode='HTML', reply_markup=reply_markup)

    async def _handle_flashcard_flip(self, update: Update, context: ContextTypes.DEFAULT_TYPE, session_id: str):
        """Handle flashcard flip action"""
        self.flashcard_manager.flip_card(session_id)
        await self._display_flashcard(update, session_id)

    async def _handle_flashcard_known(self, update: Update, context: ContextTypes.DEFAULT_TYPE, session_id: str):
        """Handle marking card as known"""
        next_card = self.flashcard_manager.mark_card_known(session_id)
        
        if isinstance(next_card, dict):
            # Still more cards
            await update.callback_query.answer("Card marked as known! ✅")
            await self._display_flashcard(update, session_id)
        else:
            # Session complete
            results = next_card
            await self._display_flashcard_results(update, session_id, results)

    async def _handle_flashcard_skip(self, update: Update, context: ContextTypes.DEFAULT_TYPE, session_id: str):
        """Handle skipping card"""
        next_card = self.flashcard_manager.skip_card(session_id)
        
        if isinstance(next_card, dict):
            # Still more cards
            await update.callback_query.answer("Card skipped! ⏭️")
            await self._display_flashcard(update, session_id)
        else:
            # Session complete
            results = next_card
            await self._display_flashcard_results(update, session_id, results)

    async def _display_flashcard_results(self, update: Update, session_id: str, results: dict):
        """Display flashcard session results"""
        performance_emojis = {
            "MEMORY_GENIUS": "🧠⚡",
            "QUICK_LEARNER": "🚀💡",
            "SOLID_RECALL": "📚✅",
            "PROGRESSING": "📈🌟",
            "NEEDS_PRACTICE": "🔄💪"
        }
        
        results_text = f"""
🏆 <b>FLASHCARD SESSION COMPLETE!</b>

📚 <b>Deck:</b> {results['deck_title']}
📊 <b>Results:</b>
• Cards Completed: {results['total_cards']}
• Cards Known: {results['cards_known']}
• Accuracy: {results['known_percentage']:.1f}%
• Time Taken: {results['time_taken']:.1f}s
• Performance: {results['performance_rating']} {performance_emojis.get(results['performance_rating'], '🎯')}

💰 <b>Points Earned:</b> {results['total_points']}

🧠 <b>Cognitive Assessment:</b>
• Memory Retention: {'Exceptional' if results['known_percentage'] >= 95 else 'Excellent' if results['known_percentage'] >= 85 else 'Good' if results['known_percentage'] >= 75 else 'Developing'}
• Learning Speed: {'Lightning Fast' if results['time_taken'] < 60 else 'Fast' if results['time_taken'] < 120 else 'Steady'}

💡 <b>Recommendation:</b> {'Outstanding memory performance! Ready for advanced decks.' if results['known_percentage'] >= 95 else 'Excellent recall! Continue practicing for mastery.' if results['known_percentage'] >= 85 else 'Good progress! Regular practice will improve retention.'}
        """
        
        keyboard = [
            [InlineKeyboardButton("🔄 Practice Again", callback_data=f"flashcard_deck:{results['deck_id']}"),
             InlineKeyboardButton("📚 Try Another Deck", callback_data="flashcard_menu")],
            [InlineKeyboardButton("📊 View Progress", callback_data="cog_profile"),
             InlineKeyboardButton("🎯 Take Quiz", callback_data="adaptive_quiz")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.callback_query.edit_message_text(results_text, parse_mode='HTML', reply_markup=reply_markup)
        
        # Update user stats and check achievements
        user = update.effective_user
        self.db.update_user(
            user.id,
            flashcard_sessions=1,
            flashcard_points=results['total_points']
        )
        await self._check_achievements(update, user.id)

    async def _flashcard_stats(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Display user's flashcard statistics"""
        user = update.effective_user
        flashcard_progress = self.db.get_flashcard_progress(user.id)
        user_data = self.db.get_user(user.id)
        
        if not flashcard_progress:
            stats_text = """
📊 <b>Your Flashcard Statistics</b>

<i>You haven't started any flashcard sessions yet!</i>

💡 <b>Get started:</b>
• Choose a deck from the Flashcard Menu
• Learn vocabulary through spaced repetition
• Track your memory progress
• Earn points and achievements

🎯 <b>Benefits of Flashcard Learning:</b>
• Enhanced long-term memory
• Improved vocabulary recall
• Better pattern recognition
• Optimized learning efficiency
            """
        else:
            stats_text = """
📊 <b>Your Flashcard Statistics</b>

<b>Deck Progress:</b>
"""
            total_sessions = 0
            total_points = 0
            total_accuracy = 0
            deck_count = 0
            
            for deck_id, sessions, avg_accuracy, points, last_session in flashcard_progress:
                deck = FLASHCARD_DATABASE.get(deck_id, {})
                stats_text += f"• {deck.get('title', deck_id)}: {sessions} session(s), {avg_accuracy:.1f}% avg accuracy\n"
                total_sessions += sessions
                total_points += points
                total_accuracy += avg_accuracy
                deck_count += 1
            
            if deck_count > 0:
                overall_accuracy = total_accuracy / deck_count
                
                stats_text += f"""
📈 <b>Overall Statistics:</b>
• Total Sessions: {total_sessions}
• Average Accuracy: {overall_accuracy:.1f}%
• Total Flashcard Points: {total_points}
• Decks Mastered: {deck_count}

🎯 <b>Your Memory Level:</b> {'Memory Genius' if overall_accuracy >= 95 else 'Quick Learner' if overall_accuracy >= 85 else 'Solid Recall' if overall_accuracy >= 75 else 'Developing'}
                """
        
        if user_data:
            stats_text += f"\n🔥 <b>Current Streak:</b> {user_data['current_streak']} days"
            stats_text += f"\n🏆 <b>Total Points:</b> {user_data['total_points']}"
        
        keyboard = [
            [InlineKeyboardButton("🎴 Flashcard Menu", callback_data="flashcard_menu"),
             InlineKeyboardButton("🏆 Achievements", callback_data="achievements")],
            [InlineKeyboardButton("📊 Full Progress", callback_data="cog_profile"),
             InlineKeyboardButton("↩️ Main Menu", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await self._send_message(update, stats_text, parse_mode='HTML', reply_markup=reply_markup)

    async def _flashcard_achievements(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Show flashcard-related achievements"""
        user = update.effective_user
        user_data = self.db.get_user(user.id)
        
        achievements_text = """
🏆 <b>Flashcard Achievements</b>

<b>Available Achievements:</b>

📚 <b>Flashcard Beginner</b>
• Complete your first flashcard session
• Reward: 50 points

🎴 <b>Flashcard Master</b>
• Complete 20 flashcard sessions  
• Reward: 300 points

💭 <b>Memory Champion</b>
• Achieve 95% accuracy in flashcard sessions
• Reward: 400 points
        """
        
        if user_data:
            achievements_text += f"\n📊 <b>Your Progress:</b>"
            achievements_text += f"\n• Flashcard Sessions: {user_data['flashcard_sessions']}"
            achievements_text += f"\n• Flashcard Points: {user_data['total_flashcard_points']}"
        
        await self._send_message(update, achievements_text, parse_mode='HTML')

    # ========== ULTIMATE STORYTELLING METHODS ==========
    async def _storytelling_menu(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ULTIMATE storytelling menu"""
        keyboard = [
            [InlineKeyboardButton("🧠 Neural Awakening", callback_data="story_neural_awakening"),
             InlineKeyboardButton("🕵️ Language Detective", callback_data="story_language_detective")],
            [InlineKeyboardButton("🌍 Cultural Journey", callback_data="story_cultural_journey"),
             InlineKeyboardButton("⚡ Quick Stories", callback_data="story_quick")],
            [InlineKeyboardButton("📚 My Story Progress", callback_data="story_progress"),
             InlineKeyboardButton("🎧 Audio Library", callback_data="story_audio")],
            [InlineKeyboardButton("🏆 Story Achievements", callback_data="story_achievements"),
             InlineKeyboardButton("↩️ Back to Main", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        menu_text = """
🎭 <b>COGNITIVE STORYTELLING</b>

<i><b>Immerse yourself in multilingual stories that train your brain!</b></i>

📖 <b>Story Types:</b>
• <b>Neural Awakening</b> - Sci-fi linguistic adventure
• <b>Language Detective</b> - Mystery solving with morphology
• <b>Cultural Journey</b> - Stories from around the world
• <b>Quick Stories</b> - Bite-sized language learning

🧠 <b>Cognitive Benefits:</b>
• Enhanced pattern recognition through story structure
• Improved vocabulary retention in context
• Better comprehension across languages
• Increased cultural awareness
• Strengthened neural pathways for narrative processing

💡 <b>Choose a story below to begin your adventure!</b>
        """
        
        await self._send_message(update, menu_text, reply_markup=reply_markup)

    async def _start_story(self, update: Update, context: ContextTypes.DEFAULT_TYPE, story_id: str):
        """Start an ULTIMATE interactive story"""
        user = update.effective_user
        
        session_id = self.story_manager.start_story_session(user.id, story_id)
        chapter = self.story_manager.get_current_chapter(session_id)
        
        if not chapter:
            await update.callback_query.edit_message_text("❌ Story not found.")
            return
        
        await self._display_story_chapter(update, session_id, chapter)

    async def _display_story_chapter(self, update: Update, session_id: str, chapter: dict):
        """Display a story chapter with interactive elements"""
        session = self.story_manager.active_story_sessions.get(session_id)
        story = STORY_DATABASE.get(session['story_id'], {})
        
        # Create chapter display
        chapter_text = f"""
🎭 <b>{story.get('title', 'Interactive Story')}</b>

{chapter['text']}

🎯 <b>Chapter {session['current_chapter']} of {len(story['chapters'])}</b>
⏱️ <b>Estimated reading time:</b> {story.get('duration', '5-7 minutes')}
🌐 <b>Language:</b> {story.get('language', 'Multilingual').title()}
🎓 <b>Difficulty:</b> {story.get('difficulty', 'Intermediate').title()}
        """
        
        # Add audio button if available
        keyboard = []
        if chapter.get('audio_file'):
            audio_url = AUDIO_BASE_URL + chapter['audio_file']
            keyboard.append([InlineKeyboardButton("🎧 Listen to Chapter", url=audio_url)])
        
        # Add interactive choices
        if chapter.get('interactive_choices'):
            for i, choice in enumerate(chapter['interactive_choices']):
                keyboard.append([InlineKeyboardButton(
                    f"→ {choice['text']}", 
                    callback_data=f"story_choice:{session_id}:{i}"
                )])
        else:
            keyboard.append([InlineKeyboardButton(
                "➡️ Continue Story", 
                callback_data=f"story_continue:{session_id}"
            )])
        
        # Add vocabulary highlights if available
        if chapter.get('vocabulary_highlight'):
            chapter_text += "\n\n📚 <b>Vocabulary Focus:</b>\n"
            for vocab in chapter['vocabulary_highlight']:
                chapter_text += f"• <b>{vocab['word']}</b>: {vocab['definition']}\n"
        
        # Add story controls
        keyboard.append([
            InlineKeyboardButton("📖 Story Menu", callback_data="story_menu"),
            InlineKeyboardButton("📊 My Progress", callback_data="story_progress")
        ])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.callback_query.edit_message_text(chapter_text, parse_mode='HTML', reply_markup=reply_markup)

    async def _handle_story_choice(self, update: Update, context: ContextTypes.DEFAULT_TYPE, 
                                  session_id: str, choice_index: int):
        """Handle story choice and advance narrative"""
        await update.callback_query.answer()
        
        # Get choice narration
        session = self.story_manager.active_story_sessions.get(session_id)
        current_chapter = self.story_manager.get_current_chapter(session_id)
        
        if current_chapter and current_chapter.get('interactive_choices'):
            choice = current_chapter['interactive_choices'][choice_index]
            if choice.get('narration'):
                await update.callback_query.edit_message_text(
                    f"💭 <b>{choice['narration']}</b>",
                    parse_mode='HTML'
                )
                await asyncio.sleep(2)
        
        next_chapter = self.story_manager.advance_story(session_id, choice_index)
        
        if isinstance(next_chapter, dict):  # Next chapter
            await self._display_story_chapter(update, session_id, next_chapter)
        else:  # Story complete
            results = next_chapter  # Results from _complete_story_session
            await self._display_story_completion(update, session_id, results)

    async def _display_story_completion(self, update: Update, session_id: str, results: dict):
        """Display story completion results"""
        performance_emojis = {
            "STORY_MASTER": "🧠⚡",
            "LINGUISTIC_GENIUS": "🎯✨", 
            "ACTIVE_LEARNER": "🚀💡",
            "BEGINNER_STORYTELLER": "📚🌟"
        }
        
        completion_text = f"""
🏆 <b>STORY COMPLETE!</b>

🎭 <b>{results['story_title']}</b>
📖 <b>Performance Rating:</b> {results['performance_rating']} {performance_emojis.get(results['performance_rating'], '🎯')}

📊 <b>Results Summary:</b>
• Comprehension Score: {results['comprehension_score']:.1f}%
• Vocabulary Learned: {len(results['vocabulary_learned'])} words
• Cognitive Effects Activated: {len(results['cognitive_effects'])}

💰 <b>Points Breakdown:</b>
• Base Points: {results['breakdown']['base_points']}
• Comprehension Bonus: +{results['breakdown']['comprehension_bonus']}
• Vocabulary Bonus: +{results['breakdown']['vocabulary_bonus']}
• Cognitive Bonus: +{results['breakdown']['cognitive_bonus']}
• Completion Bonus: +{results['breakdown']['completion_bonus']}
• <b>Total: {results['total_points']} points!</b>

🧠 <b>Cognitive Effects Activated:</b>
"""
        
        for effect, count in results['cognitive_effects'].items():
            completion_text += f"• {effect.replace('_', ' ').title()}: {count} times\n"
        
        completion_text += """
💡 <b>Learning Insights:</b>
Your brain successfully processed narrative structures while acquiring new linguistic patterns. This strengthens both language acquisition and cognitive flexibility!

🎯 <b>Ready for your next story adventure?</b>
        """
        
        keyboard = [
            [InlineKeyboardButton("📖 Another Story", callback_data="story_menu"),
             InlineKeyboardButton("🔁 Play Again", callback_data=f"story_{results['story_id']}")],
            [InlineKeyboardButton("📊 View Progress", callback_data="cog_profile"),
             InlineKeyboardButton("🎯 Take Quiz", callback_data="adaptive_quiz")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.callback_query.edit_message_text(completion_text, parse_mode='HTML', reply_markup=reply_markup)
        
        # Check for achievements
        user = update.effective_user
        await self._check_achievements(update, user.id)

    async def _story_progress(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Display user's story progress"""
        user = update.effective_user
        story_progress = self.db.get_story_progress(user.id)
        
        if not story_progress:
            progress_text = """
📚 <b>Your Story Progress</b>

You haven't started any stories yet!

💡 <b>Get started:</b>
• Choose a story from the Story Menu
• Experience interactive language learning
• Earn points and achievements
• Track your cognitive growth

🎯 <b>Benefits of Story Learning:</b>
• Contextual vocabulary acquisition
• Improved comprehension skills
• Enhanced cultural awareness
• Strengthened narrative processing
            """
        else:
            progress_text = """
📚 <b>Your Story Progress</b>

<b>Stories Completed:</b>
"""
            total_points = 0
            total_comprehension = 0
            story_count = 0
            
            for story_id, completions, avg_comprehension, points, last_completed in story_progress:
                story = STORY_DATABASE.get(story_id, {})
                progress_text += f"• {story.get('title', story_id)}: {completions} time(s), {avg_comprehension:.1f}% avg\n"
                total_points += points
                total_comprehension += avg_comprehension
                story_count += 1
            
            if story_count > 0:
                avg_comprehension = total_comprehension / story_count
                
                progress_text += f"""
📊 <b>Overall Statistics:</b>
• Total Stories Completed: {story_count}
• Average Comprehension: {avg_comprehension:.1f}%
• Total Story Points: {total_points}
• Favorite Story: {max(story_progress, key=lambda x: x[1])[0]}

🎯 <b>Your Storytelling Level:</b> {'Expert Storyteller' if avg_comprehension >= 90 else 'Advanced Learner' if avg_comprehension >= 75 else 'Developing Reader' if avg_comprehension >= 60 else 'Beginner'}
                """
        
        keyboard = [
            [InlineKeyboardButton("📖 Story Menu", callback_data="story_menu"),
             InlineKeyboardButton("🏆 Achievements", callback_data="achievements")],
            [InlineKeyboardButton("📊 Full Progress", callback_data="cog_profile"),
             InlineKeyboardButton("↩️ Main Menu", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await self._send_message(update, progress_text, parse_mode='HTML', reply_markup=reply_markup)

    async def _show_audio_library(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Show available audio stories"""
        audio_text = """
🎧 <b>Audio Story Library</b>

<b>Available Audio Stories:</b>

🧠 <b>Neural Awakening</b>
• Chapter 1: The Discovery
• Chapter 2: The Connection Forms  
• Chapter 3: The Multilingual Network
• Chapter 4: The Cognitive Revolution
• Chapter 5: The Ultimate Realization

🕵️ <b>Language Detective</b> (Coming Soon)
• Chapter 1: The Cryptic Message

💡 <b>Audio Features:</b>
• Professional voice acting
• Clear pronunciation guides
• Immersive sound effects
• Language learning focused

🎯 <b>How to listen:</b>
Click the audio buttons in each chapter to hear professional narration!
        """
        await self._send_message(update, audio_text, parse_mode='HTML')

    async def _story_achievements(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Show story-related achievements"""
        user = update.effective_user
        user_data = self.db.get_user(user.id)
        
        achievements_text = """
🏆 <b>Storytelling Achievements</b>

<b>Available Achievements:</b>

📖 <b>Story Explorer</b>
• Complete your first interactive story
• Reward: 100 points

🎭 <b>Story Master</b> 
• Complete 10 interactive stories
• Reward: 500 points

🌍 <b>Multilingual Storyteller</b>
• Complete stories in 3 different languages  
• Reward: 300 points

💯 <b>Perfect Comprehension</b>
• Get 100% on all story comprehension questions
• Reward: 400 points

🧠 <b>Cognitive Storyteller</b>
• Activate all cognitive effects in a story
• Reward: 350 points
        """
        
        if user_data:
            achievements_text += f"\n📊 <b>Your Progress:</b>"
            achievements_text += f"\n• Stories Completed: {user_data['stories_completed']}"
            achievements_text += f"\n• Story Points: {user_data['total_story_points']}"
        
        await self._send_message(update, achievements_text, parse_mode='HTML')

    # ========== WORD REQUEST SYSTEM ==========
    async def _word_request(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ULTIMATE word request system for community-driven research"""
        if not context.args:
            await update.message.reply_text(
                "💡 <b>ULTIMATE Word Request System</b>\n\n"
                "Request words for cognitive analysis and research!\n\n"
                "Usage: <code>/request [word] [language] [context?]</code>\n\n"
                "<b>Examples:</b>\n"
                "• <code>/request artificial intelligence English</code>\n"
                "• <code>/request болашақ Kazakh future tense</code>\n"
                "• <code>/request sustainability English environmental</code>\n\n"
                "💡 Your requests help build our cognitive linguistics database!",
                parse_mode='HTML'
            )
            return
        
        user = update.effective_user
        args = context.args
        
        if len(args) < 2:
            await update.message.reply_text("❌ Please provide both word and language. Usage: /request [word] [language] [context?]")
            return
        
        word = args[0]
        language = args[1]
        context_text = " ".join(args[2:]) if len(args) > 2 else ""
        
        request_id = self.request_db.add_request(user.id, user.username or user.first_name, word, language, context_text)
        
        response = f"""
💡 <b>WORD REQUEST SUBMITTED!</b>

📝 <b>Word:</b> <code>{word}</code>
🌐 <b>Language:</b> {language.title()}
👤 <b>Researcher:</b> {user.first_name}
🆔 <b>Request ID:</b> #{request_id}

{"📋 <b>Context:</b> " + context_text if context_text else ""}

🎯 <b>Next Steps:</b>
1. Community members will vote on your request
2. Top-voted requests get priority analysis
3. You'll be notified when analysis is ready
4. Earn achievement points for contributions!

🗳️ <b>Vote on other requests with</b> <code>/requests</code>
        """
        
        self.db.update_user(user.id, word_requests=1)
        await update.message.reply_text(response, parse_mode='HTML')
        await self._check_achievements(update, user.id)

    async def _view_requests(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """View and vote on word requests"""
        user = update.effective_user
        requests = self.request_db.get_pending_requests(5)
        
        if not requests:
            await update.message.reply_text(
                "📋 <b>No pending word requests!</b>\n\n"
                "💡 Be the first to contribute with <code>/request [word] [language]</code>",
                parse_mode='HTML'
            )
            return
        
        response = "📋 <b>TOP WORD REQUESTS - VOTE NOW!</b>\n\n"
        
        keyboard = []
        for req in requests:
            req_id, user_id, username, word, language, context, status, timestamp, upvotes, downvotes = req
            net_votes = upvotes - downvotes
            
            response += f"""
🆔 <b>Request #{req_id}</b>
📝 <b>Word:</b> <code>{word}</code>
🌐 <b>Language:</b> {language.title()}
👤 <b>By:</b> {username}
👍 <b>Votes:</b> {net_votes} (+{upvotes}/-{downvotes})
{"📋 <b>Context:</b> " + context if context else ""}
"""
            keyboard.append([
                InlineKeyboardButton(f"👍 Vote for #{req_id}", callback_data=f"vote_up:{req_id}"),
                InlineKeyboardButton(f"👎 Vote #{req_id}", callback_data=f"vote_down:{req_id}")
            ])
        
        keyboard.append([InlineKeyboardButton("📝 Submit New Request", callback_data="new_request")])
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        response += "\n🗳️ <b>Vote on requests to help prioritize research!</b>"
        await update.message.reply_text(response, parse_mode='HTML', reply_markup=reply_markup)

    # ========== VOCABULARY MATCHING GAME METHODS ==========
    async def _vocab_matching_menu(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ULTIMATE vocabulary matching game menu"""
        keyboard = [
            [InlineKeyboardButton("🧩 Kazakh Basics", callback_data="vocab_game:kazakh_basics"),
             InlineKeyboardButton("🧩 English Advanced", callback_data="vocab_game:english_advanced")],
            [InlineKeyboardButton("🧩 Cross-Linguistic", callback_data="vocab_game:cross_linguistic"),
             InlineKeyboardButton("🎯 Quick Match", callback_data="vocab_game:quick")],
            [InlineKeyboardButton("📊 My Stats", callback_data="vocab_stats"),
             InlineKeyboardButton("🏆 Leaderboard", callback_data="leaderboard")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        menu_text = """
🧩 <b>ULTIMATE Vocabulary Matching Challenge</b>

<i><b>Train your brain with advanced morphological pattern recognition!</b></i>

🎮 <b>Game Types:</b>
• <b>Kazakh Basics</b> - Match Kazakh words with morpheme breakdowns
• <b>English Advanced</b> - Complex English word formation
• <b>Cross-Linguistic</b> - Match patterns across languages  
• <b>Quick Match</b> - Random challenge for speed training

🏆 <b>Scoring System:</b>
• Base Points: 50-100 per game
• Time Bonuses: Faster = more points
• Efficiency Bonus: Fewer moves = higher score
• Combo Multipliers: Consecutive matches

🧠 <b>Cognitive Benefits:</b>
• Enhanced pattern recognition
• Improved memory retention
• Faster lexical access
• Cross-linguistic awareness

💡 <b>Pro Tip:</b> Look for morphological patterns and root relationships!
        """
        
        await update.message.reply_text(menu_text, parse_mode='HTML', reply_markup=reply_markup)

    async def _start_vocab_matching_game(self, update: Update, context: ContextTypes.DEFAULT_TYPE, game_type: str):
        """Start a vocabulary matching game - FIXED VERSION"""
        user = update.effective_user
        
        session_id = self.quiz_manager.create_vocab_matching_session(user.id, game_type)
        
        if not session_id:
            await update.callback_query.edit_message_text("❌ Game type not found. Use /vocab to see available games.")
            return
        
        session = self.quiz_manager.vocab_matching_sessions.get(session_id)
        if not session:
            await update.callback_query.edit_message_text("❌ Failed to create game session.")
            return
        
        game_data = VOCAB_MATCHING_GAMES.get(game_type, {})
        
        response = f"""
🧩 <b>ULTIMATE VOCABULARY MATCHING</b>

🎯 <b>Challenge:</b> {game_data.get('title', 'Vocabulary Matching')}
📝 <b>Description:</b> {game_data.get('description', 'Match word pairs')}
⏱️ <b>Time Limit:</b> {game_data.get('time_limit', 120)} seconds
🎮 <b>Difficulty:</b> {game_data.get('difficulty', 'Intermediate')}
🏆 <b>Base Points:</b> {game_data.get('points', 50)}

<b>INSTRUCTIONS:</b>
1. Click two items to find matching pairs
2. Match all {len(game_data.get('pairs', {}))} pairs to win
3. Fewer moves = higher efficiency bonus
4. Faster completion = time bonus

🧠 <b>Neural Activation:</b>
• Pattern Recognition: 🟢 Active
• Memory Recall: 🟢 Active  
• Analytical Thinking: 🟢 Active
• Cognitive Flexibility: 🟢 Active

<code>Game starting... Prepare your cognitive centers!</code>
    """
        
        await update.callback_query.edit_message_text(response, parse_mode='HTML')
        await asyncio.sleep(2)
        await self._display_vocab_game_board(update, session_id)

    async def _display_vocab_game_board(self, update: Update, session_id: str):
        """Display the current vocabulary matching game board - FIXED VERSION"""
        session = self.quiz_manager.vocab_matching_sessions.get(session_id)
        if not session:
            await update.callback_query.edit_message_text("❌ Game session not found.")
            return
        
        items = session.get('items', [])
        matched_pairs = session.get('matched_pairs', [])
        selected_items = session.get('selected_items', [])
        
        # Create game board display
        board_text = "🧩 <b>VOCABULARY MATCHING GAME</b>\n\n"
        
        # Display progress
        progress = len(matched_pairs) // 2
        total_pairs = len(session.get('pairs', {}))
        board_text += f"📊 Progress: {progress}/{total_pairs} pairs matched\n"
        board_text += f"🎯 Moves: {session.get('moves', 0)} | Score: {session.get('score', 0)}\n\n"
        
        # Create game grid
        keyboard = []
        row = []
        for i, item in enumerate(items):
            if i in matched_pairs:
                # Show matched items
                display_text = item[:12] + "..." if len(item) > 12 else item
                row.append(InlineKeyboardButton(f"✅ {display_text}", callback_data=f"vocab_matched:{session_id}:{i}"))
            elif i in selected_items:
                # Show selected items
                display_text = item[:10] + "..." if len(item) > 10 else item
                row.append(InlineKeyboardButton(f"🔍 {display_text}", callback_data=f"vocab_selected:{session_id}:{i}"))
            else:
                # Show hidden items
                row.append(InlineKeyboardButton("❓", callback_data=f"vocab_select:{session_id}:{i}"))
            
            if len(row) == 2:  # 2 items per row for better mobile display
                keyboard.append(row)
                row = []
        
        if row:  # Add remaining items
            keyboard.append(row)
        
        # Add control buttons
        keyboard.append([
            InlineKeyboardButton("🔄 Restart", callback_data=f"vocab_restart:{session_id}"),
            InlineKeyboardButton("🏃‍♂️ Quit", callback_data=f"vocab_quit:{session_id}")
        ])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        time_elapsed = int((datetime.now() - session.get('start_time', datetime.now())).total_seconds())
        time_limit = VOCAB_MATCHING_GAMES.get(session.get('game_type', ''), {}).get('time_limit', 120)
        board_text += f"⏱️ Time: {time_elapsed}s | ⏳ Limit: {time_limit}s\n\n"
        board_text += "💡 <b>Find matching word-morpheme pairs!</b>"
        
        # Check if time limit exceeded
        if time_elapsed > time_limit:
            await self._end_vocab_game_timeout(update, context, session_id) # type: ignore
            return
        
        await update.callback_query.edit_message_text(board_text, parse_mode='HTML', reply_markup=reply_markup)

    async def _handle_vocab_selection(self, update: Update, context: ContextTypes.DEFAULT_TYPE, session_id: str, item_index: int):
        """Handle vocabulary game item selection - FIXED VERSION"""
        try:
            result = self.quiz_manager.process_vocab_selection(session_id, item_index)
            
            if not result:
                await update.callback_query.answer("Invalid selection")
                return
            
            await update.callback_query.answer()
            
            if 'is_match' in result:
                if result['is_match']:
                    feedback = "🎉 <b>MATCH FOUND!</b> +10 points"
                    if result.get('completed'):
                        feedback += "\n\n🏆 <b>GAME COMPLETE!</b> All pairs matched!"
                        await update.callback_query.edit_message_text(feedback, parse_mode='HTML')
                        await asyncio.sleep(1)
                        await self._end_vocab_game(update, context, session_id)
                        return
                else:
                    feedback = "❌ <b>No match</b> - Try again!"
                
                await update.callback_query.edit_message_text(feedback, parse_mode='HTML')
                await asyncio.sleep(1)
            
            await self._display_vocab_game_board(update, session_id)
            
        except Exception as e:
            print(f"❌ Error in vocab selection: {e}")
            import traceback
            traceback.print_exc()
            await update.callback_query.answer("Error processing selection")

    async def _end_vocab_game(self, update: Update, context: ContextTypes.DEFAULT_TYPE, session_id: str):
        """End vocabulary matching game and show results - FIXED VERSION"""
        try:
            results = self.quiz_manager.get_vocab_game_results(session_id)
            
            if not results:
                await update.callback_query.edit_message_text("❌ Game session not found or not completed.")
                return
            
            user = update.effective_user
            
            # Log results to database
            self.db.log_vocab_game_result(
                user.id,
                results['game_type'],
                results['total_points'],
                results['total_pairs'],
                results['moves'],
                results['efficiency'],
                results['time_taken'],
                results['performance_rating']
            )
            
            # Update user stats
            self.db.update_user(
                user.id,
                vocab_games=1,
                points=results['total_points']
            )
            
            performance_emojis = {
                "MEMORY_GENIUS": "🧠⚡",
                "PATTERN_MASTER": "🎯✨",
                "QUICK_LEARNER": "🚀💡",
                "STRATEGIC_THINKER": "📊🎮",
                "PRACTICE_NEEDED": "📚🌟"
            }
            
            results_text = f"""
🏆 <b>VOCABULARY MATCHING COMPLETE!</b>

🎯 <b>Game:</b> {VOCAB_MATCHING_GAMES[results['game_type']]['title']}
📊 <b>Results:</b>
• Pairs Matched: {results['total_pairs']}/{results['total_pairs']}
• Total Moves: {results['moves']}
• Efficiency: {results['efficiency']:.1f}%
• Time Taken: {results['time_taken']:.1f}s
• Performance: {results['performance_rating']} {performance_emojis.get(results['performance_rating'], '🎯')}

💰 <b>Points Earned:</b>
• Base Points: {results['base_points']}
• Game Score: {results['game_score']}
• <b>Total: {results['total_points']} points!</b>

🧠 <b>Cognitive Assessment:</b>
• Pattern Recognition: {'Exceptional' if results['efficiency'] >= 90 else 'Excellent' if results['efficiency'] >= 80 else 'Good' if results['efficiency'] >= 70 else 'Developing'}
• Memory Recall: {'Superior' if results['moves'] <= results['total_pairs'] + 2 else 'Strong' if results['moves'] <= results['total_pairs'] + 5 else 'Developing'}
• Processing Speed: {'Lightning Fast' if results['time_taken'] < 60 else 'Fast' if results['time_taken'] < 90 else 'Steady'}

💡 <b>Recommendation:</b> {'Outstanding performance! Ready for advanced challenges.' if results['efficiency'] >= 90 else 'Excellent work! Focus on strategic matching.' if results['efficiency'] >= 80 else 'Good effort! Practice will improve efficiency.'}
            """
            
            keyboard = [
                [InlineKeyboardButton("🔄 Play Again", callback_data=f"vocab_game:{results['game_type']}"),
                 InlineKeyboardButton("🎯 Try Another", callback_data="vocab_menu")],
                [InlineKeyboardButton("📊 View Progress", callback_data="cog_profile"),
                 InlineKeyboardButton("🏆 Leaderboard", callback_data="leaderboard")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await update.callback_query.edit_message_text(results_text, parse_mode='HTML', reply_markup=reply_markup)
            await self._check_achievements(update, user.id)
            
        except Exception as e:
            print(f"❌ Error ending vocab game: {e}")
            import traceback
            traceback.print_exc()
            await update.callback_query.edit_message_text("❌ Error processing game results.")

    async def _end_vocab_game_timeout(self, update: Update, context: ContextTypes.DEFAULT_TYPE, session_id: str):
        """Handle vocabulary game timeout"""
        results_text = """
⏰ <b>TIME'S UP!</b>

The vocabulary matching challenge has ended due to time limit.

💡 <b>Tips for next time:</b>
• Focus on pattern recognition
• Make strategic matches
• Practice with easier levels first

🎯 <b>Try again with better time management!</b>
        """
        
        keyboard = [
            [InlineKeyboardButton("🔄 Try Again", callback_data="vocab_menu"),
             InlineKeyboardButton("📚 Practice More", callback_data="adaptive_quiz")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.callback_query.edit_message_text(results_text, parse_mode='HTML', reply_markup=reply_markup)

    async def _restart_vocab_game(self, update: Update, context: ContextTypes.DEFAULT_TYPE, session_id: str):
        """Restart vocabulary matching game"""
        session = self.quiz_manager.vocab_matching_sessions.get(session_id)
        if session:
            game_type = session.get('game_type')
            # Remove old session
            if session_id in self.quiz_manager.vocab_matching_sessions:
                del self.quiz_manager.vocab_matching_sessions[session_id]
            # Start new game
            await self._start_vocab_matching_game(update, context, game_type)

    async def _quit_vocab_game(self, update: Update, context: ContextTypes.DEFAULT_TYPE, session_id: str):
        """Quit vocabulary matching game"""
        # Remove session
        if session_id in self.quiz_manager.vocab_matching_sessions:
            del self.quiz_manager.vocab_matching_sessions[session_id]
        
        quit_text = """
🏃‍♂️ <b>Game Quit</b>

You've exited the vocabulary matching challenge.

💡 <b>Remember:</b> Practice makes perfect!
🎯 <b>Come back anytime to continue your cognitive training.</b>
        """
        
        keyboard = [
            [InlineKeyboardButton("🧩 Vocabulary Games", callback_data="vocab_menu"),
             InlineKeyboardButton("🎯 Adaptive Quiz", callback_data="adaptive_quiz")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.callback_query.edit_message_text(quit_text, parse_mode='HTML', reply_markup=reply_markup)

    async def _vocab_matching_game(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Start a vocabulary matching game"""
        user = update.effective_user
        
        if context.args:
            game_type = context.args[0]
        else:
            game_type = random.choice(list(VOCAB_MATCHING_GAMES.keys()))
        
        await self._start_vocab_matching_game(update, context, game_type)

    # ========== ENHANCED BRAINSTORM SESSION ==========
    async def _brainstorm_session(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ULTIMATE brainstorming with interactive features"""
        user = update.effective_user
        
        # Create a unique brainstorm session
        session_id = f"brainstorm_{user.id}_{datetime.now().timestamp()}"
        
        # Select a brainstorming challenge
        challenges = [
            {
                "title": "Cross-Linguistic Morphology",
                "description": "Identify common morphological patterns across Turkic languages",
                "words": ["кітаптар", "kitaplar", "kitoblar", "кiтаптар"],
                "pattern": "plural formation with -lar/-ler/-тар"
            },
            {
                "title": "Word Formation Analysis", 
                "description": "Analyze complex word formation processes in English",
                "words": ["internationalization", "unbelievableness", "misunderstanding"],
                "pattern": "multiple affixation and derivation"
            },
            {
                "title": "Cognitive Linguistics",
                "description": "Explore the relationship between language and cognition",
                "words": ["переосмысление", "rethinking", "қайта ойлау"],
                "pattern": "metacognitive processes across languages"
            }
        ]
        
        challenge = random.choice(challenges)
        
        self.user_sessions[session_id] = {
            'type': 'brainstorm',
            'challenge': challenge,
            'start_time': datetime.now(),
            'ideas': [],
            'patterns_found': 0
        }
        
        brainstorm_text = f"""
💡 <b>COGNITIVE BRAINSTORMING SESSION</b>

🎯 <b>Challenge:</b> {challenge['title']}
📝 <b>Description:</b> {challenge['description']}

🔍 <b>Words to Analyze:</b>
{chr(10).join(f'• <code>{word}</code>' for word in challenge['words'])}

🧠 <b>Brainstorming Tasks:</b>
1. Identify common patterns
2. Analyze morphological structures  
3. Compare cross-linguistic features
4. Propose cognitive explanations

💭 <b>Thinking Prompts:</b>
• What morphological patterns do you see?
• How do these words relate cognitively?
• What brain areas might be involved?
• How would you teach these patterns?

⏱️ <b>Session Duration:</b> 5 minutes
🎯 <b>Goal:</b> Generate at least 3 insights

💡 <b>Submit your insights via message!</b>
        """
        
        keyboard = [
            [InlineKeyboardButton("🎯 Start Analysis", callback_data=f"brainstorm_start:{session_id}"),
             InlineKeyboardButton("💡 Show Hints", callback_data=f"brainstorm_hint:{session_id}")],
            [InlineKeyboardButton("📋 View Words", callback_data=f"brainstorm_words:{session_id}"),
             InlineKeyboardButton("🏁 End Session", callback_data=f"brainstorm_end:{session_id}")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(brainstorm_text, parse_mode='HTML', reply_markup=reply_markup)

    # ========== ULTIMATE PRONUNCIATION METHOD ==========
    async def _pronounce_word(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ULTIMATE word pronunciation with GitHub audio hosting"""
        try:
            if not context.args:
                await update.message.reply_text(
                    "🎧 <b>ULTIMATE Pronunciation System</b>\n\n"
                    "Usage: <code>/pronounce [word]</code>\n\n"
                    "<b>Available Words:</b>\n"
                    "• Kazakh: кітаптарымыздан, жүгірушілерге, балаларға, үйлерімізде\n"
                    "• English: unbelievableness, internationalization\n"
                    "• Russian: переосмысление, взаимопонимание\n"
                    "• Turkish: öğrencilerimizin, anlayışınız\n\n"
                    "💡 <b>Example:</b> <code>/pronounce кітаптарымыздан</code>",
                    parse_mode='HTML'
                )
                return

            word = " ".join(context.args).strip().lower()
            user = update.effective_user

            await self.telegram_features.send_typing_indicator(update, 2)

            if word in WORD_DATABASE:
                data = WORD_DATABASE[word]
                audio_file = data.get('audio')
                phonetic = data.get('phonetic', 'Not available')
                neural_pathways = data.get('neural_pathways', 10)
                
                # Build the analysis response
                response = f"""
🔊 <b>ULTIMATE PRONUNCIATION ANALYSIS</b>

📝 <b>Word:</b> <code>{word}</code>
🌐 <b>Language:</b> {data['language'].title()}
🎯 <b>Phonetic:</b> {phonetic}
🧠 <b>Neural Pathways:</b> {neural_pathways} activated

💡 <b>Morphological Breakdown:</b>
{" → ".join(data["analysis"])}
"""

                if audio_file:
                    audio_url = AUDIO_BASE_URL + audio_file
                    
                    # Send the audio file directly
                    await update.message.reply_audio(
                        audio=audio_url,
                        title=f"Pronunciation: {word}",
                        performer="Metalens Cognitive Bot",
                        caption=f"🔊 {word} - {phonetic}"
                    )
                    
                    # Send the detailed analysis
                    response += f"""
                    
🎧 <b>Audio Pronunciation Sent!</b>

🎯 <b>Pronunciation Practice:</b>
1. 🎧 Listen carefully to the audio
2. 🔁 Repeat the word 3-5 times  
3. 🎯 Focus on phonetic patterns
4. 💭 Try using it in context

🧠 <b>Cognitive Benefits:</b>
• Auditory cortex activation
• Phonetic memory formation
• Language production skills
• Neural pathway strengthening

💡 <b>Pro Tip:</b> Combine with <code>/analyze {word}</code> for deeper understanding!
"""
                    await update.message.reply_text(response, parse_mode='HTML')
                    
                else:
                    response += "\n\n❌ <b>Audio not available for this word</b>"
                    response += "\n💡 <b>Suggest audio research with</b> <code>/request</code>"
                    await update.message.reply_text(response, parse_mode='HTML')

                # Update user stats
                self.db.update_user(user.id, words=1, language=data["language"])
                self.analytics.track_cognitive_metric(user.id, 'audio_processing', 0.92)

            else:
                # Word not found - show suggestions
                suggestions = []
                for known_word in WORD_DATABASE.keys():
                    if word in known_word.lower() or known_word.lower().startswith(word[:3]):
                        suggestions.append(known_word)
                        if len(suggestions) >= 3:
                            break
                
                response = f"""
❌ <b>Pronunciation Analysis</b>

Word <code>{word}</code> not found in cognitive database.
"""

                if suggestions:
                    response += "\n💡 <b>Similar Words with Audio:</b>\n"
                    for suggested_word in suggestions[:3]:
                        response += f"• <code>{suggested_word}</code>\n"
                    response += f"\n🔊 Try: <code>/pronounce {suggestions[0]}</code>"
                else:
                    response += """
💡 <b>Available Pronunciation Words:</b>
• Kazakh: <code>кітаптарымыздан</code>, <code>балаларға</code>
• English: <code>internationalization</code>  
• Russian: <code>взаимопонимание</code>
• Turkish: <code>öğrencilerimizin</code>

💡 <b>Request new words with:</b> <code>/request [word] [language]</code>
"""

                await update.message.reply_text(response, parse_mode='HTML')

            await self.telegram_features.send_cognitive_insight(update, "audio_processing")

        except Exception as e:
            logging.error(f"ULTIMATE Pronunciation error: {e}")
            await update.message.reply_text(
                "❌ <b>Audio System Temporarily Unavailable</b>\n\n"
                "The pronunciation service is experiencing high demand.\n"
                "🔄 Please try again in a few moments.\n\n"
                "💡 You can still analyze words with <code>/analyze</code>",
                parse_mode='HTML'
            )

    # ========== ULTIMATE QUIZ METHODS ==========
    async def _audio_quiz_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ULTIMATE Audio quiz command with enhanced experience"""
        user = update.effective_user
        
        await self.telegram_features.send_typing_indicator(update, 2)

        audio_questions = QUIZ_DATABASE.get("audio_challenge", [])
        if not audio_questions:
            await update.message.reply_text(
                "🎧 <b>ULTIMATE Audio Quiz System</b>\n\n"
                "No audio challenges available yet.\n\n"
                "💡 <b>Alternatives:</b>\n"
                "• Use <code>/quiz</code> for text-based challenges\n"
                "• Try <code>/pronounce</code> to hear word pronunciations\n"
                "• Use <code>/analyze</code> for word breakdowns",
                parse_mode='HTML'
            )
            return
        
        quiz_questions = random.sample(audio_questions, min(3, len(audio_questions)))
        session_id = self.quiz_manager.create_quiz_session(user.id, "audio_challenge", quiz_questions)
        
        await update.message.reply_text(
            "🎧 <b>ULTIMATE Audio Cognitive Challenge Starting!</b>\n\n"
            "<i>Prepare your auditory processing centers!</i>\n\n"
            "🧠 <b>Neural Activation:</b>\n"
            "• Auditory Cortex: 🟢 Active\n"
            "• Phonetic Processing: 🟢 Active\n"
            "• Pattern Recognition: 🟢 Active\n"
            "• Memory Formation: 🟢 Active\n\n"
            "💡 <b>Pro Tip:</b> Listen carefully to phonetic patterns and morpheme boundaries!",
            parse_mode='HTML'
        )
        
        await self._send_audio_quiz_question(update, context, session_id)

    async def _adaptive_quiz(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ULTIMATE adaptive quiz menu - FIXED 8 TYPES"""
        user = update.effective_user
        user_data = self.db.get_user(user.id)
        cognitive_level = self._calculate_cognitive_level(user_data)
        
        # Adaptive recommendation
        if cognitive_level <= 3:
            recommended_quiz = "language_families"
        elif cognitive_level <= 6:
            recommended_quiz = "morphology" 
        else:
            recommended_quiz = "cognitive_linguistics"
        
        keyboard = [
            [InlineKeyboardButton("🧠 Cognitive Linguistics", callback_data="quiz_cognitive_linguistics"),
             InlineKeyboardButton("🌍 Language Families", callback_data="quiz_language_families")],
            [InlineKeyboardButton("🔍 Morphology Master", callback_data="quiz_morphology"),
             InlineKeyboardButton("🔄 Translation Challenge", callback_data="quiz_translations")],
            [InlineKeyboardButton("🎧 Audio Challenge", callback_data="quiz_audio_challenge"),
             InlineKeyboardButton("🎯 Adaptive Challenge", callback_data="quiz_adaptive_challenge")],
            [InlineKeyboardButton("⚡ Quick Challenge", callback_data="quiz_quick_challenge"),
             InlineKeyboardButton("🔥 Combo Challenge", callback_data="quiz_combo_challenge")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        quiz_text = f"""
📚 <b>ADAPTIVE COGNITIVE QUIZ SYSTEM</b>

<b>Your Cognitive Level:</b> {cognitive_level}/10
🎯 <b>Recommended:</b> {recommended_quiz.replace('_', ' ').title()}
🏆 <b>Total Points:</b> {user_data['total_points'] if user_data else 0}

🎮 <b>Quiz Types:</b>
• 🧠 <b>Cognitive Linguistics</b> - Brain & language science
• 🌍 <b>Language Families</b> - Historical linguistics  
• 🔍 <b>Morphology Master</b> - Word structure analysis
• 🔄 <b>Translation Challenge</b> - Cross-linguistic skills
• 🎧 <b>Audio Challenge</b> - Phonetic recognition training
• 🎯 <b>Adaptive Challenge</b> - AI-tailored to your level
• ⚡ <b>Quick Challenge</b> - 60-second cognitive sprint
• 🔥 <b>Combo Challenge</b> - Consecutive correct answers

💡 <b>Features:</b>
• Time bonuses for quick answers
• Combo multipliers up to 2.0x
• Neural impact tracking
• Performance analytics

🎯 <b>Click a button below to start!</b>
        """
        
        await self._send_message(update, quiz_text, reply_markup=reply_markup)

    async def _send_message(self, update: Update, text: str, **kwargs):
        """ULTIMATE message sending with error handling"""
        try:
            # Always use HTML parse mode for beautiful formatting
            if 'parse_mode' not in kwargs:
                kwargs['parse_mode'] = 'HTML'
                
            if hasattr(update, 'message') and update.message:
                await update.message.reply_text(text, **kwargs)
            elif hasattr(update, 'callback_query') and update.callback_query:
                await update.callback_query.edit_message_text(text, **kwargs)
            else:
                await update.message.reply_text(text, **kwargs)
        except Exception as e:
            logging.error(f"Error sending message: {e}")
            # Fallback: try to send a new message without formatting
            kwargs.pop('parse_mode', None)
            if hasattr(update, 'message') and update.message:
                await update.message.reply_text(text[:4000], **kwargs)

    async def _start_quiz_session(self, update: Update, context: ContextTypes.DEFAULT_TYPE, quiz_type: str):
        """ULTIMATE quiz session starter"""
        user = update.effective_user
        
        questions = QUIZ_DATABASE.get(quiz_type, [])
        if not questions:
            await self._send_message(update, f"❌ No questions available for <b>{quiz_type.replace('_', ' ').title()}</b> quiz type.")
            return None
        
        quiz_questions = random.sample(questions, min(3, len(questions)))
        session_id = self.quiz_manager.create_quiz_session(user.id, quiz_type, quiz_questions)
        
        if quiz_type == "audio_challenge":
            await self._send_audio_quiz_question(update, context, session_id)
        else:
            await self._send_quiz_question(update, context, session_id)
        return session_id

    async def _send_audio_quiz_question(self, update: Update, context: ContextTypes.DEFAULT_TYPE, session_id: str):
        """ULTIMATE audio quiz question sender"""
        question = self.quiz_manager.get_current_question(session_id)
        if not question:
            await self._end_quiz_session(update, context, session_id)
            return
        
        keyboard = []
        for i, option in enumerate(question['options']):
            keyboard.append([InlineKeyboardButton(option, callback_data=f"quiz_answer:{session_id}:{i}")])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        question_text = f"""
🎧 <b>ULTIMATE AUDIO CHALLENGE</b>

{question['question']}

<i>Listen carefully to the pronunciation!</i>

<b>Difficulty:</b> {question.get('difficulty', 'beginner').title()}
<b>Points:</b> {question.get('points', 15)}
<b>Cognitive Skill:</b> {question.get('cognitive_skill', 'phonetic_recognition').replace('_', ' ').title()}
<b>Neural Impact:</b> {question.get('neural_impact', 'Auditory processing')}
        """
        
        if question.get('audio_hint'):
            audio_url = AUDIO_BASE_URL + question['audio_hint']
            question_text += f"\n\n🔊 <b>Audio:</b> <a href=\"{audio_url}\">Click to listen</a>"
        
        await self._send_message(update, question_text, reply_markup=reply_markup)

    async def _send_quiz_question(self, update: Update, context: ContextTypes.DEFAULT_TYPE, session_id: str):
        """ULTIMATE quiz question sender"""
        question = self.quiz_manager.get_current_question(session_id)
        if not question:
            await self._end_quiz_session(update, context, session_id)
            return
        
        keyboard = []
        for i, option in enumerate(question['options']):
            keyboard.append([InlineKeyboardButton(option, callback_data=f"quiz_answer:{session_id}:{i}")])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        question_text = f"""
🎯 <b>ULTIMATE Quiz Question</b>

{question['question']}

<b>Difficulty:</b> {question.get('difficulty', 'beginner').title()}
<b>Points:</b> {question.get('points', 15)}
<b>Cognitive Skill:</b> {question.get('cognitive_skill', 'general').replace('_', ' ').title()}
<b>Neural Impact:</b> {question.get('neural_impact', 'Cognitive processing')}
        """
        
        if question.get('audio_hint'):
            audio_url = AUDIO_BASE_URL + question['audio_hint']
            question_text += f"\n\n🔊 <b>Audio Hint:</b> <a href=\"{audio_url}\">Click to listen</a>"
        
        await self._send_message(update, question_text, reply_markup=reply_markup)

    async def _handle_quiz_answer(self, update: Update, context: ContextTypes.DEFAULT_TYPE, session_id: str, answer_index: int):
        """ULTIMATE quiz answer handler"""
        result = self.quiz_manager.submit_answer(session_id, answer_index)
        
        if not result:
            await update.callback_query.answer("Error processing answer")
            return
        
        user = update.effective_user
        
        if result['is_correct']:
            feedback = f"✅ <b>CORRECT!</b> +{result['points_earned']} points"
            if result['time_bonus'] > 0:
                feedback += f" (+{result['time_bonus']:.1f} speed bonus)"
            if result['combo_multiplier'] > 1.0:
                feedback += f" 🔥 {result['combo_multiplier']}x COMBO!"
            feedback += f"\n\n🎯 <b>Perfect Streak:</b> {result['perfect_streak']} in a row!"
            feedback += f"\n🧠 <b>Neural Impact:</b> {result['neural_impact']}"
        else:
            current_session = self.quiz_manager.active_sessions[session_id]
            current_idx = current_session['current_question'] - 1
            question = current_session['questions'][current_idx]
            correct_option = result['correct_answer']
            correct_text = question['options'][correct_option]
            feedback = f"❌ <b>INCORRECT</b>\n🎯 <b>Correct answer:</b> {correct_text}\n"
            feedback += f"💡 Learning opportunity detected!\n"
        
        feedback += f"\n💡 <b>Explanation:</b> {result['explanation']}"
        
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(feedback, parse_mode='HTML')
        
        quiz_type = self.quiz_manager.active_sessions[session_id]['quiz_type']
        is_audio_quiz = quiz_type == "audio_challenge"
        is_perfect = result.get('perfect_streak', 0) >= 3
        
        self.db.update_user(
            user.id, 
            quizzes=1, 
            audio_quizzes=1 if is_audio_quiz else 0,
            points=result['points_earned'],
            max_combo=result['combo_multiplier'],
            answer_time=result.get('time_taken', 0),
            perfect_quiz=is_perfect
        )
        
        if result['is_complete']:
            await asyncio.sleep(3)
            await self._end_quiz_session(update, context, session_id)
        else:
            await asyncio.sleep(2)
            session = self.quiz_manager.active_sessions[session_id]
            if session['quiz_type'] == "audio_challenge":
                await self._send_audio_quiz_question(update, context, session_id)
            else:
                await self._send_quiz_question(update, context, session_id)

    async def _end_quiz_session(self, update: Update, context: ContextTypes.DEFAULT_TYPE, session_id: str):
        """ULTIMATE quiz session ender"""
        results = self.quiz_manager.get_session_results(session_id)
        
        if not results:
            await self._send_message(update, "❌ Quiz session ended unexpectedly.")
            return
        
        user = update.effective_user
        
        self.db.log_quiz_result(
            user.id, 
            results['quiz_type'], 
            results['total_points'],
            results['total_questions'],
            results['accuracy'],
            results['duration'],
            results['performance_tier'],
            results['cognitive_rating'],
            results['max_combo']
        )
        
        performance_emojis = {
            "NEURAL_MASTER": "🧠⚡",
            "COGNITIVE_CHAMPION": "🏆🎯", 
            "PATTERN_EXPERT": "🔍✨",
            "ANALYTICAL_THINKER": "📊💡",
            "PRACTICE_NEEDED": "📚🌟"
        }
        
        results_text = f"""
🏆 <b>ULTIMATE QUIZ COMPLETE!</b>

<i><b>Results for {results['quiz_type'].replace('_', ' ').title()} Quiz:</b></i>

📊 <b>Performance Summary:</b>
• Correct Answers: {results['correct_answers']}/{results['total_questions']}
• Accuracy: {results['accuracy']:.1f}%
• Total Points: {results['total_points']}
• Average Time: {results['avg_time_per_question']:.1f}s per question
• Max Combo: {results['max_combo']}x
• Performance Tier: {results['performance_tier']} {performance_emojis.get(results['performance_tier'], '🎯')}
• Cognitive Rating: {results['cognitive_rating']}

🎯 <b>Cognitive Assessment:</b>
• Pattern Recognition: {'Exceptional' if results['accuracy'] >= 90 else 'Excellent' if results['accuracy'] >= 80 else 'Good' if results['accuracy'] >= 70 else 'Developing'}
• Processing Speed: {'Lightning Fast' if results['avg_time_per_question'] < 5 else 'Fast' if results['avg_time_per_question'] < 10 else 'Steady'}
• Analytical Thinking: {'Superior' if results['max_combo'] >= 1.8 else 'Strong' if results['max_combo'] >= 1.4 else 'Developing'}

🧠 <b>Neural Impacts Activated:</b>
{chr(10).join(f'• {impact}' for impact in set(results['neural_impacts']) if impact)}

💡 <b>Recommendation:</b> {'Outstanding performance! Ready for advanced challenges.' if results['accuracy'] >= 90 else 'Excellent work! Continue practicing for mastery.' if results['accuracy'] >= 80 else 'Good effort! Focus on pattern recognition.'}
        """
        
        keyboard = [
            [InlineKeyboardButton("🔄 Take Another Quiz", callback_data="adaptive_quiz"),
             InlineKeyboardButton("🎧 Audio Quiz", callback_data="audio_quiz")],
            [InlineKeyboardButton("📊 View Progress", callback_data="cog_profile"),
             InlineKeyboardButton("🔍 Analyze Words", callback_data="cog_analysis")],
            [InlineKeyboardButton("🏆 Leaderboard", callback_data="leaderboard"),
             InlineKeyboardButton("🎯 Daily Challenge", callback_data="daily_challenge")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await self._send_message(update, results_text, reply_markup=reply_markup)
        
        self.quiz_manager.cleanup_session(session_id)
        await self._check_achievements(update, user.id)

    async def _quick_quiz(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ULTIMATE quick random quiz"""
        quiz_types = [qt for qt in QUIZ_DATABASE.keys() if qt != "audio_challenge"]
        if not quiz_types:
            await update.message.reply_text("❌ No quiz categories available.")
            return
        
        quiz_type = random.choice(quiz_types)
        await self._start_quiz_session(update, context, quiz_type)

    # ========== ULTIMATE BUTTON HANDLER ==========
    async def _advanced_button_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ULTIMATE interactive button handler - ENHANCED WITH STORYTELLING AND FLASHCARDS"""
        query = update.callback_query
        await query.answer()
        
        data = query.data
        
        print(f"🔧 ULTIMATE DEBUG: Button pressed: {data}")

        try:
            if data == "cog_analysis":
                await query.edit_message_text("🔍 <b>Cognitive Analysis Ready!</b>\n\nType <code>/analyze [word]</code> to begin neural pathway analysis.", parse_mode='HTML')
            
            elif data == "adaptive_quiz":
                await self._adaptive_quiz(update, context)
            
            elif data == "audio_quiz":
                await self._start_quiz_session(update, context, "audio_challenge")
            
            elif data == "cog_profile":
                await self._cognitive_profile(update, context)
            
            elif data == "daily_challenge":
                await self._daily_cognitive_challenge(update, context)
            
            elif data == "leaderboard":
                await self._interactive_leaderboard(update, context)
            
            elif data == "vocab_menu":
                await self._vocab_matching_menu(update, context)
            
            elif data == "new_request":
                await query.edit_message_text("💡 <b>Submit Word Request</b>\n\nUse: <code>/request [word] [language] [context?]</code>\n\nExample: <code>/request artificial intelligence English</code>", parse_mode='HTML')
            
            # ========== NEW FLASHCARD HANDLERS ==========
            elif data == "flashcard_menu":
                await self._flashcard_menu(update, context)
            
            elif data == "flashcard_stats":
                await self._flashcard_stats(update, context)
            
            elif data == "flashcard_achievements":
                await self._flashcard_achievements(update, context)
            
            elif data.startswith("flashcard_deck:"):
                deck_id = data.replace("flashcard_deck:", "")
                await self._start_flashcard_session(update, context, deck_id)
            
            elif data.startswith("flashcard_flip:"):
                session_id = data.replace("flashcard_flip:", "")
                await self._handle_flashcard_flip(update, context, session_id)
            
            elif data.startswith("flashcard_known:"):
                session_id = data.replace("flashcard_known:", "")
                await self._handle_flashcard_known(update, context, session_id)
            
            elif data.startswith("flashcard_skip:"):
                session_id = data.replace("flashcard_skip:", "")
                await self._handle_flashcard_skip(update, context, session_id)
            
            elif data.startswith("flashcard_end:"):
                session_id = data.replace("flashcard_end:", "")
                # Clean up session
                if session_id in self.flashcard_manager.active_flashcard_sessions:
                    del self.flashcard_manager.active_flashcard_sessions[session_id]
                await self._flashcard_menu(update, context)
            # ========== END FLASHCARD HANDLERS ==========
            
            # ========== NEW STORYTELLING HANDLERS ==========
            elif data == "story_menu":
                await self._storytelling_menu(update, context)
            
            elif data == "story_progress":
                await self._story_progress(update, context)
            
            elif data == "story_audio":
                await self._show_audio_library(update, context)
            
            elif data == "story_achievements":
                await self._story_achievements(update, context)
            
            elif data.startswith("story_"):
                story_id = data.replace("story_", "")
                # Start a specific story - check if it exists
                if story_id in STORY_DATABASE:
                    await self._start_story(update, context, story_id)
                else:
                    await update.callback_query.edit_message_text(
                        f"❌ Story '{story_id}' not found. Available stories: {', '.join(STORY_DATABASE.keys())}"
                    )
            
            elif data.startswith("story_choice:"):
                parts = data.split(":")
                if len(parts) == 3:
                    session_id = parts[1]
                    choice_index = int(parts[2])
                    await self._handle_story_choice(update, context, session_id, choice_index)
            
            elif data.startswith("story_continue:"):
                parts = data.split(":")
                if len(parts) == 2:
                    session_id = parts[1]
                    await self._handle_story_choice(update, context, session_id, 0)
            # ========== END STORYTELLING HANDLERS ==========
            
            elif data.startswith("quiz_"):
                quiz_type = data.replace("quiz_", "")
                print(f"🔧 ULTIMATE DEBUG: Starting quiz type: {quiz_type}")
                
                quiz_mapping = {
                    "cognitive_linguistics": "cognitive_linguistics",
                    "language_families": "language_families", 
                    "morphology": "morphology",
                    "translations": "translations",
                    "audio_challenge": "audio_challenge",
                    "adaptive_challenge": "adaptive_challenge",
                    "combo_challenge": "combo_challenge", 
                    "quick_challenge": "quick_challenge"
                }
                
                actual_quiz_type = quiz_mapping.get(quiz_type, quiz_type)
                print(f"🔧 ULTIMATE DEBUG: Mapped to database: {actual_quiz_type}")
                await self._start_quiz_session(update, context, actual_quiz_type)
            
            elif data.startswith("quiz_answer:"):
                parts = data.split(":")
                if len(parts) == 3:
                    session_id = parts[1]
                    answer_index = int(parts[2])
                    print(f"🔧 ULTIMATE DEBUG: Answer submitted - Session: {session_id}, Answer: {answer_index}")
                    await self._handle_quiz_answer(update, context, session_id, answer_index)
                else:
                    await query.edit_message_text("❌ Invalid answer format.")
            
            elif data.startswith("vocab_game:"):
                game_type = data.replace("vocab_game:", "")
                print(f"🔧 ULTIMATE DEBUG: Starting vocab game: {game_type}")
                await self._start_vocab_matching_game(update, context, game_type)
            
            elif data.startswith("vocab_select:"):
                parts = data.split(":")
                if len(parts) == 3:
                    session_id = parts[1]
                    item_index = int(parts[2])
                    print(f"🔧 ULTIMATE DEBUG: Vocab selection - Session: {session_id}, Item: {item_index}")
                    await self._handle_vocab_selection(update, context, session_id, item_index)
            
            elif data.startswith("vocab_restart:"):
                parts = data.split(":")
                if len(parts) == 2:
                    session_id = parts[1]
                    await self._restart_vocab_game(update, context, session_id)
            
            elif data.startswith("vocab_quit:"):
                parts = data.split(":")
                if len(parts) == 2:
                    session_id = parts[1]
                    await self._quit_vocab_game(update, context, session_id)
            
            elif data.startswith("vote_up:") or data.startswith("vote_down:"):
                parts = data.split(":")
                if len(parts) == 2:
                    vote_type = "upvote" if data.startswith("vote_up") else "downvote"
                    request_id = int(parts[1])
                    user = update.effective_user
                    
                    success = self.request_db.vote_request(user.id, request_id, vote_type)
                    if success:
                        self.db.update_user(user.id, requests_voted=1)
                        await query.answer(f"Vote submitted! ({vote_type})")
                        await self._view_requests(update, context)
                    else:
                        await query.answer("You already voted this way!")
            
            elif data == "quick_quiz":
                await self._quick_quiz(update, context)
            
            elif data == "community":
                await self._language_community(update, context)
            
            elif data == "research_mode":
                await self._live_research_session(update, context)
            
            elif data == "achievements":
                await self._cognitive_badges(update, context)
            
            elif data == "main_menu":
                await self._revolutionary_start(update, context)
            
            else:
                await query.edit_message_text(f"❌ Unknown button action: {data}\n\n💡 Use <code>/help</code> for available commands.", parse_mode='HTML')

        except Exception as e:
            print(f"❌ ULTIMATE ERROR HANDLER: {e}")
            import traceback
            traceback.print_exc()
            await query.edit_message_text(
                "⚡ <b>Cognitive System Recovery</b>\n\n"
                "Temporary neural pathway disruption detected.\n"
                "System has automatically recovered.\n\n"
                "💡 Try again or use <code>/start</code> to refresh your session.",
                parse_mode='HTML'
            )

    # ========== ULTIMATE CORE METHODS ==========
    async def _revolutionary_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ULTIMATE revolutionary welcome with storytelling and flashcards"""
        user = update.effective_user
        self.db.update_user(user.id, user.username, user.first_name)
        
        await self.telegram_features.send_typing_indicator(update, 2)
        
        keyboard = [
            [InlineKeyboardButton("🔍 Cognitive Analysis", callback_data="cog_analysis"),
             InlineKeyboardButton("🎯 Adaptive Quiz", callback_data="adaptive_quiz")],
            [InlineKeyboardButton("🎭 Storytelling", callback_data="story_menu"),
             InlineKeyboardButton("🎴 Flashcards", callback_data="flashcard_menu")],
            [InlineKeyboardButton("🎧 Audio Quiz", callback_data="audio_quiz"),
             InlineKeyboardButton("🧩 Vocabulary Match", callback_data="vocab_menu")],
            [InlineKeyboardButton("💡 Word Requests", callback_data="new_request"),
             InlineKeyboardButton("📊 Cognitive Profile", callback_data="cog_profile")],
            [InlineKeyboardButton("⚡ Daily Challenge", callback_data="daily_challenge"),
             InlineKeyboardButton("🔬 Research Mode", callback_data="research_mode")],
            [InlineKeyboardButton("🏆 Achievements", callback_data="achievements"),
             InlineKeyboardButton("🏅 Leaderboard", callback_data="leaderboard")],
            [InlineKeyboardButton("💡 Insights", callback_data="insights"),
             InlineKeyboardButton("🆘 Help", callback_data="help_command")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        welcome_text = f"""
⚡ <b>METALENS | Ultimate Cognitive Mirror Bot</b>

<b>WELCOME, {user.first_name}!</b> Your brain is about to experience the <i>MOST ADVANCED</i> language analysis platform by 
<b>ZHUMAKHAN MUSSIRKHAN!</b>

<b>🔬 Research Focus:</b> <i>Cross-linguistic morphological transfer & Narrative Language Acquisition</i>

<b>🚀  NEW ULTIMATE FEATURES:</b>
• 🎴 <b>Interactive Flashcards</b> - Vocabulary with spaced repetition
• 🎭 <b>Interactive Storytelling</b> - Learn languages through stories
• 🔄 <b>Interactive Choices</b> - Influence story outcomes
• 📚 <b>Vocabulary in Context</b> - Learn words through narrative

<b>🚀  GET STARTED:</b>
1. <b>ANALYZE WORDS</b> - Type any word or use <code>/analyze</code>
2. <b>READ STORIES</b> - Immersive learning with <code>/story</code>
3. <b>STUDY FLASHCARDS</b> - Vocabulary mastering  <code>/flashcards</code>
4. <b>TAKE QUIZZES</b> - Test knowledge with <code>/quiz</code> or <code>/audioquiz</code>
5. <b>PLAY GAMES</b> - Vocabulary matching with <code>/vocab</code>
6. <b>REQUEST WORDS</b> - Suggest analysis with <code>/request</code>
7. <b>HEAR PRONUNCIATION</b> - Use <code>/pronounce [word]</code>
8. <b>TRACK PROGRESS</b> - View stats with <code>/progress</code>
9. <b>EARNED ACHIEVMENTS</b> - Your accomplishments <code>/badges</code>
10. <b>GLOBAL RANKING</b> - Use <code>/leaderboard</code>
11. <b>AVAILABLE COMMANDS</b> - List of commands <code>/help</code>

<b>💡  ANALYSIS EXAMPLES:</b>
<i>Try analyzing: <code>кітаптарымыздан</code> or <code>internationalization</code>!</i>

<b>📖  STORY RECOMMENDATION:</b>
<i>Start with <b>"Neural Awakening"</b> - a sci-fi adventure about language and cognition!</i>

<b>🎴  FLASHCARD TIP:</b>
<i>Try the <b>Kazakh Basics</b> deck to master fundamental morphology!</i>
        """
        
        await update.message.reply_text(welcome_text, parse_mode='HTML', reply_markup=reply_markup)
        await self.telegram_features.send_cognitive_insight(update, "neural_activity")

    async def _cognitive_analysis(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ULTIMATE cognitive analysis"""
        if not context.args:
            await update.message.reply_text(
                "🔍 <b>ULTIMATE Cognitive Analysis</b>\n\n"
                "Usage: <code>/analyze [word]</code>\n\n"
                "<b>Examples:</b>\n"
                "• <code>/analyze кітаптарымыздан</code> - Kazakh morphology\n"
                "• <code>/analyze internationalization</code> - English word formation\n"
                "• <code>/analyze взаимопонимание</code> - Russian cognition\n\n"
                "💡 <b>Pro tip:</b> Use <code>/deepdive</code> for advanced neural analysis!",
                parse_mode='HTML'
            )
            return
        
        word = " ".join(context.args).strip().lower()
        user = update.effective_user
        
        await self.telegram_features.send_typing_indicator(update, 2)
        
        if word in WORD_DATABASE:
            data = WORD_DATABASE[word]
            response = self._format_cognitive_analysis(word, data)
            self.analytics.track_cognitive_metric(user.id, 'processing_speed', random.uniform(0.8, 1.0))
            self.analytics.track_cognitive_metric(user.id, 'pattern_recognition', random.uniform(0.85, 1.0))
            self.db.update_user(user.id, words=1, language=data["language"])
            await self._check_achievements(update, user.id)
        else:
            response = self._format_ai_suggestions(word)
        
        await update.message.reply_text(response, parse_mode='HTML')
        await self.telegram_features.send_cognitive_insight(update, "pattern_recognition")

    def _format_cognitive_analysis(self, word: str, data: dict) -> str:
        """ULTIMATE analysis formatting with HTML"""
        neural_pathways = data.get('neural_pathways', 10)
        
        response = f"""
🧠 <b>ULTIMATE Cognitive Analysis of</b> <code>{word}</code>

<b>Language:</b> {data['language'].title()}
<b>Cognitive Level:</b> {data.get('cognitive_level', 'syntactic_awareness').replace('_', ' ').title()}
<b>Morpheme Complexity:</b> {data.get('morpheme_count', 3)}/10
<b>Neural Pathways:</b> {neural_pathways} activated
"""
        
        if data.get('phonetic'):
            response += f"<b>Phonetic:</b> {data['phonetic']}\n"
        
        if data.get('audio'):
            audio_url = AUDIO_BASE_URL + data['audio']
            response += f'<b>Pronunciation:</b> <a href="{audio_url}">Audio Available</a>\n'
        
        response += "\n"
        response += "<b>Neural Pathway Analysis:</b>\n"
        response += "<pre>" + "\n".join(data["analysis"]) + "</pre>\n\n"
        
        response += "<b>Cross-Linguistic Activation:</b>\n"
        for lang, trans in data["translations"].items():
            response += f"• {lang.title()}: {trans}\n"
        
        response += f"\n💡 <b>Cognitive Insight:</b> This analysis activates {neural_pathways} neural pathways for advanced morphological processing!"
        
        if data.get('audio'):
            response += f"\n\n🎧 <b>Pro Tip:</b> Use <code>/pronounce {word}</code> to hear the pronunciation!"
        
        return response

    def _format_ai_suggestions(self, word: str) -> str:
        """ULTIMATE AI suggestions with HTML"""
        suggestions = [w for w in WORD_DATABASE.keys() if word in w.lower()][:3]
        
        response = f"❌ <b>Cognitive Analysis:</b> Word <code>{word}</code> not found.\n\n"
        
        if suggestions:
            response += "💡 <b>Similar Neural Patterns:</b>\n"
            response += "\n".join(f"• <code>{s}</code>" for s in suggestions)
            response += "\n\n🔍 Try one of these or contribute to research with <code>/request</code>!"
        else:
            response += "💡 <b>Cognitive Options:</b>\n• Use <code>/list</code> to explore our database\n• Suggest new words with <code>/request</code>\n• Check spelling and try again"
        
        return response

    async def _check_achievements(self, update: Update, user_id: int):
        """ULTIMATE achievement checker"""
        user_data = self.db.get_user(user_id)
        earned = self.db.get_achievements(user_id)
        
        if not user_data:
            return
        
        # Check for new achievements
        new_achievements = []
        
        if user_data['total_words'] >= 5 and "first_analysis" not in earned:
            self.db.grant_achievement(user_id, "first_analysis")
            new_achievements.append("first_analysis")
        
        if user_data['total_quizzes'] >= 5 and "quiz_champion" not in earned:
            self.db.grant_achievement(user_id, "quiz_champion")
            new_achievements.append("quiz_champion")
        
        if user_data['max_combo'] >= 2.0 and "combo_king" not in earned:
            self.db.grant_achievement(user_id, "combo_king")
            new_achievements.append("combo_king")
        
        if user_data['vocab_games_completed'] >= 5 and "vocab_master" not in earned:
            self.db.grant_achievement(user_id, "vocab_master")
            new_achievements.append("vocab_master")
        
        if user_data['word_requests_submitted'] >= 5 and "request_contributor" not in earned:
            self.db.grant_achievement(user_id, "request_contributor")
            new_achievements.append("request_contributor")
        
        if user_data['requests_voted'] >= 10 and "community_voter" not in earned:
            self.db.grant_achievement(user_id, "community_voter")
            new_achievements.append("community_voter")
        
        # NEW: Story achievements
        if user_data['stories_completed'] >= 1 and "story_completion" not in earned:
            self.db.grant_achievement(user_id, "story_completion")
            new_achievements.append("story_completion")
        
        if user_data['stories_completed'] >= 10 and "story_master" not in earned:
            self.db.grant_achievement(user_id, "story_master")
            new_achievements.append("story_master")
        
        # NEW: Flashcard achievements
        if user_data['flashcard_sessions'] >= 1 and "flashcard_beginner" not in earned:
            self.db.grant_achievement(user_id, "flashcard_beginner")
            new_achievements.append("flashcard_beginner")
        
        if user_data['flashcard_sessions'] >= 20 and "flashcard_master" not in earned:
            self.db.grant_achievement(user_id, "flashcard_master")
            new_achievements.append("flashcard_master")
        
        # Announce new achievements
        for achievement_id in new_achievements:
            achievement = ACHIEVEMENTS.get(achievement_id, {})
            await update.message.reply_text(
                f"🎉 <b>NEW ACHIEVEMENT UNLOCKED!</b>\n\n"
                f"{achievement.get('icon', '🏆')} <b>{achievement.get('name', 'Achievement')}</b>\n"
                f"{achievement.get('description', '')}\n"
                f"🏅 +{achievement.get('points', 0)} points!",
                parse_mode='HTML'
            )

    def _calculate_cognitive_level(self, user_data: dict) -> int:
        """ULTIMATE cognitive level calculation"""
        if not user_data:
            return 1
        
        words = user_data.get('total_words', 0)
        quizzes = user_data.get('total_quizzes', 0)
        points = user_data.get('total_points', 0)
        combo = user_data.get('max_combo', 1.0)
        vocab_games = user_data.get('vocab_games_completed', 0)
        stories = user_data.get('stories_completed', 0)  # NEW: Include stories
        flashcard_sessions = user_data.get('flashcard_sessions', 0)  # NEW: Include flashcards
        
        level = min(10, (words // 8) + (quizzes // 3) + (points // 100) + int(combo * 2) + (vocab_games // 2) + (stories // 2) + (flashcard_sessions // 2))
        return max(1, level)

    # ========== ULTIMATE ADDITIONAL METHODS ==========
    async def _deep_dive_analysis(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ULTIMATE neural analysis"""
        if not context.args:
            await update.message.reply_text(
                "🧠 <b>ULTIMATE Deep Dive Neural Analysis</b>\n\n"
                "Usage: <code>/deepdive [word]</code>\n\n"
                "<b>Provides:</b>\n"
                "• Neural pathway simulation\n"
                "• Cross-linguistic brain activation\n"
                "• Morphological complexity scoring\n"
                "• Cognitive load estimation\n"
                "• Learning difficulty prediction",
                parse_mode='HTML'
            )
            return
        
        word = " ".join(context.args).strip().lower()
        await self.telegram_features.send_typing_indicator(update, 4)
        
        if word in WORD_DATABASE:
            data = WORD_DATABASE[word]
            response = self._format_neural_analysis(word, data)
        else:
            response = "🔍 <b>Neural Analysis:</b> Word not found in cognitive database.\n\n💡 Suggest it with <code>/request</code>!"
        
        await update.message.reply_text(response, parse_mode='HTML')

    def _format_neural_analysis(self, word: str, data: dict) -> str:
        """ULTIMATE neural analysis formatting with HTML"""
        complexity = data.get('morpheme_count', 3)
        neural_pathways = data.get('neural_pathways', 10)
        cognitive_load = complexity * 15
        
        response = f"""
🔬 <b>NEURAL PATHWAY ANALYSIS - {word}</b>

<b>Brain Activation Map:</b>
• Broca's Area: 🟢 High Activity
• Wernicke's Area: 🟡 Moderate Activity  
• Prefrontal Cortex: 🟢 High Activity
• Angular Gyrus: 🟡 Moderate Activity
• Auditory Cortex: 🟢 Active (if audio used)

<b>Cognitive Metrics:</b>
• Processing Complexity: {complexity}/10
• Neural Pathways: {neural_pathways} connections
• Estimated Cognitive Load: {cognitive_load}%
• Memory Formation: {100 - cognitive_load}% efficient

<b>Linguistic Features:</b>
• Morpheme Count: {complexity}
• Cross-Linguistic Transfer: High
• Syntactic Integration: Excellent

💡 <b>Neural Insight:</b> Optimal for pattern recognition training!
"""
        return response

    async def _daily_cognitive_challenge(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ULTIMATE daily challenges"""
        user = update.effective_user
        today = datetime.now().strftime("%Y-%m-%d")
        challenge = self._generate_daily_challenge(user.id)
        
        challenge_text = f"""
🎯 <b>DAILY COGNITIVE CHALLENGE - {today}</b>

<b>Today's Mission:</b> {challenge['description']}

<b>Objectives:</b>
{chr(10).join(f'• {obj}' for obj in challenge['objectives'])}

<b>Rewards:</b>
🏆 {challenge['points']} Cognitive Points
🎯 Pattern Recognition Training
🧠 Neural Pathway Strengthening
🔥 Combo Multipliers

<b>Time Limit:</b> 24 hours
<b>Difficulty:</b> {challenge['difficulty']}

🚀 <b>ULTIMATE Feature coming in next update!</b>
"""
        await update.message.reply_text(challenge_text, parse_mode='HTML')

    def _generate_daily_challenge(self, user_id: int) -> dict:
        """ULTIMATE challenge generator"""
        challenges = [
            {
                'description': 'Analyze 5 Kazakh words with complex morphology',
                'objectives': ['Identify plural suffixes', 'Recognize possessive markers', 'Map case endings'],
                'points': 100,
                'difficulty': 'Intermediate'
            },
            {
                'description': 'Complete 3 cross-linguistic comparison quizzes', 
                'objectives': ['Compare Turkic languages', 'Identify cognates', 'Map morphological patterns'],
                'points': 150,
                'difficulty': 'Advanced'
            },
        ]
        return random.choice(challenges)

    async def _cognitive_progress(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ULTIMATE progress tracking"""
        user = update.effective_user
        user_data = self.db.get_user(user.id)
        cognitive_profile = self.analytics.get_cognitive_profile(user.id)
        
        if not user_data:
            await update.message.reply_text("Start your cognitive journey with <code>/analyze</code>!", parse_mode='HTML')
            return
        
        neural_pathways = user_data['total_words'] * 3
        language_networks = len(user_data['languages_used'])
        cognitive_efficiency = cognitive_profile.get('learning_efficiency', 0) * 100
        
        progress_text = f"""
📊 <b>COGNITIVE PROGRESS DASHBOARD</b>

🧠 <b>Neural Metrics:</b>
• Neural Pathways: {neural_pathways} connections
• Language Networks: {language_networks} active
• Cognitive Efficiency: {cognitive_efficiency:.1f}%
• Max Combo: {user_data['max_combo']}x
• Avg Answer Time: {user_data['avg_answer_time']:.1f}s

🎯 <b>Skill Development:</b>
• Processing Speed: {cognitive_profile.get('processing_speed', 0):.2f}/1.0
• Pattern Recognition: {cognitive_profile.get('pattern_accuracy', 0):.2f}/1.0
• Memory Strength: {cognitive_profile.get('memory_strength', 0):.2f}/1.0
• Audio Processing: {cognitive_profile.get('audio_processing', 0):.2f}/1.0
• Analytical Thinking: {cognitive_profile.get('analytical_thinking', 0):.2f}/1.0
• Vocabulary Recall: {cognitive_profile.get('vocabulary_recall', 0):.2f}/1.0
• Narrative Comprehension: {cognitive_profile.get('narrative_comprehension', 0):.2f}/1.0
• Flashcard Memory: {cognitive_profile.get('flashcard_memory', 0):.2f}/1.0

🏆 <b>Achievements:</b>
• Words Analyzed: {user_data['total_words']}
• Quizzes Completed: {user_data['total_quizzes']}
• Vocabulary Games: {user_data['vocab_games_completed']}
• Word Requests: {user_data['word_requests_submitted']}
• Stories Completed: {user_data['stories_completed']}
• Flashcard Sessions: {user_data['flashcard_sessions']}
• Total Points: {user_data['total_points']}
• Daily Streak: {user_data['daily_streak']} days
• Achievement Points: {user_data['achievement_points']}

💡 <b>Cognitive Insight:</b> Your brain is showing excellent morphological awareness!
"""
        await update.message.reply_text(progress_text, parse_mode='HTML')

    async def _cognitive_profile(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ULTIMATE cognitive profile"""
        user = update.effective_user
        cognitive_profile = self.analytics.get_cognitive_profile(user.id)
        user_data = self.db.get_user(user.id)
        
        if not user_data:
            await update.message.reply_text("Start with <code>/analyze</code> to build your cognitive profile!", parse_mode='HTML')
            return
        
        cognitive_level = self._calculate_cognitive_level(user_data)
        
        profile_text = f"""
🧠 <b>COGNITIVE LINGUISTICS PROFILE</b>

👤 <b>Researcher:</b> {user.first_name}
🎯 <b>Cognitive Level:</b> {cognitive_level}/10
🧩 <b>Learning Style:</b> Analytical & Comparative

📈 <b>Cognitive Metrics:</b>
• Processing Speed: {cognitive_profile.get('processing_speed', 0):.2f}/1.0
• Pattern Accuracy: {cognitive_profile.get('pattern_accuracy', 0):.2f}/1.0
• Memory Retention: {cognitive_profile.get('memory_strength', 0):.2f}/1.0
• Audio Processing: {cognitive_profile.get('audio_processing', 0):.2f}/1.0
• Analytical Thinking: {cognitive_profile.get('analytical_thinking', 0):.2f}/1.0
• Vocabulary Recall: {cognitive_profile.get('vocabulary_recall', 0):.2f}/1.0
• Narrative Comprehension: {cognitive_profile.get('narrative_comprehension', 0):.2f}/1.0
• Flashcard Memory: {cognitive_profile.get('flashcard_memory', 0):.2f}/1.0
• Learning Efficiency: {cognitive_profile.get('learning_efficiency', 0)*100:.1f}%

🌍 <b>Language Affinities:</b>
• Languages Used: {len(user_data['languages_used'])}
• Words Analyzed: {user_data['total_words']}
• Vocabulary Games: {user_data['vocab_games_completed']}
• Word Requests: {user_data['word_requests_submitted']}
• Stories Completed: {user_data['stories_completed']}
• Flashcard Sessions: {user_data['flashcard_sessions']}
• Total Points: {user_data['total_points']}
• Max Combo: {user_data['max_combo']}x

💡 <b>Recommendation:</b> Focus on syntactic patterns to boost cognitive flexibility!
"""
        await update.message.reply_text(profile_text, parse_mode='HTML')

    async def _multilingual_comparison(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ULTIMATE multilingual comparison"""
        if not context.args or len(context.args) < 2:
            await update.message.reply_text(
                "🔍 <b>ULTIMATE Multilingual Comparison</b>\n\n"
                "Usage: <code>/compare [word1] [word2]</code>\n\n"
                "<b>Examples:</b>\n"
                "• <code>/compare кітаптар kitaplar</code> - Kazakh vs Turkish\n"
                "• <code>/compare understanding понимание</code> - English vs Russian\n"
                "• <code>/compare book книга kitap</code> - Triple comparison",
                parse_mode='HTML'
            )
            return
        
        words = context.args
        comparisons = []
        
        for word in words:
            if word.lower() in WORD_DATABASE:
                data = WORD_DATABASE[word.lower()]
                comparisons.append((word, data))
        
        if len(comparisons) < 2:
            await update.message.reply_text("❌ Need at least 2 valid words for comparison.")
            return
        
        response = "🔍 <b>ULTIMATE Multilingual Cognitive Comparison</b>\n\n"
        
        for word, data in comparisons:
            response += f"<b>{word}</b> ({data['language'].title()}):\n"
            response += f"• Structure: {' | '.join(data['analysis'][:3])}\n"
            response += f"• Cognitive Level: {data.get('cognitive_level', 'basic').replace('_', ' ').title()}\n"
            response += f"• Morpheme Complexity: {data.get('morpheme_count', 2)}/10\n\n"
        
        response += "💡 <b>Cognitive Insight:</b> Comparing languages strengthens cross-linguistic neural pathways!"
        await update.message.reply_text(response, parse_mode='HTML')

    async def _pattern_recognition_game(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ULTIMATE pattern recognition"""
        game_text = """
🎯 <b>PATTERN RECOGNITION CHALLENGE</b>

<i><b>Train your brain to identify linguistic patterns!</b></i>

<b>How it works:</b>
1. I'll show you word sets from different languages
2. You identify the common morphological pattern
3. Earn points for speed and accuracy
4. Unlock Pattern Master badges!

<b>Example Round:</b>
Words: "books", "кітаптар", "kitaplar"
Pattern: Plural suffix across languages

🚀 <b>ULTIMATE Feature coming in v7.1 - Pattern recognition AI in development!</b>
"""
        await update.message.reply_text(game_text, parse_mode='HTML')

    async def _interactive_leaderboard(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ULTIMATE leaderboard"""
        leaders = self.db.get_leaderboard(10)
        
        leaderboard_text = "🏆 <b>ULTIMATE Global Cognitive Linguistics Leaderboard</b>\n\n"
        
        for i, (user_id, username, total_points, achievement_points, current_streak, total_words, cognitive_level) in enumerate(leaders, 1):
            medal = ["🥇", "🥈", "🥉"][i-1] if i <= 3 else f"{i}."
            streak_icon = "🔥" if current_streak >= 7 else "⭐" if current_streak >= 3 else ""
            name = username or f"Researcher{user_id}"
            leaderboard_text += f"{medal} {name}: {total_points} pts (Lvl {cognitive_level}) {streak_icon}\n"
        
        user_rank = self._get_user_rank(update.effective_user.id)
        leaderboard_text += f"\n👤 <b>Your Rank:</b> #{user_rank}"
        leaderboard_text += "\n💡 <b>Climb the ranks by analyzing words and completing challenges!</b>"
        
        await update.message.reply_text(leaderboard_text, parse_mode='HTML')

    def _get_user_rank(self, user_id: int) -> int:
        """ULTIMATE rank calculation"""
        leaders = self.db.get_leaderboard(1000)
        for i, (uid, _, _, _, _, _, _) in enumerate(leaders, 1):
            if uid == user_id:
                return i
        return len(leaders) + 1

    async def _language_community(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ULTIMATE community features"""
        community_text = """
🌍 <b>METALENS LANGUAGE COMMUNITY</b>

<i><b>Connect with cognitive linguists worldwide!</b></i>

<b>Community Features:</b>
• 🤝 Collaborative analysis sessions
• 🗣️ Language exchange partnerships
• 🔬 Group research projects
• 🏆 Community challenges
• 💡 Knowledge sharing

<b>Active Communities:</b>
• Kazakh Linguistics Research
• Cognitive Science Enthusiasts
• Morphology Masters
• Language Acquisition Studies

🚀 <b>ULTIMATE Community features launching in v7.2!</b>
"""
        await update.message.reply_text(community_text, parse_mode='HTML')

    async def _live_research_session(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ULTIMATE research sessions"""
        research_text = """
🔬 <b>LIVE RESEARCH SESSION</b>

<i><b>Participate in real linguistic research!</b></i>

<b>Current Studies:</b>
• Cross-linguistic morphological transfer
• Cognitive load in language processing
• Neural correlates of morphology
• Language acquisition patterns

<b>Your Contribution:</b>
• Analyze unknown words
• Identify patterns
• Provide translations
• Share cognitive insights

🚀 <b>ULTIMATE Research participation launching in v7.3!</b>
"""
        await update.message.reply_text(research_text, parse_mode='HTML')

    async def _personalized_insights(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ULTIMATE personalized insights"""
        user = update.effective_user
        cognitive_profile = self.analytics.get_cognitive_profile(user.id)
        user_data = self.db.get_user(user.id)
        
        if not user_data:
            await update.message.reply_text("Start with <code>/analyze</code> to generate personalized insights!", parse_mode='HTML')
            return
        
        insights_text = f"""
💡 <b>ULTIMATE PERSONALIZED COGNITIVE INSIGHTS</b>

👋 <b>Hello {user.first_name}!</b> Here's your cognitive analysis:

🧠 <b>Current Neural Activity:</b>
• Pattern recognition: {cognitive_profile.get('pattern_accuracy', 0)*100:.1f}% efficient
• Processing speed: {cognitive_profile.get('processing_speed', 0)*100:.1f}% of optimal
• Memory formation: {cognitive_profile.get('memory_strength', 0)*100:.1f}% effective
• Audio processing: {cognitive_profile.get('audio_processing', 0)*100:.1f}% developed
• Analytical thinking: {cognitive_profile.get('analytical_thinking', 0)*100:.1f}% strong
• Vocabulary recall: {cognitive_profile.get('vocabulary_recall', 0)*100:.1f}% active
• Narrative comprehension: {cognitive_profile.get('narrative_comprehension', 0)*100:.1f}% engaged
• Flashcard memory: {cognitive_profile.get('flashcard_memory', 0)*100:.1f}% trained

🎯 <b>Recommendations:</b>
1. Practice with complex morphological structures
2. Try the vocabulary matching games daily
3. Focus on cross-linguistic comparisons
4. Submit word requests for research
5. Work on improving your combo multiplier
6. Read interactive stories to enhance narrative processing
7. Use flashcards for vocabulary retention

🏆 <b>Next Milestone:</b> Reach 100 words analyzed for the Neural Pathway Builder badge!

💭 <b>Did you know?</b> Each analysis creates approximately 3 new neural connections!
"""
        await update.message.reply_text(insights_text, parse_mode='HTML')

    async def _cognitive_badges(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ULTIMATE badges display"""
        user = update.effective_user
        user_data = self.db.get_user(user.id)
        earned_achievements = self.db.get_achievements(user_id=user.id)
        
        badges_text = "🎖️ <b>Your ULTIMATE Cognitive Badges</b>\n\n"
        
        for badge_id, badge in COGNITIVE_BADGES.items():
            has_badge = self._check_badge_requirements(user_data, badge['requirements'])
            icon = "✅" if has_badge else "🔄"
            progress = self._calculate_badge_progress(user_data, badge['requirements'])
            
            badges_text += f"{icon} {badge['icon']} <b>{badge['name']}</b>\n"
            badges_text += f"{badge['description']}\n"
            
            if not has_badge:
                badges_text += f"<b>Progress:</b> {progress}%\n"
            
            badges_text += "\n"
        
        if user_data:
            badges_text += f"🏅 <b>Total Achievement Points:</b> {user_data['achievement_points']}\n"
            badges_text += f"🔥 <b>Current Streak:</b> {user_data['current_streak']} days\n"
            badges_text += f"🎯 <b>Total Points:</b> {user_data['total_points']}\n"
        
        badges_text += "\n💡 <b>Keep analyzing words and taking quizzes to earn more badges!</b>"
        await update.message.reply_text(badges_text, parse_mode='HTML')

    def _check_badge_requirements(self, user_data: dict, requirements: dict) -> bool:
        """ULTIMATE badge requirement checker"""
        if not user_data:
            return False
        
        for req_key, req_value in requirements.items():
            if req_key == "quizzes_completed" and user_data['total_quizzes'] < req_value:
                return False
            elif req_key == "accuracy" and user_data['total_quizzes'] > 0:
                pass
            elif req_key == "languages_used" and len(user_data['languages_used']) < req_value:
                return False
            elif req_key == "words_analyzed" and user_data['total_words'] < req_value:
                return False
            elif req_key == "streak" and user_data['current_streak'] < req_value:
                return False
            elif req_key == "complex_words" and user_data['total_words'] < req_value:
                return False
            elif req_key == "audio_quizzes" and user_data['audio_quizzes_completed'] < req_value:
                return False
            elif req_key == "avg_answer_time" and user_data['avg_answer_time'] > req_value:
                return False
            elif req_key == "max_combo" and user_data['max_combo'] < req_value:
                return False
            elif req_key == "perfect_quizzes" and user_data['perfect_quizzes'] < req_value:
                return False
            elif req_key == "matching_games" and user_data['vocab_games_completed'] < req_value:
                return False
            elif req_key == "matching_efficiency" and user_data['vocab_games_completed'] > 0:
                pass
            elif req_key == "stories_completed" and user_data['stories_completed'] < req_value:
                return False
            elif req_key == "story_comprehension" and user_data['stories_completed'] > 0:
                # This would require additional tracking for story comprehension
                pass
            elif req_key == "flashcard_sessions" and user_data['flashcard_sessions'] < req_value:
                return False
            elif req_key == "flashcard_accuracy" and user_data['flashcard_sessions'] > 0:
                # This would require additional tracking for flashcard accuracy
                pass
        
        return True

    def _calculate_badge_progress(self, user_data: dict, requirements: dict) -> int:
        """ULTIMATE badge progress calculator"""
        if not user_data:
            return 0
        
        total_progress = 0
        requirement_count = len(requirements)
        
        for req_key, req_value in requirements.items():
            if req_key == "quizzes_completed":
                progress = min(100, (user_data['total_quizzes'] / req_value) * 100)
            elif req_key == "languages_used":
                progress = min(100, (len(user_data['languages_used']) / req_value) * 100)
            elif req_key == "words_analyzed":
                progress = min(100, (user_data['total_words'] / req_value) * 100)
            elif req_key == "streak":
                progress = min(100, (user_data['current_streak'] / req_value) * 100)
            elif req_key == "audio_quizzes":
                progress = min(100, (user_data['audio_quizzes_completed'] / req_value) * 100)
            elif req_key == "avg_answer_time":
                progress = min(100, max(0, (20 - user_data['avg_answer_time']) / req_value * 100))
            elif req_key == "max_combo":
                progress = min(100, (user_data['max_combo'] / req_value) * 100)
            elif req_key == "perfect_quizzes":
                progress = min(100, (user_data['perfect_quizzes'] / req_value) * 100)
            elif req_key == "matching_games":
                progress = min(100, (user_data['vocab_games_completed'] / req_value) * 100)
            elif req_key == "stories_completed":
                progress = min(100, (user_data['stories_completed'] / req_value) * 100)
            elif req_key == "flashcard_sessions":
                progress = min(100, (user_data['flashcard_sessions'] / req_value) * 100)
            else:
                progress = 0
            
            total_progress += progress
        
        return int(total_progress / requirement_count) if requirement_count > 0 else 0

    async def _revolutionary_help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ULTIMATE help system"""
        help_text = """
🆘 <b>METALENS - ULTIMATE Revolutionary Help</b>

🧠 <b>Cognitive Analysis Commands:</b>
• <code>/analyze [word]</code> - Advanced morphological analysis
• <code>/deepdive [word]</code> - Neural pathway simulation
• <code>/compare [word1] [word2]</code> - Cross-linguistic comparison
• <code>/pronounce [word]</code> - Audio pronunciation guide

🎮 <b>Brain Training Commands:</b>
• <code>/quiz</code> - Adaptive cognitive quizzes
• <code>/audioquiz</code> - Phonetic recognition challenges
• <code>/vocab</code> - Vocabulary matching games
• <code>/flashcards</code> - Interactive vocabulary flashcards
• <code>/pattern</code> - Pattern recognition games
• <code>/challenge</code> - Daily brain workouts

📖 <b>Storytelling Commands:</b>
• <code>/story</code> - Interactive multilingual stories
• <code>/story progress</code> - Your story learning journey
• Choose from sci-fi adventures, detective mysteries, and cultural journeys

💡 <b>Research & Community Commands:</b>
• <code>/request [word] [language]</code> - Submit word for analysis
• <code>/requests</code> - View and vote on word requests
• <code>/research</code> - Live research sessions
• <code>/community</code> - Language community

📊 <b>Analytics & Profile:</b>
• <code>/progress</code> - Cognitive progress dashboard
• <code>/profile</code> - Detailed cognitive profile
• <code>/insights</code> - Personalized recommendations
• <code>/badges</code> - Your cognitive badges
• <code>/leaderboard</code> - Global rankings

🏆 <b>Gamification:</b>
• Combo multipliers up to 2.0x
• Time bonuses for quick answers
• Neural impact tracking
• Tiered progression system
• Achievement system with badges
• Story completion rewards
• Flashcard memory tracking

💡 <b>ULTIMATE Pro Tips:</b>
• Use combo multipliers for higher scores
• Practice daily for streak bonuses
• Compare related languages for patterns
• Take audio quizzes to improve pronunciation
• Submit word requests to contribute to research
• Read stories for contextual vocabulary learning
• Use flashcards for long-term memory retention
• Track your cognitive metrics over time
"""
        await update.message.reply_text(help_text, parse_mode='HTML')

    async def _smart_message_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ULTIMATE smart message handler with enhanced command suggestions"""
        message = update.message.text.strip().lower()
        
        # Enhanced command suggestions
        if message.startswith('/'):
            # User is trying to use a command - provide helpful suggestions
            potential_commands = {
                'start': 'Start the Ultimate Cognitive Bot',
                'analyze': 'Analyze word morphology and structure', 
                'quiz': 'Take adaptive cognitive quizzes',
                'audioquiz': 'Audio pronunciation challenges',
                'story': 'Interactive multilingual stories',
                'flashcards': 'Vocabulary learning flashcards',
                'vocab': 'Vocabulary matching games',
                'pronounce': 'Hear word pronunciations',
                'progress': 'View your cognitive progress',
                'profile': 'Detailed cognitive profile',
                'leaderboard': 'Global rankings',
                'request': 'Suggest words for analysis',
                'help': 'Complete command list and guidance'
            }
            
            # Find closest matching command
            user_command = message[1:].split()[0]  # Remove slash and get first word
            matches = [cmd for cmd in potential_commands.keys() if cmd.startswith(user_command)]
            
            if matches:
                suggestion = matches[0]
                await update.message.reply_text(
                    f"💡 <b>Command Suggestion</b>\n\n"
                    f"Did you mean: <code>/{suggestion}</code>\n"
                    f"{potential_commands[suggestion]}\n\n"
                    f"Type <code>/help</code> for all available commands.",
                    parse_mode='HTML'
                )
                return
        
        if any(greet in message for greet in ['hello', 'hi', 'hey', 'greetings']):
            await update.message.reply_text("🧠 <b>ULTIMATE Cognitive Greetings!</b> Ready for some language analysis?", parse_mode='HTML')
        elif 'thank' in message:
            await update.message.reply_text("💡 <b>You're welcome!</b> Your brain is doing excellent work!", parse_mode='HTML')
        elif any(word in message for word in ['help', 'what can you do']):
            await self._revolutionary_help(update, context)
        else:
            if len(message.split()) == 1:
                context.args = [message]
                await self._cognitive_analysis(update, context)
            else:
                await update.message.reply_text(
                    "💭 <b>ULTIMATE Cognitive Assistant:</b> I'm here to help with language analysis! "
                    "Try analyzing a word or use <code>/help</code> to see all features.\n\n"
                    "💡 <b>Quick Start:</b>\n"
                    "• <code>/analyze [word]</code> - Analyze any word\n"
                    "• <code>/quiz</code> - Take a cognitive quiz\n"  
                    "• <code>/story</code> - Read interactive stories\n"
                    "• <code>/flashcards</code> - Study vocabulary",
                    parse_mode='HTML'
                )
    
    def run(self):
        """Start the ULTIMATE revolutionary bot"""
        print("🚀 ULTIMATE REVOLUTIONARY METALENS BOT v7.0 STARTING...")
        print("🎯 COGNITIVE INTERFACE: OPTIMAL")
        print("🧠 NEURAL ANALYTICS: ACTIVE") 
        print("🎧 AUDIO PRONUNCIATION: READY")
        print("🧩 VOCABULARY MATCHING: READY")
        print("🎴 FLASHCARD SYSTEM: ACTIVATED")
        print("💡 COMMAND SUGGESTIONS: ENABLED")
        print("🎭 STORYTELLING SYSTEM: ACTIVATED")
        print("📖 INTERACTIVE NARRATIVES: READY")
        print("🎧 AUDIO STORIES: INTEGRATED")
        print("⚡ COMBO SYSTEM: ENABLED")
        print("💫 ALL SYSTEMS: GO")
        print("🎊 BOT IS LIVE - ULTIMATE COGNITIVE REVOLUTION ACTIVATED!")
        
        try:
            self.app.run_polling()
        except Exception as e:
            print(f"❌ CRITICAL SYSTEM ERROR: {e}")
            print("🔄 AUTO-RECOVERY: Please restart the bot.")

# ========== START THE ULTIMATE REVOLUTION ==========
if __name__ == "__main__":
    bot = RevolutionaryMetalensBot()
    bot.run()