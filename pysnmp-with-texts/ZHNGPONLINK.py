#
# PySNMP MIB module ZHNGPONLINK (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHNGPONLINK
# Produced by pysmi-0.3.4 at Wed May  1 15:46:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Gauge32, Unsigned32, Integer32, MibIdentifier, ModuleIdentity, TimeTicks, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, IpAddress, Counter64, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "Integer32", "MibIdentifier", "ModuleIdentity", "TimeTicks", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "IpAddress", "Counter64", "enterprises", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
zhoneWtn, = mibBuilder.importSymbols("Zhone", "zhoneWtn")
zhnGPONLink = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43))
zhnGPONLink.setRevisions(('2012-02-03 13:46', '2011-01-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: zhnGPONLink.setRevisionsDescriptions(('Added the following objects: txPower txBiasCurrent gponTemperature gponVcc ', 'First Draft',))
if mibBuilder.loadTexts: zhnGPONLink.setLastUpdated('201202031346Z')
if mibBuilder.loadTexts: zhnGPONLink.setOrganization('Zhone Technologies, Inc.')
if mibBuilder.loadTexts: zhnGPONLink.setContactInfo('Zhone Technologies, Inc. Florida Design Center 8545 126th Avenue North Largo, FL 33773 Toll-Free: +1 877-ZHONE20 (+1 877-946-6320) Tel: +1-510-777-7000 Fax: +1-510-777-7001 E-mail: support@zhone.com')
if mibBuilder.loadTexts: zhnGPONLink.setDescription('This file defines the private Enterprise MIB extensions that define GPON interface related objects supported by the Zhone VoIP CPEs.')
zhnGPONLinkObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1))
class GPONLinkStatusValues(TextualConvention, OctetString):
    description = 'GPON interface status. An enumeration of: Up Down Initializing Unavailable '
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class GPONEnabledDisabledStatusValues(TextualConvention, OctetString):
    description = 'GPON RF Video status. An enumeration of: Disabled Enabled '
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class GPONStateValues(TextualConvention, OctetString):
    description = 'GPON ONU state. An enumeration of: INIT STANDBY SERIAL NUMBER RANGING OPERATIONAL POPUP EMERGENCY STOP DEACTIVATED '
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class GPONOnOffAlarmValues(TextualConvention, OctetString):
    description = 'GPON Alarm status. An enumeration of: On Off '
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

