#
# PySNMP MIB module HPTCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPTCP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:30:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, ModuleIdentity, TimeTicks, NotificationType, MibIdentifier, IpAddress, Gauge32, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "TimeTicks", "NotificationType", "MibIdentifier", "IpAddress", "Gauge32", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "Unsigned32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpicfTcpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79))
hpicfTcpMib.setRevisions(('2010-09-30 15:25',))
if mibBuilder.loadTexts: hpicfTcpMib.setLastUpdated('201009301525Z')
if mibBuilder.loadTexts: hpicfTcpMib.setOrganization('HP Networking')
hpTcpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 1))
hpTcpOutRstsWithAck = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpTcpOutRstsWithAck.setStatus('current')
hpTcpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 2))
hpTcpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 2, 1))
hpTcpBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 2, 1, 1)).setObjects(("HPTCP-MIB", "hpTcpOutRstsWithAck"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpTcpBaseGroup = hpTcpBaseGroup.setStatus('current')
hpTcpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 2, 2))
hpTcpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 2, 2, 1)).setObjects(("HPTCP-MIB", "hpTcpBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpTcpCompliance = hpTcpCompliance.setStatus('current')
mibBuilder.exportSymbols("HPTCP-MIB", hpTcpGroups=hpTcpGroups, hpTcpObjects=hpTcpObjects, hpTcpCompliance=hpTcpCompliance, hpTcpBaseGroup=hpTcpBaseGroup, hpicfTcpMib=hpicfTcpMib, hpTcpOutRstsWithAck=hpTcpOutRstsWithAck, PYSNMP_MODULE_ID=hpicfTcpMib, hpTcpCompliances=hpTcpCompliances, hpTcpConformance=hpTcpConformance)
