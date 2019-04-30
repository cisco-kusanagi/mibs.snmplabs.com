#
# PySNMP MIB module CISCO-VOIP-TAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOIP-TAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:03:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
cTap2StreamIndex, cTap2MediationContentId = mibBuilder.importSymbols("CISCO-TAP2-MIB", "cTap2StreamIndex", "cTap2MediationContentId")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, ObjectIdentity, TimeTicks, Integer32, IpAddress, Counter64, MibIdentifier, Gauge32, iso, NotificationType, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "ObjectIdentity", "TimeTicks", "Integer32", "IpAddress", "Counter64", "MibIdentifier", "Gauge32", "iso", "NotificationType", "Unsigned32", "ModuleIdentity")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
ciscoVoIpTapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 716))
ciscoVoIpTapMIB.setRevisions(('2009-10-01 00:00',))
if mibBuilder.loadTexts: ciscoVoIpTapMIB.setLastUpdated('200910010000Z')
if mibBuilder.loadTexts: ciscoVoIpTapMIB.setOrganization('Cisco Systems, Inc.')
ciscoVoIpTapMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 716, 0))
ciscoVoIpTapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 716, 1))
ciscoVoIpTapMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 716, 2))
cvoiptapStreamEncodePacket = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1))
class CvoipWarrantId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 30)

class CvoipSubscriberId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

cvoiptapStreamCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 1), Bits().clone(namedValues=NamedValues(("tapEnable", 0), ("usernameOrNumber", 1), ("uri", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvoiptapStreamCapabilities.setStatus('current')
cvoiptapStreamTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2), )
if mibBuilder.loadTexts: cvoiptapStreamTable.setStatus('current')
cvoiptapStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-TAP2-MIB", "cTap2MediationContentId"), (0, "CISCO-TAP2-MIB", "cTap2StreamIndex"))
if mibBuilder.loadTexts: cvoiptapStreamEntry.setStatus('current')
cvoiptapStreamId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 1), CvoipWarrantId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvoiptapStreamId.setStatus('current')
cvoiptapStreamType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("pen", 1), ("trace", 2), ("penAndTrace", 3), ("intercept", 4))).clone('intercept')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvoiptapStreamType.setStatus('current')
cvoiptapStreamMatch = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 3), CvoipSubscriberId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvoiptapStreamMatch.setStatus('current')
cvoiptapStreamMatchType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("usernameOrNumber", 1), ("uri", 2))).clone('usernameOrNumber')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvoiptapStreamMatchType.setStatus('current')
cvoiptapStreamCCMediationDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvoiptapStreamCCMediationDevice.setStatus('current')
cvoiptapStreamRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvoiptapStreamRowStatus.setStatus('current')
ciscoVoIpTapMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 716, 2, 1))
ciscoVoIpTapMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 716, 2, 2))
ciscoVoIpTapMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 716, 2, 1, 1)).setObjects(("CISCO-VOIP-TAP-MIB", "ciscoVoIpTapStreamGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoIpTapMIBCompliance = ciscoVoIpTapMIBCompliance.setStatus('current')
ciscoVoIpTapStreamGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 716, 2, 2, 1)).setObjects(("CISCO-VOIP-TAP-MIB", "cvoiptapStreamCapabilities"), ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamId"), ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamType"), ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamMatch"), ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamMatchType"), ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamCCMediationDevice"), ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoIpTapStreamGroup = ciscoVoIpTapStreamGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOIP-TAP-MIB", cvoiptapStreamEncodePacket=cvoiptapStreamEncodePacket, ciscoVoIpTapMIBObjects=ciscoVoIpTapMIBObjects, CvoipWarrantId=CvoipWarrantId, cvoiptapStreamRowStatus=cvoiptapStreamRowStatus, ciscoVoIpTapStreamGroup=ciscoVoIpTapStreamGroup, cvoiptapStreamCCMediationDevice=cvoiptapStreamCCMediationDevice, ciscoVoIpTapMIBCompliance=ciscoVoIpTapMIBCompliance, ciscoVoIpTapMIB=ciscoVoIpTapMIB, PYSNMP_MODULE_ID=ciscoVoIpTapMIB, ciscoVoIpTapMIBGroups=ciscoVoIpTapMIBGroups, ciscoVoIpTapMIBCompliances=ciscoVoIpTapMIBCompliances, cvoiptapStreamMatchType=cvoiptapStreamMatchType, cvoiptapStreamMatch=cvoiptapStreamMatch, cvoiptapStreamTable=cvoiptapStreamTable, CvoipSubscriberId=CvoipSubscriberId, cvoiptapStreamEntry=cvoiptapStreamEntry, cvoiptapStreamType=cvoiptapStreamType, cvoiptapStreamCapabilities=cvoiptapStreamCapabilities, ciscoVoIpTapMIBConform=ciscoVoIpTapMIBConform, cvoiptapStreamId=cvoiptapStreamId, ciscoVoIpTapMIBNotifs=ciscoVoIpTapMIBNotifs)
