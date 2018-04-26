# Server

## Setup

```sh
brew install mosquitto
brew services start mosquitto
brew install waon
```

## Pseudocode

### Primary code

* subscribe to mqtt topics `pi1/newfile` `pi2/newfile` on localhost.
	* On update, read wav file from upload directories,
		`~pi#/uploads/file.wav`, feed into waon, parse midi as json,
		pass into active module

### Module Code

* Accept source (pi1, pi2), and json of midi
* Decide what notes you want the pis to play (for the next while)
* Publish (70,3000) (midinote,milliseconds) style csv
  into `pi#/queue`

### Player code

(have one copy of this running for each pi)

* subscribe to `pi#/queue`
* read through one line at a time, send note, wait time, repeat
unless interrupted by updated queue
