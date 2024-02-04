let canvas = document.getElementById("canvas");
let context = canvas.getContext("2d");


canvas.width = 1440;
//canvas.width = window.innerWidth;
//canvas.width = window.innerWidth;
canvas.height = 1000;

console.log(canvas.width);
let canvas_width = canvas.width;
let canvas_height = canvas.height;
let shapes = [];
let lines = [];
let arrows = [];

shapes.push({x: 570, y: 40, width: 300, height: 90, text: "Руководитель /n /n Водоворотов П.А.", is_manager: true, font: "20px"});

shapes.push( {x: 50, y: 190, width: 160, height: 90, text: "Директор по /n стратегическому /n планированию /n Водоворотов П.А.", is_manager: true, font: "14px"} );
shapes.push( {x: 70, y: 295, width: 140, height: 40, text: "Экспериментальный /n участок", font: "12px"} );
shapes.push( {x: 70, y: 350, width: 140, height: 55, text: "Отдел /n финансового /n планирования", font: "12px"} );
shapes.push( {x: 70, y: 420, width: 140, height: 40, text: "Служба /n маркетинга", font: "12px"} );

shapes.push( {x: 230, y: 190, width: 160, height: 90, text: "Директор по /n персоналу /n Водоворотов П.А.", is_manager: true, font: "14px"} );
shapes.push( {x: 250, y: 295, width: 140, height: 40, text: "Отдел кадров", font: "12px"} );
shapes.push( {x: 250, y: 350, width: 140, height: 40, text: "Табельное бюро", font: "12px"} );
shapes.push( {x: 250, y: 405, width: 140, height: 40, text: "Отдел обучения", font: "12px"} );
shapes.push( {x: 250, y: 460, width: 140, height: 40, text: "Бытовой отдел", font: "12px"} );

shapes.push( {x: 510, y: 190, width: 500, height: 70, text: "Исполнительный директор /n /n Водоворотов П.А.", is_manager: true, font: "16px"} );

shapes.push( {x: 410, y: 320, width: 160, height: 90, text: "Заместитель /n директора /n по производству /n Водоворотов П.А.", is_manager: true, font: "14px"} );
shapes.push( {x: 430, y: 425, width: 140, height: 40, text: "Производственный /n цех 1", font: "12px"} );
shapes.push( {x: 430, y: 480, width: 140, height: 40, text: "Производственный /n цех 2", font: "12px"} );
shapes.push( {x: 430, y: 535, width: 140, height: 40, text: "Производственный /n цех 3", font: "12px"} );
shapes.push( {x: 430, y: 590, width: 140, height: 40, text: "Производственный /n цех 4", font: "12px"} );
shapes.push( {x: 430, y: 645, width: 140, height: 40, text: "Автотранспортный /n цех", font: "12px"} );
shapes.push( {x: 430, y: 700, width: 140, height: 40, text: "Служба снабжения", font: "12px"} );

shapes.push( {x: 590, y: 320, width: 160, height: 90, text: "Главный инженер", is_manager: true, font: "14px"} );
shapes.push( {x: 610, y: 425, width: 140, height: 40, text: "ОГЭ", font: "12px"} );
shapes.push( {x: 610, y: 480, width: 140, height: 40, text: "ОГМ", font: "12px"} );
shapes.push( {x: 610, y: 535, width: 140, height: 40, text: "АСУ", font: "12px"} );
shapes.push( {x: 610, y: 590, width: 140, height: 40, text: "Инструментальное /n производство", font: "12px"} );
shapes.push( {x: 610, y: 645, width: 140, height: 40, text: "ОКС", font: "12px"} );

shapes.push( {x: 770, y: 320, width: 160, height: 90, text: "Коммерческий /n директор", is_manager: true, font: "14px"} );
shapes.push( {x: 790, y: 425, width: 140, height: 40, text: "Отдел сбыта", font: "12px"} );
shapes.push( {x: 790, y: 480, width: 140, height: 40, text: "Складское хозяйство", font: "12px"} );
shapes.push( {x: 790, y: 535, width: 140, height: 40, text: "Финансовый отдел", font: "12px"} );
shapes.push( {x: 790, y: 590, width: 140, height: 40, text: "Собственный /n транспорт", font: "12px"} );
shapes.push( {x: 790, y: 645, width: 140, height: 55, text: "Производственно -/n коммерческая /n фирма", font: "12px"} );

