let canvas = document.getElementById("canvas");
let context = canvas.getContext("2d");


canvas.width = 1440;
canvas.height = 915;

let canvas_width = canvas.width;
let canvas_height = canvas.height;
//let shapes = [];

let lines = [];
let arrows = [];
let ghost_shapes = {};
let dict_shapes = {
    50: {x: 130, y: 20, width: 180, height: 90, position: "Снятие /n с занимаемой /n должности", font: "16px"},
    0: {x: 570, y: 20, width: 300, height: 90, position: "Руководитель /n ", is_manager: true, font: "20px"},

    1: {x: 50, y: 170, width: 160, height: 90, position: "Директор по /n стратегическому /n планированию", is_manager: true, font: "14px"},
    2: {x: 70, y: 275, width: 140, height: 40, position: "Экспериментальный /n участок", font: "12px"},
    3: {x: 70, y: 330, width: 140, height: 55, position: "Отдел /n финансового /n планирования", font: "12px"},
    4: {x: 70, y: 400, width: 140, height: 40, position: "Служба /n маркетинга", font: "12px"},

    5: {x: 230, y: 170, width: 160, height: 90, position: "Директор по /n персоналу", is_manager: true, font: "14px"},
    6: {x: 250, y: 275, width: 140, height: 40, position: "Отдел кадров", font: "12px"},
    7: {x: 250, y: 330, width: 140, height: 40, position: "Табельное бюро", font: "12px"},
    8: {x: 250, y: 385, width: 140, height: 40, position: "Отдел обучения", font: "12px"},
    9: {x: 250, y: 440, width: 140, height: 40, position: "Бытовой отдел", font: "12px"},

    10: {x: 510, y: 170, width: 500, height: 70, position: "Исполнительный директор /n ", is_manager: true, font: "16px"},

    11: {x: 410, y: 300, width: 160, height: 90, position: "Заместитель /n директора /n по производству", is_manager: true, font: "14px"},
    12: {x: 430, y: 405, width: 140, height: 40, position: "Производственный /n цех 1", font: "12px"},
    13: {x: 430, y: 460, width: 140, height: 40, position: "Производственный /n цех 2", font: "12px"},
    14: {x: 430, y: 515, width: 140, height: 40, position: "Производственный /n цех 3", font: "12px"},
    15: {x: 430, y: 570, width: 140, height: 40, position: "Производственный /n цех 4", font: "12px"},
    16: {x: 430, y: 625, width: 140, height: 40, position: "Автотранспортный /n цех", font: "12px"},
    17: {x: 430, y: 680, width: 140, height: 40, position: "Служба снабжения", font: "12px"},

    18: {x: 590, y: 300, width: 160, height: 90, position: "Главный инженер", is_manager: true, font: "14px"},
    19: {x: 610, y: 405, width: 140, height: 40, position: "ОГЭ", font: "12px"},
    20: {x: 610, y: 460, width: 140, height: 40, position: "ОГМ", font: "12px"},
    21: {x: 610, y: 515, width: 140, height: 40, position: "АСУ", font: "12px"},
    22: {x: 610, y: 570, width: 140, height: 40, position: "Инструментальное /n производство", font: "12px"},
    23: {x: 610, y: 625, width: 140, height: 40, position: "ОКС", font: "12px"},

    24: {x: 770, y: 300, width: 160, height: 90, position: "Коммерческий /n директор", is_manager: true, font: "14px"},
    25: {x: 790, y: 405, width: 140, height: 40, position: "Отдел сбыта", font: "12px"},
    26: {x: 790, y: 460, width: 140, height: 40, position: "Складское хозяйство", font: "12px"},
    27: {x: 790, y: 515, width: 140, height: 40, position: "Финансовый отдел", font: "12px"},
    28: {x: 790, y: 570, width: 140, height: 40, position: "Собственный /n транспорт", font: "12px"},
    29: {x: 790, y: 625, width: 140, height: 55, position: "Производственно -/n коммерческая /n фирма", font: "12px"},

    30: {x: 950, y: 300, width: 160, height: 90, position: "Главный экономист", is_manager: true, font: "14px"},
    31: {x: 970, y: 405, width: 140, height: 40, position: "ПЭО", font: "12px"},
    32: {x: 970, y: 460, width: 140, height: 40, position: "ОТиЗ", font: "12px"},

    33: {x: 1010, y: 535, width: 160, height: 90, position: "Главный бухгалтер", is_manager: true, font: "14px"},
    34: {x: 1030, y: 640, width: 140, height: 40, position: "Бухгалтерия", font: "12px"},

    35: {x: 1200, y: 170, width: 160, height: 90, position: "Начальник ОТК", is_manager: true, font: "14px"},
    36: {x: 1220, y: 275, width: 140, height: 40, position: "ВТК", font: "12px"},
    37: {x: 1220, y: 330, width: 140, height: 40, position: "ЦЗЛ", font: "12px"},
    38: {x: 1220, y: 385, width: 140, height: 40, position: "Служба /n метролога", font: "12px"},

    39: {x: 1220, y: 455, width: 140, height: 40, position: "Канцелярия", font: "12px"},
    40: {x: 1220, y: 510, width: 140, height: 40, position: "1 отдел", font: "12px"},
    41: {x: 1220, y: 565, width: 140, height: 40, position: "2 отдел", font: "12px"},
    42: {x: 1220, y: 620, width: 140, height: 40, position: "ВОХР", font: "12px"},
    43: {x: 1220, y: 675, width: 140, height: 55, position: "Служба /n экономической /n безопасности", font: "12px"},
    44: {x: 1220, y: 745, width: 140, height: 40, position: "Юридическая /n служба", font: "12px"},
    45: {x: 1220, y: 800, width: 140, height: 40, position: "Отдел охраны /n труда", font: "12px"},
    46: {x: 1220, y: 855, width: 140, height: 40, position: "Отдел экологии", font: "12px"},
};

