## API 가이드

1. Accounts

   - Signup

     > - URL : '/rest-auth/registration/'
     >
     > -  request
     >
     >   ```js
     >   body : {
     >     username: "hwang0",
     >     password1: "sdfsdf123",
     >     password2: "sdfsdf123",
     >   }
     >   ```
     >
     > - response
     >
     >   ![](./guide/auth.png)
     >
     > 

   - Login

     > - URL : '/rest-auth/login/'
     >
     > - request
     >
     >   ```js
     >   body : {
     >     username: "hwang0",
     >     password: "sdfsdf123",
     >   }
     >   ```
     >
     > - response
     >
     >   ![](./guide/auth.png)

   - UserDetail

     - get

       > - URL : '/accounts/:usename/'
       >
       > - response
       >
       >   ```js
       >   {
       >       "id": 2,
       >       "username": "hwang00",
       >       "profile_photo": null,
       >       "name": "",
       >       "gender": "",
       >       "description": "",
       >       "followers_count": 0,
       >       "following_count": 0
       >   }
       >   ```

     - put

     - delete

   - Follow

     - post

       >- URL : '/accounts/:usename/follow/'
       >
       >- request
       >
       >  ```js
       >  header: {
       >    Authorization: Token `${token}`
       >  }
       >  ```

   - UnFollow

     - post

       > - URL : '/accounts/:usename/unfollow/'
       >
       > - request
       >
       >   ```js
       >   header: {
       >     Authorization: Token `${token}`
       >   }
       >   ```

   - UserFollowers

     - get

       > - URL : '/accounts/:usename/followers/'
       >
       > - response
       >
       >   ```js
       >   [
       >       {
       >           "id": 2,
       >           "profile_photo": null,
       >           "username": "hwang00",
       >           "name": ""
       >       }
       >   ]
       >   ```

   - UserFollowings

     - get

       > - URL : '/accounts/:usename/followings/'
       >
       > - response
       >
       >   ```js
       >   [
       >       {
       >           "id": 1,
       >           "profile_photo": null,
       >           "username": "hwang0",
       >           "name": ""
       >       }
       >   ]
       >   ```
       >
       >   

