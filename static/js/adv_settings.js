$(document).ready(function () {
    var manual_choice = document.getElementById('id_choice_2');

    function move_sound_widget(e) {
        var sound_widget = document.getElementById('id_sound_level');
        if (this.checked) {
            this.parentNode.parentNode.appendChild(sound_widget);
            sound_widget.type = 'input';
            sound_widget.style.display = "inline-block";
        }
    };

    move_sound_widget.call(manual_choice);

    $('#id_choice_2').click(function (e) {
        move_sound_widget.call(this)
    });

    $('#id_choice_1').click(function (e) {
        $('#id_sound_level').hide()
    });

    $('#id_choice_0').click(function (e) {
        $('#id_sound_level').hide()
    });
});
