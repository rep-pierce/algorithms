function friend(friends){
    let actualFriends = []
    friends.forEach(friend => {
      if (friend.length == 4){
        actualFriends.push(friend)
      }
    })
    return actualFriends
  }