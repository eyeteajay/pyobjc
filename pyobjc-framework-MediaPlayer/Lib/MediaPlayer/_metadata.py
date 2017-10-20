# This file is generated by objective.metadata
#
# Last update: Fri Oct 20 14:31:45 2017

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$MPErrorDomain$MPLanguageOptionCharacteristicContainsOnlyForcedSubtitles$MPLanguageOptionCharacteristicDescribesMusicAndSound$MPLanguageOptionCharacteristicDescribesVideo$MPLanguageOptionCharacteristicDubbedTranslation$MPLanguageOptionCharacteristicEasyToRead$MPLanguageOptionCharacteristicIsAuxiliaryContent$MPLanguageOptionCharacteristicIsMainProgramContent$MPLanguageOptionCharacteristicLanguageTranslation$MPLanguageOptionCharacteristicTranscribesSpokenDialog$MPLanguageOptionCharacteristicVoiceOverTranslation$MPMediaEntityPropertyPersistentID$MPMediaItemPropertyAlbumArtist$MPMediaItemPropertyAlbumArtistPersistentID$MPMediaItemPropertyAlbumPersistentID$MPMediaItemPropertyAlbumTitle$MPMediaItemPropertyAlbumTrackCount$MPMediaItemPropertyAlbumTrackNumber$MPMediaItemPropertyArtist$MPMediaItemPropertyArtistPersistentID$MPMediaItemPropertyArtwork$MPMediaItemPropertyAssetURL$MPMediaItemPropertyBeatsPerMinute$MPMediaItemPropertyBookmarkTime$MPMediaItemPropertyComments$MPMediaItemPropertyComposer$MPMediaItemPropertyComposerPersistentID$MPMediaItemPropertyDateAdded$MPMediaItemPropertyDiscCount$MPMediaItemPropertyDiscNumber$MPMediaItemPropertyGenre$MPMediaItemPropertyGenrePersistentID$MPMediaItemPropertyHasProtectedAsset$MPMediaItemPropertyIsCloudItem$MPMediaItemPropertyIsCompilation$MPMediaItemPropertyIsExplicit$MPMediaItemPropertyLastPlayedDate$MPMediaItemPropertyLyrics$MPMediaItemPropertyMediaType$MPMediaItemPropertyPersistentID$MPMediaItemPropertyPlayCount$MPMediaItemPropertyPlaybackDuration$MPMediaItemPropertyPodcastPersistentID$MPMediaItemPropertyPodcastTitle$MPMediaItemPropertyRating$MPMediaItemPropertyReleaseDate$MPMediaItemPropertySkipCount$MPMediaItemPropertyTitle$MPMediaItemPropertyUserGrouping$MPNowPlayingInfoCollectionIdentifier$MPNowPlayingInfoPropertyAssetURL$MPNowPlayingInfoPropertyAvailableLanguageOptions$MPNowPlayingInfoPropertyChapterCount$MPNowPlayingInfoPropertyChapterNumber$MPNowPlayingInfoPropertyCurrentLanguageOptions$MPNowPlayingInfoPropertyCurrentPlaybackDate$MPNowPlayingInfoPropertyDefaultPlaybackRate$MPNowPlayingInfoPropertyElapsedPlaybackTime$MPNowPlayingInfoPropertyExternalContentIdentifier$MPNowPlayingInfoPropertyExternalUserProfileIdentifier$MPNowPlayingInfoPropertyIsLiveStream$MPNowPlayingInfoPropertyMediaType$MPNowPlayingInfoPropertyPlaybackProgress$MPNowPlayingInfoPropertyPlaybackQueueCount$MPNowPlayingInfoPropertyPlaybackQueueIndex$MPNowPlayingInfoPropertyPlaybackRate$'''
enums = '''$MPChangeLanguageOptionSettingNone@0$MPChangeLanguageOptionSettingNowPlayingItemOnly@1$MPChangeLanguageOptionSettingPermanent@2$MPMediaTypeAny@18446744073709551615$MPMediaTypeAnyAudio@255$MPMediaTypeAnyVideo@65280$MPMediaTypeAudioBook@4$MPMediaTypeAudioITunesU@8$MPMediaTypeHomeVideo@8192$MPMediaTypeMovie@256$MPMediaTypeMusic@1$MPMediaTypeMusicVideo@2048$MPMediaTypePodcast@2$MPMediaTypeTVShow@512$MPMediaTypeVideoITunesU@4096$MPMediaTypeVideoPodcast@1024$MPNowPlayingInfoLanguageOptionTypeAudible@0$MPNowPlayingInfoLanguageOptionTypeLegible@1$MPNowPlayingInfoMediaTypeAudio@1$MPNowPlayingInfoMediaTypeNone@0$MPNowPlayingInfoMediaTypeVideo@2$MPNowPlayingPlaybackStateInterrupted@4$MPNowPlayingPlaybackStatePaused@2$MPNowPlayingPlaybackStatePlaying@1$MPNowPlayingPlaybackStateStopped@3$MPNowPlayingPlaybackStateUnknown@0$MPRemoteCommandHandlerStatusCommandFailed@200$MPRemoteCommandHandlerStatusDeviceNotFound@120$MPRemoteCommandHandlerStatusNoActionableNowPlayingItem@110$MPRemoteCommandHandlerStatusNoSuchContent@100$MPRemoteCommandHandlerStatusSuccess@0$MPRepeatTypeAll@2$MPRepeatTypeOff@0$MPRepeatTypeOne@1$MPSeekCommandEventTypeBeginSeeking@0$MPSeekCommandEventTypeEndSeeking@1$MPShuffleTypeCollections@2$MPShuffleTypeItems@1$MPShuffleTypeOff@0$'''
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'MPChangeRepeatModeCommandEvent', b'preservesRepeatMode', {'retval': {'type': 'Z'}})
    r(b'MPChangeRepeatModeCommandEvent', b'setPreservesRepeatMode:', {'arguments': {2: {'type': 'Z'}}})
    r(b'MPChangeShuffleModeCommandEvent', b'preservesShuffleMode', {'retval': {'type': 'Z'}})
    r(b'MPChangeShuffleModeCommandEvent', b'setPreservesShuffleMode:', {'arguments': {2: {'type': 'Z'}}})
    r(b'MPContentItem', b'isContainer', {'retval': {'type': 'Z'}})
    r(b'MPContentItem', b'isExplicitContent', {'retval': {'type': 'Z'}})
    r(b'MPContentItem', b'isPlayable', {'retval': {'type': 'Z'}})
    r(b'MPContentItem', b'isStreamingContent', {'retval': {'type': 'Z'}})
    r(b'MPContentItem', b'setContainer:', {'arguments': {2: {'type': 'Z'}}})
    r(b'MPContentItem', b'setExplicitContent:', {'arguments': {2: {'type': 'Z'}}})
    r(b'MPContentItem', b'setPlayable:', {'arguments': {2: {'type': 'Z'}}})
    r(b'MPContentItem', b'setStreamingContent:', {'arguments': {2: {'type': 'Z'}}})
    r(b'MPFeedbackCommand', b'isActive', {'retval': {'type': 'Z'}})
    r(b'MPFeedbackCommand', b'setActive:', {'arguments': {2: {'type': 'Z'}}})
    r(b'MPFeedbackCommandEvent', b'isNegative', {'retval': {'type': 'Z'}})
    r(b'MPFeedbackCommandEvent', b'setNegative:', {'arguments': {2: {'type': 'Z'}}})
    r(b'MPMediaEntity', b'canFilterByProperty:', {'retval': {'type': 'Z'}})
    r(b'MPMediaEntity', b'enumerateValuesForProperties:usingBlock:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}, 3: {'type': b'o^Z'}}}}}})
    r(b'MPMediaEntity', b'enumerateValuesForProperties:usingBlock::', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}, 3: {'type': b'o^Z'}}}}}})
    r(b'MPMediaItem', b'hasProtectedAsset', {'retval': {'type': 'Z'}})
    r(b'MPMediaItem', b'isCloudItem', {'retval': {'type': 'Z'}})
    r(b'MPMediaItem', b'isCompilation', {'retval': {'type': 'Z'}})
    r(b'MPMediaItem', b'isExplicitItem', {'retval': {'type': 'Z'}})
    r(b'MPMediaItem', b'setCloudItem:', {'arguments': {2: {'type': 'Z'}}})
    r(b'MPMediaItem', b'setCompilation:', {'arguments': {2: {'type': 'Z'}}})
    r(b'MPMediaItem', b'setExplicitItem:', {'arguments': {2: {'type': 'Z'}}})
    r(b'MPMediaItem', b'setHasProtectedAsset:', {'arguments': {2: {'type': 'Z'}}})
    r(b'MPMediaItemArtwork', b'initWithBoundsSize:requestHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'@'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': sel32or64(b'{CGSize=ff}', b'{CGSize=dd}')}}}}}})
    r(b'MPNowPlayingInfoLanguageOption', b'isAutomaticAudibleLanguageOption', {'retval': {'type': 'Z'}})
    r(b'MPNowPlayingInfoLanguageOption', b'isAutomaticLegibleLanguageOption', {'retval': {'type': 'Z'}})
    r(b'MPNowPlayingInfoLanguageOptionGroup', b'allowEmptySelection', {'retval': {'type': 'Z'}})
    r(b'MPNowPlayingInfoLanguageOptionGroup', b'initWithLanguageOptions:defaultLanguageOption:allowEmptySelection:', {'arguments': {4: {'type': 'Z'}}})
    r(b'MPNowPlayingInfoLanguageOptionGroup', b'setAllowEmptySelection:', {'arguments': {2: {'type': 'Z'}}})
    r(b'MPPlayableContentManagerContext', b'contentLimitsEnabled', {'retval': {'type': 'Z'}})
    r(b'MPPlayableContentManagerContext', b'contentLimitsEnforced', {'retval': {'type': 'Z'}})
    r(b'MPPlayableContentManagerContext', b'endpointAvailable', {'retval': {'type': 'Z'}})
    r(b'MPPlayableContentManagerContext', b'setContentLimitsEnabled:', {'arguments': {2: {'type': 'Z'}}})
    r(b'MPPlayableContentManagerContext', b'setContentLimitsEnforced:', {'arguments': {2: {'type': 'Z'}}})
    r(b'MPPlayableContentManagerContext', b'setEndpointAvailable:', {'arguments': {2: {'type': 'Z'}}})
    r(b'MPRemoteCommand', b'addTargetWithHandler:', {'arguments': {2: {'callable': {'retval': {'type': sel32or64(b'i', b'q')}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'MPRemoteCommand', b'isEnabled', {'retval': {'type': 'Z'}})
    r(b'MPRemoteCommand', b'setEnabled:', {'arguments': {2: {'type': 'Z'}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
