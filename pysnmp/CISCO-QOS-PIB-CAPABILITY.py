#
# PySNMP MIB module CISCO-QOS-PIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-QOS-PIB-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:53:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, IpAddress, Gauge32, iso, ModuleIdentity, Integer32, Counter64, TimeTicks, Bits, NotificationType, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "IpAddress", "Gauge32", "iso", "ModuleIdentity", "Integer32", "Counter64", "TimeTicks", "Bits", "NotificationType", "MibIdentifier", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoQosPibCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 390))
ciscoQosPibCapability.setRevisions(('2003-08-14 00:00',))
if mibBuilder.loadTexts: ciscoQosPibCapability.setLastUpdated('200308140000Z')
if mibBuilder.loadTexts: ciscoQosPibCapability.setOrganization('Cisco Systems, Inc.')
ciscoQosPibCapCatOSV08R0101Cat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 390, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQosPibCapCatOSV08R0101Cat6K = ciscoQosPibCapCatOSV08R0101Cat6K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQosPibCapCatOSV08R0101Cat6K = ciscoQosPibCapCatOSV08R0101Cat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-QOS-PIB-CAPABILITY", PYSNMP_MODULE_ID=ciscoQosPibCapability, ciscoQosPibCapCatOSV08R0101Cat6K=ciscoQosPibCapCatOSV08R0101Cat6K, ciscoQosPibCapability=ciscoQosPibCapability)
