// данные для рисования блоков структуры компании
alfa_dict_blocks = {
    1: {x: 570, y: 20, width: 300, height: 90, position: "Руководитель /n ", is_manager: true, font: "20px"},
    2: {x: 510, y: 170, width: 500, height: 70, position: "Исполнительный директор /n ", is_manager: true, font: "16px"},
    3: {x: 50, y: 170, width: 160, height: 90, position: "Директор по /n стратегическому /n планированию", is_manager: true, font: "14px"},
    4: {x: 230, y: 170, width: 160, height: 90, position: "Директор по /n персоналу", is_manager: true, font: "14px"},
    5: {x: 410, y: 300, width: 160, height: 90, position: "Заместитель /n директора /n по производству", is_manager: true, font: "14px"},
    6: {x: 590, y: 300, width: 160, height: 90, position: "Главный инженер", is_manager: true, font: "14px"},
    7: {x: 770, y: 300, width: 160, height: 90, position: "Коммерческий /n директор", is_manager: true, font: "14px"},
    8: {x: 950, y: 300, width: 160, height: 90, position: "Главный экономист", is_manager: true, font: "14px"},
    9: {x: 1010, y: 535, width: 160, height: 90, position: "Главный бухгалтер", is_manager: true, font: "14px"},
    10: {x: 1200, y: 170, width: 160, height: 90, position: "Начальник ОТК", is_manager: true, font: "14px"},

    11: {x: 70, y: 275, width: 140, height: 40, position: "Экспериментальный /n участок", font: "12px"},
    12: {x: 70, y: 330, width: 140, height: 55, position: "Отдел /n финансового /n планирования", font: "12px"},
    13: {x: 70, y: 400, width: 140, height: 40, position: "Служба /n маркетинга", font: "12px"},

    14: {x: 250, y: 275, width: 140, height: 40, position: "Отдел кадров", font: "12px"},
    15: {x: 250, y: 330, width: 140, height: 40, position: "Табельное бюро", font: "12px"},
    16: {x: 250, y: 385, width: 140, height: 40, position: "Отдел обучения", font: "12px"},
    17: {x: 250, y: 440, width: 140, height: 40, position: "Бытовой отдел", font: "12px"},


    18: {x: 430, y: 405, width: 140, height: 40, position: "Производственный /n цех 1", font: "12px"},
    19: {x: 430, y: 460, width: 140, height: 40, position: "Производственный /n цех 2", font: "12px"},
    20: {x: 430, y: 515, width: 140, height: 40, position: "Производственный /n цех 3", font: "12px"},
    21: {x: 430, y: 570, width: 140, height: 40, position: "Производственный /n цех 4", font: "12px"},
    22: {x: 430, y: 625, width: 140, height: 40, position: "Автотранспортный /n цех", font: "12px"},
    23: {x: 430, y: 680, width: 140, height: 40, position: "Служба снабжения", font: "12px"},

    24: {x: 610, y: 405, width: 140, height: 40, position: "ОГЭ", font: "12px"},
    25: {x: 610, y: 460, width: 140, height: 40, position: "ОГМ", font: "12px"},
    26: {x: 610, y: 515, width: 140, height: 40, position: "АСУ", font: "12px"},
    27: {x: 610, y: 570, width: 140, height: 40, position: "Инструментальное /n производство", font: "12px"},
    28: {x: 610, y: 625, width: 140, height: 40, position: "ОКС", font: "12px"},

    29: {x: 790, y: 405, width: 140, height: 40, position: "Отдел сбыта", font: "12px"},
    30: {x: 790, y: 460, width: 140, height: 40, position: "Складское хозяйство", font: "12px"},
    31: {x: 790, y: 515, width: 140, height: 40, position: "Финансовый отдел", font: "12px"},
    32: {x: 790, y: 570, width: 140, height: 40, position: "Собственный /n транспорт", font: "12px"},
    33: {x: 790, y: 625, width: 140, height: 55, position: "Производственно -/n коммерческая /n фирма", font: "12px"},

    34: {x: 970, y: 405, width: 140, height: 40, position: "ПЭО", font: "12px"},
    35: {x: 970, y: 460, width: 140, height: 40, position: "ОТиЗ", font: "12px"},

    36: {x: 1030, y: 640, width: 140, height: 40, position: "Бухгалтерия", font: "12px"},

    37: {x: 1220, y: 275, width: 140, height: 40, position: "ВТК", font: "12px"},
    38: {x: 1220, y: 330, width: 140, height: 40, position: "ЦЗЛ", font: "12px"},
    39: {x: 1220, y: 385, width: 140, height: 40, position: "Служба /n метролога", font: "12px"},

    40: {x: 1220, y: 455, width: 140, height: 40, position: "Канцелярия", font: "12px"},
    41: {x: 1220, y: 510, width: 140, height: 40, position: "1 отдел", font: "12px"},
    42: {x: 1220, y: 565, width: 140, height: 40, position: "2 отдел", font: "12px"},
    43: {x: 1220, y: 620, width: 140, height: 40, position: "ВОХР", font: "12px"},
    44: {x: 1220, y: 675, width: 140, height: 55, position: "Служба /n экономической /n безопасности", font: "12px"},
    45: {x: 1220, y: 745, width: 140, height: 40, position: "Юридическая /n служба", font: "12px"},
    46: {x: 1220, y: 800, width: 140, height: 40, position: "Отдел охраны /n труда", font: "12px"},
    47: {x: 1220, y: 855, width: 140, height: 40, position: "Отдел экологии", font: "12px"},

    50: {x: 130, y: 20, width: 180, height: 90, position: "Снятие /n с занимаемой /n должности", font: "16px"},
};

