#
# PySNMP MIB module CISCO-BGP-POLICY-ACCOUNTING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-BGP-POLICY-ACCOUNTING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:51:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, IpAddress, Unsigned32, NotificationType, ObjectIdentity, Gauge32, Bits, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "Unsigned32", "NotificationType", "ObjectIdentity", "Gauge32", "Bits", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "ModuleIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoBgpPolAcctMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 148))
ciscoBgpPolAcctMIB.setRevisions(('2002-07-26 00:00', '1999-12-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoBgpPolAcctMIB.setRevisionsDescriptions(('Added egress, packet and octet, counters for the BGP policy accounting feature.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoBgpPolAcctMIB.setLastUpdated('200207260000Z')
if mibBuilder.loadTexts: ciscoBgpPolAcctMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoBgpPolAcctMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoBgpPolAcctMIB.setDescription('BGP policy based accounting information')
ciscoBgpPolAcctMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 148, 1))
cbpAcctTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1), )
if mibBuilder.loadTexts: cbpAcctTable.setStatus('current')
if mibBuilder.loadTexts: cbpAcctTable.setDescription('The cbpAcctTable provides statistics about ingress and egress traffic on an interface. This data could be used for purposes like billing.')
cbpAcctEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctTrafficIndex"))
if mibBuilder.loadTexts: cbpAcctEntry.setStatus('current')
if mibBuilder.loadTexts: cbpAcctEntry.setDescription("Each cbpAcctEntry provides statistics for traffic of interest on an ingress and/or egress interfaces. The traffic of interest may be used for purposes like billing, and is referred to from here on in the MIB by the term 'traffic-type', which corresponds to cbpAcctTrafficIndex. Traffic-types are configured by the user on a per interface basis. The statistics include ingress packet counts, ingress octet counts, egress packet counts and egress octet counts. Entries are created when traffic-type is configured on an interface. Entries are deleted automatically when the user removes the corresponding traffic-type configuration from an interface.")
cbpAcctTrafficIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbpAcctTrafficIndex.setStatus('current')
if mibBuilder.loadTexts: cbpAcctTrafficIndex.setDescription('An integer value greater than 0, that uniquely identifies a traffic-type. The traffic-type has no intrinsic meaning. It just means the traffic coming into an interface can be differentiated into different types. It is up to the user to give meaning to and configure the various traffic-types on an interface.')
cbpAcctInPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbpAcctInPacketCount.setStatus('current')
if mibBuilder.loadTexts: cbpAcctInPacketCount.setDescription('The total number of packets received for a particular traffic-type on an interface.')
cbpAcctInOctetCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbpAcctInOctetCount.setStatus('current')
if mibBuilder.loadTexts: cbpAcctInOctetCount.setDescription('The total number of octets received for a particular traffic-type on an interface.')
cbpAcctOutPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbpAcctOutPacketCount.setStatus('current')
if mibBuilder.loadTexts: cbpAcctOutPacketCount.setDescription('The total number of packets transmitted for a particular traffic-type on an interface.')
cbpAcctOutOctetCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbpAcctOutOctetCount.setStatus('current')
if mibBuilder.loadTexts: cbpAcctOutOctetCount.setDescription('The total number of octets transmitted for a particular traffic-type on an interface.')
ciscoBgpPolAcctMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 148, 3))
ciscoBgpPolAcctMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 1))
ciscoBgpPolAcctMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 2))
ciscoBgpPolAcctMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 1, 1)).setObjects(("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBgpPolAcctMIBCompliance = ciscoBgpPolAcctMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoBgpPolAcctMIBCompliance.setDescription('The compliance statement for entities which implement this Cisco BGP-Policy Traffic Accounting MIB.')
ciscoBgpPolAcctMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 1, 2)).setObjects(("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctTableGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBgpPolAcctMIBComplianceRev1 = ciscoBgpPolAcctMIBComplianceRev1.setStatus('current')
if mibBuilder.loadTexts: ciscoBgpPolAcctMIBComplianceRev1.setDescription('The compliance statement for entities which implement this Cisco BGP-Policy Traffic Accounting MIB.')
cbpAcctTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 2, 1)).setObjects(("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctTrafficIndex"), ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctInPacketCount"), ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctInOctetCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbpAcctTableGroup = cbpAcctTableGroup.setStatus('deprecated')
if mibBuilder.loadTexts: cbpAcctTableGroup.setDescription('A collection of objects providing customer traffic related parameters.')
cbpAcctTableGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 2, 2)).setObjects(("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctTrafficIndex"), ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctInPacketCount"), ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctInOctetCount"), ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctOutPacketCount"), ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctOutOctetCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbpAcctTableGroupRev1 = cbpAcctTableGroupRev1.setStatus('current')
if mibBuilder.loadTexts: cbpAcctTableGroupRev1.setDescription('A collection of objects providing customer traffic related parameters.')
mibBuilder.exportSymbols("CISCO-BGP-POLICY-ACCOUNTING-MIB", cbpAcctTable=cbpAcctTable, cbpAcctTableGroup=cbpAcctTableGroup, cbpAcctEntry=cbpAcctEntry, cbpAcctInPacketCount=cbpAcctInPacketCount, ciscoBgpPolAcctMIBComplianceRev1=ciscoBgpPolAcctMIBComplianceRev1, ciscoBgpPolAcctMIB=ciscoBgpPolAcctMIB, PYSNMP_MODULE_ID=ciscoBgpPolAcctMIB, cbpAcctTrafficIndex=cbpAcctTrafficIndex, cbpAcctInOctetCount=cbpAcctInOctetCount, cbpAcctTableGroupRev1=cbpAcctTableGroupRev1, cbpAcctOutOctetCount=cbpAcctOutOctetCount, ciscoBgpPolAcctMIBCompliances=ciscoBgpPolAcctMIBCompliances, ciscoBgpPolAcctMIBGroups=ciscoBgpPolAcctMIBGroups, cbpAcctOutPacketCount=cbpAcctOutPacketCount, ciscoBgpPolAcctMIBCompliance=ciscoBgpPolAcctMIBCompliance, ciscoBgpPolAcctMIBObjects=ciscoBgpPolAcctMIBObjects, ciscoBgpPolAcctMIBConformance=ciscoBgpPolAcctMIBConformance)