2. Articles

   - Feed

     - get

       > - URL : '/articles/'
       >
       > - response
       >
       >   ![](./guide/feedList.png)

     - post

       > - URL : '/articles/'
       >
       > - request
       >
       >   ```js
       >   header: {
       >     Authorization: Token `${token}`
       >   },
       >   body : {
       >     content: "잘되는지 테스트 #완성",
       >     image: "hh.png",
       >     image: "스크린샷 2020-06-22 오후 4.27.46.png"
       >   }
       >   ```
       >
       > - response
       >
       >   ![](./guide/feedCreate.png)

   - FeedDetail

     - get

       > - URL : '/articles/:feed_pk'
       >
       > - response
       >
       >   ```js
       >   {
       >       "id": 5,
       >       "user": {
       >           "id": 1,
       >           "username": "hwang0",
       >           "profile_photo": null,
       >           "feed_set": [
       >               {
       >                   "id": 6,
       >                   "images": [
       >                       {
       >                           "image": "/media/feeds/2020/06/25/hwang0/iLLrvXhO.jpg"
       >                       },
       >                       {
       >                           "image": "/media/feeds/2020/06/25/hwang0/ndiDOAgq.jpg"
       >                       }
       >                   ],
       >                   "like_count": 0,
       >                   "comment_count": 0
       >               },
       >               {
       >                   "id": 5,
       >                   "images": [
       >                       {
       >                           "image": "/media/feeds/2020/06/25/hwang0/hELlPyko.jpg"
       >                       },
       >                       {
       >                           "image": "/media/feeds/2020/06/25/hwang0/iMwAlsLj.jpg"
       >                       }
       >                   ],
       >                   "like_count": 0,
       >                   "comment_count": 0
       >               },
       >               {
       >                   "id": 4,
       >                   "images": [
       >                       {
       >                           "image": "/media/feeds/2020/06/25/hwang0/eTxITEed.jpg"
       >                       },
       >                       {
       >                           "image": "/media/feeds/2020/06/25/hwang0/SBUonIyT.jpg"
       >                       }
       >                   ],
       >                   "like_count": 0,
       >                   "comment_count": 0
       >               },
       >               {
       >                   "id": 3,
       >                   "images": [
       >                       {
       >                           "image": "/media/feeds/2020/06/25/hwang0/bnTlNiMQ.jpg"
       >                       },
       >                       {
       >                           "image": "/media/feeds/2020/06/25/hwang0/pcOwrfjq.jpg"
       >                       }
       >                   ],
       >                   "like_count": 0,
       >                   "comment_count": 0
       >               },
       >               {
       >                   "id": 2,
       >                   "images": [],
       >                   "like_count": 0,
       >                   "comment_count": 0
       >               },
       >               {
       >                   "id": 1,
       >                   "images": [],
       >                   "like_count": 0,
       >                   "comment_count": 0
       >               }
       >           ]
       >       },
       >       "content": "잘되네 ㅋㅋㅋㅋ 다행이다 다행! #재성화이팅 #종우화이팅 #커피빵화이팅",
       >       "images": [
       >           {
       >               "image": "/media/feeds/2020/06/25/hwang0/hELlPyko.jpg"
       >           },
       >           {
       >               "image": "/media/feeds/2020/06/25/hwang0/iMwAlsLj.jpg"
       >           }
       >       ],
       >       "comments": [],
       >       "comment_count": 0,
       >       "tags": [
       >           {
       >               "name": "재성화이팅"
       >           },
       >           {
       >               "name": "종우화이팅"
       >           },
       >           {
       >               "name": "커피빵화이팅"
       >           }
       >       ],
       >       "like_users": [],
       >       "like_count": 0,
       >       "created_at": "2020-06-25T05:00:43.558254Z",
       >       "updated_at": "2020-06-25T05:00:43.558300Z"
       >   }
       >   ```

     - put

       > - URL : '/articles/:feed_pk/'
       >
       > - request
       >
       >   ```js
       >   header: {
       >     Authorization: Token `${token}`
       >   },
       >   body : {
       >     content: "수정 잘되니? #잘됌",
       >   }
       >   ```
       >
       > - response
       >
       >   ```js
       >   {
       >       "id": 7,
       >       "user": {
       >           "id": 1,
       >           "username": "hwang0",
       >           "profile_photo": null,
       >           "feed_set": [
       >               {
       >                   "id": 9,
       >                   "images": [
       >                       {
       >                           "image": "/media/feeds/2020/06/26/hwang0/glimGUeV.jpg"
       >                       }
       >                   ],
       >                   "like_count": 0,
       >                   "comment_count": 0
       >               },
       >               {
       >                   "id": 8,
       >                   "images": [],
       >                   "like_count": 0,
       >                   "comment_count": 0
       >               },
       >               {
       >                   "id": 7,
       >                   "images": [
       >                       {
       >                           "image": "/media/feeds/2020/06/26/hwang0/rgIxwVrN.jpg"
       >                       },
       >                       {
       >                           "image": "/media/feeds/2020/06/26/hwang0/UfdlNQdi.jpg"
       >                       }
       >                   ],
       >                   "like_count": 1,
       >                   "comment_count": 1
       >               },
       >               {
       >                   "id": 6,
       >                   "images": [
       >                       {
       >                           "image": "/media/feeds/2020/06/25/hwang0/iLLrvXhO.jpg"
       >                       },
       >                       {
       >                           "image": "/media/feeds/2020/06/25/hwang0/ndiDOAgq.jpg"
       >                       }
       >                   ],
       >                   "like_count": 0,
       >                   "comment_count": 3
       >               },
       >               {
       >                   "id": 4,
       >                   "images": [
       >                       {
       >                           "image": "/media/feeds/2020/06/25/hwang0/eTxITEed.jpg"
       >                       },
       >                       {
       >                           "image": "/media/feeds/2020/06/25/hwang0/SBUonIyT.jpg"
       >                       }
       >                   ],
       >                   "like_count": 0,
       >                   "comment_count": 0
       >               },
       >               {
       >                   "id": 3,
       >                   "images": [
       >                       {
       >                           "image": "/media/feeds/2020/06/25/hwang0/bnTlNiMQ.jpg"
       >                       },
       >                       {
       >                           "image": "/media/feeds/2020/06/25/hwang0/pcOwrfjq.jpg"
       >                       }
       >                   ],
       >                   "like_count": 0,
       >                   "comment_count": 0
       >               }
       >           ]
       >       },
       >       "content": "수정 잘되니? #잘됌",
       >       "images": [
       >           {
       >               "image": "/media/feeds/2020/06/26/hwang0/rgIxwVrN.jpg"
       >           },
       >           {
       >               "image": "/media/feeds/2020/06/26/hwang0/UfdlNQdi.jpg"
       >           }
       >       ],
       >       "comments": [
       >           {
       >               "id": 4,
       >               "user": {
       >                   "id": 1,
       >                   "username": "hwang0",
       >                   "profile_photo": null
       >               },
       >               "content": "ㅋㅋㅋㅋ 잘되면 좋겠다 #정말루",
       >               "created_at": "2020-06-26T14:17:05.228530Z",
       >               "updated_at": "2020-06-26T14:17:05.228583Z"
       >           }
       >       ],
       >       "comment_count": 1,
       >       "tags": [
       >           {
       >               "name": "잘됌"
       >           }
       >       ],
       >       "like_users": [
       >           {
       >               "id": 2,
       >               "username": "hwang00",
       >               "profile_photo": null
       >           }
       >       ],
       >       "like_count": 1,
       >       "created_at": "2020-06-26T09:45:05.333533Z",
       >       "updated_at": "2020-06-26T14:21:56.663650Z"
       >   }
       >   ```
       >
       >   

     - delete

       > - URL : '/articles/:feed_pk/'
       >
       > - request
       >
       >   ```js
       >   header: {
       >     Authorization: Token `${token}`
       >   }
       >   ```

   - FeedComment

     - get

       > - URL : '/articles/:feed_pk/comments/'
       >
       > - response
       >
       >   ```js
       >   [
       >       {
       >           "id": 2,
       >           "user": {
       >               "id": 2,
       >               "username": "hwang00",
       >               "profile_photo": null
       >           },
       >           "content": "ㅋㅋㅋㅋㅋLCK화이팅",
       >           "created_at": "2020-06-25T08:10:45.068439Z",
       >           "updated_at": "2020-06-25T08:10:45.068612Z"
       >       },
       >       {
       >           "id": 1,
       >           "user": {
       >               "id": 2,
       >               "username": "hwang00",
       >               "profile_photo": null
       >           },
       >           "content": "좋아요 좋아",
       >           "created_at": "2020-06-25T08:10:23.545521Z",
       >           "updated_at": "2020-06-25T08:10:23.545578Z"
       >       }
       >   ]
       >   ```

     - post

       > - URL : '/articles/:feed_pk/comments/'
       >
       > - request
       >
       >   ```js
       >   header: {
       >     Authorization: Token `${token}`
       >   },
       >   body : {
       >     content: "세번째 댓글",
       >   }
       >   ```
       >
       > - response
       >
       >   ```js
       >   {
       >       "id": 3,
       >       "user": {
       >           "id": 2,
       >           "username": "hwang00",
       >           "profile_photo": null
       >       },
       >       "content": "세번째 댓글",
       >       "created_at": "2020-06-25T08:34:22.497141Z",
       >       "updated_at": "2020-06-25T08:34:22.497463Z"
       >   }
       >   ```

   - FeedCommentDetail

     - put

     - delete

       > - URL : '/articles/:feed_pk/comments/:comment_pk'
       >
       > - request
       >
       >   ```js
       >   headers: {
       >     Authorization: Token `${token}`
       >   }
       >   ```

   - FeedLike

     - post

       >
       >
       >- URL : '/articles/:feed_pk/like'
       >
       >- request
       >
       >  ```js
       >  headers: {
       >    Authorization: Token `${token}`
       >  }
       >  ```

   - FeedUnLike

     - post

       > - URL : '/articles/:feed_pk/unlike'
       >
       > - request
       >
       >   ```js
       >   headers: {
       >     Authorization: Token `${token}`
       >   }
       >   ```

   - FeedLikeUsers

     - get

       > - URL : '/articles/:feed_pk/likes'
       >
       > - response
       >
       >   ```js
       >   [
       >       {
       >           "id": 2,
       >           "profile_photo": null,
       >           "username": "hwang00",
       >           "name": ""
       >       }
       >   ]
       >   ```
       >
       >   



