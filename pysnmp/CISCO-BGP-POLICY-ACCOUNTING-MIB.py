#
# PySNMP MIB module CISCO-BGP-POLICY-ACCOUNTING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-BGP-POLICY-ACCOUNTING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:33:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, ModuleIdentity, Integer32, Bits, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, NotificationType, Gauge32, ObjectIdentity, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "Integer32", "Bits", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "NotificationType", "Gauge32", "ObjectIdentity", "Counter64", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoBgpPolAcctMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 148))
ciscoBgpPolAcctMIB.setRevisions(('2002-07-26 00:00', '1999-12-17 00:00',))
if mibBuilder.loadTexts: ciscoBgpPolAcctMIB.setLastUpdated('200207260000Z')
if mibBuilder.loadTexts: ciscoBgpPolAcctMIB.setOrganization('Cisco Systems, Inc.')
ciscoBgpPolAcctMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 148, 1))
cbpAcctTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1), )
if mibBuilder.loadTexts: cbpAcctTable.setStatus('current')
cbpAcctEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctTrafficIndex"))
if mibBuilder.loadTexts: cbpAcctEntry.setStatus('current')
cbpAcctTrafficIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbpAcctTrafficIndex.setStatus('current')
cbpAcctInPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbpAcctInPacketCount.setStatus('current')
cbpAcctInOctetCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbpAcctInOctetCount.setStatus('current')
cbpAcctOutPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbpAcctOutPacketCount.setStatus('current')
cbpAcctOutOctetCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbpAcctOutOctetCount.setStatus('current')
ciscoBgpPolAcctMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 148, 3))
ciscoBgpPolAcctMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 1))
ciscoBgpPolAcctMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 2))
ciscoBgpPolAcctMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 1, 1)).setObjects(("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBgpPolAcctMIBCompliance = ciscoBgpPolAcctMIBCompliance.setStatus('deprecated')
ciscoBgpPolAcctMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 1, 2)).setObjects(("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctTableGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBgpPolAcctMIBComplianceRev1 = ciscoBgpPolAcctMIBComplianceRev1.setStatus('current')
cbpAcctTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 2, 1)).setObjects(("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctTrafficIndex"), ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctInPacketCount"), ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctInOctetCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbpAcctTableGroup = cbpAcctTableGroup.setStatus('deprecated')
cbpAcctTableGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 2, 2)).setObjects(("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctTrafficIndex"), ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctInPacketCount"), ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctInOctetCount"), ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctOutPacketCount"), ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctOutOctetCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbpAcctTableGroupRev1 = cbpAcctTableGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-BGP-POLICY-ACCOUNTING-MIB", ciscoBgpPolAcctMIBObjects=ciscoBgpPolAcctMIBObjects, ciscoBgpPolAcctMIB=ciscoBgpPolAcctMIB, cbpAcctOutOctetCount=cbpAcctOutOctetCount, ciscoBgpPolAcctMIBGroups=ciscoBgpPolAcctMIBGroups, PYSNMP_MODULE_ID=ciscoBgpPolAcctMIB, cbpAcctTableGroupRev1=cbpAcctTableGroupRev1, ciscoBgpPolAcctMIBConformance=ciscoBgpPolAcctMIBConformance, ciscoBgpPolAcctMIBCompliance=ciscoBgpPolAcctMIBCompliance, cbpAcctEntry=cbpAcctEntry, cbpAcctTableGroup=cbpAcctTableGroup, cbpAcctTable=cbpAcctTable, cbpAcctInPacketCount=cbpAcctInPacketCount, ciscoBgpPolAcctMIBCompliances=ciscoBgpPolAcctMIBCompliances, ciscoBgpPolAcctMIBComplianceRev1=ciscoBgpPolAcctMIBComplianceRev1, cbpAcctTrafficIndex=cbpAcctTrafficIndex, cbpAcctOutPacketCount=cbpAcctOutPacketCount, cbpAcctInOctetCount=cbpAcctInOctetCount)
