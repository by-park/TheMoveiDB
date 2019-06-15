$(document).on('ready', function() {
  var slide = $('.slider-single');
  var slideTotal = slide.length - 1;
  var slideCurrent = -1;
    
  // 내가 필요한 변수
  const movie_area = document.querySelector('.slider-content');
    
  function slideInitial() {
    slide.addClass('proactivede');
    setTimeout(function() {
      slideRight();
    }, 500);
  }

  function slideRight() {
    if (slideCurrent < slideTotal) {
      slideCurrent++;
    } else {
      slideCurrent = 0;
    }

    if (slideCurrent > 0) {
      var preactiveSlide = slide.eq(slideCurrent - 1);
    } else {
      var preactiveSlide = slide.eq(slideTotal);
    }
    var activeSlide = slide.eq(slideCurrent);
    if (slideCurrent < slideTotal) {
      var proactiveSlide = slide.eq(slideCurrent + 1);
    } else {
      var proactiveSlide = slide.eq(0);

    }

    slide.each(function() {
      var thisSlide = $(this);
      if (thisSlide.hasClass('preactivede')) {
        thisSlide.removeClass('preactivede preactive active proactive').addClass('proactivede');
      }
      if (thisSlide.hasClass('preactive')) {
        thisSlide.removeClass('preactive active proactive proactivede').addClass('preactivede');
      }
    });
    preactiveSlide.removeClass('preactivede active proactive proactivede').addClass('preactive');
    activeSlide.removeClass('preactivede preactive proactive proactivede').addClass('active');
    proactiveSlide.removeClass('preactivede preactive active proactivede').addClass('proactive');
  }

  function slideLeft() {
    if (slideCurrent > 0) {
      slideCurrent--;
    } else {
      slideCurrent = slideTotal;
    }

    if (slideCurrent < slideTotal) {
      var proactiveSlide = slide.eq(slideCurrent + 1);
    } else {
      var proactiveSlide = slide.eq(0);
    }
    var activeSlide = slide.eq(slideCurrent);
    if (slideCurrent > 0) {
      var preactiveSlide = slide.eq(slideCurrent - 1);
    } else {
      var preactiveSlide = slide.eq(slideTotal);
    }
    slide.each(function() {
      var thisSlide = $(this);
      if (thisSlide.hasClass('proactivede')) {
        thisSlide.removeClass('preactive active proactive proactivede').addClass('preactivede');
      }
      if (thisSlide.hasClass('proactive')) {
        thisSlide.removeClass('preactivede preactive active proactive').addClass('proactivede');
      }
    });
    preactiveSlide.removeClass('preactivede active proactive proactivede').addClass('preactive');
    activeSlide.removeClass('preactivede preactive proactive proactivede').addClass('active');
    proactiveSlide.removeClass('preactivede preactive active proactivede').addClass('proactive');
  }
    
  function pushToDom(title, poster_url, movie_id, like_users){
        movie_area.innerHTML += `<div class="slider-single">
        <a href="https://themoveidb.herokuapp.com/movei/detail/${movie_id}"><img class="slider-single-image" src="${poster_url}" alt="movie_poster"/></a>
        <h1 class="slider-single-title">${title}</h1>
        <a class="slider-single-likes" href="javascript:void(0)">
        <i style="display:inline;" class="fa fa-heart"></i>
          <!-- <i style="display:inline;" class="far fa-heart"  onclick="javascript:myFunc(event); click_like(${movie_id});"></i> -->
          <p>${like_users}</p>
        </a>
      </div>`;
  }

  function searchAndPush(URL){
    const XHR = new XMLHttpRequest();
    XHR.open('GET', URL);
    XHR.send();

    XHR.addEventListener('load', (e) => {
        const rawData = e.target.response;
        console.log(rawData);
        const parsedData = JSON.parse(rawData);
        pushToDom(parsedData.title_ko, parsedData.poster_url, parsedData.id, parsedData.like_users.length);
      });
  }
                         
  var left = $('.slider-left');
  var right = $('.slider-right');
  left.on('click', function() {
    slide = $('.slider-single');
    slideTotal = slide.length - 1;
    slideLeft();
  });
  right.on('click', function() {
    // 내가 직접 수정한 부분 새로운 영화 데이터를 받아오는 곳    
    const URL = `https://themoveidb.herokuapp.com/api/v1/users/${current_user}/`; //movies/${random}
    searchAndPush(URL);
    slide = $('.slider-single');
    slideTotal = slide.length - 1;
    slideRight();
  });
  slideInitial();
  setInterval(function(){
    const URL = `https://themoveidb.herokuapp.com.io/api/v1/users/${current_user}/`; //movies/${random}
    searchAndPush(URL);
    slide = $('.slider-single');
    slideTotal = slide.length - 1;
    slideRight();  
  },40000);
});

