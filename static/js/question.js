$('.answer').click(function(event){
var chosenId = event.target.id
var pk = $(`#${chosenId}`).data('pk')
var letter = $(`#${chosenId}`).data('letter')
var mbti = $(`#${chosenId}`).data('mbti')

$.ajax({
    url: '/ajax/',
    dataType: "json",
    type: "POST",
    data: {
    'pk': pk,
    'letter': letter,
    'mbti': mbti
    },
    success: function (data) {
    console.log('success')

    $('#question_no').text(data['question_pk'])
    $('#question').text(data['question'])
    $('#answer1').text(data['question_ans1'])
    $('#answer1').data('pk', data['question_pk'])
    $('#answer1').data('letter', data['question_letter1'])
    $('#answer1').data('mbti', data['mbti'])
    $('#answer2').text(data['question_ans2'])
    $('#answer2').data('pk', data['question_pk'])
    $('#answer2').data('letter', data['question_letter2'])
    $('#answer2').data('mbti', data['mbti'])
    },
    error: function (request, status, error) {
    console.log('finished')
    $("#main").css('display', 'none')
    $("#loader").css('display', 'block')
    mbti += letter
    setTimeout(() => {
        window.location.href = `/result/${mbti}`
    }, 3500)
    }
    });
})