gponInterfaceNumberOfEntries = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gponInterfaceNumberOfEntries.setStatus('current')
if mibBuilder.loadTexts: gponInterfaceNumberOfEntries.setDescription('Number of instances of GPON interfaces for this ONU.')
gponLinkStatusTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2), )
if mibBuilder.loadTexts: gponLinkStatusTable.setStatus('current')
if mibBuilder.loadTexts: gponLinkStatusTable.setDescription('Table of GPON link status information.')
gponLinkStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2, 1), ).setIndexNames((0, "ZHNGPONLINK", "gponIfIndex"))
if mibBuilder.loadTexts: gponLinkStatusEntry.setStatus('current')
if mibBuilder.loadTexts: gponLinkStatusEntry.setDescription('Table of GPON link status information.')
gponIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: gponIfIndex.setStatus('current')
if mibBuilder.loadTexts: gponIfIndex.setDescription('GPON Interface index.')
gponOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2, 1, 2), GPONLinkStatusValues()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gponOperStatus.setStatus('current')
if mibBuilder.loadTexts: gponOperStatus.setDescription('Indicates the status of this GPON interface. Enumeration of: Up Down Initializing Unavailable ')
gponLinkUpTransitions = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gponLinkUpTransitions.setStatus('current')
if mibBuilder.loadTexts: gponLinkUpTransitions.setDescription('Number of times the GPON link has transitioned from down to up.')
rfVideo = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2, 1, 4), GPONEnabledDisabledStatusValues()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rfVideo.setStatus('current')
if mibBuilder.loadTexts: rfVideo.setDescription('Indicates if the RF Video over the GPON interface is enabled or disabled. Enumeration of: Disabled Enabled ')
gponOnuId = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gponOnuId.setStatus('current')
if mibBuilder.loadTexts: gponOnuId.setDescription('Optical network unit identifier.')
gponState = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2, 1, 6), GPONStateValues()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gponState.setStatus('current')
if mibBuilder.loadTexts: gponState.setDescription('Optical network unit state. Enumeration of: INIT STANDBY SERIAL NUMBER RANGING OPERATIONAL POPUP EMERGENCY STOP DEACTIVATED ')
rxLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxLevel.setStatus('current')
if mibBuilder.loadTexts: rxLevel.setDescription('GPON interface receive level, in dBm.')
txPower = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txPower.setStatus('current')
if mibBuilder.loadTexts: txPower.setDescription('GPON interface transmit power, in dBm.')
txBiasCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txBiasCurrent.setStatus('current')
if mibBuilder.loadTexts: txBiasCurrent.setDescription('GPON interface transmit bias current, in mA.')
gponTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gponTemperature.setStatus('current')
if mibBuilder.loadTexts: gponTemperature.setDescription('GPON interface diplexer/triplexer temperature, in Celsius.')
gponVcc = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gponVcc.setStatus('current')
if mibBuilder.loadTexts: gponVcc.setDescription('GPON interface voltage, in volts.')
gponAlarmStatusTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3), )
if mibBuilder.loadTexts: gponAlarmStatusTable.setStatus('current')
if mibBuilder.loadTexts: gponAlarmStatusTable.setDescription('Table of GPON alarm status information.')
gponAlarmStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1), ).setIndexNames((0, "ZHNGPONLINK", "gponIfIndex"))
if mibBuilder.loadTexts: gponAlarmStatusEntry.setStatus('current')
if mibBuilder.loadTexts: gponAlarmStatusEntry.setDescription('Table of GPON alarm status information.')
gponAlarmAutoPowerControlFail = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1, 1), GPONOnOffAlarmValues()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gponAlarmAutoPowerControlFail.setStatus('current')
if mibBuilder.loadTexts: gponAlarmAutoPowerControlFail.setDescription('If the value of this object is ON, the automatic power-control has failed. ')
gponAlarmLOS = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1, 2), GPONOnOffAlarmValues()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gponAlarmLOS.setStatus('current')
if mibBuilder.loadTexts: gponAlarmLOS.setDescription('If the value of this object is ON, no input signal has been detected. Make sure fiber is plugged in. ')
gponAlarmLOL = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1, 3), GPONOnOffAlarmValues()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gponAlarmLOL.setStatus('current')
if mibBuilder.loadTexts: gponAlarmLOL.setDescription('If the value of this object is ON, the GPON link has detected a Loss of Link condition. ')
gponAlarmLOF = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1, 4), GPONOnOffAlarmValues()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gponAlarmLOF.setStatus('current')
if mibBuilder.loadTexts: gponAlarmLOF.setDescription('If the value of this object is ON, the GPON link has detected a Loss Of Frame condition. ')
gponAlarmLCDG = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1, 5), GPONOnOffAlarmValues()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gponAlarmLCDG.setStatus('current')
if mibBuilder.loadTexts: gponAlarmLCDG.setDescription('If the value of this object is ON, the GPON link has detected a Loss of GEM Channel Delineation condition. ')
gponAlarmFailedSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1, 6), GPONOnOffAlarmValues()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gponAlarmFailedSignal.setStatus('current')
if mibBuilder.loadTexts: gponAlarmFailedSignal.setDescription('If the value of this object is ON, the GPON link has detected a bit error rate greater than 10E-5. ')
gponAlarmDegradedSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1, 7), GPONOnOffAlarmValues()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gponAlarmDegradedSignal.setStatus('current')
if mibBuilder.loadTexts: gponAlarmDegradedSignal.setDescription('If the value of this object is ON, the GPON link has detected a bit error rate greater than 10E-6. ')
gponAlarmStartupFail = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1, 8), GPONOnOffAlarmValues()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gponAlarmStartupFail.setStatus('current')
if mibBuilder.loadTexts: gponAlarmStartupFail.setDescription('If the value of this object is ON, the GPON link has detected an error during startup. ')
gponAlarmMsgErrorMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1, 9), GPONOnOffAlarmValues()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gponAlarmMsgErrorMsg.setStatus('current')
if mibBuilder.loadTexts: gponAlarmMsgErrorMsg.setDescription('If the value of this object is ON, the GPON link has received an unknown PLOAM message. ')
gponAlarmDeactivateOnuId = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1, 10), GPONOnOffAlarmValues()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gponAlarmDeactivateOnuId.setStatus('current')
if mibBuilder.loadTexts: gponAlarmDeactivateOnuId.setDescription('If the value of this object is ON, the GPON link has received a de-activate request and has successfully de-activated the link. ')
gponAlarmDisabledOnu = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1, 11), GPONOnOffAlarmValues()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gponAlarmDisabledOnu.setStatus('current')
if mibBuilder.loadTexts: gponAlarmDisabledOnu.setDescription('If the value of this object is ON, the GPON link has been disabled by the OLT or the ONU Serial Number is not configured on the OLT. ')
gponAlarmPEE = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1, 12), GPONOnOffAlarmValues()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gponAlarmPEE.setStatus('current')
if mibBuilder.loadTexts: gponAlarmPEE.setDescription('If the value of this object is ON, the GPON link has detected a physical equipment error which may indicate a possible hardware problem. ')
gponDataGemStatsTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 4), )
if mibBuilder.loadTexts: gponDataGemStatsTable.setStatus('current')
if mibBuilder.loadTexts: gponDataGemStatsTable.setDescription('Table of GPON Encapsulation Method (GEM) VoIP and Internet traffic statistics for the Data GEM port.')
gponDataGemStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 4, 1), ).setIndexNames((0, "ZHNGPONLINK", "gponIfIndex"))
if mibBuilder.loadTexts: gponDataGemStatsEntry.setStatus('current')
if mibBuilder.loadTexts: gponDataGemStatsEntry.setDescription('Table of GPON Encapsulation Method (GEM) VoIP and Internet traffic statistics for the Data GEM port.')
dataGemPortRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 4, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataGemPortRxBytes.setStatus('current')
if mibBuilder.loadTexts: dataGemPortRxBytes.setDescription('Number of bytes received on the data GEM port, not including GEM headers. ')
dataGemPortRxFragments = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 4, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataGemPortRxFragments.setStatus('current')
if mibBuilder.loadTexts: dataGemPortRxFragments.setDescription('Number of GEM fragments received on the data GEM port. ')
dataGemPortRxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 4, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataGemPortRxFrames.setStatus('current')
if mibBuilder.loadTexts: dataGemPortRxFrames.setDescription('Number of ethernet frames received on the data GEM port. ')
dataGemPortRxDroppedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 4, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataGemPortRxDroppedFrames.setStatus('current')
if mibBuilder.loadTexts: dataGemPortRxDroppedFrames.setDescription('Number of receive ethernet frames dropped due to congestion or because frame is undersized. ')
dataGemPortTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 4, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataGemPortTxBytes.setStatus('current')
if mibBuilder.loadTexts: dataGemPortTxBytes.setDescription('Number of bytes transmitted on the data GEM port, not including GEM headers. ')
dataGemPortTxFragments = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 4, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataGemPortTxFragments.setStatus('current')
if mibBuilder.loadTexts: dataGemPortTxFragments.setDescription('Number of GEM fragments transmitted on the data GEM port. ')
dataGemPortTxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 4, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataGemPortTxFrames.setStatus('current')
if mibBuilder.loadTexts: dataGemPortTxFrames.setDescription('Number of ethernet frames transmitted on the data GEM port. ')
dataGemPortTxDroppedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 4, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataGemPortTxDroppedFrames.setStatus('current')
if mibBuilder.loadTexts: dataGemPortTxDroppedFrames.setDescription('Number of ethernet frames dropped due to congestion. ')
dataGemPortAcceptedMulticastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 4, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataGemPortAcceptedMulticastFrames.setStatus('current')
if mibBuilder.loadTexts: dataGemPortAcceptedMulticastFrames.setDescription('Number of multicast frames accepted by the Multicast Filtering Function. ')
dataGemPortDroppedMulticastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 4, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataGemPortDroppedMulticastFrames.setStatus('current')
if mibBuilder.loadTexts: dataGemPortDroppedMulticastFrames.setDescription('Number of multicast frames dropped by the Multicast Filtering Function. ')
gponVideoGemStatsTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 5), )
if mibBuilder.loadTexts: gponVideoGemStatsTable.setStatus('current')
if mibBuilder.loadTexts: gponVideoGemStatsTable.setDescription('Table of GPON Encapsulation Method (GEM) Video traffic statistics for the Data GEM port.')
gponVideoGemStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 5, 1), ).setIndexNames((0, "ZHNGPONLINK", "gponIfIndex"))
if mibBuilder.loadTexts: gponVideoGemStatsEntry.setStatus('current')
if mibBuilder.loadTexts: gponVideoGemStatsEntry.setDescription('Table of GPON Encapsulation Method (GEM) Video traffic statistics for the Video GEM port.')
videoGemPortRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 5, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: videoGemPortRxBytes.setStatus('current')
if mibBuilder.loadTexts: videoGemPortRxBytes.setDescription('Number of bytes received on the video GEM port, not including GEM headers. ')
videoGemPortRxFragments = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 5, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: videoGemPortRxFragments.setStatus('current')
if mibBuilder.loadTexts: videoGemPortRxFragments.setDescription('Number of GEM fragments received on the video GEM port. ')
videoGemPortRxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 5, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: videoGemPortRxFrames.setStatus('current')
if mibBuilder.loadTexts: videoGemPortRxFrames.setDescription('Number of ethernet frames received on the video GEM port. ')
videoGemPortRxDroppedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 5, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: videoGemPortRxDroppedFrames.setStatus('current')
if mibBuilder.loadTexts: videoGemPortRxDroppedFrames.setDescription('Number of receive ethernet frames dropped due to congestion or because frame is undersized. ')
videoGemPortTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 5, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: videoGemPortTxBytes.setStatus('current')
if mibBuilder.loadTexts: videoGemPortTxBytes.setDescription('Number of bytes transmitted on the video GEM port, not including GEM headers. ')
videoGemPortTxFragments = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 5, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: videoGemPortTxFragments.setStatus('current')
if mibBuilder.loadTexts: videoGemPortTxFragments.setDescription('Number of GEM fragments transmitted on the video GEM port. ')
videoGemPortTxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 5, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: videoGemPortTxFrames.setStatus('current')
if mibBuilder.loadTexts: videoGemPortTxFrames.setDescription('Number of ethernet frames transmitted on the video GEM port. ')
videoGemPortTxDroppedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 5, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: videoGemPortTxDroppedFrames.setStatus('current')
if mibBuilder.loadTexts: videoGemPortTxDroppedFrames.setDescription('Number of ethernet frames dropped due to congestion. ')
videoGemPortAcceptedMulticastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 5, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: videoGemPortAcceptedMulticastFrames.setStatus('current')
if mibBuilder.loadTexts: videoGemPortAcceptedMulticastFrames.setDescription('Number of multicast frames accepted by the Multicast Filtering Function. ')
videoGemPortDroppedMulticastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 5, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: videoGemPortDroppedMulticastFrames.setStatus('current')
if mibBuilder.loadTexts: videoGemPortDroppedMulticastFrames.setDescription('Number of multicast frames dropped by the Multicast Filtering Function. ')
gponGtcStatsTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 6), )
if mibBuilder.loadTexts: gponGtcStatsTable.setStatus('current')
if mibBuilder.loadTexts: gponGtcStatsTable.setDescription('Table of GPON Transmission Convergence (GTC) statistics for the Data GEM port.')
gponGtcStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 6, 1), ).setIndexNames((0, "ZHNGPONLINK", "gponIfIndex"))
if mibBuilder.loadTexts: gponGtcStatsEntry.setStatus('current')
if mibBuilder.loadTexts: gponGtcStatsEntry.setDescription('Table of GPON Transmission Convergence (GTC) statistics for the Data GEM port.')
gtcBipErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 6, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtcBipErrors.setStatus('current')
if mibBuilder.loadTexts: gtcBipErrors.setDescription('Bit Interleaved Parity Errors. ')
gtcFecCorrectedCodewords = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 6, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtcFecCorrectedCodewords.setStatus('current')
if mibBuilder.loadTexts: gtcFecCorrectedCodewords.setDescription('Forward Error Coding Corrected Codewords. ')
gtcFecUncorrectableCodewords = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 6, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtcFecUncorrectableCodewords.setStatus('current')
if mibBuilder.loadTexts: gtcFecUncorrectableCodewords.setDescription('Forward Error Coding Uncorrectable Codewords. ')
gtcTotalRxDsFecCodewords = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 6, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtcTotalRxDsFecCodewords.setStatus('current')
if mibBuilder.loadTexts: gtcTotalRxDsFecCodewords.setDescription('Total Received Downstream Forward Error Coding Codewords. ')
gtcFecCorrectionSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 6, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtcFecCorrectionSeconds.setStatus('current')
if mibBuilder.loadTexts: gtcFecCorrectionSeconds.setDescription('Number of seconds during which there was a FEC correction anomaly. ')
gtcCorrectedHecErrorsGemFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 6, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtcCorrectedHecErrorsGemFrames.setStatus('current')
if mibBuilder.loadTexts: gtcCorrectedHecErrorsGemFrames.setDescription('Number of GEM frames with corrected HEC errors. ')
gtcUncorrectableHecErrorsGemFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 6, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtcUncorrectableHecErrorsGemFrames.setStatus('current')
if mibBuilder.loadTexts: gtcUncorrectableHecErrorsGemFrames.setDescription('Number of GEM frames with uncorrectable HEC errors. ')
gponPloamStatsTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 7), )
if mibBuilder.loadTexts: gponPloamStatsTable.setStatus('current')
if mibBuilder.loadTexts: gponPloamStatsTable.setDescription('Table of GPON Physical Layer Operation, Administration and Management (PLOAM) statistics for the Data GEM port.')
gponPloamStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 7, 1), ).setIndexNames((0, "ZHNGPONLINK", "gponIfIndex"))
if mibBuilder.loadTexts: gponPloamStatsEntry.setStatus('current')
if mibBuilder.loadTexts: gponPloamStatsEntry.setDescription('Table of GPON Physical Layer Operation, Administration and Management (PLOAM) statistics for the Data GEM port.')
msgsCrcError = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 7, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msgsCrcError.setStatus('current')
if mibBuilder.loadTexts: msgsCrcError.setDescription('Messages received in error and discarded. ')
msgsRxTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 7, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msgsRxTotal.setStatus('current')
if mibBuilder.loadTexts: msgsRxTotal.setDescription('Total Number of CRC correct downstream PLOAM messages received. ')
msgsRxUnicast = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 7, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msgsRxUnicast.setStatus('current')
if mibBuilder.loadTexts: msgsRxUnicast.setDescription("Number of CRC correct downstream PLOAM messages with ONU ID matching this ONU's ID. ")
msgsRxBroadcast = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 7, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msgsRxBroadcast.setStatus('current')
if mibBuilder.loadTexts: msgsRxBroadcast.setDescription('Number of CRC correct broadcast downstream PLOAM messages. ')
msgsRxDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 7, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msgsRxDiscarded.setStatus('current')
if mibBuilder.loadTexts: msgsRxDiscarded.setDescription('Number of downstream PLOAM messages discarded, because the message is unknown and not registered, or because the message is not valid in the current state. ')
msgsRxNonStandard = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 7, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msgsRxNonStandard.setStatus('current')
if mibBuilder.loadTexts: msgsRxNonStandard.setDescription('Number of non-standard downstream PLOAM messages received from the OLT. ')
msgsTxTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 7, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msgsTxTotal.setStatus('current')
if mibBuilder.loadTexts: msgsTxTotal.setDescription('Total number of PLOAM messages transmitted upstream to the OLT. ')
msgsTxNonStandard = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 7, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msgsTxNonStandard.setStatus('current')
if mibBuilder.loadTexts: msgsTxNonStandard.setDescription('Number of non-standard PLOAM messages transmitted upstream to the OLT. ')
zhnGPONLinkConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 2))
zhnGPONLinkGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 2, 1))
zhnGPONLinkCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 2, 2))
zhnGPONLinkCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 2, 2, 1)).setObjects(("ZHNGPONLINK", "zhnGPONStatusGroup"), ("ZHNGPONLINK", "zhnGPONAlarmGroup"), ("ZHNGPONLINK", "zhnGPONDataGemStatsGroup"), ("ZHNGPONLINK", "zhnGPONVideoGemStatsGroup"), ("ZHNGPONLINK", "zhnGPONGtcStatsGroup"), ("ZHNGPONLINK", "zhnGPONPloamStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    zhnGPONLinkCompliance = zhnGPONLinkCompliance.setStatus('current')
if mibBuilder.loadTexts: zhnGPONLinkCompliance.setDescription('The Compliance statement for SNMP entities which manage the Zhone ONU GPON Interfaces')
zhnGPONStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 2, 1, 1)).setObjects(("ZHNGPONLINK", "gponInterfaceNumberOfEntries"), ("ZHNGPONLINK", "gponOperStatus"), ("ZHNGPONLINK", "gponLinkUpTransitions"), ("ZHNGPONLINK", "rfVideo"), ("ZHNGPONLINK", "gponOnuId"), ("ZHNGPONLINK", "gponState"), ("ZHNGPONLINK", "rxLevel"), ("ZHNGPONLINK", "txPower"), ("ZHNGPONLINK", "txBiasCurrent"), ("ZHNGPONLINK", "gponTemperature"), ("ZHNGPONLINK", "gponVcc"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    zhnGPONStatusGroup = zhnGPONStatusGroup.setStatus('current')
if mibBuilder.loadTexts: zhnGPONStatusGroup.setDescription('A collection of Zhone GPON link objects that describe the status and state of the GPON links of the ONU.')
zhnGPONAlarmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 2, 1, 2)).setObjects(("ZHNGPONLINK", "gponAlarmAutoPowerControlFail"), ("ZHNGPONLINK", "gponAlarmLOS"), ("ZHNGPONLINK", "gponAlarmLOL"), ("ZHNGPONLINK", "gponAlarmLOF"), ("ZHNGPONLINK", "gponAlarmLCDG"), ("ZHNGPONLINK", "gponAlarmFailedSignal"), ("ZHNGPONLINK", "gponAlarmDegradedSignal"), ("ZHNGPONLINK", "gponAlarmStartupFail"), ("ZHNGPONLINK", "gponAlarmMsgErrorMsg"), ("ZHNGPONLINK", "gponAlarmDeactivateOnuId"), ("ZHNGPONLINK", "gponAlarmDisabledOnu"), ("ZHNGPONLINK", "gponAlarmPEE"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    zhnGPONAlarmGroup = zhnGPONAlarmGroup.setStatus('current')
if mibBuilder.loadTexts: zhnGPONAlarmGroup.setDescription('A collection of Zhone GPON Link objects that identify the current alarms detected by the ONU.')
zhnGPONDataGemStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 2, 1, 3)).setObjects(("ZHNGPONLINK", "dataGemPortRxBytes"), ("ZHNGPONLINK", "dataGemPortRxFragments"), ("ZHNGPONLINK", "dataGemPortRxFrames"), ("ZHNGPONLINK", "dataGemPortRxDroppedFrames"), ("ZHNGPONLINK", "dataGemPortTxBytes"), ("ZHNGPONLINK", "dataGemPortTxFragments"), ("ZHNGPONLINK", "dataGemPortTxFrames"), ("ZHNGPONLINK", "dataGemPortTxDroppedFrames"), ("ZHNGPONLINK", "dataGemPortAcceptedMulticastFrames"), ("ZHNGPONLINK", "dataGemPortDroppedMulticastFrames"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    zhnGPONDataGemStatsGroup = zhnGPONDataGemStatsGroup.setStatus('current')
if mibBuilder.loadTexts: zhnGPONDataGemStatsGroup.setDescription('A collection of Zhone GPON Link objects that identify the GPON Encapsulation Method VoIP and Internet traffic statistics for the Data GEM port.')
zhnGPONVideoGemStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 2, 1, 4)).setObjects(("ZHNGPONLINK", "videoGemPortRxBytes"), ("ZHNGPONLINK", "videoGemPortRxFragments"), ("ZHNGPONLINK", "videoGemPortRxFrames"), ("ZHNGPONLINK", "videoGemPortRxDroppedFrames"), ("ZHNGPONLINK", "videoGemPortTxBytes"), ("ZHNGPONLINK", "videoGemPortTxFragments"), ("ZHNGPONLINK", "videoGemPortTxFrames"), ("ZHNGPONLINK", "videoGemPortTxDroppedFrames"), ("ZHNGPONLINK", "videoGemPortAcceptedMulticastFrames"), ("ZHNGPONLINK", "videoGemPortDroppedMulticastFrames"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    zhnGPONVideoGemStatsGroup = zhnGPONVideoGemStatsGroup.setStatus('current')
if mibBuilder.loadTexts: zhnGPONVideoGemStatsGroup.setDescription('A collection of Zhone GPON Link objects that identify the GPON Encapsulation Method Port statistics for the Video GEM port.')
zhnGPONGtcStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 2, 1, 5)).setObjects(("ZHNGPONLINK", "gtcBipErrors"), ("ZHNGPONLINK", "gtcFecCorrectedCodewords"), ("ZHNGPONLINK", "gtcFecUncorrectableCodewords"), ("ZHNGPONLINK", "gtcTotalRxDsFecCodewords"), ("ZHNGPONLINK", "gtcFecCorrectionSeconds"), ("ZHNGPONLINK", "gtcCorrectedHecErrorsGemFrames"), ("ZHNGPONLINK", "gtcUncorrectableHecErrorsGemFrames"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    zhnGPONGtcStatsGroup = zhnGPONGtcStatsGroup.setStatus('current')
if mibBuilder.loadTexts: zhnGPONGtcStatsGroup.setDescription('A collection of Zhone GPON Link objects that identify the GPON Transmission Convergence statistics.')
zhnGPONPloamStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 2, 1, 6)).setObjects(("ZHNGPONLINK", "msgsCrcError"), ("ZHNGPONLINK", "msgsRxTotal"), ("ZHNGPONLINK", "msgsRxUnicast"), ("ZHNGPONLINK", "msgsRxBroadcast"), ("ZHNGPONLINK", "msgsRxDiscarded"), ("ZHNGPONLINK", "msgsRxNonStandard"), ("ZHNGPONLINK", "msgsTxTotal"), ("ZHNGPONLINK", "msgsTxNonStandard"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    zhnGPONPloamStatsGroup = zhnGPONPloamStatsGroup.setStatus('current')
if mibBuilder.loadTexts: zhnGPONPloamStatsGroup.setDescription('A collection of Zhone GPON Link objects that identify the GPON Physical Layer Operation, Administration and Management (PLOAM) message statistics.')
mibBuilder.exportSymbols("ZHNGPONLINK", msgsRxBroadcast=msgsRxBroadcast, zhnGPONAlarmGroup=zhnGPONAlarmGroup, gtcCorrectedHecErrorsGemFrames=gtcCorrectedHecErrorsGemFrames, GPONOnOffAlarmValues=GPONOnOffAlarmValues, txPower=txPower, gponLinkUpTransitions=gponLinkUpTransitions, videoGemPortRxFrames=videoGemPortRxFrames, msgsCrcError=msgsCrcError, dataGemPortRxFragments=dataGemPortRxFragments, GPONEnabledDisabledStatusValues=GPONEnabledDisabledStatusValues, videoGemPortTxBytes=videoGemPortTxBytes, txBiasCurrent=txBiasCurrent, videoGemPortTxFragments=videoGemPortTxFragments, rfVideo=rfVideo, gponVcc=gponVcc, gponAlarmLCDG=gponAlarmLCDG, dataGemPortRxBytes=dataGemPortRxBytes, zhnGPONLinkObjects=zhnGPONLinkObjects, dataGemPortDroppedMulticastFrames=dataGemPortDroppedMulticastFrames, gponAlarmAutoPowerControlFail=gponAlarmAutoPowerControlFail, gponPloamStatsEntry=gponPloamStatsEntry, rxLevel=rxLevel, gponIfIndex=gponIfIndex, GPONStateValues=GPONStateValues, zhnGPONLinkGroups=zhnGPONLinkGroups, gponAlarmMsgErrorMsg=gponAlarmMsgErrorMsg, dataGemPortTxBytes=dataGemPortTxBytes, gponVideoGemStatsEntry=gponVideoGemStatsEntry, gtcFecCorrectionSeconds=gtcFecCorrectionSeconds, gtcFecUncorrectableCodewords=gtcFecUncorrectableCodewords, videoGemPortDroppedMulticastFrames=videoGemPortDroppedMulticastFrames, gponAlarmLOL=gponAlarmLOL, gponInterfaceNumberOfEntries=gponInterfaceNumberOfEntries, zhnGPONPloamStatsGroup=zhnGPONPloamStatsGroup, gponPloamStatsTable=gponPloamStatsTable, GPONLinkStatusValues=GPONLinkStatusValues, gponDataGemStatsEntry=gponDataGemStatsEntry, gtcFecCorrectedCodewords=gtcFecCorrectedCodewords, gponAlarmLOF=gponAlarmLOF, msgsTxTotal=msgsTxTotal, dataGemPortRxFrames=dataGemPortRxFrames, dataGemPortAcceptedMulticastFrames=dataGemPortAcceptedMulticastFrames, gtcUncorrectableHecErrorsGemFrames=gtcUncorrectableHecErrorsGemFrames, gponLinkStatusEntry=gponLinkStatusEntry, zhnGPONGtcStatsGroup=zhnGPONGtcStatsGroup, PYSNMP_MODULE_ID=zhnGPONLink, gponDataGemStatsTable=gponDataGemStatsTable, videoGemPortRxDroppedFrames=videoGemPortRxDroppedFrames, videoGemPortRxFragments=videoGemPortRxFragments, gponOnuId=gponOnuId, zhnGPONDataGemStatsGroup=zhnGPONDataGemStatsGroup, videoGemPortRxBytes=videoGemPortRxBytes, gponAlarmPEE=gponAlarmPEE, dataGemPortTxFragments=dataGemPortTxFragments, gponAlarmStatusTable=gponAlarmStatusTable, dataGemPortTxDroppedFrames=dataGemPortTxDroppedFrames, gponVideoGemStatsTable=gponVideoGemStatsTable, videoGemPortTxFrames=videoGemPortTxFrames, msgsRxTotal=msgsRxTotal, gtcTotalRxDsFecCodewords=gtcTotalRxDsFecCodewords, gponAlarmStartupFail=gponAlarmStartupFail, videoGemPortAcceptedMulticastFrames=videoGemPortAcceptedMulticastFrames, zhnGPONLinkCompliances=zhnGPONLinkCompliances, zhnGPONLink=zhnGPONLink, videoGemPortTxDroppedFrames=videoGemPortTxDroppedFrames, zhnGPONLinkCompliance=zhnGPONLinkCompliance, gponState=gponState, dataGemPortTxFrames=dataGemPortTxFrames, zhnGPONLinkConformance=zhnGPONLinkConformance, gponAlarmDisabledOnu=gponAlarmDisabledOnu, gponOperStatus=gponOperStatus, msgsRxNonStandard=msgsRxNonStandard, gponGtcStatsEntry=gponGtcStatsEntry, gponLinkStatusTable=gponLinkStatusTable, gponAlarmStatusEntry=gponAlarmStatusEntry, msgsRxDiscarded=msgsRxDiscarded, zhnGPONVideoGemStatsGroup=zhnGPONVideoGemStatsGroup, gtcBipErrors=gtcBipErrors, gponAlarmDegradedSignal=gponAlarmDegradedSignal, gponAlarmDeactivateOnuId=gponAlarmDeactivateOnuId, zhnGPONStatusGroup=zhnGPONStatusGroup, gponGtcStatsTable=gponGtcStatsTable, msgsTxNonStandard=msgsTxNonStandard, gponTemperature=gponTemperature, gponAlarmLOS=gponAlarmLOS, gponAlarmFailedSignal=gponAlarmFailedSignal, msgsRxUnicast=msgsRxUnicast, dataGemPortRxDroppedFrames=dataGemPortRxDroppedFrames)
