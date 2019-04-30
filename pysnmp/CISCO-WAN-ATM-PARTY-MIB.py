#
# PySNMP MIB module CISCO-WAN-ATM-PARTY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-ATM-PARTY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:03:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, Integer32, Gauge32, ModuleIdentity, TimeTicks, IpAddress, Counter64, iso, ObjectIdentity, MibIdentifier, Counter32, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Gauge32", "ModuleIdentity", "TimeTicks", "IpAddress", "Counter64", "iso", "ObjectIdentity", "MibIdentifier", "Counter32", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
ciscoWanAtmPartyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 99998))
ciscoWanAtmPartyMIB.setRevisions(('2002-06-17 00:00',))
if mibBuilder.loadTexts: ciscoWanAtmPartyMIB.setLastUpdated('200206170000Z')
if mibBuilder.loadTexts: ciscoWanAtmPartyMIB.setOrganization('Cisco Systems, Inc.')
ciscoWanAtmPartyMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99998, 0))
ciscoWanAtmPartyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1))
cwapConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1))
ciscoWanAtmPartyMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99998, 2))
class WanPartyAdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class WanPartyOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ok", 1), ("fail", 2))

class WanNsapAtmAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(20, 20)
    fixedLength = 20

cwapConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1), )
if mibBuilder.loadTexts: cwapConfigTable.setStatus('current')
cwapConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-WAN-ATM-PARTY-MIB", "cwapRootVpi"), (0, "CISCO-WAN-ATM-PARTY-MIB", "cwapRootVci"), (0, "CISCO-WAN-ATM-PARTY-MIB", "cwapReference"))
if mibBuilder.loadTexts: cwapConfigEntry.setStatus('current')
cwapRootVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095)))
if mibBuilder.loadTexts: cwapRootVpi.setStatus('current')
cwapRootVci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: cwapRootVci.setStatus('current')
cwapReference = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: cwapReference.setStatus('current')
cwapNSAPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 4), WanNsapAtmAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwapNSAPAddress.setStatus('current')
cwapVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwapVpi.setStatus('current')
cwapVci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwapVci.setStatus('current')
cwapReroute = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwapReroute.setStatus('current')
cwapAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 8), WanPartyAdminStatus().clone('up')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwapAdminStatus.setStatus('current')
cwapOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 9), WanPartyOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwapOperStatus.setStatus('current')
cwapIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwapIdentifier.setStatus('current')
cwapUploadCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwapUploadCounter.setStatus('current')
cwapRootPhysicalId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwapRootPhysicalId.setStatus('current')
cwapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwapRowStatus.setStatus('current')
ciscoWanAtmPartyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99998, 2, 1))
ciscoWanAtmPartyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99998, 2, 2))
ciscoWanAtmPartyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 99998, 2, 1, 1)).setObjects(("CISCO-WAN-ATM-PARTY-MIB", "ciscoWanAtmPartyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmPartyMIBCompliance = ciscoWanAtmPartyMIBCompliance.setStatus('current')
ciscoWanAtmPartyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 99998, 2, 2, 2)).setObjects(("CISCO-WAN-ATM-PARTY-MIB", "cwapNSAPAddress"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapVpi"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapVci"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapAdminStatus"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapOperStatus"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapReroute"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapIdentifier"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapUploadCounter"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapRootPhysicalId"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmPartyGroup = ciscoWanAtmPartyGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-ATM-PARTY-MIB", PYSNMP_MODULE_ID=ciscoWanAtmPartyMIB, cwapConfigEntry=cwapConfigEntry, ciscoWanAtmPartyMIBCompliances=ciscoWanAtmPartyMIBCompliances, cwapRootVpi=cwapRootVpi, ciscoWanAtmPartyMIBConform=ciscoWanAtmPartyMIBConform, cwapRootPhysicalId=cwapRootPhysicalId, WanNsapAtmAddress=WanNsapAtmAddress, cwapUploadCounter=cwapUploadCounter, cwapRowStatus=cwapRowStatus, cwapIdentifier=cwapIdentifier, ciscoWanAtmPartyMIBGroups=ciscoWanAtmPartyMIBGroups, WanPartyAdminStatus=WanPartyAdminStatus, cwapAdminStatus=cwapAdminStatus, cwapOperStatus=cwapOperStatus, cwapReroute=cwapReroute, cwapNSAPAddress=cwapNSAPAddress, cwapConfig=cwapConfig, ciscoWanAtmPartyMIBNotifs=ciscoWanAtmPartyMIBNotifs, ciscoWanAtmPartyMIBObjects=ciscoWanAtmPartyMIBObjects, ciscoWanAtmPartyMIB=ciscoWanAtmPartyMIB, cwapVpi=cwapVpi, WanPartyOperStatus=WanPartyOperStatus, ciscoWanAtmPartyGroup=ciscoWanAtmPartyGroup, cwapConfigTable=cwapConfigTable, ciscoWanAtmPartyMIBCompliance=ciscoWanAtmPartyMIBCompliance, cwapReference=cwapReference, cwapRootVci=cwapRootVci, cwapVci=cwapVci)
