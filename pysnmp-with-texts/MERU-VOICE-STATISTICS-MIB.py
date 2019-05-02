#
# PySNMP MIB module MERU-VOICE-STATISTICS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MERU-VOICE-STATISTICS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:11:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
mwStatistics, = mibBuilder.importSymbols("MERU-SMI", "mwStatistics")
MwlDeviceType, MwlNetProtocol, MwlOnOffSwitch, MwlQosCallState, MwlQosProtocol = mibBuilder.importSymbols("MERU-TC", "MwlDeviceType", "MwlNetProtocol", "MwlOnOffSwitch", "MwlQosCallState", "MwlQosProtocol")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, Unsigned32, Counter32, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, ObjectIdentity, Counter64, Gauge32, ModuleIdentity, Integer32, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Unsigned32", "Counter32", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "ObjectIdentity", "Counter64", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "IpAddress")
RowStatus, TimeInterval, DateAndTime, TruthValue, MacAddress, TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TimeInterval", "DateAndTime", "TruthValue", "MacAddress", "TimeStamp", "DisplayString", "TextualConvention")
mwVoiceStatistics = ModuleIdentity((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3))
if mibBuilder.loadTexts: mwVoiceStatistics.setLastUpdated('200506050000Z')
if mibBuilder.loadTexts: mwVoiceStatistics.setOrganization('Meru Networks')
if mibBuilder.loadTexts: mwVoiceStatistics.setContactInfo('support@merunetworks.com')
if mibBuilder.loadTexts: mwVoiceStatistics.setDescription('This MIB defines all the managed objects used to manage the Meru WLAN Voice Statistics infrastructure')
mwPhoneTable = MibTable((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 1), )
if mibBuilder.loadTexts: mwPhoneTable.setStatus('current')
if mibBuilder.loadTexts: mwPhoneTable.setDescription('This object describes Phone Table ')
mwPhoneEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 1, 1), ).setIndexNames((0, "MERU-VOICE-STATISTICS-MIB", "mwPhoneTableIndex"))
if mibBuilder.loadTexts: mwPhoneEntry.setStatus('current')
if mibBuilder.loadTexts: mwPhoneEntry.setDescription('This object describes Phone Table ')
mwPhoneTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: mwPhoneTableIndex.setStatus('current')
if mibBuilder.loadTexts: mwPhoneTableIndex.setDescription('The index value of the table ')
mwPhoneIp = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPhoneIp.setStatus('current')
if mibBuilder.loadTexts: mwPhoneIp.setDescription('This object describes IP Address')
mwPhoneAp = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPhoneAp.setStatus('current')
if mibBuilder.loadTexts: mwPhoneAp.setDescription('This object describes AP ID')
mwPhoneMac = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPhoneMac.setStatus('current')
if mibBuilder.loadTexts: mwPhoneMac.setDescription('This object describes Mac Address')
mwPhoneType = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 1, 1, 5), MwlQosProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPhoneType.setStatus('current')
if mibBuilder.loadTexts: mwPhoneType.setDescription('This object describes Protocol Type')
mwPhoneApName = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPhoneApName.setStatus('current')
if mibBuilder.loadTexts: mwPhoneApName.setDescription('This object describes AP Name')
mwPhoneServer = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPhoneServer.setStatus('current')
if mibBuilder.loadTexts: mwPhoneServer.setDescription('This object describes Server')
mwPhoneUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPhoneUsername.setStatus('current')
if mibBuilder.loadTexts: mwPhoneUsername.setDescription('This object describes Username')
mwPhoneTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 1, 1, 9), MwlNetProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPhoneTransport.setStatus('current')
if mibBuilder.loadTexts: mwPhoneTransport.setDescription('This object describes Transport')
mwPhoneDeviceType = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 1, 1, 10), MwlDeviceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPhoneDeviceType.setStatus('current')
if mibBuilder.loadTexts: mwPhoneDeviceType.setDescription('This object describes Device Type')
mwPhoneCallTable = MibTable((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2), )
if mibBuilder.loadTexts: mwPhoneCallTable.setStatus('current')
if mibBuilder.loadTexts: mwPhoneCallTable.setDescription('This object describes Phone Call Table ')
mwPhoneCallEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1), ).setIndexNames((0, "MERU-VOICE-STATISTICS-MIB", "mwPhoneCallTableIndex"))
if mibBuilder.loadTexts: mwPhoneCallEntry.setStatus('current')
if mibBuilder.loadTexts: mwPhoneCallEntry.setDescription('This object describes Phone Call Table ')
mwPhoneCallTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: mwPhoneCallTableIndex.setStatus('current')
if mibBuilder.loadTexts: mwPhoneCallTableIndex.setDescription('The index value of the table ')
mwPhoneCallToIp = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPhoneCallToIp.setStatus('current')
if mibBuilder.loadTexts: mwPhoneCallToIp.setDescription('This object describes To IP Address')
mwPhoneCallToAp = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPhoneCallToAp.setStatus('current')
if mibBuilder.loadTexts: mwPhoneCallToAp.setDescription('This object describes To AP ID')
mwPhoneCallType = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 4), MwlQosProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPhoneCallType.setStatus('current')
if mibBuilder.loadTexts: mwPhoneCallType.setDescription('This object describes Protocol Type')
mwPhoneCallToMac = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPhoneCallToMac.setStatus('current')
if mibBuilder.loadTexts: mwPhoneCallToMac.setDescription('This object describes To MAC Address')
mwPhoneCallState = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 6), MwlQosCallState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPhoneCallState.setStatus('current')
if mibBuilder.loadTexts: mwPhoneCallState.setDescription('This object describes Call state')
mwPhoneCallFromIp = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPhoneCallFromIp.setStatus('current')
if mibBuilder.loadTexts: mwPhoneCallFromIp.setDescription('This object describes From IP Address')
mwPhoneCallFromAp = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPhoneCallFromAp.setStatus('current')
if mibBuilder.loadTexts: mwPhoneCallFromAp.setDescription('This object describes From AP ID')
mwPhoneCallFromMac = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 9), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPhoneCallFromMac.setStatus('current')
if mibBuilder.loadTexts: mwPhoneCallFromMac.setDescription('This object describes From MAC Address')
mwPhoneCallToApName = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPhoneCallToApName.setStatus('current')
if mibBuilder.loadTexts: mwPhoneCallToApName.setDescription('This object describes To AP Name')
mwPhoneCallToFlowtag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPhoneCallToFlowtag.setStatus('current')
if mibBuilder.loadTexts: mwPhoneCallToFlowtag.setDescription('This object describes To Flow Tag')
mwPhoneCallToPending = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 12), MwlOnOffSwitch()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPhoneCallToPending.setStatus('current')
if mibBuilder.loadTexts: mwPhoneCallToPending.setDescription('This object describes To Qos Pending')
mwPhoneCallFromApName = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPhoneCallFromApName.setStatus('current')
if mibBuilder.loadTexts: mwPhoneCallFromApName.setDescription('This object describes From AP Name')
mwPhoneCallToUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPhoneCallToUsername.setStatus('current')
if mibBuilder.loadTexts: mwPhoneCallToUsername.setDescription('This object describes To Username')
mwPhoneCallFromFlowtag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPhoneCallFromFlowtag.setStatus('current')
if mibBuilder.loadTexts: mwPhoneCallFromFlowtag.setDescription('This object describes From Flow Tag')
mwPhoneCallFromPending = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 16), MwlOnOffSwitch()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPhoneCallFromPending.setStatus('current')
if mibBuilder.loadTexts: mwPhoneCallFromPending.setDescription('This object describes From Qos Pending')
mwPhoneCallFromUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPhoneCallFromUsername.setStatus('current')
if mibBuilder.loadTexts: mwPhoneCallFromUsername.setDescription('This object describes From Username')
mwVoiceStatusTable = MibTable((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 3), )
if mibBuilder.loadTexts: mwVoiceStatusTable.setStatus('current')
if mibBuilder.loadTexts: mwVoiceStatusTable.setDescription('This object describes Voice Status Table ')
mwVoiceStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 3, 1), ).setIndexNames((0, "MERU-VOICE-STATISTICS-MIB", "mwVoiceStatusTableIndex"))
if mibBuilder.loadTexts: mwVoiceStatusEntry.setStatus('current')
if mibBuilder.loadTexts: mwVoiceStatusEntry.setDescription('This object describes Voice Status Table ')
mwVoiceStatusTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: mwVoiceStatusTableIndex.setStatus('current')
if mibBuilder.loadTexts: mwVoiceStatusTableIndex.setDescription('The index value of the table ')
mwVoiceStatusAp = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwVoiceStatusAp.setStatus('current')
if mibBuilder.loadTexts: mwVoiceStatusAp.setDescription('This object describes AP ID')
mwVoiceStatusApName = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwVoiceStatusApName.setStatus('current')
if mibBuilder.loadTexts: mwVoiceStatusApName.setDescription('This object describes AP Name')
mwVoiceStatusPhoneCount = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwVoiceStatusPhoneCount.setStatus('current')
if mibBuilder.loadTexts: mwVoiceStatusPhoneCount.setDescription('This object describes Phone Count')
mwVoiceStatusRejectCount = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 3, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwVoiceStatusRejectCount.setStatus('current')
if mibBuilder.loadTexts: mwVoiceStatusRejectCount.setDescription('This object describes Call Rejected Count')
mwVoiceStatusActiveCallCount = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwVoiceStatusActiveCallCount.setStatus('current')
if mibBuilder.loadTexts: mwVoiceStatusActiveCallCount.setDescription('This object describes Active Call Count')
mwVoiceStatusPendingCallCount = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwVoiceStatusPendingCallCount.setStatus('current')
if mibBuilder.loadTexts: mwVoiceStatusPendingCallCount.setDescription('This object describes Qos Pending Call Count')
mibBuilder.exportSymbols("MERU-VOICE-STATISTICS-MIB", mwPhoneCallType=mwPhoneCallType, mwPhoneApName=mwPhoneApName, mwPhoneCallToMac=mwPhoneCallToMac, mwPhoneTable=mwPhoneTable, mwPhoneIp=mwPhoneIp, mwPhoneServer=mwPhoneServer, PYSNMP_MODULE_ID=mwVoiceStatistics, mwPhoneDeviceType=mwPhoneDeviceType, mwPhoneCallTable=mwPhoneCallTable, mwVoiceStatusTableIndex=mwVoiceStatusTableIndex, mwPhoneCallToIp=mwPhoneCallToIp, mwVoiceStatusAp=mwVoiceStatusAp, mwVoiceStatusRejectCount=mwVoiceStatusRejectCount, mwVoiceStatusActiveCallCount=mwVoiceStatusActiveCallCount, mwPhoneEntry=mwPhoneEntry, mwPhoneCallFromApName=mwPhoneCallFromApName, mwPhoneCallToPending=mwPhoneCallToPending, mwPhoneCallToFlowtag=mwPhoneCallToFlowtag, mwPhoneType=mwPhoneType, mwPhoneTableIndex=mwPhoneTableIndex, mwPhoneCallToUsername=mwPhoneCallToUsername, mwPhoneCallFromMac=mwPhoneCallFromMac, mwPhoneCallFromFlowtag=mwPhoneCallFromFlowtag, mwPhoneCallEntry=mwPhoneCallEntry, mwPhoneTransport=mwPhoneTransport, mwVoiceStatistics=mwVoiceStatistics, mwPhoneCallFromAp=mwPhoneCallFromAp, mwVoiceStatusPhoneCount=mwVoiceStatusPhoneCount, mwPhoneUsername=mwPhoneUsername, mwPhoneCallFromIp=mwPhoneCallFromIp, mwVoiceStatusApName=mwVoiceStatusApName, mwPhoneCallFromPending=mwPhoneCallFromPending, mwPhoneCallTableIndex=mwPhoneCallTableIndex, mwVoiceStatusTable=mwVoiceStatusTable, mwPhoneCallToApName=mwPhoneCallToApName, mwPhoneMac=mwPhoneMac, mwPhoneAp=mwPhoneAp, mwPhoneCallFromUsername=mwPhoneCallFromUsername, mwVoiceStatusEntry=mwVoiceStatusEntry, mwVoiceStatusPendingCallCount=mwVoiceStatusPendingCallCount, mwPhoneCallState=mwPhoneCallState, mwPhoneCallToAp=mwPhoneCallToAp)
