let canvas = document.getElementById("canvas");
let context = canvas.getContext("2d");


canvas.width = 1440;
canvas.height = 915;

let canvas_width = canvas.width;
let canvas_height = canvas.height;
let shapes = [];
let ghost_shapes = [{x: 130, y: 30, width: 180, height: 10, position: "Снятие /n с занимаемой /n должности", font: "16px"}];
let lines = [];
let arrows = [];

shapes.push({x: 570, y: 20, width: 300, height: 90, position: "Руководитель /n ", is_manager: true, font: "20px"});

shapes.push( {x: 50, y: 170, width: 160, height: 90, position: "Директор по /n стратегическому /n планированию", is_manager: true, font: "14px"} );
shapes.push( {x: 70, y: 275, width: 140, height: 40, position: "Экспериментальный /n участок", font: "12px"} );
shapes.push( {x: 70, y: 330, width: 140, height: 55, position: "Отдел /n финансового /n планирования", font: "12px"} );
shapes.push( {x: 70, y: 400, width: 140, height: 40, position: "Служба /n маркетинга", font: "12px"} );

shapes.push( {x: 230, y: 170, width: 160, height: 90, position: "Директор по /n персоналу", is_manager: true, font: "14px"} );
shapes.push( {x: 250, y: 275, width: 140, height: 40, position: "Отдел кадров", font: "12px"} );
shapes.push( {x: 250, y: 330, width: 140, height: 40, position: "Табельное бюро", font: "12px"} );
shapes.push( {x: 250, y: 385, width: 140, height: 40, position: "Отдел обучения", font: "12px"} );
shapes.push( {x: 250, y: 440, width: 140, height: 40, position: "Бытовой отдел", font: "12px"} );

shapes.push( {x: 510, y: 170, width: 500, height: 70, position: "Исполнительный директор /n ", is_manager: true, font: "16px"} );

shapes.push( {x: 410, y: 300, width: 160, height: 90, position: "Заместитель /n директора /n по производству", is_manager: true, font: "14px"} );
shapes.push( {x: 430, y: 405, width: 140, height: 40, position: "Производственный /n цех 1", font: "12px"} );
shapes.push( {x: 430, y: 460, width: 140, height: 40, position: "Производственный /n цех 2", font: "12px"} );
shapes.push( {x: 430, y: 515, width: 140, height: 40, position: "Производственный /n цех 3", font: "12px"} );
shapes.push( {x: 430, y: 570, width: 140, height: 40, position: "Производственный /n цех 4", font: "12px"} );
shapes.push( {x: 430, y: 625, width: 140, height: 40, position: "Автотранспортный /n цех", font: "12px"} );
shapes.push( {x: 430, y: 680, width: 140, height: 40, position: "Служба снабжения", font: "12px"} );

shapes.push( {x: 590, y: 300, width: 160, height: 90, position: "Главный инженер", is_manager: true, font: "14px"} );
shapes.push( {x: 610, y: 405, width: 140, height: 40, position: "ОГЭ", font: "12px"} );
shapes.push( {x: 610, y: 460, width: 140, height: 40, position: "ОГМ", font: "12px"} );
shapes.push( {x: 610, y: 515, width: 140, height: 40, position: "АСУ", font: "12px"} );
shapes.push( {x: 610, y: 570, width: 140, height: 40, position: "Инструментальное /n производство", font: "12px"} );
shapes.push( {x: 610, y: 625, width: 140, height: 40, position: "ОКС", font: "12px"} );

shapes.push( {x: 770, y: 300, width: 160, height: 90, position: "Коммерческий /n директор", is_manager: true, font: "14px"} );
shapes.push( {x: 790, y: 405, width: 140, height: 40, position: "Отдел сбыта", font: "12px"} );
shapes.push( {x: 790, y: 460, width: 140, height: 40, position: "Складское хозяйство", font: "12px"} );
shapes.push( {x: 790, y: 515, width: 140, height: 40, position: "Финансовый отдел", font: "12px"} );
shapes.push( {x: 790, y: 570, width: 140, height: 40, position: "Собственный /n транспорт", font: "12px"} );
shapes.push( {x: 790, y: 625, width: 140, height: 55, position: "Производственно -/n коммерческая /n фирма", font: "12px"} );