/* lines */
lines.push( {mt_x: 130, mt_y: 140, lt_x: 1390, lt_y: 140} );
lines.push( {mt_x: 490, mt_y: 270, lt_x: 1030, lt_y: 270} );
lines.push( {mt_x: 1390, mt_y: 140, lt_x: 1390, lt_y: 875} );
lines.push( {mt_x: 50, mt_y: 260, lt_x: 50, lt_y: 420} );
lines.push( {mt_x: 230, mt_y: 260, lt_x: 230, lt_y: 460} );
lines.push( {mt_x: 410, mt_y: 390, lt_x: 410, lt_y: 700} );
lines.push( {mt_x: 590, mt_y: 390, lt_x: 590, lt_y: 645} );
lines.push( {mt_x: 770, mt_y: 390, lt_x: 770, lt_y: 652} );
lines.push( {mt_x: 950, mt_y: 390, lt_x: 950, lt_y: 480} );
lines.push( {mt_x: 1010, mt_y: 625, lt_x: 1010, lt_y: 660} );
lines.push( {mt_x: 1200, mt_y: 260, lt_x: 1200, lt_y: 405} );

/* arrow */
arrows.push( {mt_x: 720, mt_y: 110, rotate: 0, arrow_length: 30} );
arrows.push( {mt_x: 130, mt_y: 140, rotate: 0, arrow_length: 30} );
arrows.push( {mt_x: 310, mt_y: 140, rotate: 0, arrow_length: 30} );
arrows.push( {mt_x: 760, mt_y: 140, rotate: 0, arrow_length: 30} );
arrows.push( {mt_x: 1280, mt_y: 140, rotate: 0, arrow_length: 30} );
arrows.push( {mt_x: 760, mt_y: 240, rotate: 0, arrow_length: 30} );
arrows.push( {mt_x: 490, mt_y: 270, rotate: 0, arrow_length: 30} );
arrows.push( {mt_x: 670, mt_y: 270, rotate: 0, arrow_length: 30} );
arrows.push( {mt_x: 850, mt_y: 270, rotate: 0, arrow_length: 30} );
arrows.push( {mt_x: 1030, mt_y: 270, rotate: 0, arrow_length: 30} );
arrows.push( {mt_x: 1140, mt_y: 140, rotate: 0, arrow_length: 395} );

