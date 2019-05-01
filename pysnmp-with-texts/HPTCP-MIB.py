#
# PySNMP MIB module HPTCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPTCP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:42:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, Counter64, NotificationType, MibIdentifier, iso, Gauge32, TimeTicks, Counter32, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "Counter64", "NotificationType", "MibIdentifier", "iso", "Gauge32", "TimeTicks", "Counter32", "ObjectIdentity", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpicfTcpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79))
hpicfTcpMib.setRevisions(('2010-09-30 15:25',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfTcpMib.setRevisionsDescriptions(('Added hpicfTcpMib and associated objects.',))
if mibBuilder.loadTexts: hpicfTcpMib.setLastUpdated('201009301525Z')
if mibBuilder.loadTexts: hpicfTcpMib.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfTcpMib.setContactInfo('Hewlett-Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfTcpMib.setDescription('This MIB module contains HP proprietary objects for monitoring TCP traffic')
hpTcpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 1))
hpTcpOutRstsWithAck = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpTcpOutRstsWithAck.setStatus('current')
if mibBuilder.loadTexts: hpTcpOutRstsWithAck.setDescription('The number of TCP packets sent containing the RST and the ACK flags. This is useful to detect SYN packets sent to closed ports.')
hpTcpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 2))
hpTcpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 2, 1))
hpTcpBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 2, 1, 1)).setObjects(("HPTCP-MIB", "hpTcpOutRstsWithAck"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpTcpBaseGroup = hpTcpBaseGroup.setStatus('current')
if mibBuilder.loadTexts: hpTcpBaseGroup.setDescription('A collection of proprietary objects for monitoring the TCP connections.')
hpTcpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 2, 2))
hpTcpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 2, 2, 1)).setObjects(("HPTCP-MIB", "hpTcpBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpTcpCompliance = hpTcpCompliance.setStatus('current')
if mibBuilder.loadTexts: hpTcpCompliance.setDescription('The compliance statement for HP switches that support Dynamic ARP Protection.')
mibBuilder.exportSymbols("HPTCP-MIB", hpTcpCompliance=hpTcpCompliance, hpTcpObjects=hpTcpObjects, hpTcpGroups=hpTcpGroups, PYSNMP_MODULE_ID=hpicfTcpMib, hpicfTcpMib=hpicfTcpMib, hpTcpOutRstsWithAck=hpTcpOutRstsWithAck, hpTcpBaseGroup=hpTcpBaseGroup, hpTcpCompliances=hpTcpCompliances, hpTcpConformance=hpTcpConformance)