// данные для рисования линий связей блоков структуры компании
lines = [
    {mt_x: 130, mt_y: 140, lt_x: 1390, lt_y: 140},
    {mt_x: 490, mt_y: 270, lt_x: 1030, lt_y: 270},
    {mt_x: 1390, mt_y: 140, lt_x: 1390, lt_y: 875},
    {mt_x: 50, mt_y: 260, lt_x: 50, lt_y: 420},
    {mt_x: 230, mt_y: 260, lt_x: 230, lt_y: 460},
    {mt_x: 410, mt_y: 390, lt_x: 410, lt_y: 700},
    {mt_x: 590, mt_y: 390, lt_x: 590, lt_y: 645},
    {mt_x: 770, mt_y: 390, lt_x: 770, lt_y: 652},
    {mt_x: 950, mt_y: 390, lt_x: 950, lt_y: 480},
    {mt_x: 1010, mt_y: 625, lt_x: 1010, lt_y: 660},
    {mt_x: 1200, mt_y: 260, lt_x: 1200, lt_y: 405},
];

// данные для рисование стрелок от линий к блокам
arrows = [
    {mt_x: 720, mt_y: 110, rotate: 0, arrow_length: 30},
    {mt_x: 130, mt_y: 140, rotate: 0, arrow_length: 30},
    {mt_x: 310, mt_y: 140, rotate: 0, arrow_length: 30},
    {mt_x: 760, mt_y: 140, rotate: 0, arrow_length: 30},
    {mt_x: 1280, mt_y: 140, rotate: 0, arrow_length: 30},
    {mt_x: 760, mt_y: 240, rotate: 0, arrow_length: 30},
    {mt_x: 490, mt_y: 270, rotate: 0, arrow_length: 30},
    {mt_x: 670, mt_y: 270, rotate: 0, arrow_length: 30},
    {mt_x: 850, mt_y: 270, rotate: 0, arrow_length: 30},
    {mt_x: 1030, mt_y: 270, rotate: 0, arrow_length: 30},
    {mt_x: 1140, mt_y: 140, rotate: 0, arrow_length: 395},

    {mt_x: 50, mt_y: 300, rotate: 1, arrow_length: 20},
    {mt_x: 50, mt_y: 357, rotate: 1, arrow_length: 20},
    {mt_x: 50, mt_y: 420, rotate: 1, arrow_length: 20},

    {mt_x: 230, mt_y: 295, rotate: 1, arrow_length: 20},
    {mt_x: 230, mt_y: 350, rotate: 1, arrow_length: 20},
    {mt_x: 230, mt_y: 405, rotate: 1, arrow_length: 20},
    {mt_x: 230, mt_y: 460, rotate: 1, arrow_length: 20},

    {mt_x: 410, mt_y: 425, rotate: 1, arrow_length: 20},
    {mt_x: 410, mt_y: 480, rotate: 1, arrow_length: 20},
    {mt_x: 410, mt_y: 535, rotate: 1, arrow_length: 20},
    {mt_x: 410, mt_y: 590, rotate: 1, arrow_length: 20},
    {mt_x: 410, mt_y: 645, rotate: 1, arrow_length: 20},
    {mt_x: 410, mt_y: 700, rotate: 1, arrow_length: 20},

    {mt_x: 590, mt_y: 425, rotate: 1, arrow_length: 20},
    {mt_x: 590, mt_y: 480, rotate: 1, arrow_length: 20},
    {mt_x: 590, mt_y: 535, rotate: 1, arrow_length: 20},
    {mt_x: 590, mt_y: 590, rotate: 1, arrow_length: 20},
    {mt_x: 590, mt_y: 645, rotate: 1, arrow_length: 20},

    {mt_x: 770, mt_y: 425, rotate: 1, arrow_length: 20},
    {mt_x: 770, mt_y: 480, rotate: 1, arrow_length: 20},
    {mt_x: 770, mt_y: 535, rotate: 1, arrow_length: 20},
    {mt_x: 770, mt_y: 590, rotate: 1, arrow_length: 20},
    {mt_x: 770, mt_y: 652, rotate: 1, arrow_length: 20},

    {mt_x: 950, mt_y: 425, rotate: 1, arrow_length: 20},
    {mt_x: 950, mt_y: 480, rotate: 1, arrow_length: 20},

    {mt_x: 1010, mt_y: 660, rotate: 1, arrow_length: 20},

    {mt_x: 1200, mt_y: 302, rotate: 1, arrow_length: 20},
    {mt_x: 1200, mt_y: 350, rotate: 1, arrow_length: 20},
    {mt_x: 1200, mt_y: 405, rotate: 1, arrow_length: 20},

    {mt_x: 1390, mt_y: 475, rotate: 2, arrow_length: 30},
    {mt_x: 1390, mt_y: 530, rotate: 2, arrow_length: 30},
    {mt_x: 1390, mt_y: 585, rotate: 2, arrow_length: 30},
    {mt_x: 1390, mt_y: 640, rotate: 2, arrow_length: 30},
    {mt_x: 1390, mt_y: 702, rotate: 2, arrow_length: 30},
    {mt_x: 1390, mt_y: 765, rotate: 2, arrow_length: 30},
    {mt_x: 1390, mt_y: 820, rotate: 2, arrow_length: 30},
    {mt_x: 1390, mt_y: 875, rotate: 2, arrow_length: 30},
]