arrows.push( {mt_x: 50, mt_y: 300, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 50, mt_y: 357, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 50, mt_y: 420, rotate: 1, arrow_length: 20} );

arrows.push( {mt_x: 230, mt_y: 295, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 230, mt_y: 350, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 230, mt_y: 405, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 230, mt_y: 460, rotate: 1, arrow_length: 20} );

arrows.push( {mt_x: 410, mt_y: 425, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 410, mt_y: 480, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 410, mt_y: 535, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 410, mt_y: 590, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 410, mt_y: 645, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 410, mt_y: 700, rotate: 1, arrow_length: 20} );

arrows.push( {mt_x: 590, mt_y: 425, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 590, mt_y: 480, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 590, mt_y: 535, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 590, mt_y: 590, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 590, mt_y: 645, rotate: 1, arrow_length: 20} );

arrows.push( {mt_x: 770, mt_y: 425, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 770, mt_y: 480, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 770, mt_y: 535, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 770, mt_y: 590, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 770, mt_y: 652, rotate: 1, arrow_length: 20} );

arrows.push( {mt_x: 950, mt_y: 425, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 950, mt_y: 480, rotate: 1, arrow_length: 20} );

arrows.push( {mt_x: 1010, mt_y: 660, rotate: 1, arrow_length: 20} );

arrows.push( {mt_x: 1200, mt_y: 302, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 1200, mt_y: 350, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 1200, mt_y: 405, rotate: 1, arrow_length: 20} );

arrows.push( {mt_x: 1390, mt_y: 475, rotate: 2, arrow_length: 30} );
arrows.push( {mt_x: 1390, mt_y: 530, rotate: 2, arrow_length: 30} );
arrows.push( {mt_x: 1390, mt_y: 585, rotate: 2, arrow_length: 30} );
arrows.push( {mt_x: 1390, mt_y: 640, rotate: 2, arrow_length: 30} );
arrows.push( {mt_x: 1390, mt_y: 702, rotate: 2, arrow_length: 30} );
arrows.push( {mt_x: 1390, mt_y: 765, rotate: 2, arrow_length: 30} );
arrows.push( {mt_x: 1390, mt_y: 820, rotate: 2, arrow_length: 30} );
arrows.push( {mt_x: 1390, mt_y: 875, rotate: 2, arrow_length: 30} );

let is_dragging = false;
let start_shapeX;
let start_shapeY;
let current_shape;
let current_shape_key;
let startX;
let startY;

base_url = `${window.location.hostname}:${window.location.port}`
        const websocket = new WebSocket(`ws://${base_url}`)
        websocket.onopen = function (event) {
            console.log('client says connection opened')
            websocket.send("Client sends Welcomettt")
        }
        websocket.onmessage = function (event) {
            message = JSON.parse(event.data)
            let position = message.position
            /* запись имён менеджеров в фигуры */
            for(let key in position) {
                dict_shapes[key].manager_name = position[key]
            draw_all();
            }
        }

/* проверка, что указатель мыши находится в блоке */
let is_mouse_in_shape = function (x, y, shape) {
    let shape_left = shape.x;
    let shape_right = shape.x + shape.width;
    let shape_top = shape.y;
    let shape_bottom = shape.y + shape.height;
    if (x > shape_left && x < shape_right && y > shape_top && y < shape_bottom) {
        return true;
    }
    return false;
};

/* Функция для отображения текста блока и переноса строк текста */
function wrapText(context, shape) {
        let lines = ""
        if (shape.is_manager) lines = (shape.position + "/n" + shape.manager_name).split("/n")
        else lines = shape.position.split("/n");
        let countLines = lines.length;
        context.textBaseline = "middle";
        if (countLines == 1) {
            context.fillText(shape.position, shape.x + shape.width/2, shape.y + shape.height/2);
        }
        else {
            for (let n = 0; n < countLines; n++) {
//                context.fillText(lines[n], shape.x + shape.width/2, shape.y + shape.height/countLines * n);
                context.fillText(lines[n], shape.x + shape.width/2, shape.y + shape.height/2 - countLines * 20/2 + 6*countLines + n * 14);
            }
        }
    };

