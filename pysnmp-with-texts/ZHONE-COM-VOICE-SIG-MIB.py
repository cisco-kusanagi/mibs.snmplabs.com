#
# PySNMP MIB module ZHONE-COM-VOICE-SIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHONE-COM-VOICE-SIG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:47:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, iso, Integer32, ModuleIdentity, MibIdentifier, Bits, NotificationType, Counter32, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "Integer32", "ModuleIdentity", "MibIdentifier", "Bits", "NotificationType", "Counter32", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "ObjectIdentity")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
zhoneVoice, = mibBuilder.importSymbols("Zhone", "zhoneVoice")
zhoneVoiceSignalingMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7))
zhoneVoiceSignalingMib.setRevisions(('2004-10-21 14:51', '2000-10-10 18:05',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: zhoneVoiceSignalingMib.setRevisionsDescriptions(('V01.00.01 - Added endpoint specific object to voice-system', 'V01.00.00 - Initial Release',))
if mibBuilder.loadTexts: zhoneVoiceSignalingMib.setLastUpdated('200410211453Z')
if mibBuilder.loadTexts: zhoneVoiceSignalingMib.setOrganization('Zhone Technologies.')
if mibBuilder.loadTexts: zhoneVoiceSignalingMib.setContactInfo(' Postal: Zhone Technologies, Inc. @ Zhone Way 7001 Oakport Street Oakland, CA 94621 USA Toll-Free: +1 877-ZHONE20 (+1 877-946-6320) Tel: +1-510-777-7000 Fax: +1-510-777-7001 E-mail: support@zhone.com')
if mibBuilder.loadTexts: zhoneVoiceSignalingMib.setDescription('The Zhone Voice Signaling MIB defines Zhone Voice Signaling specfic information. This MIB contains system side voice specific info, like the hookflash timers. User will not create this profile, but when system comes up, it checks to see if the scalar info exists. If not, it creates one with default values.')
zhoneVoiceSignalingTimers = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1))
if mibBuilder.loadTexts: zhoneVoiceSignalingTimers.setStatus('current')
if mibBuilder.loadTexts: zhoneVoiceSignalingTimers.setDescription("This is a place holder to contain all the system wide voice specific timers. 'hookFlashTimerMin' field is read/write field so a user can set this field to a particular value. It specifies the minimum timer for hookflash. 'hookFlashTimerMax' field is a read/write field to a user can set this field to a particular value. It specifies the maximum timer for hookflash.")
hookFlashTimerMin = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hookFlashTimerMin.setStatus('current')
if mibBuilder.loadTexts: hookFlashTimerMin.setDescription('The Hookflash specifies the minimum timer that qualifies for a hookflash. Any loopopen below this time will be ignored as a glitch.')
hookFlashTimerMax = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(1550)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hookFlashTimerMax.setStatus('current')
if mibBuilder.loadTexts: hookFlashTimerMax.setDescription('The Hookflash specifies the maximum timer that qualifies for a hookflash. Any loopopen more than this timer will be considered as a onhook.')
sysPartialDialTo = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 3), Unsigned32().clone(16)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysPartialDialTo.setStatus('current')
if mibBuilder.loadTexts: sysPartialDialTo.setDescription('This object contains the maximum value of the partial dial time out.')
sysCriticalDialTo = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 4), Unsigned32().clone(4)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysCriticalDialTo.setStatus('current')
if mibBuilder.loadTexts: sysCriticalDialTo.setDescription('This object contains the maximum value of the critical \\ dial time out.')
sysBusyToneTo = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 5), Unsigned32().clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysBusyToneTo.setStatus('current')
if mibBuilder.loadTexts: sysBusyToneTo.setDescription('This object contains the default timeout value for busy tone.')
sysDialToneTo = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 6), Unsigned32().clone(16)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDialToneTo.setStatus('current')
if mibBuilder.loadTexts: sysDialToneTo.setDescription('This object contains the default timeout value for dial tone. ')
sysMsgWaitToneTo = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 7), Unsigned32().clone(16)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysMsgWaitToneTo.setStatus('current')
if mibBuilder.loadTexts: sysMsgWaitToneTo.setDescription('This object contains the default timeout value for message wait tone. ')
sysOffhookWarnToneTo = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 8), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysOffhookWarnToneTo.setStatus('current')
if mibBuilder.loadTexts: sysOffhookWarnToneTo.setDescription('This object contains the default timeout value for offhook warn tone. ')
sysRingingTo = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 9), Unsigned32().clone(180)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysRingingTo.setStatus('current')
if mibBuilder.loadTexts: sysRingingTo.setDescription('This object contains the default timeout value for ringing. ')
sysRingbackTo = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 10), Unsigned32().clone(180)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysRingbackTo.setStatus('current')
if mibBuilder.loadTexts: sysRingbackTo.setDescription('This object contains the default timeout value for ringback tone.')
sysReorderToneTo = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 11), Unsigned32().clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysReorderToneTo.setStatus('current')
if mibBuilder.loadTexts: sysReorderToneTo.setDescription('This object contains the default timeout value for reorder tone.')
sysStutterToneTo = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 12), Unsigned32().clone(16)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysStutterToneTo.setStatus('current')
if mibBuilder.loadTexts: sysStutterToneTo.setDescription('This object contains the default timeout value for stutter tone.')
sysServerMaxTimer = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 13), Unsigned32().clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysServerMaxTimer.setStatus('current')
if mibBuilder.loadTexts: sysServerMaxTimer.setDescription('This object is used as part of a retransmission algorithm when communicating with a call agent. This object contains the maximum time in seconds since the sending of the initial datagram to a call agent. If more than pktcNcsEndPntConfigTSMax time has elapsed, the endpoint becomes disconnected.')
sysConfigMax1 = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 14), Unsigned32().clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysConfigMax1.setStatus('current')
if mibBuilder.loadTexts: sysConfigMax1.setDescription('This object contains the suspicious error threshold for signaling messages. The configMax1 object indicates the retransmission threshold at which the gateway MAY actively query the domain name server (DNS) in order to detect the possible change of call agent interfaces.')
sysConfigMax2 = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 15), Unsigned32().clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysConfigMax2.setStatus('current')
if mibBuilder.loadTexts: sysConfigMax2.setDescription('This object contains the disconnect error threshold for signaling messages. The configMax2 object indicates the retransmission threshold at which the gateway SHOULD contact the DNS one more time to see if any other interfaces to the call agent have become available.')
sysMax1Enable = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 16), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysMax1Enable.setStatus('current')
if mibBuilder.loadTexts: sysMax1Enable.setDescription('This object enables/disables the Max1 domain name server (DNS) query operation when the configMax1 threshold has been reached.')
sysMax2Enable = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 17), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysMax2Enable.setStatus('current')
if mibBuilder.loadTexts: sysMax2Enable.setDescription('This object enables/disables the Max2 domain name server (DNS) query operation when the configMax2 threshold has been reached.')
sysMaxWaitingDelay = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 18), Unsigned32().clone(600)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysMaxWaitingDelay.setStatus('current')
if mibBuilder.loadTexts: sysMaxWaitingDelay.setDescription('Maximum Waiting Delay (MWD) contains the maximum number of seconds a Gateway waits after powering on, before initiating the restart procedure with the call agent.')
sysDisconnectWaitTimer = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 19), Unsigned32().clone(15)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDisconnectWaitTimer.setStatus('current')
if mibBuilder.loadTexts: sysDisconnectWaitTimer.setDescription('This object contains the initial number of seconds the gateway waits after a disconnect, before initiating the disconnected procedure with the call agent.')
sysDisconnectMinTimer = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 20), Unsigned32().clone(15)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDisconnectMinTimer.setStatus('current')
if mibBuilder.loadTexts: sysDisconnectMinTimer.setDescription('This object contains the minimum number of seconds the gatway waits after a disconnect, before initiating the disconnected procedure with the call agent.')
sysDisconnectMaxTimer = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 21), Unsigned32().clone(600)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDisconnectMaxTimer.setStatus('current')
if mibBuilder.loadTexts: sysDisconnectMaxTimer.setDescription('This object contains the maximum number of seconds the gatway waits after a disconnect, before initiating the disconnected procedure with the call agent.')
sysMaxRetransmitTimer = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 22), Unsigned32().clone(4)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysMaxRetransmitTimer.setStatus('current')
if mibBuilder.loadTexts: sysMaxRetransmitTimer.setDescription('This object contains the maximum number of seconds for the retransmission timer. When this timer expires the gateway retransmits the message.')
sysInitRetransmitTimer = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 23), Unsigned32().clone(200)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysInitRetransmitTimer.setStatus('current')
if mibBuilder.loadTexts: sysInitRetransmitTimer.setDescription('This object contains the initial number of seconds for the retransmission timer.')
sysKeepAliveTimer = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 24), Unsigned32().clone(60)).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysKeepAliveTimer.setStatus('current')
if mibBuilder.loadTexts: sysKeepAliveTimer.setDescription('Specifies a timeout value in minutes for sending long duration call notification message.')
sysNoResponseTimer = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 25), Unsigned32().clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysNoResponseTimer.setStatus('current')
if mibBuilder.loadTexts: sysNoResponseTimer.setDescription('Timeout period in seconds before no response is declared.')
sysCallWaitMaxRepeat = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 26), Unsigned32().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysCallWaitMaxRepeat.setStatus('current')
if mibBuilder.loadTexts: sysCallWaitMaxRepeat.setDescription('This object contains the default value of the maximum number of repetitions of the call waiting tone that the gateway will play.')
sysCallWaitDelay = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 27), Unsigned32().clone(10)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysCallWaitDelay.setStatus('current')
if mibBuilder.loadTexts: sysCallWaitDelay.setDescription('This object contains the delay between repetitions of the call waiting tone that the gateway will play.')
sysPulseInterDigitTimer = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 28), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(100, 1500)).clone(100)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysPulseInterDigitTimer.setStatus('current')
if mibBuilder.loadTexts: sysPulseInterDigitTimer.setDescription('This is the pulse dial inter-digit timeout.')
sysMinMakePulseWidth = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 29), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(20, 200)).clone(25)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysMinMakePulseWidth.setStatus('current')
if mibBuilder.loadTexts: sysMinMakePulseWidth.setDescription('This is the minimum make pulse width for the dial pulse.')
sysMaxMakePulseWidth = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 30), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(20, 200)).clone(55)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysMaxMakePulseWidth.setStatus('current')
if mibBuilder.loadTexts: sysMaxMakePulseWidth.setDescription('This is the maximum make pulse width for the dial pulse.')
sysMinBreakPulseWidth = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 31), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(20, 200)).clone(45)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysMinBreakPulseWidth.setStatus('current')
if mibBuilder.loadTexts: sysMinBreakPulseWidth.setDescription('This is the minimum break pulse width for the dial pulse.')
sysMaxBreakPulseWidth = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 32), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(20, 200)).clone(75)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysMaxBreakPulseWidth.setStatus('current')
if mibBuilder.loadTexts: sysMaxBreakPulseWidth.setDescription('This is the maximum break pulse width for the dial pulse.')
zhoneVoiceSignalingObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 33)).setObjects(("ZHONE-COM-VOICE-SIG-MIB", "sysPartialDialTo"), ("ZHONE-COM-VOICE-SIG-MIB", "sysCriticalDialTo"), ("ZHONE-COM-VOICE-SIG-MIB", "sysBusyToneTo"), ("ZHONE-COM-VOICE-SIG-MIB", "sysDialToneTo"), ("ZHONE-COM-VOICE-SIG-MIB", "sysMsgWaitToneTo"), ("ZHONE-COM-VOICE-SIG-MIB", "sysOffhookWarnToneTo"), ("ZHONE-COM-VOICE-SIG-MIB", "sysRingingTo"), ("ZHONE-COM-VOICE-SIG-MIB", "sysRingbackTo"), ("ZHONE-COM-VOICE-SIG-MIB", "sysReorderToneTo"), ("ZHONE-COM-VOICE-SIG-MIB", "sysStutterToneTo"), ("ZHONE-COM-VOICE-SIG-MIB", "sysServerMaxTimer"), ("ZHONE-COM-VOICE-SIG-MIB", "sysConfigMax1"), ("ZHONE-COM-VOICE-SIG-MIB", "sysConfigMax2"), ("ZHONE-COM-VOICE-SIG-MIB", "sysMax1Enable"), ("ZHONE-COM-VOICE-SIG-MIB", "sysMax2Enable"), ("ZHONE-COM-VOICE-SIG-MIB", "sysMaxWaitingDelay"), ("ZHONE-COM-VOICE-SIG-MIB", "sysDisconnectWaitTimer"), ("ZHONE-COM-VOICE-SIG-MIB", "sysDisconnectMinTimer"), ("ZHONE-COM-VOICE-SIG-MIB", "sysDisconnectMaxTimer"), ("ZHONE-COM-VOICE-SIG-MIB", "sysMaxRetransmitTimer"), ("ZHONE-COM-VOICE-SIG-MIB", "sysInitRetransmitTimer"), ("ZHONE-COM-VOICE-SIG-MIB", "sysKeepAliveTimer"), ("ZHONE-COM-VOICE-SIG-MIB", "sysNoResponseTimer"), ("ZHONE-COM-VOICE-SIG-MIB", "sysCallWaitMaxRepeat"), ("ZHONE-COM-VOICE-SIG-MIB", "sysCallWaitDelay"), ("ZHONE-COM-VOICE-SIG-MIB", "sysPulseInterDigitTimer"), ("ZHONE-COM-VOICE-SIG-MIB", "sysMinMakePulseWidth"), ("ZHONE-COM-VOICE-SIG-MIB", "sysMaxMakePulseWidth"), ("ZHONE-COM-VOICE-SIG-MIB", "sysMinBreakPulseWidth"), ("ZHONE-COM-VOICE-SIG-MIB", "sysMaxBreakPulseWidth"), ("ZHONE-COM-VOICE-SIG-MIB", "hookFlashTimerMin"), ("ZHONE-COM-VOICE-SIG-MIB", "hookFlashTimerMax"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    zhoneVoiceSignalingObjectsGroup = zhoneVoiceSignalingObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: zhoneVoiceSignalingObjectsGroup.setDescription('Description.')
mibBuilder.exportSymbols("ZHONE-COM-VOICE-SIG-MIB", sysStutterToneTo=sysStutterToneTo, sysMaxMakePulseWidth=sysMaxMakePulseWidth, PYSNMP_MODULE_ID=zhoneVoiceSignalingMib, sysServerMaxTimer=sysServerMaxTimer, sysRingbackTo=sysRingbackTo, sysInitRetransmitTimer=sysInitRetransmitTimer, sysOffhookWarnToneTo=sysOffhookWarnToneTo, sysDialToneTo=sysDialToneTo, sysMax1Enable=sysMax1Enable, hookFlashTimerMin=hookFlashTimerMin, zhoneVoiceSignalingMib=zhoneVoiceSignalingMib, sysMsgWaitToneTo=sysMsgWaitToneTo, sysMinMakePulseWidth=sysMinMakePulseWidth, sysKeepAliveTimer=sysKeepAliveTimer, sysMaxRetransmitTimer=sysMaxRetransmitTimer, sysCallWaitDelay=sysCallWaitDelay, sysMax2Enable=sysMax2Enable, zhoneVoiceSignalingObjectsGroup=zhoneVoiceSignalingObjectsGroup, sysReorderToneTo=sysReorderToneTo, sysDisconnectWaitTimer=sysDisconnectWaitTimer, sysConfigMax1=sysConfigMax1, sysBusyToneTo=sysBusyToneTo, sysMinBreakPulseWidth=sysMinBreakPulseWidth, zhoneVoiceSignalingTimers=zhoneVoiceSignalingTimers, sysPulseInterDigitTimer=sysPulseInterDigitTimer, sysPartialDialTo=sysPartialDialTo, sysCriticalDialTo=sysCriticalDialTo, sysConfigMax2=sysConfigMax2, sysMaxWaitingDelay=sysMaxWaitingDelay, sysDisconnectMinTimer=sysDisconnectMinTimer, sysCallWaitMaxRepeat=sysCallWaitMaxRepeat, sysNoResponseTimer=sysNoResponseTimer, sysMaxBreakPulseWidth=sysMaxBreakPulseWidth, sysDisconnectMaxTimer=sysDisconnectMaxTimer, sysRingingTo=sysRingingTo, hookFlashTimerMax=hookFlashTimerMax)