shapes.push( {x: 950, y: 320, width: 160, height: 90, text: "Главный экономист", is_manager: true, font: "14px"} );
shapes.push( {x: 970, y: 425, width: 140, height: 40, text: "ПЭО", font: "12px"} );
shapes.push( {x: 970, y: 480, width: 140, height: 40, text: "ОТиЗ", font: "12px"} );

shapes.push( {x: 1010, y: 555, width: 160, height: 90, text: "Главный бухгалтер", is_manager: true, font: "14px"} );
shapes.push( {x: 1030, y: 660, width: 140, height: 40, text: "Бухгалтерия", font: "12px"} );

shapes.push( {x: 1200, y: 190, width: 160, height: 90, text: "Начальник ОТК", is_manager: true, font: "14px"} );
shapes.push( {x: 1220, y: 295, width: 140, height: 40, text: "ВТК", font: "12px"} );
shapes.push( {x: 1220, y: 350, width: 140, height: 40, text: "ЦЗЛ", font: "12px"} );
shapes.push( {x: 1220, y: 405, width: 140, height: 40, text: "Служба /n метролога", font: "12px"} );

shapes.push( {x: 1220, y: 475, width: 140, height: 40, text: "Канцелярия", font: "12px"} );
shapes.push( {x: 1220, y: 530, width: 140, height: 40, text: "1 отдел", font: "12px"} );
shapes.push( {x: 1220, y: 585, width: 140, height: 40, text: "2 отдел", font: "12px"} );
shapes.push( {x: 1220, y: 640, width: 140, height: 40, text: "ВОХР", font: "12px"} );
shapes.push( {x: 1220, y: 695, width: 140, height: 55, text: "Служба /n экономической /n безопасности", font: "12px"} );
shapes.push( {x: 1220, y: 765, width: 140, height: 40, text: "Юридическая /n служба", font: "12px"} );
shapes.push( {x: 1220, y: 820, width: 140, height: 40, text: "Отдел охраны /n труда", font: "12px"} );
shapes.push( {x: 1220, y: 875, width: 140, height: 40, text: "Отдел экологии", font: "12px"} );

/* lines */
lines.push( {mt_x: 130, mt_y: 160, lt_x: 1390, lt_y: 160} );
lines.push( {mt_x: 490, mt_y: 290, lt_x: 1030, lt_y: 290} );
lines.push( {mt_x: 1390, mt_y: 160, lt_x: 1390, lt_y: 895} );
lines.push( {mt_x: 50, mt_y: 280, lt_x: 50, lt_y: 440} );
lines.push( {mt_x: 230, mt_y: 280, lt_x: 230, lt_y: 480} );
lines.push( {mt_x: 410, mt_y: 410, lt_x: 410, lt_y: 720} );
lines.push( {mt_x: 590, mt_y: 410, lt_x: 590, lt_y: 665} );
lines.push( {mt_x: 770, mt_y: 410, lt_x: 770, lt_y: 672} );
lines.push( {mt_x: 950, mt_y: 410, lt_x: 950, lt_y: 500} );
lines.push( {mt_x: 1010, mt_y: 645, lt_x: 1010, lt_y: 680} );
lines.push( {mt_x: 1200, mt_y: 280, lt_x: 1200, lt_y: 425} );

/* arrow */
arrows.push( {mt_x: 720, mt_y: 130, rotate: 0, arrow_length: 30} );
arrows.push( {mt_x: 130, mt_y: 160, rotate: 0, arrow_length: 30} );
arrows.push( {mt_x: 310, mt_y: 160, rotate: 0, arrow_length: 30} );
arrows.push( {mt_x: 760, mt_y: 160, rotate: 0, arrow_length: 30} );
arrows.push( {mt_x: 1280, mt_y: 160, rotate: 0, arrow_length: 30} );
arrows.push( {mt_x: 760, mt_y: 260, rotate: 0, arrow_length: 30} );
arrows.push( {mt_x: 490, mt_y: 290, rotate: 0, arrow_length: 30} );
arrows.push( {mt_x: 670, mt_y: 290, rotate: 0, arrow_length: 30} );
arrows.push( {mt_x: 850, mt_y: 290, rotate: 0, arrow_length: 30} );
arrows.push( {mt_x: 1030, mt_y: 290, rotate: 0, arrow_length: 30} );
arrows.push( {mt_x: 1140, mt_y: 160, rotate: 0, arrow_length: 395} );

