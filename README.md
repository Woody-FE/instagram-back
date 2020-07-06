## API 가이드

1. Accounts

   - Signup

     - post

       > - URL : '/rest-auth/registration/'
       >
       > - request
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

   - Login

     - post

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
       >       "username": "marrywill",
       >       "profile_photo": "/media/profiles/marrywill/VZNIPFN2UXRU1539215883729_kFMcned.jpg",
       >       "name": "인아",
       >       "gender": "male",
       >       "description": "잘돼?",
       >       "followings": [],
       >       "followers": [
       >           {
       >               "id": 3,
       >               "username": "marrywill0",
       >               "profile_photo": null
       >           }
       >       ],
       >       "followers_count": 1,
       >       "following_count": 0,
       >       "feed_set": [
       >           {
       >               "id": 2,
       >               "images": [
       >                   {
       >                       "id": 2,
       >                       "image": "/media/feeds/2020/07/06/marrywill/eHSnOvXT.jpg"
       >                   }
       >               ],
       >               "like_count": 0,
       >               "comment_count": 1
       >           },
       >           {
       >               "id": 1,
       >               "images": [
       >                   {
       >                       "id": 1,
       >                       "image": "/media/feeds/2020/07/06/marrywill/uVDwOhNf.jpg"
       >                   }
       >               ],
       >               "like_count": 1,
       >               "comment_count": 0
       >           }
       >       ]
       >   }
       >   ```
       
     - put
     
       > - URL : '/accounts/:usename/'
       >
       > - request
       >
       >   ```js
       >   header: {
       >     Authorization: Token `${token}`
       >   },
       >   body: {
       >     profile_photo: "GVG_085.png",
       >     name: "영인이",
       >     gender: "male",
       >     description: "0제로봇ㅋㅋㅋㅋ"
       >   }
       >   ```
       >
       > - response
       >
       >   ```js
       >   {
       >       "id": 3,
       >       "username": "marrywill0",
       >       "profile_photo": "/media/profiles/marrywill0/VZNIPFN2UXRU1539215883729.jpg",
       >       "name": "영인이",
       >       "gender": "male",
       >       "description": "0제로봇ㅋㅋㅋㅋ",
       >       "followings": [
       >         {
       >               "id": 2,
       >               "username": "marrywill",
       >               "profile_photo": "/media/profiles/marrywill/VZNIPFN2UXRU1539215883729_kFMcned.jpg"
       >           }
       >       ],
       >       "followers": [],
       >       "followers_count": 0,
       >       "following_count": 1,
       >       "feed_set": []
       >   }
       >   ```
       >   
     
     - delete
     
       > - URL : '/accounts/:username'
       >
       > - request
       >
       >   ```js
       >   header: {
     >     Authorization: Token `${token}`
       >   }
     >   ```
     
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
       >

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

2. Articles

   - Feeds

     - get

       > - URL : '/articles/'
       >
       > - response
       >
       >   ```js
       >   [
       >       {
       >           "id": 2,
       >           "user": {
       >               "id": 2,
       >               "username": "marrywill",
       >               "profile_photo": "/media/profiles/marrywill/VZNIPFN2UXRU1539215883729_kFMcned.jpg"
       >           },
       >           "content": "잘 만들어져요! #대박",
       >           "images": [
       >               {
       >                   "id": 2,
       >                   "image": "/media/feeds/2020/07/06/marrywill/eHSnOvXT.jpg"
       >               }
       >           ],
       >           "comments": [],
       >           "comment_count": 0,
       >           "tags": [
       >               {
       >                   "name": "대박"
       >               }
       >           ],
       >           "like_users": [],
       >           "like_count": 0,
       >           "created_at": "2020-07-06T13:48:01.892499Z",
       >           "updated_at": "2020-07-06T13:48:01.892558Z"
       >       },
       >       {
       >           "id": 1,
       >           "user": {
       >               "id": 2,
       >               "username": "marrywill",
       >               "profile_photo": "/media/profiles/marrywill/VZNIPFN2UXRU1539215883729_kFMcned.jpg"
       >           },
       >           "content": "황영준 #돼지",
       >           "images": [
       >               {
       >                   "id": 1,
       >                   "image": "/media/feeds/2020/07/06/marrywill/uVDwOhNf.jpg"
       >               }
       >           ],
       >           "comments": [],
       >           "comment_count": 0,
       >           "tags": [
       >               {
       >                   "name": "돼지"
       >               }
       >           ],
       >           "like_users": [],
       >           "like_count": 0,
       >           "created_at": "2020-07-06T05:35:09.269122Z",
       >           "updated_at": "2020-07-06T05:35:09.269167Z"
       >       }
       >   ]
       >   ```
       
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
       >     image: "스크린샷 2020-06-22 오후 4.27.46.png"
       >   }
       >   ```
       >
       > - response
       >
       >   ```js
       >   {
       >       "id": 2,
       >       "user": {
       >           "id": 2,
       >           "username": "marrywill",
       >           "profile_photo": "http://127.0.0.1:8000/media/profiles/marrywill/VZNIPFN2UXRU1539215883729_kFMcned.jpg"
       >       },
       >       "content": "잘되는지 테스트 #완성",
       >       "images": [
       >           {
       >               "id": 2,
       >               "image": "http://127.0.0.1:8000/media/feeds/2020/07/06/marrywill/eHSnOvXT.jpg"
       >           }
       >       ],
       >       "comments": [],
       >       "comment_count": 0,
       >       "tags": [
       >           {
       >               "name": "완성"
       >           }
       >       ],
       >       "like_users": [],
       >       "like_count": 0,
       >       "created_at": "2020-07-06T13:48:01.892499Z",
       >       "updated_at": "2020-07-06T13:48:01.892558Z"
       >   }
       >   ```
   - FeedDetail

     - get

       > - URL : '/articles/:feed_pk/'
       >
       > - response
       >
       >   ```js
       >   {
       >       "id": 2,
       >       "user": {
       >           "id": 2,
       >           "username": "marrywill",
       >           "profile_photo": "/media/profiles/marrywill/VZNIPFN2UXRU1539215883729_kFMcned.jpg",
       >           "followers": [
       >               3
       >           ],
       >           "feed_set": [
       >               {
       >                   "id": 2,
       >                   "images": [
       >                       {
       >                           "id": 2,
       >                           "image": "/media/feeds/2020/07/06/marrywill/eHSnOvXT.jpg"
       >                       }
       >                   ],
       >                   "like_count": 1,
       >                   "comment_count": 1
       >               },
       >               {
       >                   "id": 1,
       >                   "images": [
       >                       {
       >                           "id": 1,
       >                           "image": "/media/feeds/2020/07/06/marrywill/uVDwOhNf.jpg"
       >                       }
       >                   ],
       >                   "like_count": 1,
       >                   "comment_count": 0
       >               }
       >           ]
       >       },
       >       "content": "잘 만들어져요! #대박",
       >       "images": [
       >           {
       >               "id": 2,
       >               "image": "/media/feeds/2020/07/06/marrywill/eHSnOvXT.jpg"
       >           }
       >       ],
       >       "comments": [
       >           {
       >               "id": 1,
       >               "user": {
       >                   "id": 2,
       >                   "username": "marrywill",
       >                   "profile_photo": "/media/profiles/marrywill/VZNIPFN2UXRU1539215883729_kFMcned.jpg"
       >               },
       >               "content": "좋아요 대박 좋아요!",
       >               "like_users": [],
       >               "comment_like_count": 0,
       >               "created_at": "2020-07-06T13:50:41.547201Z",
       >               "updated_at": "2020-07-06T13:50:41.547239Z"
       >           }
       >       ],
       >       "comment_count": 1,
       >       "tags": [
       >           {
       >               "name": "대박"
       >           }
       >       ],
       >       "like_users": [
       >           {
       >               "id": 2,
       >               "username": "marrywill",
       >               "profile_photo": "/media/profiles/marrywill/VZNIPFN2UXRU1539215883729_kFMcned.jpg"
       >           }
       >       ],
       >       "like_count": 1,
       >       "created_at": "2020-07-06T13:48:01.892499Z",
       >       "updated_at": "2020-07-06T13:48:01.892558Z"
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
       >   content: "수정 대박 잘돼 ㅋㅋㅋㅋㅋ #잘됌",
       >   }
       >   ```
       >
       > - response
       >
       >   ```js
       >   {
       >       "id": 2,
       >       "user": {
       >           "id": 2,
       >           "username": "marrywill",
       >           "profile_photo": "/media/profiles/marrywill/VZNIPFN2UXRU1539215883729_kFMcned.jpg",
       >           "followers": [
       >               3
       >           ],
       >           "feed_set": [
       >               {
       >                   "id": 2,
       >                   "images": [
       >                       {
       >                           "id": 2,
       >                           "image": "/media/feeds/2020/07/06/marrywill/eHSnOvXT.jpg"
       >                       }
       >                   ],
       >                   "like_count": 1,
       >                   "comment_count": 1
       >               },
       >               {
       >                   "id": 1,
       >                   "images": [
       >                       {
       >                           "id": 1,
       >                           "image": "/media/feeds/2020/07/06/marrywill/uVDwOhNf.jpg"
       >                       }
       >                   ],
       >                   "like_count": 1,
       >                   "comment_count": 0
       >               }
       >           ]
       >       },
       >       "content": "수정 대박 잘돼 ㅋㅋㅋㅋㅋ #잘됌",
       >       "images": [
       >           {
       >               "id": 2,
       >               "image": "/media/feeds/2020/07/06/marrywill/eHSnOvXT.jpg"
       >           }
       >       ],
       >       "comments": [
       >           {
       >               "id": 1,
       >               "user": {
       >                   "id": 2,
       >                   "username": "marrywill",
       >                   "profile_photo": "/media/profiles/marrywill/VZNIPFN2UXRU1539215883729_kFMcned.jpg"
       >               },
       >               "content": "좋아요 대박 좋아요!",
       >               "like_users": [],
       >               "comment_like_count": 0,
       >               "created_at": "2020-07-06T13:50:41.547201Z",
       >               "updated_at": "2020-07-06T13:50:41.547239Z"
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
       >               "username": "marrywill",
       >               "profile_photo": "/media/profiles/marrywill/VZNIPFN2UXRU1539215883729_kFMcned.jpg"
       >           }
       >       ],
       >       "like_count": 1,
       >       "created_at": "2020-07-06T13:48:01.892499Z",
       >       "updated_at": "2020-07-06T14:04:50.725389Z"
       >   }
       >   ```
     
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
       >           "id": 1,
       >           "user": {
       >               "id": 2,
       >               "username": "marrywill",
       >               "profile_photo": "/media/profiles/marrywill/VZNIPFN2UXRU1539215883729_kFMcned.jpg"
       >           },
       >           "content": "좋아요 대박 좋아요!",
       >           "like_users": [],
       >           "comment_like_count": 0,
       >           "created_at": "2020-07-06T13:50:41.547201Z",
       >           "updated_at": "2020-07-06T13:50:41.547239Z"
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
       >     content: "좋아요 대박 좋아요!",
       >   }
       >   ```
       >
       > - response
       >
       >   ```js
       >   {
       >       "id": 1,
       >       "user": {
       >           "id": 2,
       >           "username": "marrywill",
       >           "profile_photo": "/media/profiles/marrywill/VZNIPFN2UXRU1539215883729_kFMcned.jpg"
       >       },
     >       "content": "좋아요 대박 좋아요!",
       >       "like_users": [],
     >       "comment_like_count": 0,
       >       "created_at": "2020-07-06T13:50:41.547201Z",
       >       "updated_at": "2020-07-06T13:50:41.547239Z"
       >   }
       >   ```
     
   - FeedCommentDetail

     - put

     - delete

       > - URL : '/articles/:feed_pk/comments/:comment_pk/'
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

       >- URL : '/articles/:feed_pk/like/'
       >
       >- request
       >
       >```js
       >headers: {
       >   Authorization: Token `${token}`
       > }
       >```
     
   - FeedUnLike

     - post

       > - URL : '/articles/:feed_pk/unlike/'
       >
       > - request
       >
       >   ```js
       >   headers: {
       >     Authorization: Token `${token}`
       >   }
       >   ```

   - FeedCommentLike

     - post

       > - URL : '/articles/:feed_pk/comments/:comment_pk/like/'
       >
       > - request
       >
       >   ```js
       >   headers: {
       >     Authorization: Token `${token}`
       >   }
       >   ```

   - FeedCommentUnLike

     - post

       > - URL :  '/articles/:feed_pk/comments/:comment_pk/unlike/'
       >
       > - request
       >
       >   ```js
       >   headers: {
       >     Authorization: Token `${token}`
       >   }
       >   ```