shapes.push( {x: 950, y: 300, width: 160, height: 90, position: "Главный экономист", is_manager: true, font: "14px"} );
shapes.push( {x: 970, y: 405, width: 140, height: 40, position: "ПЭО", font: "12px"} );
shapes.push( {x: 970, y: 460, width: 140, height: 40, position: "ОТиЗ", font: "12px"} );

shapes.push( {x: 1010, y: 535, width: 160, height: 90, position: "Главный бухгалтер", is_manager: true, font: "14px"} );
shapes.push( {x: 1030, y: 640, width: 140, height: 40, position: "Бухгалтерия", font: "12px"} );

shapes.push( {x: 1200, y: 170, width: 160, height: 90, position: "Начальник ОТК", is_manager: true, font: "14px"} );
shapes.push( {x: 1220, y: 275, width: 140, height: 40, position: "ВТК", font: "12px"} );
shapes.push( {x: 1220, y: 330, width: 140, height: 40, position: "ЦЗЛ", font: "12px"} );
shapes.push( {x: 1220, y: 385, width: 140, height: 40, position: "Служба /n метролога", font: "12px"} );

shapes.push( {x: 1220, y: 455, width: 140, height: 40, position: "Канцелярия", font: "12px"} );
shapes.push( {x: 1220, y: 510, width: 140, height: 40, position: "1 отдел", font: "12px"} );
shapes.push( {x: 1220, y: 565, width: 140, height: 40, position: "2 отдел", font: "12px"} );
shapes.push( {x: 1220, y: 620, width: 140, height: 40, position: "ВОХР", font: "12px"} );
shapes.push( {x: 1220, y: 675, width: 140, height: 55, position: "Служба /n экономической /n безопасности", font: "12px"} );
shapes.push( {x: 1220, y: 745, width: 140, height: 40, position: "Юридическая /n служба", font: "12px"} );
shapes.push( {x: 1220, y: 800, width: 140, height: 40, position: "Отдел охраны /n труда", font: "12px"} );
shapes.push( {x: 1220, y: 855, width: 140, height: 40, position: "Отдел экологии", font: "12px"} );

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

base_url = `${window.location.hostname}:${window.location.port}`
        const websocket = new WebSocket(`ws://${base_url}`)
        websocket.onopen = function (event) {
            console.log('client says connection opened')
            websocket.send("Client sends Welcome")
        }
        websocket.onmessage = function (event) {
            message = JSON.parse(event.data)
            let position = message.position
            /* функция записи имён менеджеров в фигуры */
            for(let i=0;i < shapes.length; ++i) {
                shapes[i].manager_name = position[i]
            draw_shapes(event);
            draw_arrows();
            draw_lines();
            }
        }
/* Функция для переноса строк текста */
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
    context.clearRect(0, 0, canvas_width, canvas_height);
    context.textAlign = "center";
    context.fillStyle = "#8B959B";
    context.fillRect(0, 0, canvas_width, canvas_height);

    let rect = canvas.getBoundingClientRect();

    if (event) {
        startX = event.clientX - rect.left;
        startY = event.clientY - rect.top;
    };

    for (let shape of shapes) {
        /* проверка что указатель мыши находится в блоке, исходя из этого выбираем цвет блока */
        if (event) {
            if (shape.is_manager) {
                if (startX > shape.x && startX < shape.x + shape.width && startY > shape.y && startY < shape.y + shape.height) context.fillStyle = "#FFA24C";
                else context.fillStyle = "#E67A17";
            } else {
                if (startX > shape.x && startX < shape.x + shape.width && startY > shape.y && startY < shape.y + shape.height) context.fillStyle = "#FFF2E5";
                else context.fillStyle = "#F9D5B0";
            }
        } else {
            if (shape.is_manager) context.fillStyle = "#E67A17";
            else context.fillStyle = "#F9D5B0";
        }

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

/* функция обработки нажатия клавиши мыши */
let mouse_down = function(event) {
    let rect = canvas.getBoundingClientRect();
    let startX = event.clientX - rect.left;
    let startY = event.clientY - rect.top;

    let shape_id = 1;

    for (let shape of  shapes) {
        if (is_mouse_in_shape(startX, startY, shape)) {
            window.location = `/position/` + shape_id;
        };
        shape_id += 1;
    }
};

/* обработка движения мыши */
let mouse_move = function(event) {
    draw_shapes(event);
    draw_arrows();
    draw_lines();
}

canvas.onmousemove = mouse_move;
canvas.onmousedown = mouse_down;
document.addEventListener("dblclick",
            ()=>console.log("dblclick"));


