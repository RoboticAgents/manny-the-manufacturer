#copy this script from the Apps screen to make your own python apps

sequence = [

     # grabbing block one
     { "command": "a:+5","delay": 1.0  },
     { "command": "e:+20","delay": 1.0  },
     { "command": "f:+40","delay": 0  },
     { "command": "c:-20","delay": 1.0  },
     { "command": "b:-45","delay": 1.0  },
     { "command": "f:-70","delay": 2.0  },

     # lift up, put down in machine, go down and lift back up
     { "command": "b:+25","delay": 1.0  },
     { "command": "a:-15","delay": 1.0  },
     { "command": "b:-25","delay": 1.0  },
     { "command": "f:+70","delay": 2.0  },
     { "command": "b:+25","delay": 1.0  },
     { "command": "b:-25","delay": 1.0  },
     { "command": "f:-70","delay": 2.0  },
     { "command": "b:+25","delay": 1.0  },

     # put the block in the ending position
     { "command": "a:-18","delay": 1.0  },
     { "command": "b:-25","delay": 1.0  },
     { "command": "f:+70","delay": 2.0  },
     { "command": "b:+25","delay": 1.0  },

     # grab the second block
     { "command": "a:+48","delay": 1.0  },
     { "command": "c:-18","delay": 1.0  },
     { "command": "b:-35","delay": 1.0  },
     { "command": "f:-70","delay": 2.0  },

     # lift up, put down in machine, go down and lift back up
     { "command": "b:+35","delay": 1.0  },
     { "command": "a:-30","delay": 1.0  },
     { "command": "b:-35","delay": 1.0  },
     { "command": "f:+70","delay": 2.0  },
     { "command": "b:+35","delay": 1.0  },
     { "command": "b:-35","delay": 1.0  },
     { "command": "f:-70","delay": 2.0  },
     { "command": "b:+35","delay": 1.0  },

     # put the block in the ending position
     { "command": "a:-35","delay": 1.0  },
     { "command": "b:-35","delay": 1.0  },
     { "command": "f:+70","delay": 2.0  },
     { "command": "b:+35","delay": 1.0  },

     # go back to the middle
     { "command": "a:+35","delay": 1.0  },

     # Grab the front block
     { "command": "a:+25","delay": 1.0  },
     { "command": "x:-35","delay": 1.0  },
     { "command": "c:+35","delay": 1.0  },
     { "command": "b:-25","delay": 1.0  },
     { "command": "f:-70","delay": 2.0  },
     { "command": "b:+25","delay": 1.0  },

     # go to the machine
     { "command": "a:-30","delay": 1.0  },

     # put the block down, go up, go back down and grab it and go up
     { "command": "b:-25","delay": 1.0  },
     { "command": "f:+70","delay": 2.0  },
     { "command": "b:+25","delay": 1.0  },
     { "command": "b:-25","delay": 1.0  },
     { "command": "f:-70","delay": 2.0  },
     { "command": "b:+25","delay": 1.0  },

     # go to the ending position
     { "command": "a:-45","delay": 1.0  },
     { "command": "x:+20","delay": 1.0  },
     { "command": "b:-25","delay": 1.0  },
     { "command": "f:+70","delay": 2.0  },
     { "command": "b:+25","delay": 1.0  },

     # go back to the middle
     { "command": "a:+45","delay": 1.0  },

     # grab the last block
     { "command": "a:+50","delay": 1.0  },
     { "command": "c:-10","delay": 1.0  },
     { "command": "b:-25","delay": 1.0  },
     { "command": "f:-70","delay": 2.0  },
     { "command": "b:+25","delay": 1.0  },

     # go to the machine
     { "command": "a:-45","delay": 1.0  },

     # put the block down, go up, go back down and grab it and go up
     { "command": "b:-25","delay": 1.0  },
     { "command": "f:+70","delay": 2.0  },
     { "command": "b:+25","delay": 1.0  },
     { "command": "b:-25","delay": 1.0  },
     { "command": "f:-70","delay": 2.0  },
     { "command": "b:+25","delay": 1.0  },

     # go to the ending position
     { "command": "a:-20","delay": 1.0  },
     { "command": "x:-35","delay": 1.0  },
     { "command": "b:-25","delay": 1.0  },
     { "command": "f:+70","delay": 2.0  },
     { "command": "b:+25","delay": 1.0  },
     
     # go to the machine
     { "command": "a:+20","delay": 1.0  },
     

]