/* рисуем прямоугольники */
let draw_shapes = function (event) {
    context.textAlign = "center";

    let rect = canvas.getBoundingClientRect();
    let shape;

    if (event) {
        mouseX = event.clientX - rect.left;
        mouseY = event.clientY - rect.top;
    };

    for (let key in dict_shapes) {
        /* проверка что указатель мыши находится в блоке, исходя из этого выбираем цвет блока */
        shape = dict_shapes[key]
        if (event) {
            if (is_mouse_in_shape(mouseX, mouseY, shape)) {
                if (shape.is_manager) context.fillStyle = "#FFA24C"
                else context.fillStyle = "#FFF2E5"
            }
            else {
                if (shape.is_manager) context.fillStyle = "#E67A17"
                else context.fillStyle = "#F9D5B0"
            }
        }
        else {
            if (shape.is_manager) context.fillStyle = "#E67A17"
            else context.fillStyle = "#F9D5B0"
        }

        if (key==50) context.fillStyle = "#8B959B"

        context.fillRect(shape.x, shape.y, shape.width, shape.height);
        context.fillStyle = "black";
        context.strokeRect(shape.x, shape.y, shape.width, shape.height);
        context.font = shape.font + " Arial";
        wrapText(context, shape);
    }
};

/* рисуем линии */
let draw_lines = function () {
    context.beginPath();
    for (let line of lines) {
        context.moveTo(line.mt_x, line.mt_y);
        context.lineTo(line.lt_x, line.lt_y);
    };
    context.stroke();
};

/* рисуем стрелки */
/* берутся начальные координаты стрелки и в зависимости от длинны и направления рисуются стрелки */
let draw_arrows = function () {
    context.beginPath();
    let lt = [];
    for (let arrow of arrows) {
        if (arrow.rotate == 1) lt = [[arrow.arrow_length, 0], [-4, -4], [4, 4], [-4, 4]];
        else if (arrow.rotate == 2) lt = [[-arrow.arrow_length, 0], [4, -4], [-4, 4], [4, 4]];
        else lt = [[0, arrow.arrow_length], [-4, -4], [4, 4], [4, -4]];

        context.moveTo(arrow.mt_x, arrow.mt_y);
        let temp_ltx = arrow.mt_x;
        let temp_lty = arrow.mt_y;
        for (let m of lt) {
            temp_ltx += m[0];
            temp_lty += m[1];
            context.lineTo(temp_ltx, temp_lty);
        };
    };
    context.stroke();
};

/* рисуем прямоугольники призраки */
let draw_ghost_shapes = function (event) {
    context.clearRect(0, 0, canvas_width, canvas_height);
    context.fillStyle = "#8B959B";
    context.fillRect(0, 0, canvas_width, canvas_height);
    context.textAlign = "center";
    let ghost_shape;

    for (let key in ghost_shapes) {
        ghost_shape = ghost_shapes[key]
        context.fillStyle = "#8B959B"
        context.fillRect(ghost_shape.x, ghost_shape.y, ghost_shape.width, ghost_shape.height);
        context.fillStyle = "black";
        context.strokeRect(ghost_shape.x, ghost_shape.y, ghost_shape.width, ghost_shape.height);
        context.font = ghost_shape.font + " Arial";
        wrapText(context, ghost_shapes[key]);
    }
}

let draw_all = function() {
    draw_ghost_shapes();
    draw_shapes(event);
    draw_arrows();
    draw_lines();
}

