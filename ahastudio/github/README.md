# GitHub

<https://github.com/>

GitHub은 Git을 이용해 협력할 수 있도록 돕는 소셜 서비스입니다.

물론, 대부분은 그냥 저장소 및 웹 뷰어로 활용하죠.

GitHub을 이용하면 원격으로 접속 가능한 저장소를 확보할 수 있고,
이를 통해 협력을 시스템화(Pull Request)할 수 있습니다.

## 참고 자료

[소프트웨어 개발 Workflow for Team](http://j.mp/2Gqo9uA)

## Git 이전 커밋 표기법

<https://github.com/dataitgirls3/TIL/pull/135#discussion_r314199365>

## Branch & Pull Request

작업할 때 브랜치가 어떤 상태인지 볼 수 있는 저장소를 마련했습니다.

- 공용 저장소(upstream): <https://github.com/dal-lab/github-sample>
- 내 저장소(origin): <https://github.com/ahastudio/github-sample>

```
# 내 저장소를 Clone
git clone git@github.com:ahastudio/github-sample.git

# 작업 폴더로 이동
cd github-sample

# 공용 저장소를 추가
git remote add upstream git@github.com:dal-lab/github-sample.git

# 공용 저장소 정보 가져오기
git fetch upstream

# Sourcetree 등으로 그래프를 살펴봅시다!
```

![Screenshot](https://raw.githubusercontent.com/dataitgirls3/TIL/master/ahastudio/github/images/branch.jpg)