arrows.push( {mt_x: 50, mt_y: 320, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 50, mt_y: 377, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 50, mt_y: 440, rotate: 1, arrow_length: 20} );

arrows.push( {mt_x: 230, mt_y: 315, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 230, mt_y: 370, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 230, mt_y: 425, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 230, mt_y: 480, rotate: 1, arrow_length: 20} );

arrows.push( {mt_x: 410, mt_y: 445, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 410, mt_y: 500, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 410, mt_y: 555, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 410, mt_y: 610, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 410, mt_y: 665, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 410, mt_y: 720, rotate: 1, arrow_length: 20} );

arrows.push( {mt_x: 590, mt_y: 445, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 590, mt_y: 500, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 590, mt_y: 555, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 590, mt_y: 610, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 590, mt_y: 665, rotate: 1, arrow_length: 20} );

arrows.push( {mt_x: 770, mt_y: 445, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 770, mt_y: 500, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 770, mt_y: 555, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 770, mt_y: 610, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 770, mt_y: 672, rotate: 1, arrow_length: 20} );

arrows.push( {mt_x: 950, mt_y: 445, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 950, mt_y: 500, rotate: 1, arrow_length: 20} );

arrows.push( {mt_x: 1010, mt_y: 680, rotate: 1, arrow_length: 20} );

arrows.push( {mt_x: 1200, mt_y: 322, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 1200, mt_y: 370, rotate: 1, arrow_length: 20} );
arrows.push( {mt_x: 1200, mt_y: 425, rotate: 1, arrow_length: 20} );

arrows.push( {mt_x: 1390, mt_y: 495, rotate: 2, arrow_length: 30} );
arrows.push( {mt_x: 1390, mt_y: 550, rotate: 2, arrow_length: 30} );
arrows.push( {mt_x: 1390, mt_y: 605, rotate: 2, arrow_length: 30} );
arrows.push( {mt_x: 1390, mt_y: 660, rotate: 2, arrow_length: 30} );
arrows.push( {mt_x: 1390, mt_y: 722, rotate: 2, arrow_length: 30} );
arrows.push( {mt_x: 1390, mt_y: 785, rotate: 2, arrow_length: 30} );
arrows.push( {mt_x: 1390, mt_y: 840, rotate: 2, arrow_length: 30} );
arrows.push( {mt_x: 1390, mt_y: 895, rotate: 2, arrow_length: 30} );



/* Функция для переноса строк текста */
function wrapText(context, shape)
    {
        var lines = shape.text.split("/n");
        var countLines = lines.length;
        context.textBaseline = "middle";
        if (countLines == 1) {
            context.fillText(shape.text, shape.x + shape.width/2, shape.y + shape.height/2);
        }
        else {            
            for (var n = 0; n < countLines; n++) {
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

    if (event) {
        var rect = canvas.getBoundingClientRect();
        let startX = event.clientX - rect.left;
        let startY = event.clientY - rect.top;

        for (let shape of shapes) {
        if (shape.is_manager) {
            if (startX > shape.x && startX < shape.x + shape.width && startY > shape.y && startY < shape.y + shape.height) {context.fillStyle = "#FFA24C";}
            else context.fillStyle = "#E67A17";
        }
        else {
            if (startX > shape.x && startX < shape.x + shape.width && startY > shape.y && startY < shape.y + shape.height) {context.fillStyle = "#FFF2E5";}
            else context.fillStyle = "#F9D5B0";
        }

        context.fillRect(shape.x, shape.y, shape.width, shape.height);
        context.fillStyle = "black";
        context.strokeRect(shape.x, shape.y, shape.width, shape.height);
        context.font = shape.font + " Arial";
        wrapText(context, shape);
    }
    }
    else {
        for (let shape of shapes) {
            if (shape.is_manager) {context.fillStyle = "#E67A17";}
            else {context.fillStyle = "#F9D5B0";}

            context.fillRect(shape.x, shape.y, shape.width, shape.height);
            context.fillStyle = "black";
            context.strokeRect(shape.x, shape.y, shape.width, shape.height);
            context.font = shape.font + " Arial";
            wrapText(context, shape);
        }
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

draw_shapes();
draw_lines();
draw_arrows();

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
    var rect = canvas.getBoundingClientRect();
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