/* функция обработки нажатия клавиши мыши */
let mouse_down = function(event) {
    let rect = canvas.getBoundingClientRect();
    startX = event.clientX - rect.left;
    startY = event.clientY - rect.top;

    /* если нажатие клавиши было в блоке менеджера то сохраняются
        начальные координаты x и y для возврата блока на исходное место,
       если нажат был блок отдела, то происходит переход на соответствующую страницу */

    /* проверяется нажатие на блок, если блок в данный момент, не несётся */
    if (!is_dragging && event.which == 1) {
        for (let key in dict_shapes) {
            if (is_mouse_in_shape(startX, startY, dict_shapes[key])) {
                if (dict_shapes[key].is_manager) {
                    is_dragging = true;
                    start_shapeX = dict_shapes[key].x;
                    start_shapeY = dict_shapes[key].y;
                    current_shape = dict_shapes[key];
                    current_shape_key = key;
                    /* создаём блок призрак поднятого блока и записывем его в список ghost_shapes */
                    ghost_shapes[key] = {};
                    for (let k in current_shape) {
                        ghost_shapes[key][k] = current_shape[k]
                    }
                    ghost_shapes[key].manager_name = " "
                    console.log(ghost_shapes)
                    break;    // если блок определился, происходит прерывание цикла поиска блока
                } else {
                    let num_key = +key + 1;
                    window.location = `/position/` + num_key;
                }
            };
        }
    }
};

let mouse_up = function(event) {
    /* если блок находится в зоне освобождения от занимаемой должности на сервер отправляется соответствующее сообщение */
    if (is_dragging) {
        let rect = canvas.getBoundingClientRect();
        let mouseX = event.clientX - rect.left;
        let mouseY = event.clientY - rect.top;
//        appoint a manager
        if (is_mouse_in_shape(mouseX, mouseY, dict_shapes[50])) {
            delete dict_shapes[current_shape_key];
            is_dragging = false;
            text_data = {type_message: "remove_manager", position_id: current_shape_key};
            websocket.send(JSON.stringify(text_data));
        } else {
            current_shape.x = start_shapeX;
            current_shape.y = start_shapeY;
        }
    }
    is_dragging = false;
}

/* обработка движения мыши */
let mouse_move = function(event) {
    if (!is_dragging) {
        draw_all();
//        draw_shapes(event);
//        draw_arrows();
//        draw_lines();
    }
    else {
        /* вычисляем координаты смещения мыши с поднятым блоком и перемещаем блок на это смещение */
        let rect = canvas.getBoundingClientRect();
        let mouseX = event.clientX - rect.left;
        let mouseY = event.clientY - rect.top;

        let dx = mouseX - startX;
        let dy = mouseY - startY;
        current_shape.x += dx;
        current_shape.y += dy;

        startX = mouseX;
        startY = mouseY;

        draw_all();
//        draw_shapes(event);
//        draw_arrows();
//        draw_lines();

        /* снова рисуем поднятый блок, чтобы он был сверху всех фигур */
        context.shadowBlur = 15;
        context.shadowOffsetX = 0;
        context.shadowColor = "#5D6468";
        context.fillStyle = "#FFA24C"
        context.fillRect(current_shape.x, current_shape.y, current_shape.width, current_shape.height);
        context.shadowBlur = 0;
        context.fillStyle = "black";
        context.strokeRect(current_shape.x, current_shape.y, current_shape.width, current_shape.height);
        context.font = current_shape.font + " Arial";
        wrapText(context, current_shape);

    }
}

/* если мышь с блоком выйдет за поле, блок вернётся на своё изначальное место */
let mouse_out = function(event) {
    if (is_dragging) {
        current_shape.x = start_shapeX;
        current_shape.y = start_shapeY;
    }
    is_dragging = false;
}

canvas.onmousemove = mouse_move;
canvas.onmousedown = mouse_down;
canvas.onmouseup = mouse_up;
canvas.onmouseout = mouse_out;

//canvas.addEventListener("dblclick", ()=>console.log("dblclick"));
//canvas.addEventListener("mousedown", e => mouse_down(e));
//canvas.addEventListener("mouseup", e => mouse_up(e));
//canvas.addEventListener("mousemove", e => mouse_move(e));
//canvas.addEventListener("contextmenu", e => e.preventDefault());


