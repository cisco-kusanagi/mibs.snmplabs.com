#
# PySNMP MIB module CISCO-DOT11-ASSOCIATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DOT11-ASSOCIATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:38:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
cd11IfAuxSsid, CDot11IfVlanIdOrZero, CDot11IfCipherType = mibBuilder.importSymbols("CISCO-DOT11-IF-MIB", "cd11IfAuxSsid", "CDot11IfVlanIdOrZero", "CDot11IfCipherType")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Gauge32, ObjectIdentity, Counter32, Unsigned32, IpAddress, Integer32, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Gauge32", "ObjectIdentity", "Counter32", "Unsigned32", "IpAddress", "Integer32", "Counter64", "iso")
TextualConvention, MacAddress, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString", "TruthValue")
ciscoDot11AssociationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 273))
ciscoDot11AssociationMIB.setRevisions(('2007-01-05 00:00', '2006-06-12 00:00', '2005-03-08 00:00', '2004-11-28 00:00', '2004-10-18 00:00', '2004-02-19 00:00', '2003-07-27 00:00', '2003-04-11 00:00', '2003-01-29 00:00', '2002-07-15 00:00', '2002-04-17 00:00', '2002-03-06 00:00',))
if mibBuilder.loadTexts: ciscoDot11AssociationMIB.setLastUpdated('200701050000Z')
if mibBuilder.loadTexts: ciscoDot11AssociationMIB.setOrganization('Cisco Systems Inc.')
ciscoDot11AssocMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 273, 1))
cDot11AssociationGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1))
cDot11ClientConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2))
cDot11ClientStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3))
class CDot11ClientRoleClassType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("clientStation", 0), ("repeater", 1), ("accessPoint", 2), ("bridgeHost", 3), ("bridge", 4), ("bridgeRoot", 5), ("ethernetClient", 6))

class CDot11ClientDevType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 76, 77, 84, 85, 86, 101, 102, 104, 109, 110, 111, 112, 117, 123, 124, 127, 128, 129, 130, 132, 133, 134, 135, 136, 137, 138, 139, 140))
    namedValues = NamedValues(("unknown", 1), ("ethernetAP", 76), ("ethernetBridge", 77), ("pc3000Client", 84), ("serialUC", 85), ("ethernetUC", 86), ("pc3500Client", 101), ("pc4500Client", 102), ("generic80211Client", 104), ("pc4800Client", 109), ("pc3100Client", 110), ("mc", 111), ("ethernetClient", 112), ("pc4800bClient", 117), ("wgbNoDiversity", 123), ("wgb", 124), ("series350Client", 127), ("series370Client", 128), ("c1100SeriesAP", 129), ("c1410SeriesBridge", 130), ("c1200SeriesAP", 132), ("mp2xClient", 133), ("c350SeriesAP", 134), ("cb21agClient", 135), ("radioKodiak", 136), ("c1130SeriesAP", 137), ("c1310SeriesBridge", 138), ("c7920phone", 139), ("c1240SeriesAP", 140))

class CDot11ClientRadioType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 6, 12, 13, 33, 34, 35, 36, 37, 38, 39, 40, 46))
    namedValues = NamedValues(("unknown", 1), ("ccxClient", 2), ("pc3500", 3), ("pc3000", 4), ("pc4500", 6), ("pc4800", 12), ("pc3100", 13), ("series340", 33), ("series350", 34), ("series370", 35), ("bridge1410", 36), ("mp2xSeries", 37), ("rm2xSeries", 38), ("rm2gSeries", 39), ("mp2xMAR", 40), ("cb21ag", 46))

class CDot11AuthenticationMethod(TextualConvention, Integer32):
    reference = 'IEEE Std 802.11-Jan 14 1999, Wireless LAN Medium Access Control and Physical Layer Specifications, LAN MAN Standards Committee of the IEEE Computer Society, IEEE802dot11-MIB, dot11AuthenticationAlgorithm.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 129))
    namedValues = NamedValues(("open", 1), ("sharedKey", 2), ("networkEap", 129))

class CDot11AdditionalAuthenMethod(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("mac", 0), ("eap", 1))

class CDot11Dot1xAuthenMethod(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("md5", 0), ("leap", 1), ("peap", 2), ("eapTls", 3), ("eapSim", 4), ("eapFast", 5))

class CDot11KeyManagementMethod(TextualConvention, Bits):
    status = 'deprecated'
    namedValues = NamedValues(("wpa", 0), ("cckm", 1))

