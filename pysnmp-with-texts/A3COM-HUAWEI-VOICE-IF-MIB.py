#
# PySNMP MIB module A3COM-HUAWEI-VOICE-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-VOICE-IF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:07:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cVoice, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cVoice")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Integer32, NotificationType, MibIdentifier, Bits, Counter64, Counter32, iso, ModuleIdentity, ObjectIdentity, TimeTicks, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "NotificationType", "MibIdentifier", "Bits", "Counter64", "Counter32", "iso", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cVoiceInterface = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13))
h3cVoiceInterface.setRevisions(('2007-12-10 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cVoiceInterface.setRevisionsDescriptions(('The initial version of this MIB file.',))
if mibBuilder.loadTexts: h3cVoiceInterface.setLastUpdated('200712101700Z')
if mibBuilder.loadTexts: h3cVoiceInterface.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cVoiceInterface.setContactInfo('Platform Team H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R. China Http://www.h3c.com Zip:100085')
if mibBuilder.loadTexts: h3cVoiceInterface.setDescription('This MIB file is to provide the definition of the voice interface general configuration.')
h3cVoiceIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1))
h3cVoiceIfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1, 1), )
if mibBuilder.loadTexts: h3cVoiceIfConfigTable.setStatus('current')
if mibBuilder.loadTexts: h3cVoiceIfConfigTable.setDescription('The table contains configurable parameters for both analog voice interface and digital voice interface.')
h3cVoiceIfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cVoiceIfConfigEntry.setStatus('current')
if mibBuilder.loadTexts: h3cVoiceIfConfigEntry.setDescription('The entry of voice interface table.')
h3cVoiceIfCfgCngOn = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoiceIfCfgCngOn.setStatus('current')
if mibBuilder.loadTexts: h3cVoiceIfCfgCngOn.setDescription('This object indicates whether the silence gaps should be filled with background noise. It is applicable to FXO, FXS, E&M subscriber lines and E1/T1 voice subscriber line.')
h3cVoiceIfCfgNonLinearSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoiceIfCfgNonLinearSwitch.setStatus('current')
if mibBuilder.loadTexts: h3cVoiceIfCfgNonLinearSwitch.setDescription('This object expresses the nonlinear processing is enable or disable for the voice interface. It is applicable to FXO, FXS, E&M subscriber lines and E1/T1 voice subscriber line. Currently, only digital voice subscriber lines can be set disabled.')
h3cVoiceIfCfgInputGain = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-140, 139))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoiceIfCfgInputGain.setStatus('current')
if mibBuilder.loadTexts: h3cVoiceIfCfgInputGain.setDescription('This object indicates the amount of gain added to the receiver side of the voice interface. Unit is 0.1 db. It is applicable to FXO, FXS, E&M subscriber lines and E1/T1 voice subscriber line.')
h3cVoiceIfCfgOutputGain = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-140, 139))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoiceIfCfgOutputGain.setStatus('current')
if mibBuilder.loadTexts: h3cVoiceIfCfgOutputGain.setDescription('This object indicates the amount of gain added to the send side of the voice interface. Unit is 0.1 db. It is applicable to FXO, FXS, E&M subscriber lines and E1/T1 voice subscriber line.')
h3cVoiceIfCfgEchoCancelSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoiceIfCfgEchoCancelSwitch.setStatus('current')
if mibBuilder.loadTexts: h3cVoiceIfCfgEchoCancelSwitch.setDescription('This object indicates whether the echo cancellation is enabled. It is applicable to FXO, FXS, E&M subscriber lines and E1/T1 voice subscriber line.')
h3cVoiceIfCfgEchoCancelDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoiceIfCfgEchoCancelDelay.setStatus('current')
if mibBuilder.loadTexts: h3cVoiceIfCfgEchoCancelDelay.setDescription("This object indicates the delay of the echo cancellation for the voice interface. This value couldn't be modified unless h3cVoiceIfCfgEchoCancelSwitch is enable. Unit is milliseconds. It is applicable to FXO, FXS, E&M subscriber lines and E1/T1 voice subscriber line. The default value of this object is 32.")
h3cVoiceIfCfgTimerDialInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoiceIfCfgTimerDialInterval.setStatus('current')
if mibBuilder.loadTexts: h3cVoiceIfCfgTimerDialInterval.setDescription('The interval, in seconds, between two dialing numbers. The default value of this object is 10 seconds. It is applicable to FXO, FXS, E&M subscriber lines and E1/T1 with loop-start or ground-start protocol voice subscriber line.')
h3cVoiceIfCfgTimerFirstDial = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoiceIfCfgTimerFirstDial.setStatus('current')
if mibBuilder.loadTexts: h3cVoiceIfCfgTimerFirstDial.setDescription('The period of time, in seconds, before dialing the first number. The default value of this object is 10 seconds. It is applicable to FXO, FXS subscriber lines and E1/T1 with loop-start or ground-start protocol voice subscriber line.')
h3cVoiceIfCfgPrivateline = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoiceIfCfgPrivateline.setStatus('current')
if mibBuilder.loadTexts: h3cVoiceIfCfgPrivateline.setDescription('This object indicates the E.164 phone number for plar mode. It is applicable to FXO, FXS, E&M subscriber lines and E1/T1 voice subscriber line.')
h3cVoiceIfCfgRegTone = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1, 1, 1, 10), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(2, 3), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoiceIfCfgRegTone.setStatus('current')
if mibBuilder.loadTexts: h3cVoiceIfCfgRegTone.setDescription('This object uses 2 or 3 letter country code specify voice parameters of different countrys. This value will take effect on all voice interfaces of all cards on the device.')
mibBuilder.exportSymbols("A3COM-HUAWEI-VOICE-IF-MIB", h3cVoiceIfConfigTable=h3cVoiceIfConfigTable, h3cVoiceIfCfgTimerFirstDial=h3cVoiceIfCfgTimerFirstDial, h3cVoiceIfCfgInputGain=h3cVoiceIfCfgInputGain, h3cVoiceIfCfgTimerDialInterval=h3cVoiceIfCfgTimerDialInterval, h3cVoiceIfCfgCngOn=h3cVoiceIfCfgCngOn, h3cVoiceIfCfgEchoCancelSwitch=h3cVoiceIfCfgEchoCancelSwitch, h3cVoiceIfCfgRegTone=h3cVoiceIfCfgRegTone, h3cVoiceIfCfgNonLinearSwitch=h3cVoiceIfCfgNonLinearSwitch, PYSNMP_MODULE_ID=h3cVoiceInterface, h3cVoiceInterface=h3cVoiceInterface, h3cVoiceIfCfgEchoCancelDelay=h3cVoiceIfCfgEchoCancelDelay, h3cVoiceIfCfgOutputGain=h3cVoiceIfCfgOutputGain, h3cVoiceIfConfigEntry=h3cVoiceIfConfigEntry, h3cVoiceIfCfgPrivateline=h3cVoiceIfCfgPrivateline, h3cVoiceIfObjects=h3cVoiceIfObjects)