#
# PySNMP MIB module RC7586-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RC7586-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:54:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
satcomMibs, = mibBuilder.importSymbols("CODAN-SMI", "satcomMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, iso, Gauge32, Counter64, IpAddress, ModuleIdentity, ObjectIdentity, NotificationType, Unsigned32, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "iso", "Gauge32", "Counter64", "IpAddress", "ModuleIdentity", "ObjectIdentity", "NotificationType", "Unsigned32", "Bits", "Integer32")
DisplayString, TestAndIncr, TruthValue, TimeInterval, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TestAndIncr", "TruthValue", "TimeInterval", "DateAndTime", "TextualConvention")
rc7586MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 23304, 2, 2))
rc7586MIB.setRevisions(('2009-05-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rc7586MIB.setRevisionsDescriptions(('1.0 Initial version of this MIB module.',))
if mibBuilder.loadTexts: rc7586MIB.setLastUpdated('200905130000Z')
if mibBuilder.loadTexts: rc7586MIB.setOrganization('Codan Limited.')
if mibBuilder.loadTexts: rc7586MIB.setContactInfo(' Magda Raltcheva Postal: Codan Limited 81 Graves St. Newton 5074 Australia Tel: +61-8-83050311 Fax: +61-8-83050411 Web: www.codan.com.au')
if mibBuilder.loadTexts: rc7586MIB.setDescription('The Structure of Management Information for the Codan enterprise. Copyright(c) 2009 All rights reserved')
class ComponentRevision(DisplayString):
    description = 'The hex value in the first octet - xx - represents the major revision no. and the hex value in the second octet - yy - represents the minor revision no.'
    status = 'current'
    displayHint = 'vxx.yy'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class FaultStatus7586(TextualConvention, Bits):
    description = 'Describes all the possible faults in the system as a bit pattern.'
    status = 'current'
    namedValues = NamedValues(("dc1fault", 0), ("dc2fault", 1), ("buc1fault", 2), ("buc2fault", 3), ("lnb1fault", 4), ("lnb2fault", 5), ("txswfault", 6), ("rxswfault", 7), ("internalfault", 8), ("ref10mhzfault", 9))

buc1 = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1))
buc2 = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2))
ctrl = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 2, 3))
settings = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1))
status = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 2))
info = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 3))
operationalMode = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: operationalMode.setStatus('current')
if mibBuilder.loadTexts: operationalMode.setDescription('Sets 7586 operational mode - Auto, Manual Stream1, Stream2.')
onlineStream = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: onlineStream.setStatus('current')
if mibBuilder.loadTexts: onlineStream.setDescription('Sets the online stream.')
waveguideSwitch = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: waveguideSwitch.setStatus('current')
if mibBuilder.loadTexts: waveguideSwitch.setDescription('Sets Waveguide switch Rx+Tx, Rx/Tx and Tx Only.')
startupTime = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 50))).setUnits('s').setMaxAccess("readwrite")
if mibBuilder.loadTexts: startupTime.setStatus('current')
if mibBuilder.loadTexts: startupTime.setDescription('Sets Startup time.')
lnbCurrentLimit = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 5), DisplayString()).setUnits('mA').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lnbCurrentLimit.setStatus('current')
if mibBuilder.loadTexts: lnbCurrentLimit.setDescription('Sets LNB current limits.')
ledState = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ledState.setStatus('current')
if mibBuilder.loadTexts: ledState.setDescription('Sets 7586 LED.')
refSource = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: refSource.setStatus('current')
if mibBuilder.loadTexts: refSource.setDescription('Sets 7586 reference state.')
refTrim = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: refTrim.setStatus('current')
if mibBuilder.loadTexts: refTrim.setDescription('Sets 7586 reference trim.')
refThresh = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 9), DisplayString()).setUnits('dBm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: refThresh.setStatus('current')
if mibBuilder.loadTexts: refThresh.setDescription('Sets 7586 reference alarm treshold.')
refPwr = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 10), DisplayString()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: refPwr.setStatus('current')
if mibBuilder.loadTexts: refPwr.setDescription('Gets 7586 reference power.')
ipAddr = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipAddr.setStatus('current')
if mibBuilder.loadTexts: ipAddr.setDescription('Gets the 7586 IP address.')
macAddress = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: macAddress.setStatus('current')
if mibBuilder.loadTexts: macAddress.setDescription('Gets the 7586 MAC address.')
netmask = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: netmask.setStatus('current')
if mibBuilder.loadTexts: netmask.setDescription('Gets the 7586 netmask.')
gateway = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gateway.setStatus('current')
if mibBuilder.loadTexts: gateway.setDescription('Gets the 7586 gateway address.')
lnbCurrent = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 2, 1), DisplayString()).setUnits('mA').setMaxAccess("readonly")
if mibBuilder.loadTexts: lnbCurrent.setStatus('current')
if mibBuilder.loadTexts: lnbCurrent.setDescription('Sets 7586 LNB current.')
lnbVoltage = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 2, 2), DisplayString()).setUnits('V').setMaxAccess("readonly")
if mibBuilder.loadTexts: lnbVoltage.setStatus('current')
if mibBuilder.loadTexts: lnbVoltage.setDescription('Sets 7586 LNB voltage.')
faults = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: faults.setStatus('current')
if mibBuilder.loadTexts: faults.setDescription('Gets the current fault status.')
idInfo = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: idInfo.setStatus('current')
if mibBuilder.loadTexts: idInfo.setDescription('Gets the module firmware revision, serial number and model. This string will have a zero length if the revision is unknown.')
buc1Configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1))
buc1Status = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2))
buc1Info = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 3))
buc2Configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1))
buc2Status = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2))
buc2Info = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 3))
buc1TxSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 1))
buc1PktProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 2))
buc1RCSetting = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 3))
buc1Freqs = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 4))
buc1Misc = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 5))
buc2TxSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 1))
buc2PktProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 2))
buc2RCSetting = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 3))
buc2Freqs = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 4))
buc2Misc = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 5))
buc1TxOn = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc1TxOn.setStatus('current')
if mibBuilder.loadTexts: buc1TxOn.setDescription('Sets Tx on/off. Respond -1 if buc1 not connected.')
buc2TxOn = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc2TxOn.setStatus('current')
if mibBuilder.loadTexts: buc2TxOn.setDescription('Sets Tx on/off. Respond -1 if buc2 not connected.')
buc1TxDefault = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc1TxDefault.setStatus('current')
if mibBuilder.loadTexts: buc1TxDefault.setDescription('Sets Tx default 1-last 0-off. Respond -1 if buc1 not connected.')
buc2TxDefault = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc2TxDefault.setStatus('current')
if mibBuilder.loadTexts: buc2TxDefault.setDescription('Sets Tx default 1-last 0-off. Respond -1 if buc2 not connected.')
buc1TxAttenuator = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setUnits('dBm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc1TxAttenuator.setStatus('current')
if mibBuilder.loadTexts: buc1TxAttenuator.setDescription('Sets/Gets Tx attenuation value in 1dBm steps. Respond -1 if buc1 not connected.')
buc2TxAttenuator = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setUnits('dBm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc2TxAttenuator.setStatus('current')
if mibBuilder.loadTexts: buc2TxAttenuator.setDescription('Sets/Gets Tx attenuation value in 1dBm steps. Respond -1 if buc2 not connected.')
buc1Protocol = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc1Protocol.setStatus('current')
if mibBuilder.loadTexts: buc1Protocol.setDescription('Sets/Gets packet protocol 0 - ASCII, 1 - CODAN, 2 - SAbus, 3 - Comstream, 4 - NDSatcom. Respond -1 if buc1 not connected.')
buc2Protocol = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc2Protocol.setStatus('current')
if mibBuilder.loadTexts: buc2Protocol.setDescription('Sets/Gets packet protocol 0 - ASCII, 1 - CODAN, 2 - SAbus, 3 - Comstream, 4 - NDSatcom. Respond -1 if buc2 not connected.')
buc1Address = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc1Address.setStatus('current')
if mibBuilder.loadTexts: buc1Address.setDescription('Sets/Gets packet address: 0-31 NDSatcom ...Respond -1 if buc1 not connected. ')
buc2Address = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc2Address.setStatus('current')
if mibBuilder.loadTexts: buc2Address.setDescription('Sets/Gets packet address: 0-31 NDSatcom ...Respond -1 if buc2 not connected.')
buc1Mode = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc1Mode.setStatus('current')
if mibBuilder.loadTexts: buc1Mode.setDescription('Sets/Gets redundancy mode 0-none, 1-warm, 2-hot. Respond -1 if buc1 not connected.')
buc2Mode = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc2Mode.setStatus('current')
if mibBuilder.loadTexts: buc2Mode.setDescription('Sets/Gets redundancy mode 0-none, 1-warm, 2-hot. Respond -1 if buc2 not connected.')
buc1OnLine = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 3, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc1OnLine.setStatus('current')
if mibBuilder.loadTexts: buc1OnLine.setDescription('Sets/Gets redundancy mode on on/off line state. Respond -1 if buc1 not connected.')
buc2OnLine = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 3, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc2OnLine.setStatus('current')
if mibBuilder.loadTexts: buc2OnLine.setDescription('Sets/Gets redundancy mode on on/off line state. Respond -1 if buc2 not connected.')
buc1RFFreq = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 4, 1), Integer32()).setUnits('MHz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc1RFFreq.setStatus('current')
if mibBuilder.loadTexts: buc1RFFreq.setDescription('Sets/Gets the RBUC RF frequency. Respond -1 if buc1 not connected.')
buc2RFFreq = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 4, 1), Integer32()).setUnits('MHz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc2RFFreq.setStatus('current')
if mibBuilder.loadTexts: buc2RFFreq.setDescription('Sets/Gets the RBUC RF frequency. Respond -1 if buc2 not connected.')
buc1IFFreq = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 4, 2), Integer32()).setUnits('MHz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc1IFFreq.setStatus('current')
if mibBuilder.loadTexts: buc1IFFreq.setDescription('Sets/Gets the RBUC IF frequency. Respond -1 if buc1 not connected.')
buc2IFFreq = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 4, 2), Integer32()).setUnits('MHz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc2IFFreq.setStatus('current')
if mibBuilder.loadTexts: buc2IFFreq.setDescription('Sets/Gets the RBUC IF frequency. Respond -1 if buc2 not connected.')
buc1LOFreq = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 4, 3), Integer32()).setUnits('MHz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc1LOFreq.setStatus('current')
if mibBuilder.loadTexts: buc1LOFreq.setDescription('Sets/Gets the RBUC LO frequency. Respond -1 if buc1 not connected.')
buc2LOFreq = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 4, 3), Integer32()).setUnits('MHz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc2LOFreq.setStatus('current')
if mibBuilder.loadTexts: buc2LOFreq.setDescription('Sets/Gets the RBUC LO frequency. Respond -1 if buc2 not connected.')
buc1SerIf = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 5, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc1SerIf.setStatus('current')
if mibBuilder.loadTexts: buc1SerIf.setDescription('Sets/Gets serial interface - rate, length, parity, stop, terminate RS422/485. **** No respond - message if buc1 not connected.')
buc2SerIf = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 5, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc2SerIf.setStatus('current')
if mibBuilder.loadTexts: buc2SerIf.setDescription('Sets/Gets serial interface - rate, length, parity, stop, terminate RS422/485. **** No respond - message if buc2 not connected.')
buc1PwrAlarmThresh = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 5, 2), DisplayString()).setUnits('dB').setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc1PwrAlarmThresh.setStatus('current')
if mibBuilder.loadTexts: buc1PwrAlarmThresh.setDescription('Sets/Gets power alarm threshold. **** No respond - message if buc1 not connected.')
buc2PwrAlarmThresh = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 5, 2), DisplayString()).setUnits('dB').setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc2PwrAlarmThresh.setStatus('current')
if mibBuilder.loadTexts: buc2PwrAlarmThresh.setDescription('Sets/Gets power alarm threshold. **** No respond - message if buc2 not connected.')
buc1BurstPwrThresh = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 5, 3), DisplayString()).setUnits('dB').setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc1BurstPwrThresh.setStatus('current')
if mibBuilder.loadTexts: buc1BurstPwrThresh.setDescription('Sets/Gets burst power threshold. **** No respond - message if buc1 not connected.')
buc2BurstPwrThresh = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 5, 3), DisplayString()).setUnits('dB').setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc2BurstPwrThresh.setStatus('current')
if mibBuilder.loadTexts: buc2BurstPwrThresh.setDescription('Sets/Gets burst power threshold. **** No respond - message if buc2 not connected.')
buc1RefSource = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 5, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc1RefSource.setStatus('current')
if mibBuilder.loadTexts: buc1RefSource.setDescription('Sets/Gets reference source 0-external, 1-internal (Only for RBUC). **** No respond - message if buc1 not connected.')
buc2RefSource = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 5, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc2RefSource.setStatus('current')
if mibBuilder.loadTexts: buc2RefSource.setDescription('Sets/Gets reference source 0-external, 1-internal (Only for RBUC). **** No respond - message if buc2 not connected.')
buc1LEDState = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 5, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc1LEDState.setStatus('current')
if mibBuilder.loadTexts: buc1LEDState.setDescription('Sets/Gets LEDs status on/off (Only for RBUC). **** No respond - message if buc1 not connected.')
buc2LEDState = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 5, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: buc2LEDState.setStatus('current')
if mibBuilder.loadTexts: buc2LEDState.setDescription('Sets/Gets LEDs status on/off (Only for RBUC). **** No respond - message if buc2 not connected.')
buc1PaStatus = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc1PaStatus.setStatus('current')
if mibBuilder.loadTexts: buc1PaStatus.setDescription('Gets to 1 when PA is on. Respond -1 if buc1 not connected.')
buc2PaStatus = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc2PaStatus.setStatus('current')
if mibBuilder.loadTexts: buc2PaStatus.setDescription('Gets to 1 when PA is on. Respond -1 if buc2 not connected.')
buc1TxPower = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 2), DisplayString()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: buc1TxPower.setStatus('current')
if mibBuilder.loadTexts: buc1TxPower.setDescription('Gets Tx power format x.x dB. **** No respond - message if buc1 not connected.')
buc2TxPower = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 2), DisplayString()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: buc2TxPower.setStatus('current')
if mibBuilder.loadTexts: buc2TxPower.setDescription('Gets Tx power format x.x dB. **** No respond - message if buc2 not connected.')
buc1TxBurstPower = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 3), DisplayString()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: buc1TxBurstPower.setStatus('current')
if mibBuilder.loadTexts: buc1TxBurstPower.setDescription('Gets Tx power. Format is x.x,y.y,z.z, where x.x is current burst power, y.y is min and z.z is max burts power. **** No respond - message if buc1 not connected.')
buc2TxBurstPower = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 3), DisplayString()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: buc2TxBurstPower.setStatus('current')
if mibBuilder.loadTexts: buc2TxBurstPower.setDescription('Gets Tx power. Format is x.x,y.y,z.z, where x.x is current burst power, y.y is min and z.z is max burts power. **** No respond - message if buc2 not connected.')
buc1Faults = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc1Faults.setStatus('current')
if mibBuilder.loadTexts: buc1Faults.setDescription("Gets the current fault status. Format - Bit0 PA fault, Bit1 Fan fault, Bit2 Power fault, Bit3 Temp fault, Bit4 10MHz fault, Bit5 Internal fault Bit6 LNB fault, Bit7 Red'cy Cont fault. Respond -1 if buc2 not connected.")
buc2Faults = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc2Faults.setStatus('current')
if mibBuilder.loadTexts: buc2Faults.setDescription("Gets the current fault status. Format - Bit0 PA fault, Bit1 Fan fault, Bit2 Power fault, Bit3 Temp fault, Bit4 10MHz fault, Bit5 Internal fault Bit6 LNB fault, Bit7 Red'cy Cont fault. Respond -1 if buc2 not connected.")
buc1LatchedFaults = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc1LatchedFaults.setStatus('current')
if mibBuilder.loadTexts: buc1LatchedFaults.setDescription('Gets the current latched faults. Format is same as Faults. Respond -1 if buc2 not connected.')
buc2LatchedFaults = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc2LatchedFaults.setStatus('current')
if mibBuilder.loadTexts: buc2LatchedFaults.setDescription('Gets the current latched faults. Format is same as Faults. Respond -1 if buc2 not connected.')
buc1Temperature = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc1Temperature.setStatus('current')
if mibBuilder.loadTexts: buc1Temperature.setDescription('Gets the BUC temperature. Format is x.x. **** No respond - message if buc1 not connected.')
buc2Temperature = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc2Temperature.setStatus('current')
if mibBuilder.loadTexts: buc2Temperature.setDescription('Gets the BUC temperature. Format is x.x. **** No respond - message if buc2 not connected.')
buc1MinMaxTemperature = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc1MinMaxTemperature.setStatus('current')
if mibBuilder.loadTexts: buc1MinMaxTemperature.setDescription('Gets the BUC temperature. Format is x.x,y.y where x.x is max and y.y is min temperature. **** No respond - message if buc1 not connected.')
buc2MinMaxTemperature = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc2MinMaxTemperature.setStatus('current')
if mibBuilder.loadTexts: buc2MinMaxTemperature.setDescription('Gets the BUC temperature. Format is x.x,y.y where x.x is max and y.y is min temperature. **** No respond - message if buc2 not connected.')
buc1SystemSetting = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2047))).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc1SystemSetting.setStatus('current')
if mibBuilder.loadTexts: buc1SystemSetting.setDescription('Gets the current system status. Format is Bit0 - PA state, Bit1 - RS232 Tx, Bit2 - FSK Tx, Bit3 - RS485 Tx Bit4 - Redundancy mode, Bit5 - Online, Bit6..Bit7 - Redundancy cold or hot mode, Bit8 - HTTP Tx, Bit9 - TELNET Tx, Bit10 - SNMP Tx. Respond -1 if buc1 not connected.')
buc2SystemSetting = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2047))).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc2SystemSetting.setStatus('current')
if mibBuilder.loadTexts: buc2SystemSetting.setDescription('Gets the current system status. Format is Bit0 - PA state, Bit1 - RS232 Tx, Bit2 - FSK Tx, Bit3 - RS485 Tx Bit4 - Redundancy mode, Bit5 - Online, Bit6..Bit7 - Redundancy cold or hot mode, Bit8 - HTTP Tx, Bit9 - TELNET Tx, Bit10 - SNMP Tx. Respond -1 if buc2 not connected.')
buc1SystemPoll = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc1SystemPoll.setStatus('current')
if mibBuilder.loadTexts: buc1SystemPoll.setDescription('Gets the system poll status. Format is Bit0 - Fault, Bit1 - System change. Respond -1 if buc1 not connected.')
buc2SystemPoll = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc2SystemPoll.setStatus('current')
if mibBuilder.loadTexts: buc2SystemPoll.setDescription('Gets the system poll status. Format is Bit0 - Fault, Bit1 - System change. Respond -1 if buc2 not connected.')
buc1DeviceType = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc1DeviceType.setStatus('current')
if mibBuilder.loadTexts: buc1DeviceType.setDescription('Gets the device type. Format is X,Y where X is the model and Y is software version. **** No respond - message if buc1 not connected.')
buc2DeviceType = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc2DeviceType.setStatus('current')
if mibBuilder.loadTexts: buc2DeviceType.setDescription('Gets the device type. Format is X,Y where X is the model and Y is software version. **** No respond - message if buc2 not connected.')
buc1Gateway = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc1Gateway.setStatus('current')
if mibBuilder.loadTexts: buc1Gateway.setDescription('Gets the BUC gateway address (Only for RBUC). **** No respond - message if buc1 not connected.')
buc2Gateway = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc2Gateway.setStatus('current')
if mibBuilder.loadTexts: buc2Gateway.setDescription('Gets the BUC gateway address (Only for RBUC). **** No respond - message if buc2 not connected.')
buc1IpAddress = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc1IpAddress.setStatus('current')
if mibBuilder.loadTexts: buc1IpAddress.setDescription('Gets the BUC IP address (Only for RBUC). **** No respond - message if buc1 not connected.')
buc2IpAddress = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc2IpAddress.setStatus('current')
if mibBuilder.loadTexts: buc2IpAddress.setDescription('Gets the BUC IP address (Only for RBUC). **** No respond - message if buc2 not connected.')
buc1MACAddress = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc1MACAddress.setStatus('current')
if mibBuilder.loadTexts: buc1MACAddress.setDescription('Gets the BUC MAC address (Only for RBUC). **** No respond - message if buc1 not connected.')
buc2MACAddress = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc2MACAddress.setStatus('current')
if mibBuilder.loadTexts: buc2MACAddress.setDescription('Gets the BUC MAC address (Only for RBUC). **** No respond - message if buc2 not connected.')
buc1Netmask = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc1Netmask.setStatus('current')
if mibBuilder.loadTexts: buc1Netmask.setDescription('Gets the BUC netmask (Only for RBUC). **** No respond - message if buc1 not connected.')
buc2Netmask = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc2Netmask.setStatus('current')
if mibBuilder.loadTexts: buc2Netmask.setDescription('Gets the BUC netmask (Only for RBUC). **** No respond - message if buc2 not connected.')
buc1RefPower = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc1RefPower.setStatus('current')
if mibBuilder.loadTexts: buc1RefPower.setDescription('Gets the BUC reference power. **** No respond - message if buc1 not connected.')
buc2RefPower = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc2RefPower.setStatus('current')
if mibBuilder.loadTexts: buc2RefPower.setDescription('Gets the BUC reference power. **** No respond - message if buc2 not connected.')
buc1Config = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc1Config.setStatus('current')
if mibBuilder.loadTexts: buc1Config.setDescription('Gets the BUC configuration. **** No respond - message if buc1 not connected.')
buc2Config = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc2Config.setStatus('current')
if mibBuilder.loadTexts: buc2Config.setDescription('Gets the BUC configuration. **** No respond - message if buc2 not connected.')
buc1BuildStandard = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc1BuildStandard.setStatus('current')
if mibBuilder.loadTexts: buc1BuildStandard.setDescription('Gets the BUC build standard. **** No respond - message if buc1 not connected.')
buc2BuildStandard = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc2BuildStandard.setStatus('current')
if mibBuilder.loadTexts: buc2BuildStandard.setDescription('Gets the BUC build standard. **** No respond - message if buc2 not connected.')
buc1IdInfo = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc1IdInfo.setStatus('current')
if mibBuilder.loadTexts: buc1IdInfo.setDescription('Gets the module firmware revision, serial number and model. This string will have a zero length if the revision is unknown. **** No respond - message if buc1 not connected.')
buc2IdInfo = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc2IdInfo.setStatus('current')
if mibBuilder.loadTexts: buc2IdInfo.setDescription('Gets the module firmware revision, serial number and model. This string will have a zero length if the revision is unknown. **** No respond - message if buc2 not connected.')
buc1Limits = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 3, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc1Limits.setStatus('current')
if mibBuilder.loadTexts: buc1Limits.setDescription('Gets the limit data for the BUC. Format is: Power meter MIN/MAX , IF,RF and LO frequencies. This string will have a zero length if the revision is unknown. **** No respond - message if buc1 not connected.')
buc2Limits = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 3, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc2Limits.setStatus('current')
if mibBuilder.loadTexts: buc2Limits.setDescription('Gets the limit data for the BUC. Format is: Power meter MIN/MAX , IF,RF and LO frequencies. This string will have a zero length if the revision is unknown. **** No respond - message if buc2 not connected.')
buc1PktProtocolsInfo = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 3, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc1PktProtocolsInfo.setStatus('current')
if mibBuilder.loadTexts: buc1PktProtocolsInfo.setDescription('Gets supported packet protocols and the corresponding address ranges. **** No respond - message if buc1 not connected.')
buc2PktProtocolsInfo = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 3, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buc2PktProtocolsInfo.setStatus('current')
if mibBuilder.loadTexts: buc2PktProtocolsInfo.setDescription('Gets supported packet protocols and the corresponding address ranges. **** No respond - message if buc2 not connected.')
mibBuilder.exportSymbols("RC7586-MIB", buc1IFFreq=buc1IFFreq, buc2Faults=buc2Faults, buc2Gateway=buc2Gateway, buc2RCSetting=buc2RCSetting, ledState=ledState, buc1TxOn=buc1TxOn, buc2SystemPoll=buc2SystemPoll, buc2RFFreq=buc2RFFreq, buc1PaStatus=buc1PaStatus, buc2TxDefault=buc2TxDefault, buc1Status=buc1Status, macAddress=macAddress, buc1LOFreq=buc1LOFreq, buc2IdInfo=buc2IdInfo, buc1Limits=buc1Limits, lnbCurrent=lnbCurrent, status=status, refThresh=refThresh, faults=faults, buc1OnLine=buc1OnLine, buc1Faults=buc1Faults, buc1Misc=buc1Misc, buc2Netmask=buc2Netmask, buc1SystemSetting=buc1SystemSetting, onlineStream=onlineStream, buc1Protocol=buc1Protocol, buc1LatchedFaults=buc1LatchedFaults, buc2Protocol=buc2Protocol, buc1DeviceType=buc1DeviceType, buc1Temperature=buc1Temperature, buc1Config=buc1Config, buc1RCSetting=buc1RCSetting, buc2OnLine=buc2OnLine, buc1SerIf=buc1SerIf, buc1TxPower=buc1TxPower, buc2=buc2, buc1Mode=buc1Mode, buc2TxBurstPower=buc2TxBurstPower, PYSNMP_MODULE_ID=rc7586MIB, refPwr=refPwr, ipAddr=ipAddr, buc1BurstPwrThresh=buc1BurstPwrThresh, buc1PktProtocolsInfo=buc1PktProtocolsInfo, buc1TxBurstPower=buc1TxBurstPower, buc1IpAddress=buc1IpAddress, buc2IpAddress=buc2IpAddress, buc2RefSource=buc2RefSource, buc2Misc=buc2Misc, buc2PaStatus=buc2PaStatus, buc2Temperature=buc2Temperature, buc2Configuration=buc2Configuration, buc2LOFreq=buc2LOFreq, buc2TxSettings=buc2TxSettings, buc2TxAttenuator=buc2TxAttenuator, buc2SystemSetting=buc2SystemSetting, buc2Freqs=buc2Freqs, buc2Config=buc2Config, buc1Freqs=buc1Freqs, buc2BuildStandard=buc2BuildStandard, buc2RefPower=buc2RefPower, buc1Gateway=buc1Gateway, buc2Status=buc2Status, buc2LEDState=buc2LEDState, lnbCurrentLimit=lnbCurrentLimit, buc2MinMaxTemperature=buc2MinMaxTemperature, buc1TxAttenuator=buc1TxAttenuator, buc2PktProtocol=buc2PktProtocol, buc2MACAddress=buc2MACAddress, info=info, buc2TxOn=buc2TxOn, operationalMode=operationalMode, buc1Netmask=buc1Netmask, buc1Address=buc1Address, buc2PktProtocolsInfo=buc2PktProtocolsInfo, buc1RefSource=buc1RefSource, idInfo=idInfo, ctrl=ctrl, buc1=buc1, buc1BuildStandard=buc1BuildStandard, buc2Limits=buc2Limits, buc1Info=buc1Info, buc1MACAddress=buc1MACAddress, buc2DeviceType=buc2DeviceType, waveguideSwitch=waveguideSwitch, buc2TxPower=buc2TxPower, buc2PwrAlarmThresh=buc2PwrAlarmThresh, buc2Info=buc2Info, refTrim=refTrim, buc2Mode=buc2Mode, refSource=refSource, buc1PwrAlarmThresh=buc1PwrAlarmThresh, FaultStatus7586=FaultStatus7586, buc1MinMaxTemperature=buc1MinMaxTemperature, buc1SystemPoll=buc1SystemPoll, buc2BurstPwrThresh=buc2BurstPwrThresh, buc1Configuration=buc1Configuration, buc2IFFreq=buc2IFFreq, buc1RefPower=buc1RefPower, buc1TxDefault=buc1TxDefault, settings=settings, buc2LatchedFaults=buc2LatchedFaults, lnbVoltage=lnbVoltage, buc1RFFreq=buc1RFFreq, ComponentRevision=ComponentRevision, rc7586MIB=rc7586MIB, buc1TxSettings=buc1TxSettings, buc1LEDState=buc1LEDState, buc1PktProtocol=buc1PktProtocol, buc2SerIf=buc2SerIf, gateway=gateway, buc2Address=buc2Address, startupTime=startupTime, buc1IdInfo=buc1IdInfo, netmask=netmask)