class CDot11NewKeyManagementMethod(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("cckm", 0), ("wpa1", 1), ("wpa2", 2))

cDot11ParentAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ParentAddress.setStatus('current')
cDot11ActiveDevicesTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 2), )
if mibBuilder.loadTexts: cDot11ActiveDevicesTable.setStatus('current')
cDot11ActiveDevicesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cDot11ActiveDevicesEntry.setStatus('current')
cDot11ActiveWirelessClients = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 2, 1, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 2007))).setUnits('Device').setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ActiveWirelessClients.setStatus('current')
cDot11ActiveBridges = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 2, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 2007))).setUnits('Device').setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ActiveBridges.setStatus('current')
cDot11ActiveRepeaters = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 2, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 2007))).setUnits('Device').setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ActiveRepeaters.setStatus('current')
cDot11AssociationStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 3), )
if mibBuilder.loadTexts: cDot11AssociationStatsTable.setStatus('current')
cDot11AssociationStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cDot11AssociationStatsEntry.setStatus('current')
cDot11AssStatsAssociated = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 3, 1, 1), Counter32()).setUnits('client').setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11AssStatsAssociated.setStatus('current')
cDot11AssStatsAuthenticated = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 3, 1, 2), Counter32()).setUnits('client').setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11AssStatsAuthenticated.setStatus('current')
cDot11AssStatsRoamedIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 3, 1, 3), Counter32()).setUnits('client').setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11AssStatsRoamedIn.setStatus('current')
cDot11AssStatsRoamedAway = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 3, 1, 4), Counter32()).setUnits('client').setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11AssStatsRoamedAway.setStatus('current')
cDot11AssStatsDeauthenticated = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 3, 1, 5), Counter32()).setUnits('client').setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11AssStatsDeauthenticated.setStatus('current')
cDot11AssStatsDisassociated = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 3, 1, 6), Counter32()).setUnits('client').setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11AssStatsDisassociated.setStatus('current')
cd11IfCipherStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 4), )
if mibBuilder.loadTexts: cd11IfCipherStatsTable.setStatus('current')
cd11IfCipherStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cd11IfCipherStatsEntry.setStatus('current')
cd11IfCipherMicFailClientAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 4, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cd11IfCipherMicFailClientAddress.setStatus('current')
cd11IfCipherTkipLocalMicFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cd11IfCipherTkipLocalMicFailures.setStatus('current')
cd11IfCipherTkipRemotMicFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cd11IfCipherTkipRemotMicFailures.setStatus('current')
cd11IfCipherTkipCounterMeasInvok = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cd11IfCipherTkipCounterMeasInvok.setStatus('current')
cd11IfCipherCcmpReplaysDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cd11IfCipherCcmpReplaysDiscarded.setStatus('current')
cd11IfCipherTkipReplaysDetected = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cd11IfCipherTkipReplaysDetected.setStatus('current')
cDot11ClientConfigInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1), )
if mibBuilder.loadTexts: cDot11ClientConfigInfoTable.setStatus('current')
cDot11ClientConfigInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-DOT11-IF-MIB", "cd11IfAuxSsid"), (0, "CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientAddress"))
if mibBuilder.loadTexts: cDot11ClientConfigInfoEntry.setStatus('current')
cDot11ClientAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: cDot11ClientAddress.setStatus('current')
cDot11ClientParentAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientParentAddress.setStatus('current')
cDot11ClientRoleClassType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 3), CDot11ClientRoleClassType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientRoleClassType.setStatus('current')
cDot11ClientDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 4), CDot11ClientDevType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientDevType.setStatus('current')
cDot11ClientRadioType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 5), CDot11ClientRadioType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientRadioType.setStatus('current')
cDot11ClientWepEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientWepEnabled.setStatus('current')
cDot11ClientWepKeyMixEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientWepKeyMixEnabled.setStatus('current')
cDot11ClientMicEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 8), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientMicEnabled.setStatus('current')
cDot11ClientPowerSaveMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("powersave", 2))).clone('active')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientPowerSaveMode.setStatus('current')
cDot11ClientAid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2008))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientAid.setStatus('current')
cDot11ClientDataRateSet = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 126))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientDataRateSet.setStatus('current')
cDot11ClientSoftwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 12), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientSoftwareVersion.setStatus('current')
cDot11ClientName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 13), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientName.setStatus('current')
cDot11ClientAssociationState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("initial", 1), ("authenNotAssociated", 2), ("assocAndAuthenticated", 3), ("assocNotAnuthenticated", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientAssociationState.setStatus('current')
cDot11ClientIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 15), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientIpAddressType.setStatus('current')
cDot11ClientIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 16), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientIpAddress.setStatus('current')
cDot11ClientVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 17), CDot11IfVlanIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientVlanId.setStatus('current')
cDot11ClientSubIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 18), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientSubIfIndex.setStatus('current')
cDot11ClientAuthenAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 19), CDot11AuthenticationMethod()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientAuthenAlgorithm.setStatus('current')
cDot11ClientAdditionalAuthen = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 20), CDot11AdditionalAuthenMethod()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientAdditionalAuthen.setStatus('current')
cDot11ClientDot1xAuthenAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 21), CDot11Dot1xAuthenMethod()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientDot1xAuthenAlgorithm.setStatus('current')
cDot11ClientKeyManagement = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 22), CDot11KeyManagementMethod()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientKeyManagement.setStatus('deprecated')
cDot11ClientUnicastCipher = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 23), CDot11IfCipherType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientUnicastCipher.setStatus('current')
cDot11ClientMulticastCipher = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 24), CDot11IfCipherType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientMulticastCipher.setStatus('current')
cDot11ClientDevObjectID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 25), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientDevObjectID.setStatus('current')
cDot11ClientNewKeyManagement = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 26), CDot11NewKeyManagementMethod()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientNewKeyManagement.setStatus('current')
cDot11ClientStatisticTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1), )
if mibBuilder.loadTexts: cDot11ClientStatisticTable.setStatus('current')
cDot11ClientStatisticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1), )
cDot11ClientConfigInfoEntry.registerAugmentions(("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientStatisticEntry"))
cDot11ClientStatisticEntry.setIndexNames(*cDot11ClientConfigInfoEntry.getIndexNames())
if mibBuilder.loadTexts: cDot11ClientStatisticEntry.setStatus('current')
cDot11ClientCurrentTxRateSet = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 126))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientCurrentTxRateSet.setStatus('current')
cDot11ClientUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 2), Unsigned32()).setUnits('second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientUpTime.setStatus('current')
cDot11ClientSignalStrength = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 0))).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientSignalStrength.setStatus('current')
cDot11ClientSigQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientSigQuality.setStatus('current')
cDot11ClientAgingLeft = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 5), Gauge32()).setUnits('second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientAgingLeft.setStatus('current')
cDot11ClientPacketsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 6), Counter32()).setUnits('packet').setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientPacketsReceived.setStatus('current')
cDot11ClientBytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 7), Counter32()).setUnits('byte').setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientBytesReceived.setStatus('current')
cDot11ClientPacketsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 8), Counter32()).setUnits('packet').setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientPacketsSent.setStatus('current')
cDot11ClientBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 9), Counter32()).setUnits('byte').setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientBytesSent.setStatus('current')
cDot11ClientDuplicates = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 10), Counter32()).setUnits('packet').setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientDuplicates.setStatus('current')
cDot11ClientMsduRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 11), Counter32()).setUnits('packet').setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientMsduRetries.setStatus('current')
cDot11ClientMsduFails = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 12), Counter32()).setUnits('packet').setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientMsduFails.setStatus('current')
cDot11ClientWepErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 13), Counter32()).setUnits('packet').setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientWepErrors.setStatus('current')
cDot11ClientMicErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 14), Counter32()).setUnits('error').setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientMicErrors.setStatus('current')
cDot11ClientMicMissingFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 15), Counter32()).setUnits('packet').setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11ClientMicMissingFrames.setStatus('current')
ciscoDot11AssocMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 273, 2))
ciscoDot11AssocMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 1))
ciscoDot11AssocMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 2))
ciscoDot11AssocMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 1, 1)).setObjects(("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11AssocGlobalGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ClientConfigGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ClientStatGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11AssocMIBCompliance = ciscoDot11AssocMIBCompliance.setStatus('deprecated')
ciscoDot11AssocMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 1, 2)).setObjects(("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11AssocGlobalGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ClientConfigGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ClientStatGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ClientInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11AssocMIBComplianceRev1 = ciscoDot11AssocMIBComplianceRev1.setStatus('deprecated')
ciscoDot11AssocMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 1, 3)).setObjects(("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ClientConfigGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ClientStatGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ClientInfoGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11IfAssocStatGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11IfCipherStatGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ApAssocGlobalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11AssocMIBComplianceRev2 = ciscoDot11AssocMIBComplianceRev2.setStatus('deprecated')
ciscoDot11AssocMIBComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 1, 4)).setObjects(("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ClientConfigGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ClientAuthenGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ClientStatGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ClientInfoGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11IfAssocStatGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11IfCipherStatGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ApAssocGlobalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11AssocMIBComplianceRev3 = ciscoDot11AssocMIBComplianceRev3.setStatus('deprecated')
ciscoDot11AssocMIBComplianceRev4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 1, 5)).setObjects(("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ClientConfigGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ClientAuthenGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ClientStatGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ClientInfoGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11IfAssocStatGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11IfCipherStatGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ClientConfigExtGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ApAssocGlobalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11AssocMIBComplianceRev4 = ciscoDot11AssocMIBComplianceRev4.setStatus('current')
ciscoDot11AssocMIBComplianceRev5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 1, 6)).setObjects(("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ClientConfigGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ClientAuthenGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ClientStatGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ClientInfoGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11IfAssocStatGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11IfCipherStatGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ClientConfigExtGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ClientNewAuthenGroup"), ("CISCO-DOT11-ASSOCIATION-MIB", "ciscoDot11ApAssocGlobalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11AssocMIBComplianceRev5 = ciscoDot11AssocMIBComplianceRev5.setStatus('current')
ciscoDot11AssocGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 2, 1)).setObjects(("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ParentAddress"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ActiveWirelessClients"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ActiveBridges"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ActiveRepeaters"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11AssStatsAssociated"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11AssStatsAuthenticated"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11AssStatsRoamedIn"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11AssStatsRoamedAway"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11AssStatsDeauthenticated"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11AssStatsDisassociated"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11AssocGlobalGroup = ciscoDot11AssocGlobalGroup.setStatus('deprecated')
ciscoDot11ClientConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 2, 2)).setObjects(("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientParentAddress"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientRoleClassType"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientDevType"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientRadioType"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientWepEnabled"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientWepKeyMixEnabled"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientMicEnabled"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientPowerSaveMode"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientAid"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientDataRateSet"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11ClientConfigGroup = ciscoDot11ClientConfigGroup.setStatus('current')
ciscoDot11ClientStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 2, 3)).setObjects(("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientCurrentTxRateSet"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientUpTime"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientSignalStrength"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientSigQuality"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientPacketsReceived"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientBytesReceived"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientPacketsSent"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientBytesSent"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientAgingLeft"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientDuplicates"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientMsduRetries"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientMsduFails"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientWepErrors"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientMicErrors"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientMicMissingFrames"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11ClientStatGroup = ciscoDot11ClientStatGroup.setStatus('current')
ciscoDot11ClientInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 2, 4)).setObjects(("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientSoftwareVersion"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientName"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientAssociationState"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientIpAddressType"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientIpAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11ClientInfoGroup = ciscoDot11ClientInfoGroup.setStatus('current')
ciscoDot11ApAssocGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 2, 5)).setObjects(("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ParentAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11ApAssocGlobalGroup = ciscoDot11ApAssocGlobalGroup.setStatus('current')
ciscoDot11IfAssocStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 2, 6)).setObjects(("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ActiveWirelessClients"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ActiveBridges"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ActiveRepeaters"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11AssStatsAssociated"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11AssStatsAuthenticated"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11AssStatsRoamedIn"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11AssStatsRoamedAway"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11AssStatsDeauthenticated"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11AssStatsDisassociated"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11IfAssocStatGroup = ciscoDot11IfAssocStatGroup.setStatus('current')
ciscoDot11IfCipherStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 2, 7)).setObjects(("CISCO-DOT11-ASSOCIATION-MIB", "cd11IfCipherMicFailClientAddress"), ("CISCO-DOT11-ASSOCIATION-MIB", "cd11IfCipherTkipLocalMicFailures"), ("CISCO-DOT11-ASSOCIATION-MIB", "cd11IfCipherTkipRemotMicFailures"), ("CISCO-DOT11-ASSOCIATION-MIB", "cd11IfCipherTkipCounterMeasInvok"), ("CISCO-DOT11-ASSOCIATION-MIB", "cd11IfCipherCcmpReplaysDiscarded"), ("CISCO-DOT11-ASSOCIATION-MIB", "cd11IfCipherTkipReplaysDetected"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11IfCipherStatGroup = ciscoDot11IfCipherStatGroup.setStatus('current')
ciscoDot11ClientAuthenGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 2, 8)).setObjects(("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientVlanId"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientSubIfIndex"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientAuthenAlgorithm"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientAdditionalAuthen"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientDot1xAuthenAlgorithm"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientKeyManagement"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientUnicastCipher"), ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientMulticastCipher"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11ClientAuthenGroup = ciscoDot11ClientAuthenGroup.setStatus('deprecated')
ciscoDot11ClientConfigExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 2, 9)).setObjects(("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientDevObjectID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11ClientConfigExtGroup = ciscoDot11ClientConfigExtGroup.setStatus('current')
ciscoDot11ClientNewAuthenGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 2, 10)).setObjects(("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientNewKeyManagement"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11ClientNewAuthenGroup = ciscoDot11ClientNewAuthenGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-ASSOCIATION-MIB", ciscoDot11AssocMIBComplianceRev3=ciscoDot11AssocMIBComplianceRev3, cDot11ClientKeyManagement=cDot11ClientKeyManagement, CDot11ClientRadioType=CDot11ClientRadioType, cDot11AssStatsRoamedIn=cDot11AssStatsRoamedIn, cDot11ClientName=cDot11ClientName, ciscoDot11AssocMIBConformance=ciscoDot11AssocMIBConformance, ciscoDot11ClientConfigGroup=ciscoDot11ClientConfigGroup, CDot11AuthenticationMethod=CDot11AuthenticationMethod, CDot11KeyManagementMethod=CDot11KeyManagementMethod, cDot11AssociationGlobal=cDot11AssociationGlobal, cd11IfCipherTkipReplaysDetected=cd11IfCipherTkipReplaysDetected, cDot11ClientRadioType=cDot11ClientRadioType, ciscoDot11ApAssocGlobalGroup=ciscoDot11ApAssocGlobalGroup, cDot11AssStatsDeauthenticated=cDot11AssStatsDeauthenticated, cDot11ClientSigQuality=cDot11ClientSigQuality, cDot11ClientDuplicates=cDot11ClientDuplicates, ciscoDot11AssocMIBObjects=ciscoDot11AssocMIBObjects, cDot11ClientConfigInfoTable=cDot11ClientConfigInfoTable, cDot11ClientIpAddressType=cDot11ClientIpAddressType, ciscoDot11AssociationMIB=ciscoDot11AssociationMIB, cDot11ClientWepEnabled=cDot11ClientWepEnabled, cDot11ClientUpTime=cDot11ClientUpTime, cDot11AssStatsAssociated=cDot11AssStatsAssociated, cDot11AssStatsRoamedAway=cDot11AssStatsRoamedAway, cd11IfCipherMicFailClientAddress=cd11IfCipherMicFailClientAddress, cDot11ClientSignalStrength=cDot11ClientSignalStrength, cDot11ParentAddress=cDot11ParentAddress, cDot11ClientAid=cDot11ClientAid, ciscoDot11AssocMIBComplianceRev5=ciscoDot11AssocMIBComplianceRev5, cDot11ClientDevType=cDot11ClientDevType, ciscoDot11AssocGlobalGroup=ciscoDot11AssocGlobalGroup, ciscoDot11ClientStatGroup=ciscoDot11ClientStatGroup, ciscoDot11IfCipherStatGroup=ciscoDot11IfCipherStatGroup, cDot11ClientVlanId=cDot11ClientVlanId, cDot11ClientMicMissingFrames=cDot11ClientMicMissingFrames, ciscoDot11AssocMIBCompliance=ciscoDot11AssocMIBCompliance, cDot11ClientAddress=cDot11ClientAddress, cDot11ClientBytesReceived=cDot11ClientBytesReceived, cDot11ClientStatistics=cDot11ClientStatistics, ciscoDot11IfAssocStatGroup=ciscoDot11IfAssocStatGroup, cd11IfCipherTkipRemotMicFailures=cd11IfCipherTkipRemotMicFailures, cDot11ClientAdditionalAuthen=cDot11ClientAdditionalAuthen, CDot11AdditionalAuthenMethod=CDot11AdditionalAuthenMethod, cDot11ClientDevObjectID=cDot11ClientDevObjectID, cDot11ClientParentAddress=cDot11ClientParentAddress, ciscoDot11ClientConfigExtGroup=ciscoDot11ClientConfigExtGroup, cDot11ActiveBridges=cDot11ActiveBridges, CDot11ClientDevType=CDot11ClientDevType, cDot11ClientPacketsReceived=cDot11ClientPacketsReceived, cDot11ClientPacketsSent=cDot11ClientPacketsSent, cd11IfCipherTkipCounterMeasInvok=cd11IfCipherTkipCounterMeasInvok, CDot11NewKeyManagementMethod=CDot11NewKeyManagementMethod, ciscoDot11ClientInfoGroup=ciscoDot11ClientInfoGroup, CDot11Dot1xAuthenMethod=CDot11Dot1xAuthenMethod, cDot11ClientBytesSent=cDot11ClientBytesSent, cDot11ClientIpAddress=cDot11ClientIpAddress, ciscoDot11AssocMIBGroups=ciscoDot11AssocMIBGroups, ciscoDot11AssocMIBCompliances=ciscoDot11AssocMIBCompliances, ciscoDot11ClientNewAuthenGroup=ciscoDot11ClientNewAuthenGroup, cDot11ClientUnicastCipher=cDot11ClientUnicastCipher, cDot11ActiveDevicesTable=cDot11ActiveDevicesTable, CDot11ClientRoleClassType=CDot11ClientRoleClassType, cDot11ClientSoftwareVersion=cDot11ClientSoftwareVersion, ciscoDot11AssocMIBComplianceRev4=ciscoDot11AssocMIBComplianceRev4, cDot11ClientNewKeyManagement=cDot11ClientNewKeyManagement, cDot11ActiveDevicesEntry=cDot11ActiveDevicesEntry, cDot11ActiveRepeaters=cDot11ActiveRepeaters, cDot11ClientSubIfIndex=cDot11ClientSubIfIndex, cDot11ClientWepKeyMixEnabled=cDot11ClientWepKeyMixEnabled, cDot11ClientAgingLeft=cDot11ClientAgingLeft, PYSNMP_MODULE_ID=ciscoDot11AssociationMIB, cDot11ClientMicEnabled=cDot11ClientMicEnabled, cDot11ClientPowerSaveMode=cDot11ClientPowerSaveMode, cDot11ClientStatisticTable=cDot11ClientStatisticTable, ciscoDot11ClientAuthenGroup=ciscoDot11ClientAuthenGroup, cDot11ClientDot1xAuthenAlgorithm=cDot11ClientDot1xAuthenAlgorithm, ciscoDot11AssocMIBComplianceRev1=ciscoDot11AssocMIBComplianceRev1, cDot11AssStatsAuthenticated=cDot11AssStatsAuthenticated, cDot11ClientWepErrors=cDot11ClientWepErrors, cDot11AssStatsDisassociated=cDot11AssStatsDisassociated, cDot11ClientConfigInfoEntry=cDot11ClientConfigInfoEntry, cDot11ClientMulticastCipher=cDot11ClientMulticastCipher, cd11IfCipherTkipLocalMicFailures=cd11IfCipherTkipLocalMicFailures, cDot11ClientMsduRetries=cDot11ClientMsduRetries, cDot11AssociationStatsEntry=cDot11AssociationStatsEntry, cd11IfCipherStatsTable=cd11IfCipherStatsTable, cDot11ClientAssociationState=cDot11ClientAssociationState, cDot11ClientStatisticEntry=cDot11ClientStatisticEntry, cDot11ActiveWirelessClients=cDot11ActiveWirelessClients, cDot11ClientRoleClassType=cDot11ClientRoleClassType, cDot11ClientMicErrors=cDot11ClientMicErrors, ciscoDot11AssocMIBComplianceRev2=ciscoDot11AssocMIBComplianceRev2, cd11IfCipherCcmpReplaysDiscarded=cd11IfCipherCcmpReplaysDiscarded, cDot11ClientCurrentTxRateSet=cDot11ClientCurrentTxRateSet, cDot11ClientMsduFails=cDot11ClientMsduFails, cDot11ClientAuthenAlgorithm=cDot11ClientAuthenAlgorithm, cDot11AssociationStatsTable=cDot11AssociationStatsTable, cd11IfCipherStatsEntry=cd11IfCipherStatsEntry, cDot11ClientDataRateSet=cDot11ClientDataRateSet, cDot11ClientConfiguration=cDot11ClientConfiguration)
